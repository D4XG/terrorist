import subprocess
import os

def install_python_packages():
    try:
        # Install additional Python packages
        subprocess.check_call(['pip', 'install', 'termcolor'])

        subprocess.check_call(['pip', 'install', 'colorama'])

        subprocess.check_call(['pip', 'install', 'datetime'])

        subprocess.check_call(['pip', 'install', 'opencv-python'])

        subprocess.check_call(['pip', 'install', 'cfscrape'])

        subprocess.check_call(['pip', 'install', 'socks'])

        subprocess.check_call(['pip', 'install', 'pysocks'])

        subprocess.check_call(['pip', 'install', 'cloudscraper'])

        subprocess.check_call(['pip', 'install', 'pystyle'])

        subprocess.check_call(['pip', 'install', 'requests'])

        subprocess.check_call(['pip', 'install', 'scapy'])

        subprocess.check_call(['pip', 'install', 'cython'])

        subprocess.check_call(['pip', 'install', 'darksky'])

        subprocess.check_call(['pip', 'install', 'darkskylib'])

        subprocess.check_call(['pip', 'install', 'termcolor'])

        subprocess.check_call(['pip', 'install', 'aiohttp_socks'])

        print("All Python packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install Python packages - {e}")

        # Go to AA
        os.chdir('AA')

        # Install additional Python packages
        subprocess.check_call(['pip', 'install', 'termcolor'])

        subprocess.check_call(['pip', 'install', 'colorama'])

        subprocess.check_call(['pip', 'install', 'datetime'])

        subprocess.check_call(['pip', 'install', 'cfscrape'])

        subprocess.check_call(['pip', 'install', 'socks'])

        subprocess.check_call(['pip', 'install', 'pysocks'])

        subprocess.check_call(['pip', 'install', 'cloudscraper'])

        subprocess.check_call(['pip', 'install', 'pystyle'])

        subprocess.check_call(['pip', 'install', 'requests'])

        subprocess.check_call(['pip', 'install', 'scapy'])

        subprocess.check_call(['pip', 'install', 'cython'])

        subprocess.check_call(['pip', 'install', 'darksky'])

        subprocess.check_call(['pip', 'install', 'darkskylib'])

        subprocess.check_call(['pip', 'install', 'termcolor'])

        subprocess.check_call(['pip', 'install', 'aiohttp_socks'])

        print("All Python packages installed successfully!")
        os.chdir('..')
        
def install_npm_packages():
    npm_commands = [
        'npm i user-agents', 'npm i header-generator', 'npm i request', 'npm i fake-useragent',
        'npm i randomstring', 'npm i colors', 'npm i axios', 'npm i cheerio', 'npm i gradient-string',
        'npm i cloudscraper', 'npm i random-useragent', 'npm i crypto-random-string', 'npm i playwright-extra',
        'npm i fingerprint-generator', 'npm i fingerprint-injector', 'npm i ua-parser-js', 'npm i http2',
        'npm i minimist', 'npm i socks', 'npm i puppeteer', 'npm i hcaptcha-solver', 'npm i puppeteer-extra',
        'npm i puppeteer-extra-plugin-recaptcha', 'npm i puppeteer-extra-plugin-stealth', 'npm i http', 'npm i http2',
        'npm i zombie', 'npm i random-referer', 'npm i jar'
    ]
    
    try:
        # Change directory to L7
        os.chdir('L7')
        for command in npm_commands:
            subprocess.run(command, shell=True, check=True)
            print(f"NPM package '{command}' installed successfully in L7 folder!")
        
        # Change directory to VIP
        os.chdir('../VIP')
        for command in npm_commands:
            subprocess.run(command, shell=True, check=True)
            print(f"NPM package '{command}' installed successfully in VIP folder!")

        # Change directory back to the main directory
        os.chdir('..')

        print("All NPM packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install NPM package - {e}")

def setup():
    install_python_packages()
    install_npm_packages()

if __name__ == "__main__":
    setup()
