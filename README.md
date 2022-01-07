# rutScraper
## Scraper 'Quick-and-Dirty' de la página nombrerutyfirma.com
Un pequeño script hecho en Python que te permite obtener un archivo CSV que contiene nombre, RUT y/o dirección de una lista de personas a partir de un archivo CSV de nombres completos o RUT.
## Ejemplo
### Datos de entrada (input.csv)
```CSV
RUT
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
Juan Pérez,Pasaje Almirante Señoret 70 Valparaíso
Pedro Pérez, Calle Arturo Prat 2910 San Miguel
No encontrado!,No encontrado!
John Doe,Calle San Gerardo 1148 Recoleta
Benjamin Brereton,No Disponible: Territorio Extranjero
Jane Doe,Avenida Isidora Goyenechea 2890 Las Condes
John Smith,Calle Almirante Montt 472 Santiago
Cosme Fulanito,Avenida Ñuble 350 Pucón
```
