# SyriaCTF – Dega

* **Category: Digital Forensics
* **Points: 200

## Solution

The solution.

We exported the objects from the pcap file and browse through them and we deleted all of the html files then we noticed that there is some base64 code divided into parts each part in a file....
We wrote a script [filter.py](filter.py) and extracted the parts and merged them together. then we urldecode it because we noticed some url encoded characters, after that we got a json file with a field called payload. Again with base64 we find another json file.. so we recursivly decode the json files to get the flag [solve.py](solve.py)

solved by jeebaleepa and thecarrot