Debugging
Este ejercicio tiene como propósito enseñarte cómo detectar y corregir errores (bugs) en un programa usando herramientas de depuración (debugging).

## Instrucciones para diagnostico.py:

Lee el código cuidadosamente. Ejecuta el programa. ¿Qué errores aparecen?
Usa técnicas de depuración como:
print() para imprimir variables y entender el flujo.
El depurador pdb (escribe import pdb; pdb.set_trace() en el código).
Corrige los errores hasta que el programa funcione correctamente.
Escribe las respuestas a estas preguntas:
1. ¿Qué errores encontraste?
#    - NameError: el programa intentaba usar la variable 'calificacion' en lugar de 'calificaciones'.
#    - Otro NameError: dentro de la función se usaba 'len(notas)' en vez de 'len(calificaciones)'.

2. ¿Cómo los descubriste?
#    - Ejecutando el programa y leyendo el mensaje de error (traceback) que indicaba 
#      la línea y la variable no definida.
#    - Revisando las variables en la función y notando la diferencia entre singular y plural.
3. ¿Cómo los corregiste?
#    - Cambié 'calificacion' por 'calificaciones' para que coincidiera con el nombre correcto de la lista.
#    - Reemplacé 'len(notas)' por 'len(calificaciones)' para usar la variable correcta.
#    - Probé el programa hasta que el promedio se mostró correctamente.

## Instrucciones para gestor.py:
Descarga el pdf llamado Gestor de Notas y sigue las preguntas.