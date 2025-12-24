from fastapi import APIRouter, HTTPException
from snoot.schema.user import UserInput
from snoot.service import user_service

# from snoot.model.user import User

router = APIRouter()


@router.get("/{user_id}")
async def get_user_endpoint(user_id: int):
    """Get user details by user_id."""
    return user_service.get_user(user_id)

@router.post("/")
async def create_user_endpoint(body: UserInput):
    """Create a new user."""
    return user_service.create_user(body)

@router.patch("/{user_id}")
async def update_user_endpoint(user_id: int, body: UserInput):
    """Update user details by user_id."""
    return user_service.update_user(user_id, body)
