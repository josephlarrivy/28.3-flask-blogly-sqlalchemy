from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, City

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-psql-sqalchemy-practice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "flask-psql-sqalchemy-practice"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)





@app.route('/')
def list_cities():
    cities = City.query.all()
    return render_template('list.html', cities=cities)

@app.route('/', methods=['POST'])
def add_city():
    name = request.form['name']
    country = request.form['country']
    state_province = request.form['state_province']
    population = request.form['population']

    new_city = City(name=name, country=country, state_province=state_province, population=population)

    db.session.add(new_city)
    db.session.commit()

    return redirect('/')
