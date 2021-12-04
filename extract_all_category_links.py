import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/index.html"
response = requests.get(url)
page = response.content


def extract_all_category_links():
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    all_category_links_list = []

    class_category_links = soup.find(class_="side_categories")
    all_category_links = class_category_links.findAll("li")
    for link in all_category_links:

        a = link.find('a')
        try:
            if 'href' in a.attrs:
                data = a.get('href')
                all_category_links_list.append("https://books.toscrape.com/"+data)
        except:
            pass
    return all_category_links_list

all_cat_links = []

lst = extract_all_category_links()
for i in lst:
    all_cat_links.append(i.replace("index.html", "page-1.html"))

del all_cat_links[0]

print(all_cat_links)