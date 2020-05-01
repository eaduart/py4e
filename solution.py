#!/usr/bin/env python3
'''This another xml read.'''

import urllib.request
import xml.etree.ElementTree as ET
import sys
# from object_discovery import object_discovery

URL = input('Enter location: ')

# try:
FHAND = urllib.request.urlopen(URL)
# except:
#    print("Error opening: " + URL)
#    sys.exit(1)

try:
    TREE = ET.parse(FHAND)
# except xml.etree.ElementTree.ParseError:
except ET.ParseError:
    print("Error XML parsing: " + URL)
    ERROR = sys.exc_info()[0]
    print("Exception: " + str(ERROR))
    sys.exit(1)

LST = TREE.findall('comments/comment/count')

COUNT = 0
TOTAL = 0
for item in LST:
    COUNT += 1
    TOTAL += int(item.text)

print("count: " + str(COUNT))
print("total: " + str(TOTAL))
