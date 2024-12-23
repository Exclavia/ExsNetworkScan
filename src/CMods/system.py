import os
import requests
from datetime import datetime
import configparser
import cursor as crs

# Load configuration once at the start
config = configparser.ConfigParser()
config.read("../exnsConfig.ini")

def exit_program(code):
    print("Exiting...")
    os._exit(code)

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cwd():
    """Returns current working directory."""
    return os.getcwd()

def cursor(visible):
    """Show/Hide console cursor."""
    crs.show() if visible else crs.hide()

def cdt():
    """Returns the current datetime."""
    return datetime.now()

def stringify_datetime(current_datetime):
    """Stringify/Safe filename datetime."""
    return current_datetime.strftime('%Y-%m-%d %H:%M:%S')

def filename_datetime(current_datetime):
    """Format datetime for filenames."""
    return current_datetime.strftime('%Y-%m-%d_%H.%M.%S')

def api_check(key):
    """Check if the API key is valid."""
    url = f"https://api.maclookup.app/v2/macs/C8:D7:19:FF:FF:FF?apiKey={key}"
    try:
        response = requests.get(url)
        return response.status_code != 401
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        exit_program(1)