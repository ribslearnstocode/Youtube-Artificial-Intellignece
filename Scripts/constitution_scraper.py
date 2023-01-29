
import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.pakistani.org/pakistan/constitution/"
BASE_URL = "https://www.pakistani.org"
dataset = []

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html5lib')

uls = soup.find('ul', attrs=['class', 'mine'])


for link in uls.find_all('a')[1:]:
    response = requests.get(BASE_URL+link['href'])
    soup = BeautifulSoup(response.text, 'html5lib')
    part = soup.find('h2').text
    try:
        chapter = soup.find_all('h2')[1].text
    except:
        chapter = ''
    
    tables = soup.find_all('table')
    for table in tables:
        rows = table.findChildren('tr')
        for row in rows:
            try:
                article_number = row.find('td').find('b').text
                article_title = row.find_all('td')[1].find('b').text.strip()
                article_desc_raw = row.find_all('td')[1]
                for sup in article_desc_raw('sup'):
                    sup.decompose()
                article_desc = article_desc_raw.text.strip().replace("  ","").replace("\n\n", "")

                article = {
                    "part" : part,
                    "chapter" : chapter,
                    "article_number" : article_number,
                    "article_title" : article_title,
                    "article_desc" : article_desc 
                }
                dataset.append(article)
                print(article)
            except:
                pass

    
    

with open("data.json", "w+") as jsonFile:
    jsonFile.write(json.dumps({"dataset" : dataset}))
