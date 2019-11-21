# geändert auf dem iPad mit Pythonista 3
import re, urllib.request
htmlSource = urllib.request.urlopen("http://www.spiegel.de").read(200000).decode('utf-8')
linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
for link in linksList:
    print(link)
