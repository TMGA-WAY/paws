import traceback

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
        user = User.new(body.model_dump())

        return JSONResponse(
            content={
                "message": "User created successfully",
                "user_id": user.get_user_id()
            },
            status_code=201
        )
    except Exception as e:
        # Todo: Research on some logging framework
        print(traceback.format_exc())
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error!!")


def get_user(user_id: int):
    """
    Retrieve user details by user_id.
    """
    try:
        user = User(user_id)
        return user.to_dict()
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        print(traceback.format_exc())
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error!!")


def update_user(user_id: int, body: UserInput):
    """
    Update user details by user_id.
    """
    try:
        update_data = body.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(status_code=400, detail="No data provided for update")

        # todo: Validate if user exists
        user = User(user_id)
        if not user.is_exist():
            return JSONResponse(
                content={
                    "message": f"User with id {user_id} does not exist"
                },
                status_code=404
            )

        # todo: @saswat exclude email, phone from updates for now; email and phone updates should go through a verification process; we will do that later
        database.sql_update(
            table_name=const.USER_TABLE_NAME,
            where={"user_id": user_id},
            values=update_data
        )

        return JSONResponse(
            content={
                "message": "User updated successfully",
                "user_id": user_id
            },
            status_code=200
        )
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        print(traceback.format_exc())
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error!!")
