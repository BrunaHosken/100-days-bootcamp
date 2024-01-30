from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from time import strftime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# blogs = [
#     {
#     "id": 1,
#     "img_url": "https://atlondonbridge.com/wp-content/uploads/2019/02/Pano_9758_9761-Edit-190918_LTS_Science_Gallery-Medium-Crop-V2.jpg",
#     "title": "Test",
#     "subtitle": "Only a Test",
#     "date": "January 25, 2024",
#     "body": "Curabitur aliquam quam sed ornare finibus. Pellentesque vitae ipsum tempus, sodales metus convallis, egestas velit. Nam aliquam velit dui, eget semper sem auctor quis. Suspendisse leo risus, porta ac nisi sit amet, lacinia tempus metus. Pellentesque ut felis a nisi auctor dignissim vitae ac justo. Mauris a iaculis enim. In hac habitasse platea dictumst. Integer pretium enim lacus, sit amet pellentesque lacus dignissim a. Cras tristique nulla nisl, eget lobortis augue ultricies ut. Proin ultrices, ex ut aliquet gravida, lectus justo tincidunt sapien, quis laoreet velit nunc vitae dui. Pellentesque imperdiet magna nibh. Nam interdum leo non lectus sollicitudin aliquam. ",
#     "author": "Me"
#     },
#     {
#     "id": 2,
#     "title": "Test2",
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOhkJk2MBtFW1RydPU0zf3bf8upGkTQWyhDpXzZ=s0",
#     "subtitle": "Only a Test",
#     "date": "January 25, 2024",
#     "body": "Etiam massa leo, maximus vitae massa ac, volutpat feugiat nunc. Nulla aliquet sit amet purus sit amet sagittis. Fusce at finibus est. Aliquam aliquet nibh leo, id semper neque placerat vitae. Nunc facilisis varius efficitur. Nulla facilisi. Curabitur et enim pellentesque, dignissim sapien sed, auctor purus. Nulla facilisi. Pellentesque elementum arcu id tincidunt feugiat. Vivamus suscipit tellus vel lobortis facilisis. ",
#     "author": "Me"
#     },
#     {
#     "id": 3,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0",
#     "title": "Test3",
#     "subtitle": "Only a Test",
#     "date": "January 25, 2024",
#     "body": "Vivamus pretium aliquet felis sit amet hendrerit. Nam ac gravida mauris. Integer sapien magna, mattis quis neque ac, bibendum aliquam arcu. Nunc ultrices orci ullamcorper, auctor erat eu, vestibulum augue. Mauris laoreet libero vitae nisl ultrices, eu commodo urna tincidunt. Cras non arcu arcu. Fusce augue augue, porta ac volutpat tempus, convallis ultricies erat. Mauris cursus posuere commodo. Morbi elementum diam sed dolor maximus, ut luctus metus ultricies. Donec euismod mollis vehicula. Vestibulum quis cursus erat. Donec tincidunt finibus eros. Donec posuere arcu mi, vitae bibendum enim bibendum in. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean pretium quis. ",
#     "author": "Me"
#     }
#     ]
# with app.app_context():
    # for blog in blogs:
    #     blog_page = BlogPost(
    #         id= blog["id"],
    #         img_url= blog["img_url"],
    #         title= blog["title"],
    #         subtitle= blog["subtitle"],
    #         body= blog["body"],
    #         date= blog["date"],
    #         author= blog["author"],
    #        )
    #     db.session.add(blog_page)
    # db.session.commit()


with app.app_context():
    db.create_all()

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.route('/')
def get_all_posts():
    posts = []
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
