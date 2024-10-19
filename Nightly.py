import os
import time
import requests
import colorama
from termcolor import colored, cprint

ver = {'1.0.2b'}



psws = {"KEY_qyOtw7IwjU_jjlol"}


def cl():
    clt = 'https://raw.githubusercontent.com/kurwahub/Nightly/refs/heads/main/cl.txt'
    rs = requests.get(clt, allow_redirects=True)
    print(rs.text)
    hs = input("press enter to go back")
    main()



def load():
    for i in range (1, 101) :
        time.sleep(0.05)
        os.system("clear")
        print(i)
        time.sleep(3) 
        print("loaded")
        main()

def numc():
    phone_number = input("enter phone number: ")
    url = f"https://callerapi.com/api/phone/info/{phone_number}"
    headers = {
        "X-Auth": "input api"
    }
    response = requests.get(url, headers=headers)
    print("result: ", response.json())
    time.sleep(5)
    main()

def main():
    os.system("clear")
    cprint(logo, 'cyan')
    time.sleep(0.5)
    cprint('    version: 1.0.2', 'green')
    time.sleep(0.5)
    print("    |")
    print("    |")
    ns = input("    [nightly] @")
    if ns == "help":
        print("    help - shows this menu")
        print("    title - set a custom title")
        print("    echo - prints out text")
        print("    checknum - pretty self explanatory")
        print("    credits - prints out credits")
        print("    vip - vip mode")
        time.sleep(2)
        main()
    if ns == "checknum":
        numc()
    if ns == "changelog":
        cl()
    if ns == "credits":
        print("    @hqzpidor - owner, developer")
        time.sleep(2)
        main1()
    if ns == "echo":
        echoes = input("    enter text:")
        print(echoes)
        time.sleep(2)
        main()
    if ns == "title":
        os.system("title NIGHTLY 1.0")
        time.sleep(2)
        main()
    else:
        print("    wrong command: ", ns)
        time.sleep(2)
        main()
    


version = "1.0.2"



logo = """
███╗░░██╗██╗░██████╗░██╗░░██╗████████╗██╗░░░░░██╗░░░██╗
████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝██║░░░░░╚██╗░██╔╝
██╔██╗██║██║██║░░██╗░███████║░░░██║░░░██║░░░░░░╚████╔╝░
██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░██║░░░░░░░╚██╔╝░░
██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░███████╗░░░██║░░░
╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░╚═╝░░░
"""

os.system("pip install termcolor colorama requests")

os.system("clear")
cprint('[*] Loading...', 'yellow')
time.sleep(2)
check = requests.get("https://github.com")

if check.status_code == 404:
    cprint('[-] Not found.', 'red')
cprint('[*] Checking version...', 'yellow')
url = 'https://pastebin.com/raw/na8gYMyF'
r = requests.get(url, allow_redirects=True)
print(r.text)
if r.text in ver:
    cprint('[+] Correct version!', 'green')
    time.sleep(2)
    main()
else:
    cprint('[*] Version may be wrong, download the latest one from github! (The program will still load)', 'cyan')
    time.sleep(2)
    main()