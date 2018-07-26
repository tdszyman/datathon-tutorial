@echo off
pip -V >nul 2>nul || (echo unable to find pip && pause && EXIT)
echo.
echo.
echo ##########################################
echo Installing virtualenv
echo ##########################################
echo.
echo.
pip install virtualenv
echo.
echo.
echo ##########################################
echo Created virtual environment
echo ##########################################
echo.
echo.
virtualenv venv
echo.
echo.
echo ##########################################
echo Activating virtual environment
echo ##########################################
echo.
echo.
CALL venv/Scripts/activate.bat
echo.
echo.
echo ##########################################
echo Installing python packages
echo ##########################################
echo.
echo.
pip install -r requirements.txt

echo.
echo.
echo ##########################################
echo Successfully installed all dependancies
echo ##########################################
echo.
echo.
pause