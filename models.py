from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



class City(db.Model):
    
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    country = db.Column(db.String(30), nullable=False)
    state_province = db.Column(db.String(30))
    population = db.Column(db.Integer)



