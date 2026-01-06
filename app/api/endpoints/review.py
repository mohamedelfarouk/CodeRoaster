from fastapi import APIRouter, HTTPException
from app.schemas.review import ReviewRequest, ReviewResponse
from app.services import ai_reviewer

router = APIRouter()


@router.post("/review", response_model=ReviewResponse)
async def review_code(request: ReviewRequest):
    """
    Submit code for an AI-powered review.
    """
    result = await ai_reviewer.perform_review(
        code=request.code, 
        language=request.language
    )
    
    return result