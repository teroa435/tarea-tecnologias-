def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula el promedio de temperaturas de cada ciudad durante un período de semanas.

    Parámetros:
    temperaturas (list): Lista 3D que contiene temperaturas de múltiples ciudades en diferentes semanas.

    Retorna:
    dict: Diccionario con las ciudades como claves y los promedios semanales como valores.
    """
    # Nombres de las ciudades para referencia
    ciudades = ["Loja", "Quito", "Manta", "Guayaquil"]

    # Validar que la longitud de las temperaturas coincide con el número de ciudades
    if len(temperaturas) != len(ciudades):
        raise ValueError("El número de ciudades no coincide con los datos proporcionados.")

    promedios = {}  # Diccionario para almacenar los promedios de cada ciudad

    for ciudad_idx, ciudad in enumerate(temperaturas):
        total_temp = 0
        total_dias = 0

        for semana in ciudad:
            total_temp += sum(semana)
            total_dias += len(semana)

        promedio_ciudad = total_temp / total_dias
        promedios[ciudades[ciudad_idx]] = promedio_ciudad

    return promedios


# Ejemplo de datos de temperaturas para 4 ciudades durante 4 semanas
temperaturas = [
    [  # Loja
        [78, 80, 82, 79, 85, 88, 92],  # Semana 1
        [76, 79, 83, 81, 87, 89, 93],  # Semana 2
        [77, 81, 85, 82, 88, 91, 95],  # Semana 3
        [75, 78, 80, 79, 84, 87, 91]  # Semana 4
    ],
    [  # Quito
        [62, 64, 68, 70, 73, 75, 79],  # Semana 1
        [63, 66, 70, 72, 75, 77, 81],  # Semana 2
        [61, 65, 68, 70, 72, 76, 80],  # Semana 3
        [64, 67, 69, 71, 74, 77, 80]  # Semana 4
    ],
    [  # Manta
        [90, 92, 94, 91, 88, 85, 82],  # Semana 1
        [89, 91, 93, 90, 87, 84, 81],  # Semana 2
        [91, 93, 95, 92, 89, 86, 83],  # Semana 3
        [88, 90, 92, 89, 86, 83, 80]  # Semana 4
    ],
    [  # Guayaquil
        [72, 74, 76, 73, 71, 70, 68],  # Semana 1
        [73, 75, 77, 74, 72, 71, 69],  # Semana 2
        [74, 76, 78, 75, 73, 72, 70],  # Semana 3
        [75, 77, 79, 76, 74, 73, 71]  # Semana 4
    ]
]

# Llamar a la función para calcular los promedios
promedios_ciudades = calcular_promedio_temperaturas(temperaturas)

# Mostrar resultados
for ciudad, promedio in promedios_ciudades.items():
    print(f"{ciudad}: {promedio:.2f} grados")
