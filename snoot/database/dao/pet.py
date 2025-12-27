import threading
import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class Pet:
    def __init__(self, pet_id: int):
        table_name = const.PET_TABLE_NAME
        query = f"""SELECT * FROM "{table_name}" WHERE pet_id = {pet_id};"""

        self.df = database.sql_to_pandas(query=query)
        self.exists = not self.df.empty

    @classmethod
    def new(cls, pet_data: dict):
        _lock = threading.Lock()

        if not pet_data:
            raise ValueError("Pet data cannot be empty")

        with _lock:
            table_name = const.PET_TABLE_NAME
            query = f"""SELECT * FROM "{table_name}" ORDER BY pet_id DESC LIMIT 1"""
            df = database.sql_to_pandas(query=query)

            last_pet_id = int(df.loc[0, "pet_id"]) if not df.empty else 0

            pet_record = {
                "pet_id": last_pet_id + 1,
                "user_id": pet_data["user_id"],
                "pet_type": pet_data["pet_type"],
                "name": pet_data["name"],
                "image_urls": pet_data.get("image_urls", []),
                "description": pet_data.get("description"),
                "created_at": pd.Timestamp.now(tz="Asia/Kolkata"),
                "updated_at": None
            }

            df = pd.DataFrame([pet_record])
            database.pandas_to_sql(df, table_name)

            return cls(pet_id=last_pet_id + 1)

    # ---------- getters ----------
    def is_exist(self):
        return self.exists

    def to_dict(self):
        return self.df.to_dict(orient="records")[0] if self.exists else {}

    def get_pet_id(self):
        return self.df.loc[0, "pet_id"]

    def get_user_id(self):
        return self.df.loc[0, "user_id"]

    def get_pet_type(self):
        return self.df.loc[0, "pet_type"]

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
