#UNIVERSIDAD ESTATAL AMAZONICA
#WILLIAM DELGADO
#FUNDAMENTOS DE PROGRAMACION
#Programa 1: REGISTRO DE TEMPERATURAS DIARIAS
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula el promedio de temperaturas para cada ciudad y semana.

    Parámetros:
    temperaturas: Lista de listas que contiene los datos de temperaturas.
    ciudades: Lista de nombres de las ciudades.
    """
    for ciudad_idx, ciudad in enumerate(temperaturas):
        for semana_idx, semana in enumerate(ciudad):
            suma_temperaturas = sum([dia["temp"] for dia in semana])
            promedio = suma_temperaturas / len(semana)
            print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

# Datos de temperaturas
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 99},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 99},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 55}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 57},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 66},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 46},
            {"day": "Miércoles", "temp": 54},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 49}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 56},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 55},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 67},
            {"day": "Domingo", "temp": 44}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 64}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 97},
            {"day": "Jueves", "temp": 45},
            {"day": "Viernes", "temp": 49},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 56},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 48},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 98},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 46},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 56}
        ]
    ]
]

# Lista de ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamada a la función
calcular_promedio_temperaturas(temperaturas, ciudades)