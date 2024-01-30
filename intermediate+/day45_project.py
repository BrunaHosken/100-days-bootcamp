#100 movies
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

article_tags = soup.find_all(name="h3", class_="title")

articles_text =[text.getText() for text in article_tags]
movies = articles_text[::-1]

with open("./movies_scraping/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")