from app.services.gemini_service import GeminiService
from app.services.prompt_service import PromptService

class EmailClassifierService:
    """
    Serviço responsável pela classificação de e-mails.

    Nas próximas etapas, esta classe será responsável por:
    - Construir o prompt.
    - Enviar a solicitação para a IA.
    - Validar a resposta.
    - Retornar os dados para a API.
    """

    def __init__(self):
        """Inicializa os serviços utilizados na classificação."""

        self.prompt_service = PromptService()
        self.gemini_service = GeminiService()

    def classify(self, email: str):
        """
        Classifica um e-mail.

        Por enquanto, retorna uma resposta simulada.
        """

        prompt = self.prompt_service.load_prompt("email_classifier")

        full_prompt = f"""
    {prompt}

    E-mail para análise:

    {email}
    """
        response = self.gemini_service.generate(full_prompt)
        return response