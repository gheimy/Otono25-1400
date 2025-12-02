import csv
import json

# -------------------------------
# PARTE 1: ARCHIVOS DE TEXTO
# -------------------------------

# 1. Crear archivo mi_registro.txt
with open("mi_registro.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Usuario: Ana - Ciudad: Madrid\n")
    archivo.write("Usuario: Marleny - Ciudad: Barcelona\n")
    archivo.write("Usuario: Sandra - Ciudad: Sevilla\n")
    archivo.write("Usuario: Enrique - Ciudad: Valencia\n")

print("✔ Archivo mi_registro.txt creado.")

# 2. Leer archivo y filtrar ciudades
print("\n📌 Usuarios de Madrid o Sevilla:")

with open("mi_registro.txt", "r", encoding="utf-8") as archivo:
    lineas_registro = archivo.readlines()

for linea in lineas_registro:
    if "Madrid" in linea or "Sevilla" in linea:
        print(linea.strip())

# 3. Añadir nueva línea
with open("mi_registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Usuario: Elena - Ciudad: Bilbao\n")

print("\n✔ Línea de Elena añadida.\n")

# Verificar que se agregó
print("📌 Confirmación del archivo actualizado:")
with open("mi_registro.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())


# -------------------------------
# PARTE 2: CSV → JSON
# -------------------------------

# 4. Leer CSV e imprimir productos con stock < 100
print("\n📦 PRODUCTOS CON STOCK < 100:")

with open("inventario_productos.csv", "r", encoding="utf-8") as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector)  # saltar encabezado
    for fila in lector:
        stock = int(fila[3])
        if stock < 100:
            print(fila)


# 5. Convertir diccionario a JSON
nuevo_producto = {
    "ID": 104,
    "Nombre": "Webcam",
    "Precio": 45.99,
    "Stock": 50
}

with open("producto_nuevo.json", "w", encoding="utf-8") as json_file:
    json.dump(nuevo_producto, json_file, indent=4)

print("\n✔ Archivo producto_nuevo.json creado.")

# 6. Cargar JSON de vuelta
with open("producto_nuevo.json", "r", encoding="utf-8") as json_file:
    data_cargada = json.load(json_file)

print("\n📦 PRODUCTO CARGADO DESDE JSON:")
print("Nombre:", data_cargada["Nombre"])
print("Precio:", data_cargada["Precio"])
