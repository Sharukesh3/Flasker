import key

from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.secret_key=key.getKey()

#creating form class
class namerfield(FlaskForm):
    name=StringField("Enter your good name ",validators=[DataRequired()])
    submit=SubmitField("submit")
    
@app.route('/')
def index():
    return render_template("index.html")

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
    return render_template('name.html',name=name,form=form)

@app.errorhandler(404) #page not found
def page_not_found(e):
    return render_template("404.html"),404 

@app.errorhandler(500) #internal server error
def page_not_found(e):
    return render_template("500.html"),500

if __name__=="__main__":
    app.run(debug=True)