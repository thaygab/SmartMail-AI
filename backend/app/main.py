from fastapi import FastAPI

from app.api.email_routes import router as email_router

from app.schemas.email_schema import EmailRequest
from app.services.email_classifier_service import EmailClassifierService

app = FastAPI(
    title="SmartMail-AI",
    description="API para classificação inteligente de e-mails utilizando Inteligência Artificial.",
    version="1.0.0",
)

app.include_router(email_router)

@app.get("/")
def root():
    return {
        "message": "SmartMail-AI API online!"
    }

@app.post("/classificar-email")
def classificar_email(email: EmailRequest):
    resultado = service.classify(email.email)
    return resultado

