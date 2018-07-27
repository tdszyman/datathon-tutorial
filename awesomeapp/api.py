import json
import sqlite3
import pandas as pd
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

database_path = 'data/database'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/heatmap')
def getHeatmapController():
    df = getEducationTable()
    df = df.set_index(['age', 'education_num'])
    heat = df.value.unstack().fillna(0).T.sort_index(ascending=False)
    heat = heat / heat.sum(axis=0)  # Normalize based on age
    return jsonify(heat.values.tolist())


@app.route('/api/education')
def getEducationController():
    limit = int(request.args.get('limit', 0))
    df = getEducationTable(limit)
    meta = getEducationMetadata()
    return json.dumps({
        # little bit of a hack because df.to_dict doesn't play nice with json encoding
        "data": json.loads(df.to_json(orient='records')),
        "metadata": json.loads(meta.to_json(orient="records"))
    })


@app.route('/api/top')
def getEducationTopController():
    num = int(request.args.get('num', 0))
    df = getEducationTopTable(num).sort_values('age')
    return df.to_html(border="", index=None)


# Functions to read data from the database into Pandas DataFrames.

def getEducationTable(limit=0):
    con = sqlite3.connect(database_path)
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
    con = sqlite3.connect(database_path)
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
