from flask import Flask, render_template
import datetime as dt
import requests
from post import Post

app = Flask(__name__)


def routes(url):
    response= requests.get(url)
    response.raise_for_status()
    return response.json()


url_blog = "https://api.npoint.io/c6f9af3cb7e76125a01a"
data_url = routes(url_blog)
post_objects = []
for post in data_url:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route("/")
def home():
    return render_template("index.html", posts = data_url)


@app.route("/guess/<name>")
def guess(name):
    url_gender = f"https://api.genderize.io?name={name}" 
    data_gender = routes(url_gender)
    gender = data_gender["gender"]
    url_age = f"https://api.agify.io?name={name}"
    data_age = routes(url_age) 
    age = data_age["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<int:id>")
def get_blog(id):
    requested = None
    for post in post_objects:
        if post.id == id:
            requested = post
    return render_template("post.html", post = requested)


if __name__ == "__main__":
    app.run(debug=True)