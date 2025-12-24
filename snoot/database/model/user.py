from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from snoot.database.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    ## Derived Attributes
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True,
                                         comment="The unique identifier for the user")
    active: Mapped[bool] = mapped_column(nullable=False, default=False, comment="Indicates user pet is given for stay")

    ## Personal Information
    first_name: Mapped[str] = mapped_column(String(60), nullable=False, comment="The first name of the user")
    last_name: Mapped[str] = mapped_column(String(60), nullable=False, comment="The last name of the user")
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False,
                                       comment="The email address of the user")

    phone: Mapped[str] = mapped_column(String(13), unique=True, nullable=True,
                                       comment="The phone number of the user")
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False, comment="The date of birth of the user")
    gender: Mapped[str] = mapped_column(String(10), nullable=False, comment="The gender of the user")

    ## Extended Information
    profile_picture_url: Mapped[str] = mapped_column(String(255), nullable=True,
                                                     comment="The URL of the user's profile picture")

    ## Metadata
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False,
                                                 comment="The timestamp when the user account was created")
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True,
                                                 comment="The timestamp when the user account was last updated")



########### Adjust below model as needed ##############
############ DO not remove at this time ################



# class AuthenticationDetails(BaseModel):
#     password_hash: str = Field(..., description="The hashed password of the user")
#     password_salt: str = Field(..., description="The salt used for hashing the password")
#     is_email_verified: bool = Field(..., description="Indicates if the user's email is verified")
#     is_phone_verified: bool = Field(..., description="Indicates if the user's phone number is verified")
#     last_login_at: Optional[str] = Field(None, description="The timestamp of the user's last login")
#     last_password_change: Optional[str] = Field(None, description="The timestamp of the last password change")
#     two_factor_enabled: bool = Field(..., description="Indicates if two-factor authentication is enabled for the user")
#     failed_login_attempts: int = Field(..., description="The number of consecutive failed login attempts")
#     account_locked_until: Optional[str] = Field(None, description="The timestamp until which the account is locked due to failed login attempts")
#     security_questions: Optional[Dict[str, str]] = Field(None, description="A dictionary containing security questions and answers for account recovery")
#
# class Address(BaseModel):
#     address_line1: str = Field(..., description="The first line of the address")
#     address_line2: Optional[str] = Field(None, description="The second line of the address")
#     city: str = Field(..., description="The city of the user")
#     state: str = Field(..., description="The state or province of the user")
#     postal_code: str = Field(..., description="The postal code of the user")
#     country: str = Field(..., description="The country of the user")
#
# class AccountMetadata(BaseModel):
#     is_active: bool = True
#     is_verified: bool = False
#     created_at: datetime
#     last_login: Optional[datetime] = None
#
#
# class UserRole(str, Enum):
#     USER = "USER"
#     ADMIN = "ADMIN"
#     MODERATOR = "MODERATOR"
#
# class AccountPermissions(BaseModel):
#     is_staff: bool = False
#     is_admin: bool = False
#     is_superuser: bool = False
#     role: UserRole = UserRole.USER
#
#
# class PreferencesAndSettings(BaseModel):
#     language: str = Field(..., description="The preferred language of the user")
#     timezone: str = Field(..., description="The preferred timezone of the user")
#     theme: Optional[str] = Field(None, description="The preferred theme (e.g., light or dark mode) of the user")
#     notification_settings: Optional[dict] = Field(None, description="A dictionary containing the user's notification preferences")
#     email_notifications: bool = Field(..., description="Indicates if the user wants to receive email notifications")
#     sms_notifications: bool = Field(..., description="Indicates if the user wants to receive SMS notifications")
#
#
# class LegalAndComplianceInfo(BaseModel):
#     terms_accepted: bool = Field(..., description="Indicates if the user has accepted the terms and conditions")
#     privacy_policy_accepted: bool = Field(..., description="Indicates if the user has accepted the privacy policy")
#     data_sharing_consent: bool = Field(..., description="Indicates if the user has consented to data sharing policies")
#     last_terms_update: Optional[datetime] = Field(None, description="The timestamp of the last update to the terms and conditions accepted by the user")
#     last_privacy_policy_update: Optional[datetime] = Field(None, description="The timestamp of the last update to the privacy policy accepted by the user")
#
#
# class User(BaseModel):
#     id: UUID = Field(..., description="The unique identifier for the user")
#     username: str = Field(..., description="The username of the user")
#     email: EmailStr = Field(..., description="The email address of the user")
#     phonenumber: Optional[str] = Field(None, description="The phone number of the user")
#
#     personal_info: PersonalInfo
#     auth_details: AuthenticationDetails
#     address: Optional[Address] = None
#     account_metadata: AccountMetadata
#     account_permissions: AccountPermissions
#     preferences: PreferencesAndSettings
