from bs4 import BeautifulSoup
import requests
import locale
from datetime import datetime

url = 'https://happycoin.club/cryptocurrencies-news/'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
news = soup.find_all(class_='grid-list-content')
news_list = []
for new in news:
    locale.setlocale(locale.LC_ALL, '')
    if new.find('li').text == datetime.now().strftime("%d %B, %Y"):
        new_list = []
        url_new= new.find('h4').find('a').get('href')
        html_new = requests.get(url_new)
        soup_new = BeautifulSoup(html_new.text, 'html.parser')
        title = new.find('h4').find('a').text
        new_list.append(title)
        category = 4
        new_list.append(category)
        img = soup_new.find('img', class_='img-responsive').get('src')
        new_list.append(img)
        content_new = soup_new.find(class_='single-post-text').find_all('p')
        content= []
        for paragraph in content_new:
            content.append(paragraph.text)
        content.pop()
        content.pop()
        new_list.append(content)
        news_list.append(new_list)
print(news_list)

        
    