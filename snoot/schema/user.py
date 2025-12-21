from pydantic import BaseModel
from typing import Optional


class UserInput(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: str
    date_of_birth: str  # ISO format
    gender: Optional[str] = None
