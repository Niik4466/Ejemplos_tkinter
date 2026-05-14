import csv
import os

FILE_NAME = 'data.csv'

def initialize_file():
    """Crea el archivo CSV con sus cabeceras si no existe."""
    try:
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['RUT', 'FECHA', 'MONTO', 'LUGAR'])
        return True, "Archivo inicializado correctamente."
    except Exception as e:
        return False, f"Error de Sistema al inicializar el archivo: {e}"

def guardar_pago(rut:str, fecha:str, monto:str, lugar:str) -> tuple[bool, any]:
    """
    Añade un nuevo registro de pago al archivo CSV.
    Devuelve un booleando indicando si tuvo exito y un mensaje o datos
    """
    try:
        with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([rut, fecha, monto, lugar])
        return True, "Datos guardados en el archivo."
    except PermissionError:
        return False, "Error: Permiso denegado al escribir en el archivo (data.csv podría estar abierto en otro programa)."
    except Exception as e:
        return False, f"Error de Sistema al escribir en el archivo: {e}"

def obtener_pagos():
    """Lee y retorna todos los registros de pagos desde el archivo CSV."""
    try:
        if not os.path.exists(FILE_NAME):
            return True, []
        
        pagos = []
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pagos.append(row)
        return True, pagos
    except PermissionError:
        return False, "Error: Permiso denegado al leer el archivo."
    except csv.Error as e:
        return False, f"Error: El archivo CSV está corrupto o mal formado. Detalles: {e}"
    except Exception as e:
        return False, f"Error de Sistema al leer el archivo: {e}"
