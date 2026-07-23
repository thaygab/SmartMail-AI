from fastapi import APIRouter

from app.schemas.email_schema import EmailRequest
from app.services.email_classifier_service import EmailClassifierService

router = APIRouter()

service = EmailClassifierService()


@router.post("/classificar-email")
def classificar_email(email: EmailRequest):
    return service.classify(email.email)