from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def getLinks(url):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, 'lxml')
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links

print( getLinks("https://www.walter-tools.com/en-us/search/pages/default.aspx#/product/A1247-3~2F16IN") )