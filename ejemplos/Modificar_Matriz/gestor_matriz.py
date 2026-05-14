import os
import csv

def cargar_matriz(ruta_archivo):
    """
    Lee un archivo CSV y valida que contenga una matriz simétrica (AxA) 
    con números enteros exclusivamente.
    """
    # Validación 1: ¿Existe el archivo?
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe. ¡Asegúrate de crearlo!")

    matriz = []
    
    # Lectura del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            # Omitir filas en blanco si las hay
            if not fila:
                continue
                
            fila_enteros = []
            for valor in fila:
                # Validación 2: ¿Son números enteros?
                try:
                    entero = int(valor.strip())
                    fila_enteros.append(entero)
                except ValueError:
                    raise ValueError(f"El valor '{valor}' no es válido. Solo se permiten números enteros.")
            matriz.append(fila_enteros)
            
    # Validación 3: ¿La matriz está vacía?
    if len(matriz) == 0:
        raise ValueError("El archivo está vacío.")
        
    # Validación 4: ¿Es simétrica (AxA)?
    cantidad_filas = len(matriz)
    for i in range(len(matriz)):
        if len(matriz[i]) != cantidad_filas:
            raise ValueError(f"La matriz no es simétrica. Tiene {cantidad_filas} filas, pero la fila {i+1} tiene {len(matriz[i])} columnas.")
            
    return matriz

def guardar_matriz(ruta_archivo, matriz):
    """
    Guarda una matriz bidimensional en un archivo CSV.
    """
    with open(ruta_archivo, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.writer(archivo)
        for fila in matriz:
            escritor.writerow(fila)
