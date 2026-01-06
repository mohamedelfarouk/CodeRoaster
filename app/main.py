from fastapi import FastAPI
from app.api.endpoints import review

app = FastAPI(
    title="Code Roaster API",
    description="An AI-powered code review tool using Gemini 1.5 Flash.",
    version="1.0.0"
)

# Wire up the router
app.include_router(review.router, prefix="/api/v1", tags=["Reviews"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Roaster is ready to roast."}