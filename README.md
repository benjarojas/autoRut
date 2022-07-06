# autoRut
## Scraper 'Quick-and-Dirty' de la página nombrerutyfirma.com
Un pequeño script hecho en Python que permite automatizar el proceso de recolección de datos públicos.\
Crea un archivo CSV que contiene nombre, RUT y/o dirección de una lista de personas a partir de un archivo CSV de sus nombres completos o RUT a consultar.

## Nota: El sitio ahora usa CloudFlare, por lo que este script ya no funciona

## Dependencias
- ```Python 3.9.6 o posterior```
- ```rut-chile```
- ```bs4```

### Instalación de Dependencias
```sh
$ git clone https://github.com/benjarojas/autoRut
$ cd autoRut
$ pip install -U -r requirements.txt
```
## Ejemplos de uso
### Ejemplo de uso con RUT
```sh
$ python3 autoRut.py input.csv output.csv rut --addr --delay 1
```
### Datos de entrada (input.csv)
```CSV
rut
12345678-5
11111111-1
1-9
22222222-2
33333333-3
44444444-4
77777777-7
```
### Datos de salida (output.csv)
```CSV
nombres,direccion
Juan Pérez,Arauco 769 Punta Arenas
Pedro Pérez,Baquedano 532 Antofagasta
no encontrado!,no encontrado!
John Doe,Casilla 9 Los Rios
Benjamin Brereton,No Disponible:Territorio Extranjero Inglaterra
John Smith,Calle Andes 4050 Quinta Normal
Cosme Fulanito,Avenida Sargento Silva 673 Pto. Montt
```
### Ejemplo de uso con nombres
```sh
$ python3 autoRut.py input.csv output.csv name --delay 1
```
### Datos de entrada (input.csv)
```CSV
nombres
Juan Pérez
Pedro Pérez
John Cena
John Doe
Benjamin Brereton
John Smith
Cosme Fulanito
```
### Datos de salida (output.csv)
```CSV
rut
12345678-5
11111111-1
no encontrado!
22222222-2
33333333-3
44444444-4
77777777-7
```
