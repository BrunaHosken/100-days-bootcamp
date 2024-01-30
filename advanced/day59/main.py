from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib
import requests

load_dotenv()

my_email = os.getenv('EMAIL_FROM')
password=os.getenv('PASSWORD_FROM')

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

@app.route("/contact", methods=["GET","POST"])
def receive_data():
    if(request.method == "POST"):
        data=request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        
        return render_template("contact.html", msg_sent= True)
    
    return render_template("contact.html", msg_sent= False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=email_message)
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)