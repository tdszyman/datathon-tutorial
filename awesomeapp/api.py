from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/heatmap_png')
def heatmap_png():
    import io
    import pandas as pd
    import sqlite3
    import seaborn as sns
    from matplotlib import pyplot as plt
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
    heat = df.value.unstack().fillna(0).T.sort_index(ascending=False)
    heat = heat / heat.sum(axis=0)  # Normalize based on age
    plt.clf()
    _ = sns.heatmap(heat)
    fakefile = io.BytesIO()
    plt.savefig(fakefile)
    fakefile.seek(0)
    return send_file(fakefile, mimetype='image/png')



@app.route('/heatmap_json')
def heatmap_json():
    import io
    import pandas as pd
    import sqlite3
    import seaborn as sns
    from matplotlib import pyplot as plt
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
    return df.to_json(orient='records')
