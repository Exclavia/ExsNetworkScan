




# ExsNetworkScan


![PyPI - Status](https://img.shields.io/pypi/status/ExsNetworkScan?pypiBaseUrl=https%3A%2F%2Ftest.pypi.org&style=flat-square) 
![GitHub License](https://img.shields.io/github/license/Exclavia/ExsNetworkScan?style=flat-square)

![Network-Scanner](https://i.imgur.com/97i705Y.png)

A simple network scanner written in Python using [Scapy](https://github.com/secdev/scapy).

 ## Usage and Setup
 
 Install with pip:
 ```
pip install -i https://test.pypi.org/simple/ ExsNetworkScan
```

<br>

To run, just type command:  `netscan`

<br>
 
 On first run you will be prompted to set your **default gateway IP** and to set an **API Key** for the vendor lookup service.
 - To get your **gateway IP**, open command prompt and type: `ipconfig` *- Will be labeled as Default Gateway*

 <br>

 **API Key (Optional but recommended):**\
To get an API Key (It's free and it stops lookup rate limits), create an account at https://my.maclookup.app/login

 ## Dependencies

 - [Scapy](https://github.com/secdev/scapy)
 - [Cursor](https://github.com/GijsTimmers/cursor)

<br>

 > [!NOTE]
 > I'm not entirely sure how much of Scapy is required to run it (as there are some optional dependencies you can opt out of, but I'm fairly certain you are going to most likely need [npcap](https://npcap.com/),
 > however you can try running it first to see if you can just use the base Scapy package.
