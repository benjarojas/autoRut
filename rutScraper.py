import csv
import requests
from time import sleep
from bs4 import BeautifulSoup
from rut_chile.rut_chile import format_rut_with_dots

URL = "https://www.nombrerutyfirma.com/rut" # Url de la API RUT

# Nombre a partir de RUT
# Abrimos el archivo donde guardaremos los resultados
with open('names.csv', 'w', encoding='UTF8', newline='') as out:
    writer = csv.writer(out)
    writer.writerow(['nombres'])
    with open ('rut.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0 # RUT procesados
        found = 0 # RUT encontrados
        for line in csv_reader:
            if(count == 0):
                print("Archivo:", csv_file.name)
                count += 1
            sleep(3) # Delay para evitar bloqueo de IP (cloudflare)
            print("")
            print("Procesando:", format_rut_with_dots(line["RUT"]))
            response = requests.get(URL, params={'term': format_rut_with_dots(line["RUT"])}).text
            soup = BeautifulSoup(response, 'html.parser')
            out = soup.find_all('td')  # Buscamos todas las etiquetas <td> dentro de la respuesta HTML
            if out: # Si el set no está vacio
                print("Nombre encontrado:", out[0].text)
                writer.writerow([out[0].text])
                found += 1
            else: # Si el set esta vacio
                print("No encontrado!")
                writer.writerow(['No encontrado!'])
            count += 1
        print(count-1, "RUT procesados,", found, "encontrados!")