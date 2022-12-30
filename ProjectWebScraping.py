
# Project Web Scraping

"""The brief

For this project we're going to be scraping a site called http://books.toscrape.com/. It's a purpose-built site for
learning how to scrape real websites.

What you need to do is scrape the front page of this site, and grab some data for every book on that page.

For each book, I want you to grab the title, the star rating, and the price. You should write all of this information
to a new file in CSV format.

Before you can do any of this, you need to get hold of the actual HTML document. To do this, add the following lines
to your file:

import requests

data = requests.get("http://books.toscrape.com/").content

Note that you will have to install the requests library, as it's not part of the standard library.

You have a few options for actually viewing the HTML. You can get hold of the data in a nice format by using the
prettify method on your soup, which you can write to a file or print to the console. You can also go to the site
directly and right click on the page. You should see an option to view page source. If you can't see this, try
pressing ctrl + u."""

import requests
from bs4 import BeautifulSoup

price_selector = ".price_color"
title_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

rating_mappings = {
    "One":   "★",
    "Two":   "★ ★",
    "Three": "★ ★ ★",
    "Four":  "★ ★ ★ ★",
    "Five":  "★ ★ ★ ★ ★"
}

def get_rating(tag):
    for term, rating in rating_mappings.items():
        if term in tag["class"]:
            return rating

rating_mappings = {
    "One":   "★",
    "Two":   "★ ★",
    "Three": "★ ★ ★",
    "Four":  "★ ★ ★ ★",
    "Five":  "★ ★ ★ ★ ★"
}

data = requests.get("http://books.toscrape.com/").content
soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

prices = soup.select(price_selector)
titles = soup.select(title_selector)
ratings = soup.select(rating_selector)

with open("books.csv", "w", encoding = "utf-8") as book_file:
    for price, title, rating in zip(prices, titles, ratings):
        book_file.write(f"{title['title']} , {price.string} , {get_rating(rating)}\n")




