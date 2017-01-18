import json
import urllib

url='http://python-data.dr-chuck.net/comments_298010.json'

data =urllib.urlopen(url).read()

info = json.loads(data)
comments=info["comments"]

counts=[]

for comment in comments:
    counts.append(int(comment['count']))

print(sum(counts))
