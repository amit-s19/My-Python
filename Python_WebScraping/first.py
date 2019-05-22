# First implementation of BeautifulSoup and Requests module.
import requests
from bs4 import BeautifulSoup

# get method used to get the content of the requested webpage.
result = requests.get('https://www.google.co.in')

# stats_code gives the connection code, 200 if successfull and the page exists, 404 otherewise and etc...
print('Status code = ', result.status_code)

# headers displays extra information related to that webpage.
print(result.headers)
print('\n')

# src method to retrieve the content from the result of "get".
src = result.content
print(src)

# Now using BeautifulSoup to parse and process the extracted information.
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')
for _ in links:
    print(_)
print('\n')

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])
