from app.services.gemini_service import GeminiService
from app.services.prompt_service import PromptService
from app.schemas.email_schema import EmailResponse
from fastapi import HTTPException

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
        try:
           prompt = self.prompt_service.load_prompt("email_classifier")

           full_prompt = f"""
    {prompt}

    E-mail para análise:

    {email}
    """
           response = self.gemini_service.generate(full_prompt)

           print(response)

           lines = response.split("\n")

           categoria = lines[0].replace("Categoria:", "").strip()
           prioridade = lines[1].replace("Prioridade:", "").strip()
           resumo = lines[2].replace("Resumo:", "").strip()
           acao_sugerida = lines[3].replace("Ação sugerida:", "").strip()

           return EmailResponse(
               categoria=categoria,
               prioridade=prioridade,
               resumo=resumo,
               acao_sugerida=acao_sugerida

            )
        except Exception as e:
            print(f"Erro na classificação: {e}")

            raise HTTPException(
                status_code=500,
                detail="Não foi possível classificar o e-mail no momento"
            )