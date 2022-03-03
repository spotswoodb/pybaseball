from flask import Flask, render_template, request
from dotenv import load_dotenv
import pandas as pd


app = Flask(__name__)
file = pd.read_csv("stats.csv")
file.to_csv('sample_data.csv', index=None)

@app.route('/')
@app.route('/FirstStatcastTable')
def table():
    data = pd.read_csv('stats.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run(host="localhost", port=int('5000'))