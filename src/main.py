# src/main.py

from fastapi import FastAPI
from src.api import router


def create_app() -> FastAPI:
    """
    Factory method to create FastAPI application.
    """
    app = FastAPI(
        title="Heart Disease Predictor (Synthetic Data)",
        description="Allows user to specify how many synthetic patients to generate.",
        version="1.0.0",
    )

    app.include_router(router, prefix="", tags=["heart-disease"])
    return app


app = create_app()
