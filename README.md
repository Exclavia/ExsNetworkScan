![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

# Network Scanner - ![GitHub License](https://img.shields.io/github/license/Exclavia/gpl2)
A simple network scanner written in Python using [Scapy](https://github.com/secdev/scapy).

![Network-Scanner](https://github.com/Exclavia/Network-Scanner/blob/master/Assets/git.png)


 ## Usage and Setup
 You can either run via the `run.bat` or by running the `main.py` script.

<br>
 
 On first run you will be prompted to set your default gateway IP and to set an API Key for the vendor lookup service.
 - To get your gateway IP, open command prompt and type: `ipconfig` <sup> Will be labeled as Default Gateway </sup>

 <br>
To get an API Key (It's free and it stops lookup rate limits), create an account at https://my.maclookup.app/login

 ## Requirements

```
cd Network-Scanner
pip install -r requirements.txt
```

  or just make sure you grab [Scapy](https://github.com/secdev/scapy) and [Cursor](https://github.com/GijsTimmers/cursor)

 > [!NOTE]
 > I'm not entirely sure how much of Scapy is required to run it (as there are some optional dependencies you can opt out of, but I'm fairly certain you are going to most likely need [npcap](https://npcap.com/),
 > however you can try running it first to see if you can just use the base Scapy package.

 > [!WARNING]
> Has not been tested on anything besides Windows.
