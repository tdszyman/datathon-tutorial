@echo off

Rem starts the flask server
set FLASK_APP=awesomeapp/api.py
set FLASK_DEBUG=1
flask run