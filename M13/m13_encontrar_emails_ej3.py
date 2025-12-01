# --------------------------------------------------------------------------
#          FUNCIÓN PARA ENCONTRAR EMAILS USANDO EXPRESIONES REGULARES
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que utilice el módulo `re` (expresiones
# regulares) para encontrar todas las direcciones de correo electrónico
# válidas dentro de una cadena de texto.
#
# Instrucciones para el estudiante:
# 1. Importa el módulo `re`.
# 2. Completa la función `encontrar_emails`.
# 3. Dentro de la función, define un patrón de expresión regular para un email.
#    Un patrón simple puede ser: r'[\w\.-]+@[\w\.-]+'
#    (Este patrón busca secuencias de caracteres de palabra, puntos o guiones,
#    seguidos de un @, y luego otra secuencia similar).
# 4. Usa la función `re.findall(patron, texto)` para encontrar todas las
#    coincidencias del patrón en el texto de entrada.
# 5. La función `re.findall` ya devuelve una lista de todas las coincidencias,
#    así que simplemente devuelve el resultado de esa llamada.
# --------------------------------------------------------------------------

# TODO: Paso 1. Importa el módulo de expresiones regulares.
import re


def encontrar_emails(texto):
    """
    Encuentra todas las direcciones de correo electrónico en una cadena de texto.

    Args:
      texto (str): El texto en el que se buscarán los correos.

    Returns:
      list: Una lista de cadenas, donde cada cadena es un email encontrado.
            Devuelve una lista vacía si no se encuentra ninguno.
    """

    # TODO: Paso 2. Define el patrón de expresión regular para un email.
    patron = r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}'

    # TODO: Paso 3. Usa re.findall() para encontrar todas las coincidencias.
    emails_encontrados = re.findall(patron, texto)

    # TODO: Paso 4. Devuelve la lista de emails encontrados.
    return emails_encontrados


# --- Bloque para probar tu función ---
if __name__ == "__main__":
    texto_de_prueba = """
    Este es un texto de prueba. El correo del admin es admin@example.com.
    Para soporte, contacte a support@mi-weber.edu.
    No enviar correo a usuario.invalido@.
    El correo de Juana es juana.perez@email.utah.
    """

    emails = encontrar_emails(texto_de_prueba)
    print("Emails encontrados:")
    print(emails)
   # Salida esperada: ['admin@example.com', 'support@mi-weber.edu', 'juana.perez@email.utah']


# TODO Analizar
"""
1.  **Impacto de la TLD (`{2,}`) y el Patrón de Dominio:**

  - Si cambiamos `\.[a-zA-Z]{2,}` a `\.[a-zA-Z]{1,}`, la expresión comenzaría a aceptar dominios como:
    `.a`, `.b`, `.x`, que NO existen en la vida real. Aceptaría dominios inválidos.

  - Si cambiamos a `\.[a-zA-Z]{3}`, solamente aceptaría dominios de EXACTAMENTE tres letras.
    Esto haría fallar correos válidos:
      - `example.pe` (2 letras → inválido para este patrón)
      - `example.io` (2 letras → inválido)
      - `example.info` (4 letras → inválido)
    Es decir, volvería la expresión demasiado estricta.

2.  **Límites del Patrón de Nombre de Usuario:**

  El patrón `[a-zA-Z0-9._%+-]+` permite usar `_` o `-`, pero:
  - No controla **dónde** se colocan esos caracteres.
  - Por eso un email como `_mi-usuario-@dominio.com` puede fallar en validaciones más estrictas,
    porque no se quiere permitir que el nombre de usuario empiece o termine con caracteres especiales.

  Si queremos permitir un guion bajo SOLO si va seguido de letra o número, podríamos usar:

    `(?:_[A-Za-z0-9]|[A-Za-z0-9])[A-Za-z0-9._%+-]*[A-Za-z0-9]`

  Este patrón garantiza:
  - No empieza con guion bajo suelto.
  - No termina en guion bajo.
  - Solo permite `_` si lo sigue una letra o número.

3.  **Diferencia entre `re.search()`, `re.match()` y `re.findall()`:**

  - `re.findall()` devuelve **una lista de TODAS las coincidencias**.
    Ejemplo:  
    `['admin@example.com', 'support@mi-weber.edu', 'juana.perez@email.utah']`

  - `re.search()` devuelve SOLO la **primera coincidencia** como un objeto Match.
    En este texto, solo devolvería:
    `admin@example.com`

  - `re.match()` busca SOLO al **inicio del texto**.
    Como el texto empieza con “Este es un texto…”, NO hay email al inicio → devuelve `None`.

  **Conclusión:**  
  `findall()` es la única opción correcta para este ejercicio porque necesitamos encontrar
  **varios correos a la vez**, no solo el primero.
"""
