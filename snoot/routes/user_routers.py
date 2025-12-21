from fastapi import APIRouter, HTTPException
from snoot.schema.user import UserInput
from snoot.service import user_service

# from snoot.model.user import User

router = APIRouter()




@router.post("/")
async def create_user(body: UserInput):
    return user_service.create_user(body)

