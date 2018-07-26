import os
import requests
import sqlite3
import pandas as pd
from pathlib import Path


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
data_fn = Path(data_fn)

db_fn = "./data/database"
db_fn = Path(db_fn)

data_folder = "./data"
data_folder = Path(data_folder)

def download_data():
    with open(data_fn.absolute(), "wb") as f:
        f.write(requests.get(data_url).content)


def create_database():
    if(db_fn.is_file()):
        os.remove(db_fn.absolute())
    con = sqlite3.connect(str(db_fn.absolute()))
    con.close()
    return


def load_data():
    df = pd.read_csv(data_fn.absolute(), index_col=None)
    df.columns = [col[0] for col in data_cols]
    for col, type in data_cols:
        df[col] = df[col].astype(type)
        if type == 'object':
            df[col] = df[col].str.strip()
    print(df.head())
    con = sqlite3.connect(str(db_fn.absolute()))
    df.to_sql('adult', con=con, index=False)
    con.close()
    return


def main():
    if( not data_folder.is_dir()):
        os.makedirs(data_folder.absolute())
    download_data()
    create_database()
    load_data()
    return


if __name__ == '__main__':
    main()
