from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/comments_1689836.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
count = 0

# Retrieve all of the anchor tags
lines = soup('td')
for line in lines:
    numbers = re.findall('[0-9]+',str(line))
    if len(numbers)>=1:
        sum+=1
        count+=int(numbers[len(numbers)-1])

print(count)