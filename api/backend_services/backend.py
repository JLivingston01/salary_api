import pandas as pd
import sqlite3

def make_connection(database = "data/sqlite.db"):

    conn = sqlite3.Connection(database)

    return conn

def get_levels():

    conn = make_connection()

    sql = """
    SELECT DISTINCT LEVEL FROM SALARIES;
    """ 

    data = pd.read_sql(sql=sql,con=conn)

    return list(data['LEVEL'])


def get_titles(request_dict):

    LEVEL = request_dict['LEVEL']

    conn = make_connection()

    sql = f"""
    SELECT DISTINCT TITLE FROM SALARIES
    where LEVEL = '{LEVEL}';
    """ 

    data = pd.read_sql(sql=sql,con=conn)

    return list(data['TITLE'])