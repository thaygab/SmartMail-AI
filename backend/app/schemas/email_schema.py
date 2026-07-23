from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    """
    Representa a requisição enviada pelo cliente.

    Contém o texto do e-mail que será analisado pela IA.
    """

    email: str = Field(
        min_length=10,
        max_length=5000,
        description="Texto do e-mail que será classificado."
    )


class EmailResponse(BaseModel):
    """
    Representa a resposta da API após a classificação do e-mail.
    """

    categoria: str
    prioridade: str
    resumo: str
    acao_sugerida: str