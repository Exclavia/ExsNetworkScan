

# ExsNetworkScan



<a href="https://test.pypi.org/project/ExsNetworkScan/" target="_blank"><img alt="TestPyPi" src="https://img.shields.io/pypi/status/ExsNetworkScan?pypiBaseUrl=https%3A%2F%2Ftest.pypi.org&style=flat-square&label=TestPyPi"></a>
<a href="https://git.exclavia.network/license/" target="_blank"><img alt="GitHub License" src="https://img.shields.io/github/license/Exclavia/ExsNetworkScan?style=flat-square"></a>
<a href="https://git.exclavia.network/ExsNetworkScan" target="_blank"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fgit.exclavia.network%2FExsNetworkScan?style=flat-square"></a>


![Network-Scanner](https://raw.githubusercontent.com/Exclavia/ExsNetworkScan/refs/heads/master/Assets/git.png)

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

 > I'm not entirely sure how much of Scapy is required to run it (as there are some optional dependencies you can opt out of, but I'm fairly certain you are going to most likely need [npcap](https://npcap.com/),
 > however you can try running it first to see if you can just use the base Scapy package.


### Download master.zip
- [Download](https://github.com/Exclavia/ExsNetworkScan/archive/refs/heads/master.zip)
