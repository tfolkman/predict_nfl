__author__ = 'tylerfolkman'

import psycopg2
import pandas as pd


def connect_to_nfl_db():
    conn = psycopg2.connect("dbname=nfldb user=nfldb")
    return conn


def list_tables_in_db(cur):
    return cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")


if __name__ == "__main__":

    conn = connect_to_nfl_db()
    x = pd.read_sql("select * from agg_play limit 5;", conn)
    print(x)