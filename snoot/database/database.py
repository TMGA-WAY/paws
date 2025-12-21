import os

import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine

ENGINE = os.environ.get("SQLALCHEMY_DATABASE_URL")
engine = create_engine(ENGINE)


def sql_to_pandas(table_name: str = None, query: str = None):
    """
    This function retrieves data from a specified table or executes a provided SQL query and returns the result as a pandas DataFrame.
    :param table_name: The name of the table to query data from
    :param query: If provided, this SQL query will be executed instead of querying the entire table
    :return: pandas DataFrame containing the queried data
    """

    if query is None:
        query = f"select * from {table_name};"
    with engine.connect() as con:
        df = pd.read_sql_query(sql=sqlalchemy.text(query), con=con)
    return df


def pandas_to_sql(df, table_name: str, if_exists: str = "append", index=False):
    """
    This function writes a pandas DataFrame to a specified table in the database.
    :param df: pandas DataFrame to be written to the database
    :param table_name: The name of the table to write data to
    :param if_exists: Behavior when the table already exists. Options are 'fail', 'replace', 'append'
    :param index: Whether to write DataFrame index as a column
    """
    with engine.connect() as con:
        df.to_sql(con=con, name=table_name, if_exists=if_exists, index=index, method='multi')


def sql_update(table_name: str = None, where: dict = None, values: dict = None, query: str = None):
    """
    This function updates data in a specified table based on given conditions, or executes a provided SQL update query.
    :param table_name: The name of the table to update data in
    :param where: A dictionary specifying the WHERE clause conditions
    :param values: A dictionary specifying the column-value pairs to be updated
    :param query: If provided, this SQL update query will be executed instead of constructing one
    :return: None
    """
    if query is None:
        set_clause = ", ".join([f"{k} = :{k}" for k in values.keys()])
        where_clause = " and ".join([f"{k} = :{k}" for k in where.keys()])
        query = f"update {table_name} set {set_clause} where {where_clause};"
        params = {**values, **where}
        query = sqlalchemy.text(query).bindparams(**params)
    else:
        query = sqlalchemy.text(query)

    with engine.connect() as connection:
        connection.execute(query)


def get_table_columns(table_name: str):
    """
    This function retrieves the column names of a specified table in the database.
    :param table_name: The name of the table to get columns from
    :return: List of column names in the specified table
    """
    columns = sql_to_pandas(query="show columns from " + table_name)
    return columns['Field'].tolist()
