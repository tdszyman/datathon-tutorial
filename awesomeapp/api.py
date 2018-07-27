from flask import Flask, render_template, jsonify, send_file, request, abort
import pandas as pd
import sqlite3
import traceback
import json

app = Flask(__name__)

database_path = 'data/database'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/education')
def getEducationController():
    try:
        limit = int(request.args.get('limit', 0))
    except Exception as e:
        return abort(400)
    try:
        df = getEducationTable(limit)
        meta = getEducationMetadata()
        return json.dumps( {
            # little bit of a hack because df.to_dict doesn't play nice with json encoding
            "data": json.loads(df.to_json(orient='records')),
            "metadata": json.loads(meta.to_json(orient="records"))
        } )
    except Exception as e:
        return abort(500)  # internal server error

@app.route('/api/top')
def getEducationTopController():
    try:
        num = int(request.args.get('num', 10))
    except Exception as e:
        return abort(400)
    try:
        df = getEducationTopTable(num)
        return df.to_json(orient="records")
    except Exception as e:
        return abort(500)

def getEducationTopTable(num):
    con = sqlite3.connect('data/database')
    df = pd.read_sql("""
            SELECT 
              age,
              MAX(education_num) as education_num,
              SUM(fnlwgt) as value
            FROM adult
              WHERE sex = 'Female'
            GROUP BY
              age
            ORDER BY
                value DESC
            ;
            """,
                     con)
    return df.head(num)

# separates the request end point from the data retrieval logic
def getEducationTable(limit):
    # gets data from server
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
    con)
    if limit != 0:
        df = df.head(limit)
    return df

def getEducationMetadata():
    con = sqlite3.connect('data/database')
    df = pd.read_sql("""
        SELECT
            MIN(age) as min_age,
            MAX(age) as max_age,
            MIN(education_num) as min_education_num,
            MAX(education_num) as max_education_num,
            MIN(value) as min_value,
            Max(value) as max_value
        FROM
            (
                SELECT 
                  age,
                  education_num,
                  SUM(fnlwgt) as value
                FROM adult
                  WHERE sex = 'Female'
                GROUP BY
                  age,
                  education_num
            )
    """, con)
    return df
