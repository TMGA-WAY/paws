from datetime import date

from pydantic import BaseModel, validator, EmailStr
from typing import Optional
import phonenumbers


class UserInput(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    date_of_birth: date
    gender: str

    @validator("phone")
    def validate_phone(cls, v):
        # Todo: @Saswat properly validate the phone number including country codes
        # if not v.isdigit() or len(v) < 7 or len(v) > 15:
        #     raise ValueError("Invalid phone number format")
        try:
            parsed_number = phonenumbers.parse(v, "IN")
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid phone number format")
        except phonenumbers.NumberParseException:
                raise ValueError("Invalid phone number format")
        return phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.E164
        )

    @validator("email")
    def validate_email(cls, v):
        # Todo: @Saswat properly validate the email format
        # if v is not None and "@" not in v:
        #     raise ValueError("Invalid email format")
        # return v
        return v.lower() if v else v

    @validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        if v >= date.today():
            raise ValueError("Date of birth must be in the past")
        return v