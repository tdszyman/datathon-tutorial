from flask import Flask, render_template, jsonify
import pandas as pd
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/heatmap')
def heatmap():
    con = sqlite3.connect('data/database')
    df = pd.read_sql("""
    SELECT 
      age,
      education_num,
      SUM(fnlwgt) as value
    FROM adult
      WHERE sex = 'Female'
    GROUP BY
      age,
      education_num
    ;
    """,
    con).set_index(['age', 'education_num'])
    print(df.head())
    return df.to_html()
