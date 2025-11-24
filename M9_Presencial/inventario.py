# --- Base de datos de Inventario --- Trabajo entre parejas ---
# Este programa gestiona un inventario de productos utilizando un diccionario.
# Cada producto se almacena como una clave en el diccionario, con su valor
inventario = {
    "Laptop": (1200.00, 15),
    "Mouse Inalámbrico": (25.50, 40),
    "Teclado Mecánico": (85.00, 22),
    "Monitor 27in": (350.00, 10)
}

def mostrar_inventario():
    """Imprime el inventario actual de forma legible."""
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'PRODUCTO':<20}{'PRECIO':>10}{'STOCK':>10}")
    print("-" * 40)
    for nombre, detalles in inventario.items():
        precio, stock = detalles
        print(f"{nombre:<20}${precio:>9.2f}{stock:>10}")
    print("-------------------------")

def agregar_producto(nombre, precio, stock):
    """Agrega un nuevo producto o actualiza el stock/precio de uno existente."""
    nueva_tupla = (precio, stock)
    inventario[nombre] = nueva_tupla
    print(f"\n✅ Producto '{nombre}' agregado/actualizado.")

def buscar_precio(nombre):
    """Busca y retorna el precio unitario de un producto."""
    if nombre in inventario:
        precio, _ = inventario[nombre]     # Solo usamos el precio, ignoramos el stock
        return precio
    else:
        return None                        # Retorna None si no existe

def valor_total_inventario():
    """Calcula el valor monetario total de todos los productos en stock."""
    valor_total = 0.0
    for precio, stock in inventario.values():
        valor_total += precio * stock
    return valor_total

# --- Pruebas del Programa ---

# 1. Mostrar el inventario inicial
mostrar_inventario()

# 2. Agregar un nuevo producto
agregar_producto("Webcam HD", 49.99, 30)

# 3. Mostrar inventario actualizado
mostrar_inventario()

# 4. Buscar el precio de un producto
precio_mouse = buscar_precio("Mouse Inalámbrico")

if precio_mouse is not None:
    print(f"\nPrecio del Mouse Inalámbrico: ${precio_mouse:.2f}")
else:
    print("\nProducto 'Mouse Inalámbrico' no encontrado en el inventario.")

# 5. Calcular el valor total del inventario
total = valor_total_inventario()
print(f"\nValor total estimado de todo el inventario: ${total:,.2f}")

# --- Fin del programa ---
