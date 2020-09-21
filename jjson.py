import urllib.request, urllib.parse,urllib.error
import json

url ="http://py4e-data.dr-chuck.net/comments_703487.json"
y = urllib.request.urlopen(url)
data = y.read()
sum=0

x = json.loads(data)
for i in x["comments"]:
    sum = sum + int(i["count"])
print(sum)
