from fastapi import HTTPException
from fastapi.responses import JSONResponse

from snoot.database import database
from snoot.database.dao.user import User
from snoot.schema.user import UserInput
from snoot.util import string_constant as const


def create_user(body: UserInput):
    """
    Create a new user in the database.
    """
    try:
        user = User.new(UserInput(
            first_name="John",
            last_name="Doe",
            email="ajkn@sknf.com",
            phone="1234567890",
            date_of_birth="1990-01-01",
            gender="Male"
        ).dict())

        print(body.dict())

        return JSONResponse(
            status_code=201,
            content=body.dict()
        )
    except Exception as e:
        return HTTPException(status_code=500, detail="Internal Server Error!!")
