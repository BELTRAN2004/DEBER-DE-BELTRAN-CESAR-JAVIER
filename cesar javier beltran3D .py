# Crear una matriz 3D con temperaturas para 3 ciudades (Ciudad A, Ciudad B, Ciudad C)
# Cada ciudad tiene 4 días de la semana (Lunes a Jueves) y 2 semanas.
# Las temperaturas son valores aleatorios para este ejemplo.

import random

# Inicializar la matriz 3D
# [ciudades][días de la semana][semanas]
temperaturas = [
    [  # Ciudad A
        [random.randint(20, 30) for _ in range(4)],  # Semana 1
        [random.randint(20, 30) for _ in range(4)],  # Semana 2
    ],
    [  # Ciudad B
        [random.randint(15, 25) for _ in range(4)],  # Semana 1
        [random.randint(15, 25) for _ in range(4)],  # Semana 2
    ],
    [  # Ciudad C
        [random.randint(10, 20) for _ in range(4)],  # Semana 1
        [random.randint(10, 20) for _ in range(4)],  # Semana 2
    ]
]

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(matriz_3d):
    for i, ciudad in enumerate(matriz_3d):
        print(f"Ciudad {chr(65+i)}:")
        for j, semana in enumerate(ciudad):
            promedio = sum(semana) / len(semana)
            print(f"  Semana {j+1}: Promedio de temperatura: {promedio:.2f}°C")

# Llamar a la función para mostrar los promedios
calcular_promedio_temperaturas(temperaturas)