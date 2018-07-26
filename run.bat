@echo off

Rem starts the flask server
CALL venv/Scripts/activate.bat
set FLASK_APP=awesomeapp/api.py
set FLASK_DEBUG=1
flask run