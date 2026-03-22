@echo off
echo DefterX Backend baslatiliyor...
call venv\Scripts\activate
uvicorn main:app --reload --port 8000
pause