from fastapi import FastAPI

app = FastAPI(
    title="E-commerce Growth Intelligence API",
    description="API for e-commerce analytics and business intelligence.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}