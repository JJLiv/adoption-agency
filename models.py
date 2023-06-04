from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True, nullable=False)



def connect_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()