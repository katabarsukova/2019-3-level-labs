import requests
from bs4 import BeautifulSoup

page_url= 'https://lenta.ru/rubrics/russia/'

lenta_russia_req = requests.get(page_url)

lenta_text = lenta_russia_req.text

if lenta_russia_req.status_code==200:
    #print(lenta_text)
    print('wow you are genius!!!')
else:
    print('something went wrong')

parsed_page = BeautifulSoup(lenta_text)

#print(parsed_page)

print(parsed_page.title.text)

