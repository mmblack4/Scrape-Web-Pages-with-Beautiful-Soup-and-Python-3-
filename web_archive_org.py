import requests
import csv
from bs4 import BeautifulSoup

page=requests.get('https://web.archive.org/web/20170131230332/https://www.nga.gov/collection/anA1.htm')

soup=BeautifulSoup(page.text, 'html.parser')

f=csv.writer(open('a-artist-names.csv','w'))
f.writerow(['name','link'])

contents_name_list=soup.find(class_='BodyText')
contents_name_item=contents_name_list.find_all('a')
for contents_name in contents_name_item:
	names=contents_name.contents[0]
	links='https://web.archive.org'+contents_name.get('href')
	f.writerow([names,links])