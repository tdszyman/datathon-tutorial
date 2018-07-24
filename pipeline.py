import os
import requests
import sqlite3
import pandas as pd


data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
data_cols = [
    ('age', 'int'),
    ('workclass', 'object'),
    ('fnlwgt', 'int'),
    ('education', 'object'),
    ('education_num', 'int'),
    ('marital_status', 'object'),
    ('occupation', 'object'),
    ('relationship', 'object'),
    ('race', 'object'),
    ('sex', 'object'),
    ('capital_gain', 'int'),
    ('capital_loss', 'int'),
    ('hours_per_week', 'int'),
    ('native_country', 'object'),
    ('class_label', 'object')
]

data_fn = "./data/adult.csv"

db_fn = "./data/database"


def download_data():
    with open(data_fn, "wb") as f:
        f.write(requests.get(data_url).content)


def create_database():
    os.remove(db_fn)
    con = sqlite3.connect(db_fn)
    con.close()
    return


def load_data():
    df = pd.read_csv(data_fn, index_col=None)
    df.columns = [col[0] for col in data_cols]
    for col, type in data_cols:
        df[col] = df[col].astype(type)
        if type == 'object':
            df[col] = df[col].str.strip()
    print(df.head())
    con = sqlite3.connect(db_fn)
    df.to_sql('adult', con=con, index=False)
    con.close()
    return


def main():
    #download_data()
    create_database()
    load_data()
    return


if __name__ == '__main__':
    main()
