import urllib
fhand=urllib.urlopen('http://www.google.com/about/')

for line in fhand:
    print line.strip()