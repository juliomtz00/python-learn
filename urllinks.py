# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

position = int(input('Enter position:'))
count = int(input('Enter count:'))
print(f"Retrieving: {url}")

# Retrieve all of the anchor tags

while((count-1)>=0):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for x in range(len(tags)):
        if x == position-1:
            tag = tags[x]
            url = tag.get('href', None)
            print(f"Retrieving: {url}")
            break
    count-=1