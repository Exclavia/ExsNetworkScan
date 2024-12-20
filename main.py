from scapy.all import ARP, Ether, srp
import socket
import requests
import time
import os
from datetime import datetime
import cursor

current_datetime = datetime.now()
datetime_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
dt_file_str = current_datetime.strftime('%Y-%m-%d_%H.%M.%S')
cwd_str = str(os.getcwd()).replace("\\", "/") + "/"
apikey_load = open("apikey.config", "r")
apiKey = apikey_load.readline()
default_gateway = open("default_gateway.config", "r")
def clear_console():
    """Clears the console."""
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)
    
def get_mac_details(mac_address):
     
    # We will use an API to get the vendor details
    url = "https://api.maclookup.app/v2/macs/"
    # Use get method to fetch details
    
    response = requests.get(url+mac_address+'?apiKey='+apiKey)
    if response.status_code != 200:
        return "[ Unknown Vendor ]"
    API_Data = response.json()
    if API_Data['company'] == "":
        return "[ Unknown Vendor ]"
    return API_Data['company']
cursor.hide()
print(" Scanning network...")
print("")
gateway = default_gateway.readline()
target_ip = gateway + "/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []
i = 0
for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    getBrand = get_mac_details(str(received.hwsrc))
    if len(getBrand) > 20:
        vndr = getBrand[0:20] + "..."
    if len(getBrand) < 20:
        vndr = getBrand
    
    clients.append({'ip': received.psrc, 'Vendor(MAC)': str(received.hwsrc) + " "*8 + vndr})
    i = i + 1
    if i > 0:
        print(" " + str(i) + " device(s) found...")
    

# print clients
if i == 0:
    clear_console()
    print("")
    print(" No devices found in the network.")
    print(" Make sure your default gateway is set in the config file.")
    print("")
    print(" Current gateway set: " + gateway)
    print("")
    exit()
    
clear_console()
print("")
print(" " + str(i) + " available devices in the network [Gateway - " + gateway + "]:")
print("")
print("  IP" + " "*18+"MAC" + " "*22 + "Vendor")
print("  " + "="*68)
for client in clients:
    
    time.sleep(0.02)
    print("  {:16}    {}".format(client['ip'], client['Vendor(MAC)']))
    
print("  " + "="*68)
print("")
print(" Network scanned at: " + datetime_string)
print("")
cursor.show()
saveout = input("Save results?[y/n]: ")

if saveout.capitalize() == "Y":
    f = open("saved/" + dt_file_str + "_network-scan.txt", "w")
    f.write("IP" + " "*18+"MAC" + " "*22 + "Vendor")
    f.write("\n" + "="*68)
    for client in clients:
        f.write("\n{:16}    {}".format(client['ip'], client['Vendor(MAC)']))
    f.write("\n" + "="*68)
    f.write("\n")
    f.write("\nNetwork scanned at: " + datetime_string)
    f.close()
    print("")
    print("Results saved: "+ cwd_str + "saved/"+ dt_file_str + "_network-scan.txt")
    print("")
if saveout.capitalize() == "N":
    print("")
    print("Results not saved.")
    print("")
if saveout.capitalize() == "":
    print("")
    print("Results not saved.")
    print("")
if saveout.capitalize() != "Y" and saveout.capitalize() != "N":
    print("")
    print("Results not saved.")
    print("")



