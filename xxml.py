import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_703486.xml").read()
tree= ET.fromstring(url)

counts= tree.findall('.//count')
sum= 0
for i in counts:
    sum = sum + int(i.text)

print(sum)


