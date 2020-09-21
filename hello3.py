import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Yahya.html").read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
sum = 0
for i in tags:
    sum = sum+int(i.contents[0])
print(sum)
