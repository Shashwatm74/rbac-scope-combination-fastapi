from pydantic import BaseModel, Field

class Submission(BaseModel):
    title: str = Field(..., example="AI-Powered Hackathon Assistant")
    description: str = Field(..., example="An AI tool that helps participants organize and manage their hackathon projects effectively.")
    submitted_by: str = Field(..., example="participant123")
