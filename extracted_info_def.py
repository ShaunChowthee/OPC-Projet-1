import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
response = requests.get(url)
page = response.content

def extract_book_info(url):
    response = requests.get(url)

    dict = {}

    page = response.content
    soup = BeautifulSoup(page, "html.parser")

    dict["title"] = soup.find("h1") #Title

    dict["page_url"] = response.url  # Page URL

    description = soup.find(id="product_description")
    if description is not None:
        dict["product_description"] = description.find_next_sibling("p")
    else:
        dict["product_description"] = " "

    product_information_table = soup.find("table")
    dict["product_tds"] = product_information_table.find_all("td")

    image_url = soup.find("img")
    dict["src"] = image_url.get("src")

    header = soup.find(class_="breadcrumb")
    dict["category"] = header.findAll("li")

    star_rating = soup.find(class_="star-rating")
    dict["review_rating"] = star_rating.attrs
    for keys, values in dict["review_rating"].values():
        dict["review_rating_number"] = values

    #print(dict["page_url"])
    #print(dict["product_tds"][0].get_text())
    print(dict["title"].string)
    #print(dict["product_tds"][2].string)
    #print(dict["product_tds"][3].string)
    #print(dict["product_tds"][5].string.split()[2][1:])
    #print(dict["product_description"].string)
    print(dict["category"][2].get_text())
    #print(values)
    #print(dict["src"].replace("../..", "https://books.toscrape.com"))


    return dict

r = extract_book_info(url)

