![GitHub License](https://img.shields.io/github/license/Exclavia/ExsNetworkScan?style=for-the-badge&logoSize=auto)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)
![PyPi](https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7)



# ExsNetworkScan
A simple network scanner written in Python using [Scapy](https://github.com/secdev/scapy).

![Network-Scanner](https://github.com/Exclavia/ExsNetworkScan/blob/master/Assets/git.png)


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
