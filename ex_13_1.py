from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    num = tag.contents[0]
    count += 1
    try:
        total += int(num)
    except:
        print("is not a number")
        quit()
print('Count: ', count)
print('Total: ', total)
