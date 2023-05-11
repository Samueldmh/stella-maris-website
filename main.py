# from crypt import methods
# from wsgiref.validate import validator
from flask import Flask, render_template, redirect, url_for
# from flask_bootstrap import Bootstrap
import phonenumbers
from flask_wtf import FlaskForm
from requests import request
from wtforms import StringField, EmailField, SubmitField, TelField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'samuelezeigwe5@gmail.com'
app.config['MAIL_PASSWORD'] = 'imjmgwoepmlwwrju'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = 'bkjjoiepjfpjvpoino'
# Bootstrap (app)
mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email(message='Invalid Email')])
    phone = TelField("Phone", validators=[DataRequired()], id='phone')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField("Submit")



    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")

@app.route("/organisations")
def organisations():
    return render_template("organisations.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact_us():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(contact_form.name.data)
        msg = Message(subject='New message from a member', sender="samuelezeigwe5@gmail.com", recipients = ['solomonezeigwe207@gmail.com'], body=f"Name{contact_form.name.data}\nEmail:{contact_form.email.data}\nPhone: {contact_form.phone.data}\n Message:{contact_form.message.data}")
        mail.send(msg)
        return redirect(url_for("contact_us"))
    return render_template("contact.html", contact_form = contact_form)


 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
