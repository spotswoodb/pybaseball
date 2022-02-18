import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
# from send_mail import send_mail

a = pd.read_csv("Exit_Velocity_Percentiles_2021_LD_FB_EV_Percentiles_Table.csv")
a.to_html("EVP_2021_LD_FB_EVP_Table.html")
html_file = a.to_html()

load_dotenv()
POSTGRES_URI = os.environ.get('POSTGRES_URI')



app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(200), unique=True)
    player = db.Column(db.String(200), unique=True)
    

    def __init__(self, player_id, player):
        self.player_id = player_id
        self.player = player

# class ExitVelocityPercentiles2021LDFBEVPercentilesTable(html_file):

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        player_id = request.form['player_id']
        player = request.form['player']
        # print(customer, dealer, rating, comments)
        if player == '' or player_id == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.player_id == player_id).count() == 0:
            data = Feedback(player_id, player)
            db.session.add(data)
            db.session.commit()
            # send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()
