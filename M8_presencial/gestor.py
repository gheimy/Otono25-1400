# Programa para gestionar las notas de los estudiantes

def mostrar_menu():
    print("\n=== MENÚ ===")
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Salir")

def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

def main():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            notas = []

            for i in range(3):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {i+1}: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("⚠️ La nota debe estar entre 0 y 10.")
                    except ValueError:
                        print("⚠️ Ingresa un número válido.")

            promedio = calcular_promedio(notas)
            aprobado = promedio >= 6.0

            estudiante = {
                "nombre": nombre,
                "notas": notas,
                "promedio": promedio,
                "aprobado": aprobado
            }

            estudiantes.append(estudiante)
            print(f"\n✅ Estudiante {nombre} agregado correctamente.\n")

        elif opcion == "2":
            if not estudiantes:
                print("\nNo hay estudiantes registrados aún.")
            else:
                print("\n=== LISTA DE ESTUDIANTES ===")
                for est in estudiantes:
                    estado = "Aprobado ✅" if est["aprobado"] else "Reprobado ❌"
                    print(f"{est['nombre']:<15} | Promedio: {est['promedio']:.2f} | {estado}")

        elif opcion == "3":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

main()
