import threading
import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class Cat:
    def __init__(self, cat_id: int):
        table_name = const.CAT_TABLE_NAME
        query = f"""SELECT * FROM "{table_name}" WHERE cat_id = {cat_id};"""

        self.df = database.sql_to_pandas(query=query)
        self.exists = not self.df.empty

    @classmethod
    def new(cls, cat_data: dict):
        _lock = threading.Lock()

        if not cat_data:
            raise ValueError("Cat data cannot be empty")

        with _lock:
            table_name = const.CAT_TABLE_NAME
            query = f"""SELECT * FROM "{table_name}" ORDER BY cat_id DESC LIMIT 1"""
            df = database.sql_to_pandas(query=query)

            last_cat_id = int(df.loc[0, "cat_id"]) if not df.empty else 0

            cat_record = {
                "cat_id": last_cat_id + 1,
                "owner_id": cat_data["owner_id"],  
                "breed": cat_data["breed"],
                "name": cat_data["name"],
                "image_urls": cat_data.get("image_urls", []),
                "description": cat_data.get("description"),
                "created_at": pd.Timestamp.now(tz="Asia/Kolkata"),
                "updated_at": None
            }

            df = pd.DataFrame([cat_record])
            database.pandas_to_sql(df, table_name)

            return cls(cat_id=last_cat_id + 1)

    # ---------- getters ----------
    def is_exist(self):
        return self.exists

    def to_dict(self):
        return self.df.to_dict(orient="records")[0] if self.exists else {}

    def get_cat_id(self):
        return self.df.loc[0, "cat_id"]

    def get_owner_id(self):
        return self.df.loc[0, "owner_id"]

    def get_breed(self):
        return self.df.loc[0, "breed"]

    def get_name(self):
        return self.df.loc[0, "name"]

    def get_image_urls(self):
        return self.df.loc[0, "image_urls"] or []

    def get_description(self):
        return self.df.loc[0, "description"]

    def get_created_at(self):
        return self.df.loc[0, "created_at"]

    def get_updated_at(self):
        return self.df.loc[0, "updated_at"]
