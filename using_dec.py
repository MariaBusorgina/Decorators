import os
import bs4
import requests
from fake_headers import Headers
from utils import decorator_logger_path

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = 'https://habr.com/ru/all/'

path = os.path.relpath(path='parser.txt', start=None)


@decorator_logger_path(path)
def parser(list_words, url):
    header = Headers().generate()
    response = requests.get(url, headers=header)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    article = soup.find_all('article')
    result = []
    for item in article:
        item_text = item.text.lower()

        for word in list_words:
            if word in item_text:
                data = item.find("time")["title"].split(",")[0]
                title = item.find("h2").text
                href = item.find(class_="tm-article-snippet__title-link").attrs["href"]

                res = f'{data} - {title} - https://habr.com{href}'
                result.append(res)
                print(res)
                print(" ")

    return result


if __name__ == '__main__':
    parser(KEYWORDS, URL)
