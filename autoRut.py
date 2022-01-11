import csv     
import argparse            
import requests
from time import sleep
from bs4 import BeautifulSoup
from rut_chile.rut_chile import format_rut_with_dots

parser = argparse.ArgumentParser(description='autoRut.py - script para automatizar la recolección de datos de nombrerutyfirma.com')

parser.add_argument('csv_input', type=str,
                    help='archivo de datos de entrada (.csv)')

parser.add_argument('csv_output', type=str,
                    help='archivo de datos de salida (.csv)')

parser.add_argument('mode', type=str,
                    help='define el tipo de datos del conjunto de entrada (rut|nom)')

parser.add_argument('--addr', action='store_true',
                    help='incluir dirección en los datos de salida')
""" Falta implementar:
parser.add_argument('--name', action='store_true',
                   help='incluir nombre en los datos de salida del modo name')

parser.add_argument('--rut', action='store_true',
                   help='incluir RUT en los datos de salida del modo rut')
"""

parser.add_argument('--delay', type=float,
                    help='definir delay entre cada petición en segundos para evitar ban de cloudflare (default: 2)')

args = parser.parse_args()

if(args.mode != "name" and args.mode != "rut"):
    parser.error("formato de entrada invalido, debe ser 'rut' o 'name'")

if(args.delay):
    delay = args.delay
else:
    delay = 2

if(args.mode == "rut"):
    URL = "https://www.nombrerutyfirma.com/rut"
else:
    URL = "https://www.nombrerutyfirma.com/buscar"

with open(args.csv_output, 'w', encoding='UTF8', newline='') as out:
    
    writer = csv.writer(out)
    
    if(args.addr):
        if(args.mode == "rut"):
            writer.writerow(['nombres', 'direccion'])
        else:
            writer.writerow(['rut', 'direccion'])
    else:
        if(args.mode == "rut"):
            writer.writerow(['nombres'])
        else:
            writer.writerow(['rut'])
    
    with open (args.csv_input, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0 # lineas procesadas
        found = 0 # lineas encontradas
    
        for line in csv_reader:
            if(count == 0):
                print("archivo de salida:", csv_file.name)
                count += 1
            sleep(delay) # Delay para evitar bloqueo de IP (cloudflare)
            print("")
            if(args.mode == "rut"):
                print("procesando rut:", format_rut_with_dots(line["RUT"]))
                response = requests.get(URL, params={'term': format_rut_with_dots(line["RUT"])}).text
            else:
                print("procesando nombre:", line["nombres"])
                response = requests.get(URL, params={'term': line["nombres"]}).text

            soup = BeautifulSoup(response, 'html.parser')
            out = soup.find_all('td')  # Buscamos todas las etiquetas <td> dentro de la respuesta HTML

            if out: # Si el set no está vacio
                if(args.addr):
                    if(args.mode == "rut"):
                        address = out[3].text + " " + out[4].text
                        print("nombre encontrado:", out[0].text)
                        print("dirección:", address)
                        writer.writerow([out[0].text, address])
                    else:
                        address = out[3].text + " " + out[4].text
                        print("RUT encontrado:", out[1].text)
                        print("dirección:", address)
                        writer.writerow([out[1].text, address])
                else:
                    if(args.mode == "rut"):
                        print("nombre encontrado:", out[0].text)
                        writer.writerow([out[0].text])
                    else:
                        print("RUT encontrado:", out[1].text)
                        writer.writerow([out[1].text])
                found += 1
            else: # Si el set esta vacio
                print("no encontrado!")
                if(args.addr):
                    writer.writerow(['no encontrado!', 'no encontrado!'])
                else:
                    writer.writerow(['no encontrado!'])
            count += 1
        if(args.mode == "rut"):    
            print(count-1, "RUT procesados,", found, "encontrados!")
        else:
            print(count-1, "nombres procesados,", found, "encontrados!")