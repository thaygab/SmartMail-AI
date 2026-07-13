from app.services.gemini_service import GeminiService


service = GeminiService()

response = service.generate("Responda apenas com a palavra 'Olá'.")

print(response)