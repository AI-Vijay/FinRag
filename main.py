from fastapi import FastAPI

from routes.dashboard import router as dashboard_router
from routes.health import router as health_router

app = FastAPI(
    title="FinRag",
    description=(
        "FinRag is an AI-powered financial document "
        "intelligence platform using Retrieval-Augmented "
        "Generation (RAG) to analyze financial reports, "
        "extract key metrics, and answer investment-related questions."
    ),
    version="1.0.0",
)

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
