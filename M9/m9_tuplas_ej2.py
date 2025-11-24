"""
PROYECTO DE PROGRAMACIÓN: Cadenas, tuplas, diccionarios y anagramas

Instrucciones:
Lee con atención cada ejercicio. Completa el código en las secciones marcadas como TODO.
Puedes probar tus funciones en la sección "if __name__ == '__main__'".
"""

# ============================
# EJERCICIO 1: Tuplas no hashables
# ============================

def tupla_no_hashable():  
    """
    Crea una tupla que contiene listas como elementos. Intenta usarla como clave en un diccionario.
    """
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    # Añadir el número 6 a la segunda lista usando la tupla
    t[1].append(6)
    print("Tupla modificada:", t)

    # Intentar usarla como clave en un diccionario
    try:
        dic = {t: "valor"}
    except TypeError:
        print("No se puede usar una tupla con listas como clave en un diccionario.")


# ============================
# EJERCICIO 2: Cifrado César
# ============================

def shift_word(word, shift):
    """
    Aplica un cifrado César a la palabra dada, desplazando cada letra por 'shift' posiciones.
    Se espera que la palabra esté en minúsculas y sin caracteres especiales.

    Ejemplo:
    shift_word("alegria", 7) -> "alegre"
    shift_word("melon", 16) -> "al cubo"
    """
    letters = 'abcdefghijklmnopqrstuvwxyzáéíóúñ '
    letter_map = dict(zip(letters, range(len(letters))))
    reverse_map = dict(zip(range(len(letters)), letters))

    result = []

    for letter in word:
        if letter in letter_map:
            new_pos = (letter_map[letter] + shift) % len(letters)
            result.append(reverse_map[new_pos])
        else:
            # Si es carácter no válido, lo dejamos igual
            result.append(letter)

    return ''.join(result)


# ============================
# EJERCICIO 3: Letras más frecuentes
# ============================

def most_frequent_letters(texto):
    """
    Recibe una cadena y muestra las letras ordenadas por frecuencia (de mayor a menor).
    """
    texto = texto.replace(" ", "").lower()

    conteo = {}
    for letra in texto:
        if letra.isalpha() or letra in "áéíóúñ":
            conteo[letra] = conteo.get(letra, 0) + 1

    # Ordenar por frecuencia
    ordenadas = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    print("Letras ordenadas por frecuencia:")
    for letra, freq in ordenadas:
        print(letra, "→", freq)


# ============================
# EJERCICIO 4: Anagramas en lista
# ============================

def encontrar_anagramas(lista_palabras):
    """
    Dada una lista de palabras, imprime todos los grupos de palabras que son anagramas.
    """
    grupos = {}

    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))  # palabra ordenada
        grupos.setdefault(clave, []).append(palabra)

    # imprimir solo los grupos con más de 1 palabra
    for grupo in grupos.values():
        if len(grupo) > 1:
            print(grupo)


# ============================
# EJERCICIO 5: Distancia entre palabras
# ============================

def word_distance(word1, word2):
    """
    Devuelve el número de letras distintas entre dos palabras de igual longitud.
    """
    diferencias = 0
    for a, b in zip(word1, word2):
        if a != b:
            diferencias += 1
    return diferencias


# ============================
# EJERCICIO 6: Pares de metátesis
# ============================

def encontrar_metatesis(lista_palabras):
    """
    Imprime todos los pares de palabras que son anagramas y difieren solo por una transposición.
    """
    # Primero, agrupar anagramas
    grupos = {}
    for palabra in lista_palabras:
        clave = ''.join(sorted(palabra))
        grupos.setdefault(clave, []).append(palabra)

    # Para cada grupo buscar pares que sean metátesis
    for grupo in grupos.values():
        if len(grupo) > 1:
            for i in range(len(grupo)):
                for j in range(i + 1, len(grupo)):
                    p1, p2 = grupo[i], grupo[j]

                    # Deben diferir exactamente en 2 posiciones
                    dif = [(a, b) for a, b in zip(p1, p2) if a != b]

                    if len(dif) == 2:
                        print((p1, p2))



# ============================
# PRUEBAS
# ============================

if __name__ == '__main__':
    print("EJERCICIO 1: Tupla no hashable")
    tupla_no_hashable()

    print("\nEJERCICIO 2: Cifrado César")
    print(shift_word("alegria", 7))    # Esperado: "alegre"
    print(shift_word("melon", 16))     # Esperado: "al cubo"

    print("\nEJERCICIO 3: Letras más frecuentes")
    most_frequent_letters("el veloz murciélago hindú comía feliz cardillo y kiwi")

    print("\nEJERCICIO 4: Anagramas en lista")
    palabras = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
                'retainers', 'ternaries', 'generating', 'greatening',
                'resmelts', 'smelters', 'termless']
    encontrar_anagramas(palabras)

    print("\nEJERCICIO 5: Distancia entre palabras")
    print(word_distance("casa", "cata"))  # Esperado: 1
    print(word_distance("luz", "pez"))    # Esperado: 2

    print("\nEJERCICIO 6: Pares de metátesis")
    palabras = ['conserve', 'converse', 'recostar', 'rescatro',
                'resmelts', 'smelters', 'termless']
    encontrar_metatesis(palabras)
