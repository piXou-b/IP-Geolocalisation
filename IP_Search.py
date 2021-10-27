import socket

#My IP adresse
hostname = socket.gethostname()
IPaddress = socket.gethostbyname(hostname)

print("Computer name is: %s" % hostname)
print("IP address is: %s" % IPaddress)

#---------------------------------------------------------------- 
import requests
import folium
import json


API_KEY = "fd2233f0-3456-11ec-9eeb-c1b33a419b4f"
BASE_URL = "https://api.freegeoip.app/json/"

ip = input("Quel est l'IPv6 a recherché? ")
url = BASE_URL + ip + "?apikey=" + API_KEY 

response = requests.get(url)
data = json.loads(response.content)


def data_ip_adresses():
    if response.status_code == 200:
        print(data)
    else:
        return None


def geolocation_ip_adresses():
    lat = data.get("latitude")
    long = data.get("longitude")
    coords = (lat, long)

    if coords != (0,0):
        map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=15)

        coords = [lat, long]
        folium.Marker(location=coords, popup = "IP target").add_to(map)

        map.save(outfile='./map.html')
        
        print()
        print("fichier .html creér: aller voir sur StreetmapView !!!")
    else:
        print("L'IP ne contient pas assez d'information !!!")


data_ip_adresses()
geolocation_ip_adresses()
