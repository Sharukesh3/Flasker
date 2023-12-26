import key

from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField
from wtforms.validators import DataRequired,Email
from flask_sqlalchemy import SQLAlchemy
import datetime

app=Flask(__name__)

#crefColumn
app.secret_key=key.getKey()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sharukesh:1234@localhost/users' 

#initialising db
db = SQLAlchemy(app)

#creating a class for db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(150),unique=True)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        
    def __repr__(self):
        return '<Name %r>' % self.name

class namerfield(FlaskForm):
    name=StringField("Enter your good name ",validators=[DataRequired()])
    submit=SubmitField("submit")
    
class userfield(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=EmailField("email",validators=[DataRequired()])
    submit=SubmitField("submit")

    


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/add', methods = ['get','post'])
def add_user():
    form = userfield()
    name = None
    user = "xyz"
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            # Create a new User object and add it to the session
            new_user = User(name=form.name.data, email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
        
    name = form.name.data
    form.name.data = ''
    form.email.data = ''
    flash("Form submitted successfully")
    #our_users = db.Query.order_by(user.name)
    return render_template('add_user.html',form=form,name=name)

    

@app.route('/user/<name>')
def user(name):
    stuff = "This is <strong> bold </strong> text"
    favourite_anime = ["mushoku_tensai", "slime", "date_a_live"]                        #variables
    return render_template("user.html", user_name=name, stuff=stuff, f=favourite_anime) #passing to templates

@app.route('/name', methods=['get','post'])
def name ():
    name = None
    form = namerfield()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("Form submitted successfully")
    return render_template('name.html',name=name,form=form)

@app.errorhandler(404) #page not found
def page_not_found(e):
    return render_template("404.html"),404 

@app.errorhandler(500) #internal server error
def page_not_found(e):
    return render_template("500.html"),500

if __name__=="__main__":
    app.run(debug=True)