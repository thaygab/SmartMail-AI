@echo off
title SmartMail-AI - Setup Inicial
color 0A

echo ==========================================
echo         SmartMail-AI Setup
echo ==========================================
echo.

:: ==========================================
:: ETAPA 1 - CRIAR PASTAS
:: ==========================================

echo [1\4] Criando estrutura de pastas...
echo.

call :CreateFolder "backend"
call :CreateFolder "backend\app"
call :CreateFolder "backend\app\api"
call :CreateFolder "backend\app\core"
call :CreateFolder "backend\app\prompts"
call :CreateFolder "backend\app\schemas"
call :CreateFolder "backend\app\services"
call :CreateFolder "backend\app\utils"

call :CreateFolder "backend\tests"

call :CreateFolder "docs"
call :CreateFolder "docs\diario"
call :CreateFolder "docs\documentacao"
call :CreateFolder "docs\diagramas"
call :CreateFolder "docs\imagens"

echo.

:: ==========================================
:: ETAPA 2 - CRIAR ARQUIVOS
:: ==========================================

echo [2\4] Criando arquivos iniciais...
echo.

call :CreateFile "backend\app\schemas\email_schema.py"
call :CreateFile "backend\app\schemas\__init__.py"

call :CreateFile "backend\app\api\email_routes.py"
call :CreateFile "backend\app\api\__init__.py"

call :CreateFile "backend\app\core\config.py"
call :CreateFile "backend\app\core\__init__.py"

call :CreateFile "backend\app\services\email_classifier_service.py"
call :CreateFile "backend\app\services\gemini_service.py"
call :CreateFile "backend\app\services\prompt_service.py"
call :CreateFile "backend\app\services\__init__.py"

call :CreateFile "backend\app\utils\__init__.py"

call :CreateFile "backend\app\prompts\email_classifier.txt"

call :CreateFile "backend\requirements.txt"
call :CreateFile "backend\requirements-dev.txt"

call :CreateFile "backend\.env"
call :CreateFile "backend\.env.example"

call :CreateFile "backend\.gitignore"

call :CreateFile "README.md"

:: Documentação

call :CreateFile "docs\diario\README.md"
call :CreateFile "docs\diario\2026-07-12.md"

call :CreateFile "docs\documentacao\arquitetura.md"
call :CreateFile "docs\documentacao\api.md"
call :CreateFile "docs\documentacao\estrutura.md"
call :CreateFile "docs\documentacao\prompt-engineering.md"

echo.

:: ==========================================
:: ETAPA 3 - GIT
:: ==========================================

echo [3\4] Verificando Git...
echo.

if not exist ".git" (
    git init
    echo [OK] Repositorio Git inicializado.
) else (
    echo [--] Repositorio Git ja existe.
)

echo.

:: ==========================================
:: ETAPA 4 - AMBIENTE VIRTUAL
:: ==========================================

echo [4\4] Verificando ambiente virtual...
echo.

if not exist "backend\venv" (
    cd backend
    python -m venv venv
    cd ..
    echo [OK] Ambiente virtual criado.
) else (
    echo [--] Ambiente virtual ja existe.
)

echo.
echo ==========================================
echo Setup finalizado com sucesso!
echo ==========================================
echo.

pause
exit /b

:: =====================================================
:: FUNÇÃO - CRIAR PASTA
:: =====================================================

:CreateFolder

if not exist "%~1" (
    mkdir "%~1"
    echo [OK] Pasta criada: %~1
) else (
    echo [--] Pasta ja existe: %~1
)

exit /b

:: =====================================================
:: FUNÇÃO - CRIAR ARQUIVO
:: =====================================================

:CreateFile

if not exist "%~1" (
    type nul > "%~1"
    echo [OK] Arquivo criado: %~1
) else (
    echo [--] Arquivo ja existe: %~1
)

exit /b