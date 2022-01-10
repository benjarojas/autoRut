# autoRut.py
## Scraper 'Quick-and-Dirty' de la página nombrerutyfirma.com
Un pequeño script hecho en Python que permite automatizar el proceso de recolectar datos públicos.\
Crea un archivo CSV que contiene nombre, RUT y/o dirección de una lista de personas a partir de un archivo CSV de sus nombres completos o RUT a consultar.
## Requisitos
- ```Python 3.9.6 o posterior```
- ```rut-chile```
- ```bs4```

### Instalación de Requisitos
```sh
$ git clone https://github.com/benjarojas/autoRut.py
$ cd autoRut.py
$ pip install -U -r requirements.txt
```
## Ejemplo de uso
```sh
$ python3 autoRut.py input.csv output.csv rut
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
nombres
Juan Pérez
Pedro Pérez
No encontrado!
John Doe
Benjamin Brereton
Jane Doe
John Smith
Cosme Fulanito
```
