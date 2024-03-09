# Build a todo list website.
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

items = [] 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        task = request.form.get("task")
        items.append(task)

    return render_template("index.html", items=items)

@app.route("/delete_item/<int:index>")
def delete_item(index):
    if 0 <= index < len(items):
        del items[index]

    return render_template("index.html", items=items)

if __name__ == '__main__':
    app.run(debug=True)
