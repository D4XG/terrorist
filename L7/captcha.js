const Captcha = require("2captcha");

const solver = new Captcha.Solver("key");

function solveCaptcha(key, site, type)
{
    return new Promise(function(resolve, reject) {
        if (type == "hCaptcha") {
            solver.hcaptcha(key, site)
               .then((response) => {
                   return resolve(response);
               })
               .catch((err) => {
                   return reject(err);
               })
               .catch(reject);
        } else if (type == "ReCaptcha") {
            solver.recaptcha(key, site)
                .then((response) => {
                    return resolve(response);
                })
                .catch((err) => {
                    return reject(err);
                })
        }
    });
}

module.exports = solveCaptcha;