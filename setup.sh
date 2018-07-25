#!/usr/bin/env bash

pip -V >nul 2>nul || (echo failed to find pip)
echo
echo
echo ##########################################
echo Installing virtualenv
echo ##########################################
echo
echo
pip install virtualenv
echo
echo
echo ##########################################
echo Created virtual environment
echo ##########################################
echo
echo
virtualenv venv
echo
echo
echo ##########################################
echo Activating virtual environment
echo ##########################################
echo
echo
source venv/bin/activate
echo
echo
echo ##########################################
echo Installing python packages
echo ##########################################
echo
echo
pip install -r requirements.txt
echo
echo ##########################################
echo Successfully installed all dependancies
echo ##########################################
echo