from datetime import date

from pydantic import BaseModel, validator
from typing import Optional


class UserInput(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: str
    date_of_birth: date
    gender: Optional[str] = None

    @validator("phone")
    def validate_phone(cls, v):
        # Todo: @Saswat properly validate the phone number including country codes
        if not v.isdigit() or len(v) < 7 or len(v) > 15:
            raise ValueError("Invalid phone number format")
        return v

    @validator("email")
    def validate_email(cls, v):
        # Todo: @Saswat properly validate the email format
        if v is not None and "@" not in v:
            raise ValueError("Invalid email format")
        return v

    @validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        if v >= date.today():
            raise ValueError("Date of birth must be in the past")
        return v