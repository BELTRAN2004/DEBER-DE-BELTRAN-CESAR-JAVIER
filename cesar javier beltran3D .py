import random

# Función para generar temperaturas aleatorias para las ciudades
def generar_temperaturas():
    """
    Genera una matriz 3D de temperaturas aleatorias para 3 ciudades y 2 semanas.
    Cada ciudad tiene 4 días de la semana (Lunes a Jueves).
    
    Retorna:
    list: Una matriz 3D con las temperaturas generadas.
    """
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
    return temperaturas

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula el promedio de temperaturas para varias ciudades durante varias semanas.

    Parámetros:
    temperaturas (list): Una matriz 3D con las temperaturas por ciudad, semana y días de la semana.
    """
    # Recorrer la matriz 3D para calcular el promedio
    for i, ciudad in enumerate(temperaturas):
        print(f"Ciudad {chr(65 + i)}:")  # 'A' es 65 en el código ASCII
        for j, semana in enumerate(ciudad):
            promedio = sum(semana) / len(semana)  # Calcular el promedio de la semana
            print(f"  Semana {j + 1}: Promedio de temperatura: {promedio:.2f}°C")

# Llamada a la función para generar las temperaturas
temperaturas = generar_temperaturas()

# Llamar a la función para calcular y mostrar los promedios
calcular_promedio_temperaturas(temperaturas)
