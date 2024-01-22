from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c6f9af3cb7e76125a01a").json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<int:index>")
def get_post(index):
    requested = None
    for post in posts:
        if post["id"] == index:
            requested = post
    return render_template("post.html", post = requested)

if __name__ == "__main__":
    app.run(debug=True)