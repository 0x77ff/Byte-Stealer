@echo off

REM Set the Python version to install
set "PYTHON_VERSION=3.9.12"

REM Construct the Python download URL
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"

REM Set the name of the Python installer executable
set "PYTHON_EXE=python-installer.exe"

REM Download Python installer using PowerShell and Invoke-WebRequest
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_EXE%'"

REM Run the Python installer silently with desired options
start /wait %PYTHON_EXE% /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1 Include_doc=0

REM Add Python to the system PATH
setx PATH "%PATH%;C:\Python39;C:\Python39\Scripts" /M

REM Delete the Python installer after installation
del %PYTHON_EXE%

echo Python is installed!
pause