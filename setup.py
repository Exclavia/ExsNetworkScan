import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ExsNetworkScan",
    version = "1.2.8",
    author = "Exclavia",
    author_email = "git@exclavia.network",
    description = "A simple network scanner written in Python using Scapy",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://test.pypi.org/project/ExsNetworkScan/",
    project_urls = {
        "Homepage": "https://git.exclavia.network/ExsNetworkScan",
        "Repository": "https://github.com/Exclavia/ExsNetworkScan.git",
        "Issues": "https://github.com/Exclavia/ExsNetworkScan/issues",
        "Changelog": "https://github.com/Exclavia/ExsNetworkScan/commits"
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Environment :: Console",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Utilities"
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.8"
)

print("Command: netscan to run a scan.")
