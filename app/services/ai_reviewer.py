import json
import google.generativeai as genai
from app.core.config import settings
from app.schemas.review import ReviewResponse

genai.configure(api_key=settings.GEMINI_API_KEY)

async def perform_review(code: str, language: str) -> ReviewResponse:
    """
    Send The Code to Gemini and returns a structured review.
    """
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={"response_mime_type": "application/json"}
    )

    prompt = f"""
    You are a Senior Principal Software Engineer known for strict, clean code reviews.
    Review the following {language} code.
    
    Your output MUST be a valid JSON object matching this exact structure:
    {{
        "quality_score": (integer 0-10),
        "issues": [list of strings describing specific bad practices, bugs, or style violations],
        "refactored_code": (string, the full fixed code block),
        "roast": (string, a short, witty, sarcastic comment about how bad the code was)
    }}

    Analyze this code strictly:
    {code}
    """

    try:

        response = await model.generate_content_async(prompt)
        return ReviewResponse.model_validate_json(response.text)
    
    except Exception as e:
        return ReviewResponse(
            quality_score=0,
            issues=["Error communicating with AI Service"],
            refactored_code=code,
            roast=f"I'm broken. Error: {str(e)}"
        )

