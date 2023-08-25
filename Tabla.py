from bs4 import BeautifulSoup
import requests
import time
import os
 
tabla = []


url = "https://www.promiedos.com.ar/primera"

r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

        
partidos = soup.find_all("table",class_='tablesorter5')

for tbody in partidos:
    partidos = tbody.find_all("tr")
    for partido in partidos:
        posicion = partido.td
       
        for equipo in partido.find_all("td",{"align" : "left"}): 

            imagen = str("https://www.promiedos.com.ar/" + equipo.img.get('src'))
            modelo = {
                "equipo": equipo.text,
                "posicion": posicion.text,
                "imagen": imagen
            }
            tabla.append(modelo)
            
for equipo in tabla:
    print(str("Pos: " + equipo['posicion'] + " - Equipo: " +  equipo['equipo'] + " - Imagen del Equipo: " + equipo['imagen']))