from fastapi import FastAPI
from roles.endpoints import router as roles_router
from submissions.endpoints import router as submissions_router
from db.database import initialize_database

app = FastAPI()

# Include Routers
app.include_router(roles_router, prefix="/roles", tags=["Roles"])
app.include_router(submissions_router, prefix="/submissions", tags=["Submissions"])

# Application startup event
@app.on_event("startup")
def startup_event():
    initialize_database()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Hackathon Platform"}
