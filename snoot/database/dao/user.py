import threading

import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class User:
    def __init__(self, user_id):
        table_name = const.USER_TABLE_NAME
        query = f"""select * from "{table_name}" where user_id = {user_id};"""

        self.df = database.sql_to_pandas(query=query)
        self.exists = not self.df.empty

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
                columns=["user_id", "active", "first_name", "last_name", "email", "phone", "date_of_birth", "gender",
                         "created_at"],
                data=[[last_user_id + 1,
                       False,
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

            return cls(user_id=last_user_id + 1)

    # all getter methods
    def is_exist(self):
        return self.exists

    def to_dict(self):
        return self.df.to_dict(orient="records")[0]

    def get_user_id(self):
        return self.df.loc[0, "user_id"]

    def get_first_name(self):
        return self.df.loc[0, "first_name"]

    def get_last_name(self):
        return self.df.loc[0, "last_name"]

    def get_email(self):
        return self.df.loc[0, "email"]

    def get_phone(self):
        return self.df.loc[0, "phone"]

    def get_date_of_birth(self):
        return self.df.loc[0, "date_of_birth"]

    def get_gender(self):
        return self.df.loc[0, "gender"]

    def is_active(self):
        return self.df.loc[0, "active"]

    def get_created_at(self):
        return self.df.loc[0, "created_at"]

    def get_profile_picture_url(self):
        return self.df.loc[0, "profile_picture_url"] if pd.notna(self.df.loc[0, "profile_picture_url"]) else ""

    def get_last_updated_at(self):
        return self.df.loc[0, "updated_at"]
