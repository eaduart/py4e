#!/usr/bin/env python3
'''Json sum of data.'''

import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

# from pprint import pprint
# import sys

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

URL = input("Enter URL:")
UH = urllib.request.urlopen(URL, context=CTX)
DATA = UH.read().decode()

# pprint(DATA)
INFO = json.loads(DATA)

TOTAL = 0
COUNT = 0

for item in range(len(INFO['comments'])):
    TOTAL += int(INFO["comments"][item]['count'])
    COUNT += 1

print("count: " + str(COUNT))
print("total: " + str(TOTAL))
