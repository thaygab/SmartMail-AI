from app.services.email_classifier_service import EmailClassifierService


service = EmailClassifierService()

email = """
Olá,

Meu computador não está ligando desde ontem.

Poderiam me ajudar?

Obrigado.
"""

email = """
Olá,

Meu computador não está ligando desde ontem.

Poderiam me ajudar?

Obrigado.
"""

response = service.classify(email)

print(response)