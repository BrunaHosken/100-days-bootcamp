from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

article_tags = soup.find_all(name="span", class_="titleline")

articles_text =[text.getText() for text in article_tags]
articles_links =[link.find(name="a").get("href") for link in article_tags]
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_upvote = max(article_upvote)
max_index = article_upvote.index(max_upvote)

print(articles_text[max_index])
print(articles_links[max_index])
print(max_upvote)





# with open("beautiful-soup-files/website.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
# anchor_tags = soup.find_all(name="a")

# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# heading = soup.find(name="h3", class_="heading")
# print(heading.name)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(".heading")
# print(headings)

# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print(max_length)