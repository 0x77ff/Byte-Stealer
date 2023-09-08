@echo off

set /p "ICON=Enter .ico file path for your exe?(Leave empty for no icon): "

if "%ICON%"=="" (
    echo pyarmor pack --clean -e "--onefile --noconsole " Logger.py
    call pyarmor pack --clean -e "--onefile --noconsole " Logger.py
    pause
) else (
    IF EXIST "%ICON%" (
        echo 
        call pyarmor pack --clean -e "--onefile --noconsole  --icon " "%ICON%" Logger.py
        pause
    ) ELSE (
        echo "%ICON%" is not a valid path.
    )
)

