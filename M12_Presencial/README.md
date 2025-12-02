## Entrega
El archivo Python gestion_registros.py (que debe contener la solución a ambas partes).
Los archivos de datos generados: mi_registro.txt y producto_nuevo.json.

# Parte 1: El Lector de Registros (Archivos de Texto Plano)
Conceptos a practicar: open(), modos 'w' y 'r', with open(), write(), readlines().

Instrucciones:
1. Crear el Registro Inicial (Escritura):
2. Crea un nuevo archivo Python llamado gestion_registros.py.
3. Dentro de este script, usa el modo de escritura 'w' y la estructura with open(...) para crear un archivo de texto llamado mi_registro.txt.
4. Escribe las siguientes cuatro líneas en el archivo 
(asegúrate de incluir el salto de línea ’\n 
′
 ):

"Usuario: Ana - Ciudad: Madrid"
"Usuario: Marleny - Ciudad: Barcelona"
"Usuario: Sandra - Ciudad: Sevilla"
"Usuario: Enrique - Ciudad: Valencia"

5. Leer y Filtrar el Registro (Lectura):
En el mismo script, usa la estructura with open(...) nuevamente, pero esta vez con el modo de lectura 'r', para abrir mi_registro.txt.

6. Utiliza el método readlines() para cargar todas las líneas del archivo en una variable de tipo lista llamada lineas_registro.

7. Itera sobre esta lista e imprime solamente las líneas que contengan la palabra "Madrid" o "Sevilla".

8. Anexar Nuevos Datos (Anexar):
Usa el modo 'a' (anexar) para abrir mi_registro.txt.
9. Añade una nueva línea al final del archivo: "Usuario: Elena - Ciudad: Bilbao".
10. Vuelve a realizar el paso 2 para confirmar que la nueva línea de Elena ahora está presente cuando lees el archivo.

# Parte 2: El Conversor de Datos (CSV y JSON)

Instrucciones:
1. Crear un Archivo CSV:
2. Crea un archivo llamado inventario_productos.csv con el siguiente contenido (puedes crearlo manualmente o usando Python, si ya conoces el módulo csv.writer):

Code snippet

ID,Nombre,Precio,Stock
101,Monitor,150.99,25
102,Teclado,35.50,150
103,Raton,18.00,300
Leer el CSV e Imprimir:

3. En tu script gestion_registros.py, importa el módulo csv.
4. Usa with open(...) y csv.reader para leer inventario_productos.csv.
5. Itera sobre las filas e imprime solo los productos cuyo Stock sea menor a 100.
6. Convertir a JSON (Serialización):
Crea un diccionario de Python que represente un nuevo producto:

Python
nuevo_producto = {
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}

7. Importa el módulo json.

8. Usa la función json.dump() para guardar este diccionario en un nuevo archivo llamado producto_nuevo.json.

Cargar desde JSON (Deserialización):
9. Usa la función json.load() para leer el contenido del archivo producto_nuevo.json y cargarlo de nuevo en una variable de Python llamada data_cargada.
10. Imprime el Nombre y el Precio del producto cargado para verificar que la conversión fue exitosa.

---

# 📘 Desarrollo – Módulo 12 Presencial: Gestión de Registros

## Parte 1: Lector y Gestor de Registros (mi_registro.txt)

En la Parte 1, el programa crea el archivo **mi_registro.txt** usando el modo de escritura `'w'` y la función `open()` dentro de un bloque `with`.  
Se escriben cuatro líneas con usuarios y ciudades:

- Usuario: Ana – Madrid  
- Usuario: Marleny – Barcelona  
- Usuario: Sandra – Sevilla  
- Usuario: Enrique – Valencia  

Luego, el programa vuelve a abrir el archivo en modo lectura `'r'` y usa `readlines()` para cargar todas las líneas en una lista llamada `lineas_registro`.  
Se recorre esa lista e imprime solo las líneas que contienen las palabras **"Madrid"** o **"Sevilla"`, cumpliendo con el filtro pedido.

Después, se abre el archivo en modo anexar `'a'` y se añade una nueva línea:

- Usuario: Elena – Bilbao  

Finalmente, se vuelve a leer el archivo completo para confirmar que la nueva línea de Elena se agregó correctamente.

---

## Parte 2: Conversor de Datos (CSV y JSON)

En la Parte 2 se trabaja con el archivo **inventario_productos.csv**, que contiene:

- ID, Nombre, Precio, Stock  
- 101, Monitor, 150.99, 25  
- 102, Teclado, 35.50, 150  
- 103, Raton, 18.00, 300  

El programa usa `csv.reader` para leer el archivo y recorre cada fila, imprimiendo solo los productos cuyo **Stock es menor a 100**.  
Con los datos actuales, se imprime únicamente el **Monitor**, que tiene stock 25.

Luego se crea un diccionario de Python:

```python
{
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}
