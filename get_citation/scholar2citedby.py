import bs4 as bs
from urllib.request import Request, urlopen
import re


def scholar2citedby(string):
    title = re.sub(' ', '+', string)
    print(title)
    req = Request('https://scholar.google.se/scholar?hl=en&q={}&num=1'.format(title), headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs.BeautifulSoup(webpage, 'lxml')

    for paragraph in soup.find_all('div', class_='gs_fl'):
        if 'Cited by' in paragraph.text:
            print(paragraph.text.split('Cited by')[1].split(None, 1)[0])


scholar2citedby('Aron Skaftason')
