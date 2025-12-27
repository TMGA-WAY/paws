import threading
import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class Dog:
    def __init__(self, dog_id: int):
        table_name = const.DOG_TABLE_NAME
        query = f"""SELECT * FROM "{table_name}" WHERE dog_id = {dog_id};"""

        self.df = database.sql_to_pandas(query=query)
        self.exists = not self.df.empty

    @classmethod
    def new(cls, dog_data: dict):
        _lock = threading.Lock()

        if not dog_data:
            raise ValueError("Dog data cannot be empty")

        with _lock:
            table_name = const.DOG_TABLE_NAME
            query = f"""SELECT * FROM "{table_name}" ORDER BY dog_id DESC LIMIT 1"""
            df = database.sql_to_pandas(query=query)

            last_dog_id = int(df.loc[0, "dog_id"]) if not df.empty else 0

            dog_record = {
                "dog_id": last_dog_id + 1,
                "owner_id": dog_data["owner_id"],  
                "breed": dog_data["breed"],
                "name": dog_data["name"],
                "image_urls": dog_data.get("image_urls", []),
                "description": dog_data.get("description"),
                "created_at": pd.Timestamp.now(tz="Asia/Kolkata"),
                "updated_at": None
            }

            df = pd.DataFrame([dog_record])
            database.pandas_to_sql(df, table_name)

            return cls(dog_id=last_dog_id + 1)

    # ---------- getters ----------
    def is_exist(self):
        return self.exists

    def to_dict(self):
        return self.df.to_dict(orient="records")[0] if self.exists else {}

    def get_dog_id(self):
        return self.df.loc[0, "dog_id"]

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
