# 📧 SmartMail-AI

Sistema inteligente para classificação automática de e-mails utilizando Inteligência Artificial.

O SmartMail-AI é um projeto desenvolvido com foco em **Engenharia de IA**, aplicando boas práticas de arquitetura de software, separação de responsabilidades e integração com modelos de linguagem (LLMs).

Atualmente, o sistema é capaz de receber um e-mail, construir um prompt, enviá-lo ao Google Gemini e retornar uma classificação automática.

---

## 🚀 Tecnologias

* Python 3
* FastAPI
* Google Gemini API
* python-dotenv
* Pydantic
* Uvicorn

---

## 📂 Estrutura do Projeto

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── prompts/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── uploads/
├── logs/
└── requirements.txt

docs/
├── diario/
├── documentacao/
├── diagramas/
└── imagens/
```

---

## 🏗️ Arquitetura

O projeto foi desenvolvido utilizando uma arquitetura em camadas, onde cada componente possui uma responsabilidade única.

```text
Cliente
    │
    ▼
FastAPI
    │
    ▼
EmailClassifierService
    ├──────────────┐
    ▼              ▼
PromptService   GeminiService
                    │
                    ▼
             Google Gemini
```

---

## ✨ Funcionalidades atuais

* Classificação automática de e-mails utilizando IA.
* Carregamento de prompts externos.
* Integração com Google Gemini.
* Configuração por variáveis de ambiente.
* Estrutura organizada para evolução do projeto.
* Testes de integração dos serviços.

---

## ⚙️ Como executar

1. Clone o repositório.
2. Crie um ambiente virtual.
3. Instale as dependências:

```bash
pip install -r backend/requirements.txt
```

4. Crie um arquivo `.env` dentro da pasta `backend`:

```env
GEMINI_API_KEY=sua_chave_aqui
MODEL_NAME=gemini-3.5-flash
```

5. Inicie a API:

```bash
uvicorn app.main:app --reload
```

---

## 📌 Status do Projeto

🚧 Em desenvolvimento.

Próximas etapas:

* Resposta estruturada em JSON.
* Integração completa com FastAPI.
* Tratamento de erros.
* Logs da aplicação.
* Testes automatizados.
* Melhorias no Prompt Engineering.

---

## 🎯 Objetivo do Projeto

Mais do que criar um classificador de e-mails, este projeto tem como objetivo estudar e aplicar conceitos de:

* Engenharia de IA
* Arquitetura de Software
* Backend com Python
* Integração com LLMs
* Boas práticas de desenvolvimento

Cada funcionalidade é construída de forma incremental, priorizando organização, reutilização de código e facilidade de manutenção.
