from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

from snoot.routes import user_routers

app = FastAPI(
    title="Pows",
    description="This is the api-service for Pows.",
    summary="This service handles all API requests for Pows application."
)
### Additional configuration can be added here ###
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



################## Routers ##################
app.include_router(user_routers.router, prefix="/users", tags=["Users"])
# app.include_router(pet_routers.router, prefix="/pets", tags=["Pets"])
# app.include_router(host_routers.router, prefix="/hosts", tags=["Hosts"])