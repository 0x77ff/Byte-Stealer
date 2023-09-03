@echo off

set /p "USER_INPUT=Input Logger.py file path: "
set /p "ICON=Enter .ico file path for your exe?(Leave empty for no icon): "

IF EXIST "%USER_INPUT%" (
    if "%ICON%"=="" (
        call Python -m pyarmor pack --clean -e "--onefile --clean --ascii --noconsole  --icon "%ICON%" " %USER_INPUT%
    ) else (
        IF EXIST "%ICON%" (
            call Python -m pyarmor pack --clean -e "--onefile --clean --ascii --noconsole  --icon "%ICON%" " %USER_INPUT%
        ) ELSE (
            echo "%ICON%" is not a valid path.
        )
    )
) ELSE (
    echo "%USER_INPUT%" is not a valid path.
)

pause
