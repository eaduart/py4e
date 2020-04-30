# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
repeat = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

for i in range(repeat):
    #print(i)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
#    exit(0)
    if len(tags) >= position:
        name = list(tags[position].children)[0]
        print(name)
        print(tags[position].get('href',None))
        #print(type(tags[position].get('href',None)))
        url = tags[position].get('href',None)
#    for tag in tags:
#	print(tag.get('href', None))
