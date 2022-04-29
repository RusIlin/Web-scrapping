import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'сервер', 'автомобиль', 'спутник', 'linux']
HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/100.0.4896.127 Safari/537.36'
    }
url = 'https://habr.com'
response = requests.get(url, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
all_words = soup.find_all(class_='tm-article-snippet')

for word in all_words:
    for keyword in KEYWORDS:
        if word.text.lower().find(keyword) > 0:
            data = word.find('time').get('title')
            header = word.find('h2').find('span').text
            link = word.find('h2').find('a').get('href')
            print(f'{data} {header} {url + link}')
