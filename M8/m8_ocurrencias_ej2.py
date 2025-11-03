# --------------------------------------------------------------------------
#          FUNCIÓN PARA ELIMINAR UN ELEMENTO DE UNA LISTA
# --------------------------------------------------------------------------

def eliminar_elemento(lista_original, elemento_a_eliminar):
    """
    Crea una nueva lista sin las ocurrencias de un elemento específico.

    Args:
      lista_original (list): La lista de la que se eliminarán elementos.
      elemento_a_eliminar: El elemento que se desea eliminar.

    Returns:
      list: Una nueva lista sin el elemento especificado.
    """
    nueva_lista = []  # Paso 1
    for item in lista_original:  # Paso 2
        if item != elemento_a_eliminar:  # Paso 3
            nueva_lista.append(item)  # Paso 4
    return nueva_lista  # Paso 5


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    colores = ["rojo", "verde", "azul", "rojo", "amarillo", "rojo"]
    elemento = "rojo"

    lista_filtrada = eliminar_elemento(colores, elemento)

    print(f"Lista original: {colores}")
    print(f"Elemento a eliminar: '{elemento}'")
    print(f"Lista resultante: {lista_filtrada}")
