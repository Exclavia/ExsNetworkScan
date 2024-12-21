from scapy.all import ARP, Ether, srp
import socket
import requests
import time
import os
from datetime import datetime
import cursor

# Path to Config files
gwc_path = "Config/default_gateway.ini"
api_path = "Config/apiKey.ini"



cwd_str = str(os.getcwd()).replace("\\", "/") + "/"

# Global list for scanned items
clients = []


def clear_console():
    """Clears the console."""
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)


# Get vendor names based on mac address
def get_mac_details(mac_address, use_api=False):
    
    if use_api == True:
        apiKey = open(api_path, "r").readline()
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
    
    if use_api == False:
        # Same as above
        # No api key, so results may be rate limited
        url = "https://api.maclookup.app/v2/macs/"
        # Sleeps for 1 second to combat rate limit.
        time.sleep(1)
        response = requests.get(url+mac_address)
        if response.status_code != 200:
            return "[ Unknown Vendor ]"
        API_Data = response.json()
        if API_Data['company'] == "":
            return "[ Unknown Vendor ]"
        return API_Data['company']


# If no devices are found
# the gateway most likely is set incorrectly.
def no_devices(default_gateway):
    clear_console()
    gateway = default_gateway
    print("")
    print(" No devices found in the network.")
    print(" Make sure your default gateway is set in the Config/default_gateway.ini file.")
    print("")
    print(" Current gateway set: " + gateway)
    print("")
    exit()



# Save result function
def result_options(api_check, current_gateway, dtstr, dtstr_file):
    setApi = api_check
    gateway = current_gateway
    datetime_string = dtstr
    dt_file_str = dtstr_file
    
    cursor.show()
    print("")
    print("[0] Save results and exit")
    print("[1] Save results and run again")
    print("[2] Run again without saving")
    print("[3] Exit without saving")
    print("")
    saveout = input("[0/1/2/3]: ")
    if saveout == "0":
        # Saves to the saved/ folder that comes with the script.
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
        exit()
        
        
        
    if saveout == "1":
        # Saves to the saved/ folder that comes with the script.
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
        print("Running again...")
        time.sleep(1)
        net_scan(api_check=setApi, default_gateway=gateway)
        
        
        
    if saveout == "2":
        # No save, run again.
        print("")
        print("Results not saved.")
        print("")
        print("Running again...")
        time.sleep(1)
        net_scan(api_check=setApi, default_gateway=gateway)
        
        
    if saveout == "3":
        # No save, exit.
        print("")
        print("Results not saved.")
        print("")
        exit()
        
    # Catch for any invalid inputs.
    if saveout != "0" and saveout != "1" and saveout != "2" and saveout != "3":
        print("")
        print("Invalid option!")
        print("")
        result_options(api_check=setApi, current_gateway=gateway, dtstr=datetime_string, dtstr_file=dt_file_str)
        

# Overall net scanning function
# api_check (bool) - If using api key or not.
# default_gateway - Pretty self explanatory.
def net_scan(api_check, default_gateway):
    clear_console()
    cursor.hide()
    clients.clear()
    gateway = default_gateway
    
    # Set date/time of run
    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    dt_file_str = current_datetime.strftime('%Y-%m-%d_%H.%M.%S')
    
    # '/24' - Checks IP on network 1 - 255 ( 192.168.1.xxx)
    target_ip = gateway + "/24"
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    
    # Keeps track of found devices
    i = 0
    
    # If using api key.
    if api_check == True:
        print(" Scanning network...")
        print("")
        
        for sent, received in result:
            # for each response, append ip, mac address, and vendor to `clients` list
            getBrand = get_mac_details(str(received.hwsrc), use_api=True)
            if len(getBrand) > 20:
                vndr = getBrand[0:20] + "..."
            if len(getBrand) < 20:
                vndr = getBrand
            clients.append({'ip': received.psrc, 'Vendor(MAC)': str(received.hwsrc) + " "*8 + vndr})
            
            i = i + 1
            if i > 0:
                # Console out as devices are scanned.
                print(" " + str(i) + " device(s) found...")

        if i == 0:
            no_devices(gateway)
        if i > 0:
            # Sends to print function (along with gateway and device count)
            network_print(apiCheck=True, default_gateway=gateway, device_count=i, current_dt=datetime_string, cdt_file=dt_file_str)
            
    # No api key.        
    if api_check == False:
        print(" Scanning network...")
        print(" No API key set. Vendor lookup may be rate limited.")
        print("")
        
        for sent, received in result:
            getBrand = get_mac_details(str(received.hwsrc), use_api=False)
            if len(getBrand) > 20:
                vndr = getBrand[0:20] + "..."
            if len(getBrand) < 20:
                vndr = getBrand
            clients.append({'ip': received.psrc, 'Vendor(MAC)': str(received.hwsrc) + " "*8 + vndr})
            
            i = i + 1
            if i > 0:
                print(" " + str(i) + " device(s) found...")

        if i == 0:
            no_devices(gateway)
        if i > 0:
            network_print(apiCheck=False, default_gateway=gateway, device_count=i, current_dt=datetime_string, cdt_file=dt_file_str)


# Print/Console out function
def network_print(apiCheck, default_gateway, device_count, current_dt, cdt_file):
    clear_console()
    api = apiCheck
    gateway = default_gateway
    i = device_count
    datetime_string = current_dt
    dt_string_file = cdt_file
    
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
    # Calls save function.
    result_options(api_check=api, current_gateway=gateway, dtstr=datetime_string, dtstr_file=dt_string_file)
    
    

# Configuration check/setting. Also acts as main starting function.

def config_set():
    
    clear_console()
    
    # Checks if gateway/api key is set first to be able to skip other checks if true.
    if os.path.exists(gwc_path) and os.path.exists(api_path):
        gateway = open(gwc_path, "r").readline()
        net_scan(api_check=True, default_gateway=gateway)

    # Check/Set for API Key.
    # Setting an API key is entirely optional.
    
    if os.path.exists(gwc_path) and os.path.exists(api_path) == False:
        cursor.show()
        print("No API key set (Get one for free at https://my.maclookup.app/)")
        api_ask = input("Would you like to set a key? [y/n]: ")
        
        if api_ask.capitalize() == "Y":
            clear_console()
            key_in = input("Input your API Key:\n")
            open(api_path, "w").write(key_in)
            clear_console()
            print("API key set!")
            time.sleep(0.5)
            
            gateway = open(gwc_path, "r").readline()
            net_scan(api_check=True, default_gateway=gateway)
            
        if api_ask.capitalize() == "N":
            gateway = open(gwc_path, "r").readline()
            net_scan(api_check=False, default_gateway=gateway)
            
        if api_ask.capitalize() != "Y" and api_ask.capitalize() != "N":
            print("")
            print("Invalid input.")
            config_set()
            
    # Check/Set for Gateway IP
    # Not optional, gateway HAS to be set. Program won't continue otherwise.
    # No checks for whether the gateway entered is proper/correct though.
    # If not: no_device() function will catch.
    if os.path.exists(gwc_path) == False:
        
            cursor.show()
            
            print("No gateway IP set.")
            ip_in = input("Please set your default gateway IP: ")
            if ip_in == "":
                print("")
                print("Gateway IP cannot be blank!")
                time.sleep(1)
                config_set()
                
            open(gwc_path, "w").write(ip_in)
            clear_console()
            print(ip_in + " set as gateway IP.")
            time.sleep(0.5)
            config_set()
            



config_set()

    

    



