import urllib.request, urllib.parse,urllib.error,urllib

from bs4 import BeautifulSoup

#url = 'http://python-data.dr-chuck.net/known_by_Conar.html'

count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Yahya.html").read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')


for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')