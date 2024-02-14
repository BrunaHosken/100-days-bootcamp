# Build a website that lists cafes with wifi and power for remote working.
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes_project.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Cafe Image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Cafe Location', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet?')
    has_wifi = BooleanField('Has Wi-Fi?')
    has_sockets = BooleanField('Has Sockets?')
    can_take_calls = BooleanField('Can Take Calls?')
    seats = StringField('Quantity seats (e.g. 50+)', validators=[DataRequired()])
    coffee_price = StringField('Coffe Price (e.g. £3.00)', validators=[DataRequired()])
    
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return render_template('cafes.html', cafes=all_cafes)


@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name= request.form["name"],
            map_url= request.form["map_url"],
            img_url= request.form["img_url"],
            location= request.form["location"],
            seats= request.form["seats"],
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price= request.form["coffee_price"],
            )
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('get_all_cafe'))
    return render_template('add.html', form=form)
   



@app.route("/report-closed/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"
    if api_key == "TopSecretAPIKey":
        cafe= db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
    return redirect(url_for('get_all_cafe'))
      


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
