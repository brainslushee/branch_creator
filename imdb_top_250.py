import requests
import re
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

titles = soup.find_all("td", {"class": "titleColumn"})

ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})


for title in titles:
    print(title.text)

for rating in ratings:
    print(rating.text)
