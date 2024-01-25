from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
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

    def to_dict(self):
    #Method 1. 
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     #Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search_cafe():
    query = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])
    
    else:
        return jsonify(error = {"Not Found": "Sorry, we don't have a have in your location :c"}),404

@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:
        new_cafe = Cafe(
            name= request.form["name"],
            map_url= request.form["map_url"],
            img_url= request.form["img_url"],
            location= request.form["location"],
            seats= request.form["seats"],
            has_toilet= eval(request.form["has_toilet"].title()),
            has_wifi= eval(request.form["has_wifi"].title()),
            has_sockets= eval(request.form["has_sockets"].title()),
            can_take_calls= eval(request.form["can_take_calls"].title()),
            coffee_price= request.form["coffee_price"],
        )
    except KeyError:
        return jsonify(error={"Bad Request": "Some or all fields were incorrect or missing."})
    else:
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe= db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe= db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
# cafes = [
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.40",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": False,
#     "id": 1,
#     "img_url": "https://atlondonbridge.com/wp-content/uploads/2019/02/Pano_9758_9761-Edit-190918_LTS_Science_Gallery-Medium-Crop-V2.jpg",
#     "location": "London Bridge",
#     "map_url": "https://g.page/scigallerylon?share",
#     "name": "Science Gallery London",
#     "seats": "50+"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.75",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 2,
#     "img_url": "https://images.squarespace-cdn.com/content/v1/5734f3ff4d088e2c5b08fe13/1555848382269-9F13FE1WQDNUUDQOAOXF/ke17ZwdGBToddI8pDm48kAeyi0pcxjZfLZiASAF9yCBZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzV8NE8s7067ZLWyi1jRvJklJnlBFEUyq1al9AqaQ7pI4DcRJq_Lf3JCtFMXgpPQyk/copeland-park-bar-peckham",
#     "location": "Peckham",
#     "map_url": "https://g.page/CopelandSocial?share",
#     "name": "Social - Copeland Road",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.75",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 3,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOMzXpKAQNyUvrjTGHqCgWk8spwnzwP8Ml2aDKt=s0",
#     "location": "Peckham",
#     "map_url": "https://g.page/one-all-cafe?share",
#     "name": "One & All Cafe Peckham",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.80",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 4,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipPBAt6bYna7pv5c7e_PhCDPMKPb6oFf6kMT2VQ1=s0",
#     "location": "Peckham",
#     "map_url": "https://www.google.com/maps/place/Old+Spike+Roastery/@51.4651552,-0.0666088,17z/data=!4m12!1m6!3m5!1s0x487603a3a7dd838d:0x4105b39b30a737cf!2sOld+Spike+Roastery!8m2!3d51.4651552!4d-0.0666088!3m4!1s0x487603a3a7dd838d:0x4105b39b30a737cf!8m2!3d51.4651552!4d-0.0666088",
#     "name": "Old Spike",
#     "seats": "0-10"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.65",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 5,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipM9Dz_QMkOF2da1aNLuTzS_vPvVWBnE84rZLK_G=s0",
#     "location": "Bermondsey",
#     "map_url": "https://goo.gl/maps/ugP2B1AV7FELHSgn6",
#     "name": "Fuckoffee Bermondsey",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.80",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 6,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipN-C650VmJ1XZhzOIBTg1bUu3_to_GHpyrmUplt=s0",
#     "location": "Hackney",
#     "map_url": "https://goo.gl/maps/DWnwaeeiwdYsBkEH9",
#     "name": "Mare Street Market",
#     "seats": "50+"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£3.00",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 7,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipP_NbZH7A1fIQyp5pRm1jOGwzKsDWewaxka6vDt=s0",
#     "location": "Shoreditch",
#     "map_url": "https://g.page/acehotellondon?share",
#     "name": "Ace Hotel Shoreditch",
#     "seats": "50+"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.10",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 8,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipPnOfo7wTICdiAyybF3iFhD3l5aoQjSO-GErma1=s0",
#     "location": "Clerkenwell",
#     "map_url": "https://goo.gl/maps/D9nXNYK3fa1cxwpK8",
#     "name": "Goswell Road Coffee",
#     "seats": "10-20"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.30",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 9,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipMrdTyRRozGBltwxAseQ4QeuNhbED6meQXlCPsx=s0",
#     "location": "London Bridge",
#     "map_url": "https://goo.gl/maps/LU1imQzBCRLFBxKUA",
#     "name": "The Southwark Cathedral Cafe",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.70",
#     "has_sockets": False,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 10,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipNtHqqIc3kwhpjknrVcMdkhmpA77LDYKmpOJlxf=s0",
#     "location": "Whitechapel",
#     "map_url": "https://goo.gl/maps/v5tzRBVhPFueYp4x6",
#     "name": "Trade Commercial Road",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.70",
#     "has_sockets": False,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 11,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOFimpFQmUORVGg0ER3lrfEiEnKpnYJck5guFqC=s0",
#     "location": "Bankside",
#     "map_url": "https://goo.gl/maps/6RvPHyhsDDUPs1ox8",
#     "name": "The Tate Modern Cafe",
#     "seats": "30-40"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.50",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 12,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipPyJHFtVzxor4RyQrT-ZEk7ej7OxvmIQYZUHe6G=s0",
#     "location": "Clerkenwell",
#     "map_url": "https://goo.gl/maps/HC4e9FJL48kLRH8W9",
#     "name": "Forage Cafe",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.80",
#     "has_sockets": True,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 13,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipNJQIg-6YTOZhbLu12yGPN3klDxygs7cNAjEo0C=s0",
#     "location": "Shoreditch",
#     "map_url": "https://g.page/citizenm-london-shoreditch?share",
#     "name": "Citizen M Hotel Shoreditch",
#     "seats": "30-40"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£3.00",
#     "has_sockets": False,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 14,
#     "img_url": "https://images.adsttc.com/media/images/5014/ec99/28ba/0d58/2800/0d0f/large_jpg/stringio.jpg?1414576924",
#     "location": "Barbican",
#     "map_url": "https://goo.gl/maps/XPrcFj91LsQBvUa27",
#     "name": "Barbican Centre",
#     "seats": "50+"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.60",
#     "has_sockets": False,
#     "has_toilet": True,
#     "has_wifi": True,
#     "id": 15,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOL6jxxpE_D3YS-Zzih61DqNXJKvRIDFiP6ieUI=s0",
#     "location": "Clerkenwell",
#     "map_url": "https://goo.gl/maps/mwAG272nQwSUc9bn8",
#     "name": "The Slaughtered Lamb",
#     "seats": "20-30"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£1.80",
#     "has_sockets": False,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 16,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOchpT9ipgb7tpqglcTKpp2E8kZhsKvlYjUZ4e1=s0",
#     "location": "South Kensington",
#     "map_url": "https://goo.gl/maps/GPFSEuGEiDvQG8BH7",
#     "name": "Fernandez and Wells Exhibition Road",
#     "seats": "10-20"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.60",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 17,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOZ3WDAAxphLu657afVVATJ5TGxtturIOr8gt8u=s0",
#     "location": "Whitechapel",
#     "map_url": "https://goo.gl/maps/xv29seioiETAAZgN9",
#     "name": "Whitechapel Grind",
#     "seats": "30-40"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.60",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 18,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOutkI7wjWNXiPSTdf8CX0jXwyVHFTwFnVhyVJE=s0",
#     "location": "Peckham",
#     "map_url": "https://goo.gl/maps/qpcpX7MWhFSS1qxH9",
#     "name": "The Peckham Pelican",
#     "seats": "0 - 10"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.00",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 19,
#     "img_url": "https://www.nhm.ac.uk/content/dam/nhmwww/business-services/filming/Earth-Sciences-Library-1.jpg",
#     "location": "South Kensington",
#     "map_url": "https://goo.gl/maps/VU2PwnDDtH1WqCnK7",
#     "name": "Natural History Museum Library",
#     "seats": "40-50"
#     },
#     {
#     "can_take_calls": False,
#     "coffee_price": "£2.80",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 20,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipNlBWFgXBiP9YjKARy4dgjHGePOmtsfuQPRwGvb=s0",
#     "location": "Shoreditch",
#     "map_url": "https://goo.gl/maps/gYX271NxyuawiMcK8",
#     "name": "The Bike Shed",
#     "seats": "10-20"
#     },
#     {
#     "can_take_calls": True,
#     "coffee_price": "£2.40",
#     "has_sockets": True,
#     "has_toilet": False,
#     "has_wifi": True,
#     "id": 21,
#     "img_url": "https://lh3.googleusercontent.com/p/AF1QipOhkJk2MBtFW1RydPU0zf3bf8upGkTQWyhDpXzZ=s0",
#     "location": "Borough",
#     "map_url": "https://g.page/fora---borough?share",
#     "name": "FORA Borough",
#     "seats": "20-30"
#     }
# ]


# with app.app_context():
#     for cafe in cafes:
#         cafe = Cafe(
#             id= cafe["id"],
#             name= cafe["name"],
#             map_url= cafe["map_url"],
#             img_url= cafe["img_url"],
#             location= cafe["location"],
#             seats= cafe["seats"],
#             has_toilet= cafe["has_toilet"],
#             has_wifi= cafe["has_wifi"],
#             has_sockets= cafe["has_sockets"],
#             can_take_calls= cafe["can_take_calls"],
#             coffee_price= cafe["coffee_price"],
#            )
#         db.session.add(cafe)
#     db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")



# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
