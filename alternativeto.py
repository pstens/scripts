import requests
import sys
from bs4 import BeautifulSoup as BS

base_url = "https://alternativeto.net/software/{}/"


def parse(url):
    r = requests.get(base_url.format(url))
    soup = BS(r.text, 'html.parser')
    app_list = soup.find('ul', {'class': 'app-list alternative-list'})
    list_items = app_list.find_all('article', {'class': 'row app-list-item'})
    for item in list_items:
        alternative = item.find('h3').find('a')
        print(alternative.string)


def usage():
    print('usage: python3 donotbugme.py <host>')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        software = sys.argv[1]
        print('Fetching alternatives for {}:'.format(software))
        parse(software)
