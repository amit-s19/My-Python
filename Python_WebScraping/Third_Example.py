import requests
from bs4 import BeautifulSoup

url = "http://yellowpages.in/search/hyderabad/tea"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
hrefs = soup.find_all('a')
for href in hrefs:
    print ("<a href='{0}'>{1}</a>".format(href.get('href'), href.text))

div_data = soup.find_all('div', {'class': 'popularTitleTextBlock'})
print("""

*************//////////\\\\\\\\\\\\************

""")
for elem in div_data:
    print(elem.text)

for elem in div_data:
    print(elem.contents)
    #print('\n')
