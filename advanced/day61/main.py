from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

    
app = Flask(__name__)
app.secret_key = "password"
app.testing = True
bootstrap = Bootstrap5(app) 
permitedEmail="admin@email.com"
permitedPassword="12345678"

class LoginForm(FlaskForm):
    email = StringField(label = "Email", validators=[DataRequired(), Email(granular_message=True,check_deliverability=True), AnyOf(values=[permitedEmail])])
    password = PasswordField(label ="Password", validators=[DataRequired(), Length(min=8), AnyOf(values=[permitedPassword])])
    submit= SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    print(login_form.validate_on_submit())
    if request.method == 'GET':
        return render_template('login.html', form = login_form)
    else:
        if login_form.validate_on_submit():
            if login_form.email.data == permitedEmail and  login_form.password.data == permitedPassword:
                return render_template('success.html')
        else:
            return render_template('denied.html')



if __name__ == '__main__':
    app.run(debug=True)