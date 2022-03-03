from click import launch
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
    xba = db.Column(db.Integer)
    xslg = db.Column(db.Integer)
    woba = db.Column(db.Integer)
    xwoba = db.Column(db.Integer)
    xobp = db.Column(db.Integer)
    xiso = db.Column(db.Integer)
    exit_velocity_avg = db.Column(db.Integer)
    launch_angle_avg = db.Column(db.Integer)
    sweet_spot_percent = db.Column(db.Integer)
    barrel_batted_rate = db.Column(db.Integer)

    def __init__(self, last_name, first_name, player_id, year, player_age, xba, xslg, woba, xwoba, xobp, xiso, exit_velocity_avg, launch_angle_avg, sweet_spot_percent, barrel_batted_rate):
        self.last_name = last_name
        self.first_name = first_name
        self.player_id = player_id
        self.year = year
        self.player_age = player_age
        self.xba = xba
        self.xslg = xslg
        self.woba = woba
        self.xwoba = xwoba
        self.xobp = xobp
        self.xiso = xiso
        self.exit_velocity_avg = exit_velocity_avg
        self.launch_angle_avg = launch_angle_avg
        self.sweet_spot_percent = sweet_spot_percent
        self.barrel_batted_rate = barrel_batted_rate


@app.route('/')
@app.route('/FirstStatcastTable')
def table():
    data = pd.read_csv('stats.csv')
    return render_template('FirstStatcastTable.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run()