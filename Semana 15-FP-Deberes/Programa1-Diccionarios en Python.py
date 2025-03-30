#UNIVERSIDAD ESTATAL AMAZONICA
#WILLIAM DELGADO
#FUNDAMENTOS DE PROGRAMACION
#Programa 1: Diccionarios en Python

# Creación del diccionario
informacion_personal = {
    "nombre": "William Delgado",
    "edad": 24,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceso y modificacion de la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Ver si el telefono existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999888777"

# Eliminar la edad
del informacion_personal["edad"]

# Imprimir el diccionario
print(informacion_personal)