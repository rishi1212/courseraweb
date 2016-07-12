import urllib
import xml.etree.ElementTree as ET

url='http://python-data.dr-chuck.net/comments_298006.xml'
counts=[]
page=urllib.urlopen(url)
tree=ET.parse(page)

comments=tree.findall('comments/comment')

for comment in comments:
    counts.append(int(comment.find('count').text))
print sum(counts)