import requests
import sys
from bs4 import BeautifulSoup as BS
from termcolor import cprint

base_url = "http://www.bugmenot.com/view/{}"
colors = ['red', 'yellow', 'green']


def get_color(rating):
    if 0 <= rating <= 20:
        return colors[0]
    elif 20 < rating <= 50:
        return colors[1]
    else:
        return colors[2]


def parse(url):
    r = requests.get(base_url.format(url))
    soup = BS(r.text, 'html.parser')
    accounts = soup.find_all('article')
    for (i, account) in enumerate(accounts):
        dds = account.find_all('dd')
        username = dds[0].string
        password = dds[1].string
        rating = int(account.find_all('li')[0].string.rsplit()[0][:-1])
        color = get_color(rating)
        cprint('{} - {}:{} ({}%)'.format(i, username, password, rating), color)


def usage():
    print('usage: python3 donotbugme.py <host>')
    sys.exit(1)


if __name__ == '__main__':
    if (len(sys.argv) < 2 or sys.argv[1].startswith('http')):
        usage()
    else:
        url = sys.argv[1]
        print('Fetching logins for {}:'.format(url))
        parse(url)
