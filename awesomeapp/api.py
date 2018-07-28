import json
import sqlite3
import pandas as pd
from flask import Flask, render_template, jsonify, request
from jinja2 import Template

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


@app.route('/api/table')
def getTableController():
    limit = request.args.get('limit', None)
    if limit is not None:
        limit = int(limit)
    gender = request.args.get('gender', None)
    df = getEducationTable(limit=limit, gender=gender)
    return df.to_html(index=None)


@app.route('/api/summary')
def getSummaryController():
    con = sqlite3.connect(database_path)
    df = pd.read_sql(
        """
        SELECT
          sex AS gender,
          MIN(education_num) AS min,
          MAX(education_num) AS max,
          AVG(education_num) AS mean
        FROM adult
        GROUP BY
          sex 
        """,
        con
    )
    print(df)
    return df.to_html(index=False, border="")

@app.route('/api/levels')
def getLevelsController():
    con = sqlite3.connect(database_path)
    df = pd.read_sql(
        """
        SELECT
        DISTINCT 
          education_num AS Number,
          education AS Level
        FROM adult
        ORDER BY
          education_num ASC
        """,
        con
    )
    print(df)
    return df.to_html(index=False, border="")


# Functions to read data from the database into Pandas DataFrames.

def getEducationTable(limit=None, gender=None):
    con = sqlite3.connect(database_path)
    query = """
        SELECT 
          age,
          education_num,
          SUM(fnlwgt) as value
        FROM adult
          {% if gender == 'f' %}
          WHERE sex = 'Female'
          {% elif gender == 'm' %}
          WHERE sex = 'Male'
          {% else %}
          {% endif %}
        GROUP BY
          age,
          education_num
        ORDER BY
          age,
          education_num
        ;
        """
    query = Template(query).render(**locals())
    df = pd.read_sql(query, con)
    if limit is not None:
        df = df.head(limit)
    return df


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
