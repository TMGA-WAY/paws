from fastapi import FastAPI
from paws.snoot.routes import user_routers, pet_routers, host_routers

app = FastAPI(
    title="Pows",
    description="This is the api-service for Pows.",
    summary="This service handles all API requests for Pows application."
)


app.include_router(user_routers.router, prefix="/users", tags=["Users"])
app.include_router(pet_routers.router, prefix="/pets", tags=["Pets"])
app.include_router(host_routers.router, prefix="/hosts", tags=["Hosts"])