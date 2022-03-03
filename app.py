from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from dotenv import load_dotenv
import os



app = Flask(__name__)

file = pd.read_csv("stats.csv")
file.to_csv('stats.csv', index=None)

load_dotenv()
POSTGRES_URI = os.environ.get('POSTGRES_URI')

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    player_id = db.Column(db.Integer, unique=True)
    year = db.Column(db.Integer)
    player_age = db.Column(db.Integer)
    xba = db.Column



@app.route('/')
@app.route('/FirstStatcastTable')
def table():
    data = pd.read_csv('stats.csv')
    return render_template('FirstStatcastTable.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run()