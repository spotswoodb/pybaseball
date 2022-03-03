import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

# file = pd.read_csv("stats.csv")
# file.to_html('FirstStatcastTable.html')

app = Flask(__name__)

@app.route('/')
def index():
    file = pd.read_csv("stats.csv")
    file.to_html("FirstStatcastTable.html")
    return render_template("FirstStatcastTable.html")