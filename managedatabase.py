import sqlite3 as sql
import pandas as pd
import json


def managedatabase(dataframe):
    connection = sql.connect("database.db")
    dataframe.to_sql(name="Languages", con=connection, index=False)
    connection.close()


def databasetojson():
    connection = sql.connect("database.db")
    dataframe = pd.read_sql_query("SELECT * from Languages", connection)
    dict = dataframe.to_dict(orient="index")
    connection.close()
    with open('data.json', 'w') as fp:
        json.dump(dict, fp)