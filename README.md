
# Network Scanner
A simple network scanner written in Python using [Scapy](https://github.com/secdev/scapy).

## Download & setup
Download and unzip [master package](https://github.com/tjwehler/Network-Scanner/archive/refs/heads/master.zip)

or clone the git:
```
git clone https://github.com/tjwehler/Network-Scanner
```

 - You **have** to make sure to set your networks default gateway IP in the [config](https://github.com/tjwehler/Network-Scanner/blob/master/default_gateway.config) file.

      Easy way to get your default gateway IP is to just open **command prompt** and type: `ipconfig`

      Your gateway IP (A common one is `192.168.1.1`, however this is not standard) will be labeled as `Default Gateway` usually at the bottom of the list on whichever network adapter you use.

- You also need an API key for the mac address lookup service. It's free at [maclookup.app](https://my.maclookup.app/)

    Once you get a key, replace the line in the [apikey](https://github.com/tjwehler/Network-Scanner/blob/master/apikey.config) config.

 ## Usage
 You can either run via the `run.bat` or by running the `main.py` script.

 ## Requirements

 ```
cd Network-Scanner
pip install -r requirements.txt
```

  or just make sure you grab [Scapy](https://github.com/secdev/scapy) and [Cursor](https://github.com/GijsTimmers/cursor)
 
  I'm not entirely sure how much of Scapy is required to run it (as there are some optional dependencies you can opt out of, but I'm fairly certain you are going to most likely need [npcap](https://npcap.com/),
 however you can try running it first to see if you can just use the base Scapy package.

 
