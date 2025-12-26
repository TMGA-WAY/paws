import threading
import pandas as pd

from snoot.util import string_constant as const
from snoot.database import database


class Pet:
    def __init__(self, pet_id: int):
        table_name = const.PET_TABLE_NAME
        query = f'''SELECT * FROM "{table_name}" WHERE pet_id = {pet_id};'''

        self.df = database.sql_to_pandas(query=query)
        self.exists = not self.df.empty

    # ---------- CREATE ----------
    @classmethod
    def new(cls, pet_data: dict):
        _lock = threading.Lock()

        if not pet_data:
            raise ValueError("Pet data cannot be empty")

        with _lock:
            table_name = const.PET_TABLE_NAME

            # get last pet_id
            query = f'''SELECT pet_id FROM "{table_name}" ORDER BY pet_id DESC LIMIT 1'''
            df = database.sql_to_pandas(query=query)

            last_pet_id = int(df.loc[0, "pet_id"]) if not df.empty else 0

            pet_df = pd.DataFrame(
                columns=[
                    "pet_id", "user_id", "pet_type", "name", "age", "month",
                    "breed", "gender", "weight", "color",
                    "image_urls", "description", "created_at", "updated_at"
                ],
                data=[[
                    last_pet_id + 1,
                    pet_data.get("user_id"),
                    pet_data.get("pet_type"),
                    pet_data.get("name"),
                    pet_data.get("age"),
                    pet_data.get("month"),
                    pet_data.get("breed"),
                    pet_data.get("gender"),
                    pet_data.get("weight"),
                    pet_data.get("color"),
                    pet_data.get("image_urls"),
                    pet_data.get("description"),
                    pd.Timestamp.now(tz="Asia/Kolkata"),
                    None
                ]]
            )

            database.pandas_to_sql(pet_df, table_name)
            return cls(pet_id=last_pet_id + 1)

    # ---------- READ ----------
    def is_exist(self):
        return self.exists

    def to_dict(self):
        return self.df.to_dict(orient="records")[0]

    # ---------- GETTERS ----------
    def get_pet_id(self):
        return self.df.loc[0, "pet_id"]

    def get_user_id(self):
        return self.df.loc[0, "user_id"]

    def get_name(self):
        return self.df.loc[0, "name"]

    def get_pet_type(self):
        return self.df.loc[0, "pet_type"]

    def get_age(self):
        return self.df.loc[0, "age"]

    def get_gender(self):
        return self.df.loc[0, "gender"]

    def get_color(self):
        return self.df.loc[0, "color"]

    def get_created_at(self):
        return self.df.loc[0, "created_at"]

    # ---------- UPDATE ----------
    def update(self, values: dict):
        if not self.exists:
            raise ValueError("Pet does not exist")

        database.sql_update(
            table_name=const.PET_TABLE_NAME,
            where={"pet_id": self.get_pet_id()},
            values=values
        )
