import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/travel_2/page-1.html"
response = requests.get(url)
page = response.content

def extract_category(url, i):
    response = requests.get(url)
    lst =[]
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    category_all_books = []

    for link in soup.findAll(class_="image_container"):

        a = link.find('a')
        try:
            if 'href' in a.attrs:
                data = a.get('href')
                category_all_books.append(data)

        except:
            pass

    for data in category_all_books:
        lst.append(data.replace("../../..", "https://books.toscrape.com/catalogue"))

    url = url[:len(url) - 6]
    url += str(i + 1) + ".html"

    if response.status_code == 404:
        url = url.replace("page-2", "index")
        if response.status_code == 200:
            data = extract_category(url, i + 1)
            for i in data:
                lst.append(i)
        return lst


url_links = extract_category(url, 1)