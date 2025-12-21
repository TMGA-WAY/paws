# snoot/model/host.py - Host Model

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime, date
from enum import Enum


class HostIdentity(BaseModel):
    id: UUID = Field(..., description="The unique identifier for the host")
    username: str = Field(..., description="The username of the host")
    email: EmailStr = Field(..., description="The email address of the host")
    phone_number: Optional[str] = Field(None, description="The phone number of the host")
    
    
    

class HostAuthenticationDetails(BaseModel):
    password_hash: str = Field(..., description="The hashed password of the host")
    password_salt: Optional[str] = Field(None, description="The salt used for hashing the password")
    is_email_verified: bool = Field(False, description="Indicates if the host's email is verified")
    is_phone_verified: bool = Field(False, description="Indicates if the host's phone number is verified")
    last_login_at: Optional[datetime] = Field(None, description="Timestamp of the host's last login")
    failed_login_attempts: int = Field(0, description="Number of consecutive failed login attempts")
    account_locked_until: Optional[datetime] = Field(None, description="Timestamp until which the account is locked due to failed login attempts")
    
    
    
class HostGender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"

class HostPersonalInfo(BaseModel):
    first_name: str = Field(..., description="The first name of the host")
    last_name: str = Field(..., description="The last name of the host")
    full_name: str = Field(..., description="The full name of the host (can be derived from first_name and last_name)")
    date_of_birth: date = Field(..., description="The date of birth of the host (YYYY-MM-DD)")
    gender: HostGender = Field(..., description="The gender of the host")
    profile_picture_url: str = Field(..., description="URL to the host's profile picture")
    bio: Optional[str] = Field(None, description="A short biography of the host")
    

class HostRole(str, Enum):
    HOST = "HOST"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"

class HostAccountStatus(BaseModel):
    is_active: bool = Field(True, description="Indicates if the host account is active")
    is_staff: bool = Field(False, description="Indicates if the host is staff")
    is_admin: bool = Field(False, description="Indicates if the host is admin")
    is_superuser: bool = Field(False, description="Indicates if the host is a superuser")
    role: HostRole = Field(HostRole.HOST, description="Role assigned to the host")
    
    
class Theme(str, Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"

class HostPreferencesAndSettings(BaseModel):
    language: str = Field("en", description="Preferred language of the host")
    timezone: str = Field(..., description="Preferred timezone of the host")
    theme: Theme = Field(Theme.SYSTEM, description="Preferred UI theme for the host")
    email_notifications: bool = Field(True, description="Indicates if the host wants email notifications")
    sms_notifications: bool = Field(False, description="Indicates if the host wants SMS notifications")
    
    

class HostAddress(BaseModel):
    address_line_1: Optional[str] = Field(None, description="First line of the address")
    address_line_2: Optional[str] = Field(None, description="Second line of the address")
    city: Optional[str] = Field(None, description="City of the host")
    state: Optional[str] = Field(None, description="State or province of the host")
    country: Optional[str] = Field(None, description="Country of the host")
    postal_code: Optional[str] = Field(None, description="Postal code of the host")


class HostType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"

class PetType(str, Enum):
    DOG = "DOG"
    CAT = "CAT"
    BIRD = "BIRD"
    OTHER = "OTHER"

class PetSize(str, Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    ANY = "ANY"

class HostHostingDetails(BaseModel):
    host_type: HostType = Field(HostType.INDIVIDUAL, description="Type of host (individual or business)")
    hosting_capacity: Optional[int] = Field(None, description="Maximum number of pets the host can accommodate")
    available_for_pet_types: Optional[list[PetType]] = Field(None, description="Types of pets the host can accommodate")
    hosting_rules: Optional[str] = Field(None, description="Rules and guidelines for hosting pets")
    preferred_pet_size: Optional[PetSize] = Field(None, description="Preferred size of pets the host can host")
    preferred_pet_age_range: Optional[tuple[int, int]] = Field(None, description="Preferred age range of pets (min_age, max_age)")
    special_requirements: Optional[str] = Field(None, description="Special requirements or notes for hosting")




class HostVerificationAndBackgroundCheck(BaseModel):
    identity_verified: bool = Field(False, description="Indicates if the host's identity has been verified")
    background_check_passed: bool = Field(False, description="Indicates if the host has passed a background check")
    documents_uploaded: Optional[list[str]] = Field(None, description="List of uploaded documents for verification")


class HostAuditInfo(BaseModel):
    created_at: datetime = Field(..., description="Timestamp when the host profile was created")
    updated_at: datetime = Field(..., description="Timestamp when the host profile was last updated")
    created_by: Optional[UUID] = Field(None, description="User ID of the creator (foreign key → User.id)")
    updated_by: Optional[UUID] = Field(None, description="User ID of the last updater (foreign key → User.id)")



class HostLegalConsent(BaseModel):
    terms_accepted_at: Optional[datetime] = Field(None, description="Timestamp when the host accepted the terms and conditions")
    privacy_policy_accepted_at: Optional[datetime] = Field(None, description="Timestamp when the host accepted the privacy policy")
    insurance_coverage_confirmed: bool = Field(False, description="Indicates if the host has confirmed insurance coverage")
    emergency_protocol_acknowledged: bool = Field(False, description="Indicates if the host has acknowledged emergency protocols")
    
    
    
class Host(BaseModel):
    identity: HostIdentity
    auth_details: HostAuthenticationDetails
    personal_info: HostPersonalInfo
    account_status: HostAccountStatus
    preferences: HostPreferencesAndSettings
    address: Optional[HostAddress] = None
    hosting_details: Optional[HostHostingDetails] = None
    verification: Optional[HostVerificationAndBackgroundCheck] = None
    audit: HostAuditInfo
    legal_consent: Optional[HostLegalConsent] = None




