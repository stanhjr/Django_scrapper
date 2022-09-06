import concurrent.futures
import time

import requests
from bs4 import BeautifulSoup

from home.models import OlxModel

start = time.time()

main_url = 'https://www.olx.ua'
URL = 'https://www.olx.ua/d/uk/hobbi-otdyh-i-sport/muzykalnye-instrumenty/'


def string_to_price(string_: str) -> tuple:
    list_ = string_.split(' ')
    result_string = ''
    for elem in list_:
        if elem.isnumeric():
            result_string += elem
        elif elem[0] == '$':
            return int(result_string) * 100, int(int(result_string) * 36.6 * 100)
        elif elem[0] == 'г':
            return int(result_string) * 100, int(int(result_string) / 36.6 * 100)


def get_one_page_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        prices_h3 = soup.find_all('h3')[0]
        quotes2 = soup.find_all('h4')
        title = soup.find_all('h1')[0].text
        div = soup.find('div', {"class": "swiper-zoom-container"})
        src = div.find('img').attrs['src']
        src = "https" + src.split("https")[1]
        name = quotes2[0].text
        price = prices_h3.text

        price_grv, price_dollar = string_to_price(price)
        if name and title and src and price_grv and price_dollar and src:
            olx_model = OlxModel.objects.create(tittle=title,
                                                name=name,
                                                price_dollar=price_dollar,
                                                price_grv=price_grv,
                                                src=src)

            olx_model.save()
            print("save")

        return True
    except:
        return False


def get_links(olx_url, count_links):
    urls = []
    count = 0
    count_pages = 1
    while count_links > count:
        print(count)
        response = requests.get(olx_url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('h6')
        for elem in quotes:
            div = elem.findParent('a', href=True)
            url = main_url + div['href']
            urls.append(url)
            count = len(urls)
        if count_links < count:
            count_pages += 1
            olx_url = f'{URL}?page={count_pages}'
    return urls


def get_links_in_one_page(olx_url):
    urls = []
    response = requests.get(olx_url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h6')
    for elem in quotes:
        div = elem.findParent('a', href=True)
        url = main_url + div['href']
        urls.append(url)
    return urls


def get_all_links(count_of_links: int) -> list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for url in range(1, count_of_links // 50 + 1):
            if url > 1:
                olx_url = f'{URL}?page={url}'
            else:
                olx_url = URL
            print(olx_url)
            futures.append(executor.submit(get_links_in_one_page, olx_url=olx_url))
        for future in concurrent.futures.as_completed(futures):
            futures += future.result()

        return futures


def start_parser(count_of_links: int):
    urls = get_all_links(count_of_links)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(get_one_page_data, url=url))


if __name__ == '__main__':
    start_parser(count_of_links=320)

print(time.time() - start)
