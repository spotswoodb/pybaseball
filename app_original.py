import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import tablib
# from send_mail import send_mail

# a = pd.read_csv("Exit_Velocity_Percentiles_2021_LD_FB_EV_Percentiles_Table.csv")
# a.to_html("EVP_2021_LD_FB_EVP_Table.html")
# html_file = a.to_html()

load_dotenv()
POSTGRES_URI = os.environ.get('POSTGRES_URI')



app = Flask(__name__)

# dataset = tablib.Dataset()
# with open(os.path.join(os.path.dirname(__file__), 'stats.csv')) as f:
#     dataset.csv = f.read()
    

# columns = ['last_name','first_name', 'player_id', 'year', 'player_age',	'xba', 'xslg',	'woba',	'xwoba', 'xobp', 'xiso', 'exit_velocity_avg', 'launch_angle_avg', 'sweet_spot_percent',	'barrel_batted_rate']
# df = pd.read_csv('stats.csv', names=columns)

# print(df.to_html())

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    file = pd.read_csv("stats.csv")
    return file.to_html("StudentTable.html") 
    # data = dataset
    # return render_template('index.html', data=data)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(200), unique=True)
    player = db.Column(db.String(200), unique=True)
    

    def __init__(self, player_id, player):
        self.player_id = player_id
        self.player = player

# class ExitVelocityPercentiles2021LDFBEVPercentilesTable(html_file):

    # return render_template('index.html')


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
