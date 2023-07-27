from bs4 import BeautifulSoup
import requests

links=[]

for page in range(1, 4):
     url = "https://sid.ir/search/paper/%D8%B1%D9%88%D8%A7%D9%86%D8%B4%D9%86%D8%A7%D8%B3%DB%8C/fa/" + "?page=" +str(page)+"&sort=1&ftyp=all&fgrp=all&fyrs=1379%2c1402"
     furl = requests.get(url)
     jsoup = BeautifulSoup(furl.text , 'html.parser')
     productslist=[]
     for products in jsoup.find_all('p', class_="srtitle" ):
          products = products.find('a').get('href')
          p = productslist.append(products)


     for web in productslist:
          web='https://sid.ir/'+web

          a = requests.get(web)
          b = BeautifulSoup(a.content, 'html.parser')

          try:
              for link in b.find_all(id='downloadbottom'):
                  link = link.find('a').get('href')
                  l=links.append('sid.ir'+ link)
          except:
              continue






