# from fastapi import APIRouter, HTTPException
# from typing import List
# from snoot.database.model.pet import PetIdentity
#
# router = APIRouter()
#
# pets_db: List[PetIdentity] = []
#
# @router.get("/", response_model=List[PetIdentity])
# def get_all_pets():
#     return pets_db
#
# @router.get("/{pet_id}", response_model=PetIdentity)
# def get_pet(pet_id: int):
#     for pet in pets_db:
#         if pet.id == pet_id:
#             return pet
#     raise HTTPException(status_code=404, detail="Pet not found")
#
# @router.post("/", response_model=PetIdentity)
# def create_pet(pet: PetIdentity):
#     pets_db.append(pet)
#     return pet
