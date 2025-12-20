# snoot/mdel/pet.py - Pet Model

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, List
from enum import Enum
from datetime import date, datetime
from uuid import UUID




class PetIdentity(BaseModel):
    id: int = Field(..., description="The unique identifier for the pet")
    name: str = Field(..., description="The name of the pet")
    owners_id: int = Field(...,description="Foreign key referencing users.id (pet owner)") # Link to User model
    microchip_id: str = Field(..., description="The microchip ID of the pet, if applicable")
    

class PetSpecies(str, Enum):
    DOG = "DOG"
    CAT = "CAT"
    BIRD = "BIRD"
    OTHER = "OTHER"


class PetGender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"
    
    
class PetBasicDetails(BaseModel):
    species: PetSpecies = Field(...,description="Species of the pet (DOG, CAT, BIRD, OTHER)")
    breed: Optional[str] = Field(None,description="Breed of the pet")
    gender: Optional[PetGender] = Field(None,description="Gender of the pet")
    date_of_birth: Optional[date] = Field(None,description="Date of birth of the pet (YYYY-MM-DD)")
    age: Optional[int] = Field(None,description="Age of the pet in years (derived from date_of_birth)")
    color: Optional[str] = Field(None,description="Color of the pet")
    weight: Optional[int] = Field(None,description="Weight of the pet (in kg)")
    height: Optional[int] = Field(None,description="Height of the pet (in cm)")
    
class PetHealthInfo(BaseModel):
    is_vaccinated: bool = Field(False, description="Indicates whether the pet is vaccinated")
    vaccination_records: Optional[dict] = Field(None, description="Vaccination history and records of the pet")
    medical_conditions: Optional[str] = Field(None, description="Known medical conditions of the pet")
    allergies: Optional[str] = Field(None, description="Allergies the pet may have")
    special_needs: Optional[str] = Field(None, description="Special care or needs required by the pet")
    neutered_or_spayed: Optional[bool] = Field(None, description="Indicates whether the pet is neutered or spayed")
    last_vet_visit: Optional[date] = Field(None, description="Date of the pet's last veterinary visit")
    vet_contact_info: Optional[str] = Field(None, description="Veterinarian or clinic contact information")
    

class PetTemperament(str, Enum):
    CALM = "CALM"
    FRIENDLY = "FRIENDLY"
    AGGRESSIVE = "AGGRESSIVE"
    ANXIOUS = "ANXIOUS"
    MIXED = "MIXED"

class TrainingLevel(str, Enum):
    NONE = "NONE"
    BASIC = "BASIC"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"

class PetBehaviorInfo(BaseModel):
    temperament: Optional[PetTemperament] = Field(None, description="General temperament of the pet")
    is_house_trained: Optional[bool] = Field(None, description="Indicates whether the pet is house trained")
    good_with_kids: Optional[bool] = Field(None, description="Indicates whether the pet is good with children")
    good_with_other_pets: Optional[bool] = Field(None, description="Indicates whether the pet is good with other pets")
    training_level: Optional[TrainingLevel] = Field(None, description="Training level of the pet")
    behavior_notes: Optional[str] = Field(None, description="Additional notes about the pet's behavior and temperament")
    
    

class WalkFrequency(str, Enum):
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class PetCareRoutine(BaseModel):
    feeding_schedule: Optional[dict] = Field(None, description="Feeding schedule details such as time and quantity")
    food_type: Optional[str] = Field(None, description="Type of food the pet consumes")
    walk_frequency: Optional[WalkFrequency] = Field(None, description="Frequency of walks required by the pet")
    exercise_needs: Optional[str] = Field(None, description="Exercise requirements of the pet")
    sleep_schedule: Optional[str] = Field(None, description="Typical sleeping schedule of the pet")
    care_instructions: Optional[str] = Field(None, description="Special care instructions for the pet")
    
    
    

class PetMediaInfo(BaseModel):
    profile_picture_url: Optional[str] = Field(None, description="Primary profile picture URL of the pet")
    gallery_images: Optional[List[str]] = Field(None, description="Gallery image URLs of the pet")
    identification_marks: Optional[str] = Field(None, description="Distinct identification marks of the pet")
    
    


class PreferredHostGender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    ANY = "ANY"

class PreferredEnvironment(str, Enum):
    HOME = "HOME"
    FARM = "FARM"
    KENNEL = "KENNEL"
    ANY = "ANY"

class PetHostingPreferences(BaseModel):
    can_be_hosted: bool = Field(True, description="Indicates whether the pet can be hosted")
    preferred_host_gender: Optional[PreferredHostGender] = Field(None, description="Preferred gender of the host")
    preferred_environment: Optional[PreferredEnvironment] = Field(None, description="Preferred hosting environment")
    special_hosting_notes: Optional[str] = Field(None, description="Special instructions or notes for hosting the pet")
    
    
class PetVisibility(str, Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    FRIENDS_ONLY = "FRIENDS_ONLY"

class PetStatus(BaseModel):
    is_active: bool = Field(True, description="Indicates whether the pet profile is active")
    is_available_for_booking: bool = Field(False, description="Indicates whether the pet is available for booking")
    visibility: PetVisibility = Field(PetVisibility.PRIVATE, description="Visibility level of the pet profile")


class PetAuditInfo(BaseModel):
    created_at: datetime = Field(..., description="Timestamp when the pet profile was created")
    updated_at: datetime = Field(..., description="Timestamp when the pet profile was last updated")
    created_by: Optional[UUID] = Field(None, description="User ID of the creator (foreign key → User.id)")
    updated_by: Optional[UUID] = Field(None, description="User ID of the last updater (foreign key → User.id)")
    
    
class PetLegalConsent(BaseModel):
    owner_consent_given: bool = Field(False, description="Indicates whether the pet owner has given consent for hosting")
    medical_emergency_consent: bool = Field(False, description="Indicates whether the pet owner has authorized medical intervention in emergencies")
    
    





    

    
    

    
    
