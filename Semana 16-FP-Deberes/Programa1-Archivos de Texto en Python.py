#UNIVERSIDAD ESTATAL AMAZONICA
#WILLIAM DELGADO
#FUNDAMENTOS DE PROGRAMACION
#Programa 1: Diccionarios en Python

# Escritura del archivo my_notes.txt

def escribir_archivo():
    """crear y escribir en el archivo de notas"""
    print("\nCreando archivo 'my_notes.txt'...")

    try:
        # Abrimos el archivo en escritura
        with open('my_notes.txt', 'w', encoding='utf-8') as file:
            # Escribimos tres líneas de notas personales
            file.write("1. Recordar salir a correr el dia sabado.\n")
            file.write("2. Terminar deberes y pruebas pendientes.\n")
            file.write("3. Recordar salir a pasear en visicleta el dia domingo.\n")

        print("Archivo creado y datos escritos correctamente.")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

# Lectura del archivo línea por línea

def leer_archivo():
    """Función para leer el archivo línea por línea"""
    print("\nLeyendo archivo 'my_notes.txt':")

    try:
        # Abrimos el archivo en lectura
        with open('my_notes.txt', 'r', encoding='utf-8') as file:
            # Usando readline() en un bucle
            print("\nMétodo 1 - Usando readline():")
            line = file.readline()
            while line:
                print(f"Línea: {line.strip()}")
                line = file.readline()

            # Iterando directamente sobre el archivo
            print("\nMétodo 2 - Iterando sobre el archivo:")
            file.seek(0)  # Volvemos al inicio del archivo
            for line_num, line in enumerate(file, 1):
                print(f"Línea {line_num}: {line.strip()}")

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

# Ejecución principal del programa

if __name__ == "__main__":
    # Escribimos el archivo
    escribir_archivo()

    # Leemos el archivo
    leer_archivo()

    print("\nProceso completado. El archivo se cerró automáticamente.")