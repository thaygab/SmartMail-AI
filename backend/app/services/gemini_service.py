from google import genai

from app.core.config import GEMINI_API_KEY, MODEL_NAME


class GeminiService:
    """Responsável pela comunicação com o Gemini."""

    def __init__(self):
        """Inicializa o cliente do Gemini."""

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        """Envia um prompt para o Gemini e retorna a resposta."""

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        return response.text