
from bs4 import BeautifulSoup
import concurrent
import concurrent.futures

import requests

main_url = 'https://www.olx.ua'
url = 'https://www.olx.ua/d/uk/zapchasti-dlya-transporta/avtozapchasti/kuzovnyye-zapchasti/'


def request_post(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('h3')
        quotes2 = soup.find_all('h4')
        div = soup.find('div', {"class": "swiper-zoom-container"})
        print(div.find('img').attrs['src'])
        print(quotes2[0].text, quotes[0].text)
        return "YES"
    except:
        ...


if __name__ == '__main__':
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h6')
    print(len(quotes))
    urls = []
    for i in quotes:
        div = i.findParent('a', href=True)
        url = main_url + div['href']
        urls.append(url)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(request_post, url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


    #     print(i.parent.parent.parent)
    #     print(div.find('img').attrs['src'])
    # print(quotes.parent)














