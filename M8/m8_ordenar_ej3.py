# --------------------------------------------------------------------------
#          FUNCIÓN PARA ORDENAR UNA LISTA Y DEMOSTRAR REFERENCIAS
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que modifique una lista directamente
# (in-place), ordenándola de mayor a menor. Además, este ejercicio
# demostrará cómo las variables en Python pueden apuntar al mismo objeto.
# --------------------------------------------------------------------------

def ordenar_de_mayor_a_menor(lista_numeros):
    """
    Ordena una lista de números de mayor a menor, modificándola en el lugar.

    Args:
      lista_numeros (list): La lista de números a ordenar.
    """
    # Paso 1. Ordena la lista de menor a mayor usando .sort()
    lista_numeros.sort()

    # Paso 2. Invierte la lista para que quede de mayor a menor.
    lista_numeros.reverse()

    # No se devuelve nada porque la lista se modifica directamente.


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    # --- Parte 1: Demostración de referencias ---
    print("--- Demostración de Referencias ---")
    numeros_a = [3, 1, 4, 1, 5, 9, 2]
    # 'numeros_b' no es una copia, ¡es otra etiqueta para la misma lista!
    numeros_b = numeros_a

    print(f"Antes de ordenar, lista A: {numeros_a}")
    print(f"Antes de ordenar, lista B: {numeros_b}")

    # Llamamos a la función para ordenar la lista A
    ordenar_de_mayor_a_menor(numeros_a)

    print(f"Después de ordenar, lista A: {numeros_a}")
    print(f"Después de ordenar, lista B: {numeros_b}")
    print("Observa: ¡La lista B también cambió! Ambas variables apuntan al mismo objeto.")

    # --- Parte 2: Cómo evitarlo con .copy() ---
    print("\n--- Evitando el problema con .copy() ---")
    numeros_c = [3, 1, 4, 1, 5, 9, 2]
    # 'numeros_d' es una copia independiente de la lista C.
    numeros_d = numeros_c.copy()

    print(f"Antes de ordenar, lista C: {numeros_c}")
    print(f"Antes de ordenar, lista D (copia): {numeros_d}")

    ordenar_de_mayor_a_menor(numeros_d)

    print(f"Después de ordenar la copia D, lista C: {numeros_c}")
    print(f"Después de ordenar la copia D, lista D: {numeros_d}")
    print("Observa: La lista C no cambió.")
# --------------------------------------------------------------------------
