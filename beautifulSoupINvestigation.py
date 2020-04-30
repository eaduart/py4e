#!/usr/bin/env python3
"""This is my investigation into a data strucutre so that I can better understand the 
   beautifulsoup library."""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
from object_discovery import object_discovery

URL="https://www.google.com"
result = requests.get(URL)

print("Details for object result:")
print(id(result))
object_discovery(result, True, 'result')


src = result.content

soup = BeautifulSoup(src, features="html.parser")
print("Details for object result:")
print(id(soup))
object_discovery(soup)
