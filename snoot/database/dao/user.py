import threading

import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class User:
    def __init__(self, user_id):
        table_name = const.USER_TABLE_NAME
        query = f"select * from {table_name} where user_id = {user_id}"
        print(query)

        self.df = database.sql_to_pandas(query)
        if self.df.empty:
            raise ValueError(f"User with id {user_id} does not exist.")

    @classmethod
    def new(cls, user_data: dict):
        _lock = threading.Lock()

        if not user_data:
            raise ValueError(f"User with id {user_data['user_id']} does not exist.")

        # to prevent race conditions
        with _lock:
            # get the last user_id
            table_name = const.USER_TABLE_NAME
            query = f""" select * from "{table_name}" order by user_id desc limit 1"""
            df = database.sql_to_pandas(query=query)

            last_user_id = int(df.loc[0, "user_id"]) if not df.empty else 0

            df = pd.DataFrame(
                columns=["user_id", "first_name", "last_name", "email", "phone", "date_of_birth", "gender",
                         "created_at"],
                data=[[last_user_id + 1,
                       user_data.get("first_name"),
                       user_data.get("last_name"),
                       user_data.get("email"),
                       user_data.get("phone"),
                       user_data.get("date_of_birth"),
                       user_data.get("gender"),
                       pd.Timestamp.now(tz="Asia/Kolkata")
                       ]]
            )

            database.pandas_to_sql(df, table_name)
