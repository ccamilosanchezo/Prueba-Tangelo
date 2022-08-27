import sqlite3 as sql


def managedatabase(dataframe):
    connection = sql.connect("database.db")
    dataframe.to_sql(name="Languages", con=connection)
    connection.close()