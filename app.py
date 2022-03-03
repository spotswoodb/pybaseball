from flask import Flask, render_template, request
from dotenv import load_dotenv
import pandas as pd


app = Flask(__name__)
file = pd.read_csv("stats.csv")
file.to_csv('stats.csv', index=None)

@app.route('/')
@app.route('/FirstStatcastTable')
def table():
    data = pd.read_csv('stats.csv')
    return render_template('FirstStatcastTable.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.debug = True
    app.run()