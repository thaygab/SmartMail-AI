from pydantic import BaseModel


class EmailRequest(BaseModel):
    """
    Representa a requisição enviada pelo cliente.

    Contém o texto do e-mail que será analisado pela IA.
    """

    email: str


class EmailResponse(BaseModel):
    """
    Representa a resposta da API após a classificação do e-mail.
    """

    categoria: str
    prioridade: str
    resumo: str
    acao_sugerida: str