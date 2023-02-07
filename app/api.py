from fastapi import FastAPI
from app.routes.language import LanguageRouter

app = FastAPI(
    title="Language detector",
    version="1.0",
    description="Language detector api.",
)

app.include_router(LanguageRouter)
