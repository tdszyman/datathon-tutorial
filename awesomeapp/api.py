import io
import pandas as pd
import sqlite3
from flask import Flask, render_template, jsonify, send_file, request, abort
import pandas as pd
import sqlite3


app = Flask(__name__)

database_path = 'data/database'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/heatmap')
def heatmap():
    format = request.args.get('format', default='html')
    limit = request.args.get('limit', default=None)
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
    if limit is not None:
        df = df.head(int(limit))
    if format == 'html':
        return df.to_html()
    elif format == 'json':
        return df.to_json(orient='records')
    elif format == 'png':
        import matplotlib
        matplotlib.use('AGG')
        from matplotlib import pyplot as plt
        import seaborn as sns
        df = df.set_index(['age', 'education_num'])
        heat = df.value.unstack().fillna(0).T.sort_index(ascending=False)
        heat = heat / heat.sum(axis=0)  # Normalize based on age
        plt.clf()
        _ = sns.heatmap(heat)
        fakefile = io.BytesIO()
        plt.savefig(fakefile)
        fakefile.seek(0)
        return send_file(fakefile, mimetype='image/png')
    else:
        # Bad request
        return abort(400)

