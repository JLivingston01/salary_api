
import pandas as pd
import sqlite3

def pull_data(URL:str = "https://www.bls.gov/oes/current/oes_nat.htm") -> pd.DataFrame:
    """Accesses salary survey data and returns as dataframe.

    Args:
        URL (str, optional): URL to obtain the salary survey data. Defaults to "https://www.bls.gov/oes/current/oes_nat.htm".

    Returns:
        pd.DataFrame: Salary data
    """
    tables = pd.read_html(URL)

    data = tables[0]
    data.columns = ['OCC_CODE',
    'TITLE',
    'LEVEL',
    'EMPLOYMENT',
    'EMPLOYMENT_RSE',
    'EMPLOYMENT_PER_1000',
    'MEDIAN_HOURLY_WAGE',
    'MEAN_HOURLY_WAGE',
    'MEAN_ANNUAL_WAGE',
    'MEAN_WAGE_RSE',
    ]

    return data

def insert_data(data: pd.DataFrame,
    database_location:str = "data/sqlite.db",
    table_name:str = "SALARIES",
    if_exists:str = 'replace',
    index:bool = False
    ) -> None:
    """Loads a dataframe into the salaries table, but is generically written

    Args:
        data (pd.DataFrame): Salary data
        database_location (str, optional): sqlite database location. Defaults to "../data/sqlite.db".
    """
    
    conn = sqlite3.Connection(database_location)
    data.to_sql(table_name,con=conn,if_exists=if_exists,index=index)
    conn.close()

    return

def main() -> None:

    data = pull_data()

    insert_data(data = data)

    return

if __name__=='__main__':
    main()