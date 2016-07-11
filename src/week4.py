import urllib
from BeautifulSoup import *

url=('http://python-data.dr-chuck.net/comments_298009.html')

html=urllib.urlopen(url).read()
soup=BeautifulSoup(html)
tags=soup('span')
sum1=0
for tag in tags:
    sum1+=int( tag.contents[0])
print sum1