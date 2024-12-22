import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://kinoogo.zone/'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request



def get_data(html):
    bs = BS4(html, features='html.parser')
    items = bs.find_all('div', class_='col-main flex-grow-1 d-flex fd-column')
    kinoogo_list = []
    for item in items:
        title = item.find('div', class_='card__title').get_text(strip=True)
        image = URL + item.find('div', class_='card__img img-fit-cover').find('img').get('src')
        description = item.find('div', class_='card__text line-clamp').get_text(strip=True)
        watch_online = URL + item.find('div', class_='card__btn btn').find('a').get('href')
        kinoogo_list.append(
            {
                'title': title,
                'image': image,
                'description': description,
                'watch_online': watch_online,
            }
        )
        return kinoogo_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        kinoogo_list2 = []
        for page in range(1,2):
            response = get_html("https://kinoogo.zone/filmy/2024/", params={"page": page})
            kinoogo_list2.extend(get_data(response.text))
        return kinoogo_list2
    else:
        raise Exception('Error in parsing')


