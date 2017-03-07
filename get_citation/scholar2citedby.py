# Importing packages, Packages used BeautifulSoup for parsing text, urlib.request to get the webpage in raw format and re for
#  switching out from strings
import bs4 as bs
from urllib.request import Request, urlopen
import re

# Simple function to scrape 'cited by' form google.scholar
def scholar2citedby(string):
    title = re.sub(' ', '+', string) # swich out space for + with re
    req = Request('https://scholar.google.se/scholar?hl=en&q={}&num=1'.format(title), headers={'User-Agent': 'Mozilla/5.0'})
    # get url and add the searchword  the header command means what kind of browser it looks like it is comming form for the site
    webpage = urlopen(req).read() # open the url to get the raw page
    soup = bs.BeautifulSoup(webpage, 'lxml') # parse the page for better naviagion

    for paragraph in soup.find_all('div', class_='gs_fl'): # find specific tag on the page
        if 'Cited by' in paragraph.text:
            print(paragraph.text.split('Cited by')[1].split(None, 1)[0])
        # subset the string to get only the number

scholar2citedby('Aron Skaftason') # run the function
