from typing import List
from pydantic import BaseModel, Field

class ReviewRequest(BaseModel):
    code : str = Field(...,min_length = 10, description = "The code to review")
    language : str = Field( default= "Python", description = "Programming Language")


class ReviewResponse(BaseModel):
    quality_score : int = Field(..., ge = 0, le = 10, description = "Quality score of the code from 0 to 10")
    issues : List[str] = Field(..., description = "List of Critiques")
    refactored_code : str = Field(..., description = "Fixed code snippet")
    roast : str = Field(..., description = "Sarcastic Comment")