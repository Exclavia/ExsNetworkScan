from scapy.all import ARP, Ether, srp
import time
import requests
import configparser
from CMods.system import *

config = configparser.ConfigParser()
ini_file = "exnsConfig.ini"

clients = []

def get_mac_details(mac_address, use_api=False):
    """Get vendor names based on MAC address."""
    apiKey = config["apiKey"].get("key") if use_api else None
    url = f"https://api.maclookup.app/v2/macs/{mac_address}"
    if apiKey:
        url += f'?apiKey={apiKey}'
    
    time.sleep(1 if not use_api else 0)  # Sleep only if not using API key
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get('company', "[ Unknown Vendor ]")
    return "[ Unknown Vendor ]"

def new_gateway():
    if input(" Would you like to change the currently set default gateway IP? [y/n]: ").strip().lower() == "y":
        new_ip = input(" Please enter a new gateway IP: ").strip()
        if new_ip and new_ip.replace(".", "").isnumeric():
            config["DefaultGateway"]["ip"] = new_ip
            with open(ini_file, "w") as f:
                config.write(f)
            print(f" {new_ip} set as gateway IP.")
            time.sleep(0.5)
            main()
        else:
            print(" Please enter a valid IP address.")
            time.sleep(0.5)
            clear_console()
            new_gateway()
    else:
        exit_program(0)
            
            

def no_devices(default_gateway):
    """Handle case when no devices are found."""
    clear_console()
    print(f"\n No devices found in the network.\n Make sure your default gateway is set in the {cwd()}\\exnsConfig.ini file.\n Current gateway set: {default_gateway}\n")
    new_gateway()
                
    

def save_results(dt_file_str, datetime_string):
    """Save scan results to a file."""
    with open(f"{dt_file_str}_network-scan.txt", "w") as f:
        f.write("IP" + " " * 18 + "MAC" + " " * 22 + "Vendor\n")
        f.write("=" * 68 + "\n")
        for client in clients:
            f.write(f"{client['ip']:16}    {client['Vendor(MAC)']}\n")
        f.write("=" * 68 + f"\n\nNetwork scanned at: {datetime_string}\n")
    print(f"\nResults saved: {cwd()}\\{dt_file_str}_network-scan.txt\n")

def result_options(api_check, current_gateway, dtstr, dtstr_file):
    """Handle user options after scanning."""
    cursor(True)
    print("\n[0] Save results and exit\n[1] Save results and run again\n[2] Run again without saving\n[3] Exit without saving\n")
    
    while True:
        saveout = input("[0/1/2/3]: ")
        if saveout in {"0", "1", "2", "3"}:
            break
        print("\nInvalid option!\n")
    
    if saveout in {"0", "1"}:
        save_results(dtstr_file, dtstr)
        if saveout == "1":
            time.sleep(1)
            net_scan(api_check, current_gateway)
        exit_program(0)
    
    if saveout in {"2", "3"}:
        if saveout == "2":
            print("\nResults not saved.\n")
            time.sleep(1)
            net_scan(api_check, current_gateway)
        exit_program(0)

def net_scan(api_check, default_gateway):
    """Perform network scanning."""
    clear_console()
    cursor(False)
    clients.clear()
    
    current_datetime = cdt()
    datetime_string = stringify_datetime(current_datetime)
    dt_file_str = filename_datetime(current_datetime)
    
    target_ip = f"{default_gateway}/24"
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]
    
    print(" Scanning network...\n")
    
    for i, (sent, received) in enumerate(result, start=1):
        vndr = get_mac_details(str(received.hwsrc), use_api=api_check)
        vndr_display = (vndr[:20] + "...") if len(vndr) > 20 else vndr
        clients.append({'ip': received.psrc, 'Vendor(MAC)': f"{str(received.hwsrc)}    {vndr_display}"})
        print(f" {i} device(s) found...")

    if not clients:
        no_devices(default_gateway)
    
    network_print(api_check, default_gateway, len(clients), datetime_string, dt_file_str)

def network_print(apiCheck, default_gateway, device_count, current_dt, cdt_file):
    """Print the network scan results."""
    clear_console()
    print(f"\n {device_count} available devices in the network [Gateway - {default_gateway}]:\n")
    print("  IP" + " " * 18 + "MAC" + " " * 22 + "Vendor")
    print("  " + "=" * 68)
    
    for client in clients:
        time.sleep(0.02)
        print(f"  {client['ip']:16}    {client['Vendor(MAC)']}")
        
    print("  " + "=" * 68 + f"\n\n Network scanned at: {current_dt}\n")
    result_options(apiCheck, default_gateway, current_dt, cdt_file)

def main():
    """Check and set configuration for gateway and API key."""
    clear_console()
    
    if not os.path.exists(ini_file):
        config.add_section("DefaultGateway")
        config.add_section("apiKey")
        config.set("DefaultGateway", "IP", "")
        config.set("apiKey", "Key", "")
        with open(ini_file, "w") as configfile:
            config.write(configfile)
            
    config.read(ini_file)        
    gateway = config["DefaultGateway"].get("ip", "")
    api_key = config["apiKey"].get("key", "")
    
    if gateway:
        if api_key:
            net_scan(api_check=True, default_gateway=gateway)
        else:
            if input("No API key set (Free at https://my.maclookup.app/). Would you like to set a key? [y/n]: ").strip().lower() == "y":
                key_in = input("Input your API Key:\n").strip()
                if key_in:
                    try:
                        if api_check(key_in):
                            config["apiKey"]["key"] = key_in
                            with open(ini_file, "w") as f:
                                config.write(f)
                            print("API key set!")
                            time.sleep(0.5)
                            net_scan(api_check=True, default_gateway=gateway)
                        else:
                            print("Error in API Key")
                            time.sleep(1)
                            main()
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        exit_program(1)
                else:
                    print("API Key cannot be blank!")
                    time.sleep(1)
                    main()
            else:
                net_scan(api_check=False, default_gateway=gateway)
    else:
        ip_in = input("No gateway IP set. Please set your default gateway IP: ").strip()
        if ip_in and ip_in.replace(".", "").isnumeric():
            config["DefaultGateway"]["ip"] = ip_in
            with open(ini_file, "w") as f:
                config.write(f)
            print(f"{ip_in} set as gateway IP.")
            time.sleep(0.5)
            main()
        else:
            print("Please enter a valid IP address.")
            time.sleep(0.5)
            main()

try:
    main()
except Exception as e:
    print(f"An error occurred: {e}")
    exit_program(1)
