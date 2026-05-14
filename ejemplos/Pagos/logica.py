from datos import guardar_pago, obtener_pagos

def registrar_pago(rut:str, fecha:str, monto:str, lugar:str):
    """
    Valida los datos y registra un nuevo pago.
    Retorna una tupla (booleano, mensaje) indicando éxito o error.
    """
    try:
        # Validaciones básicas de campos vacíos
        if not rut or not fecha or not monto or not lugar:
            return False, "Todos los campos son obligatorios."
            
        # Validar RUT (9 caracteres)
        if len(rut) != 9:
            return False, "El RUT debe tener exactamente 9 caracteres."
            
        # Validar Fecha (mes <= 12)
        try:
            partes_fecha = fecha.split('/')
            if len(partes_fecha) != 3:
                return False, "La fecha debe tener el formato DD/MM/YYYY."
            mes = int(partes_fecha[1])
            if mes < 1 or mes > 12:
                return False, "El mes de la fecha debe ser válido (entre 1 y 12)."
        except ValueError:
            return False, "El mes de la fecha debe ser numérico."
            
        # Validar Lugar (> 1 carácter)
        if len(lugar) <= 1:
            return False, "El nombre de la tienda debe tener más de 1 carácter."
        
        # Validar que el monto sea un número válido y mayor a 0
        try:
            monto_float = float(monto)
            if monto_float <= 0:
                return False, "El monto debe ser mayor a 0."
        except ValueError:
            return False, "El monto debe ser un valor numérico válido."
            
        # Llamar a la capa de datos verificando si hubo error a nivel de sistema o archivo
        exito_datos, mensaje_datos = guardar_pago(rut, fecha, f"{monto_float:.2f}", lugar)
        if not exito_datos:
            return False, mensaje_datos
            
        return True, "Pago registrado con éxito."
    except Exception as e:
        return False, f"Error inesperado en la lógica al registrar: {e}"

def listar_pagos():
    """
    Obtiene la lista de pagos registrados. 
    Retorna (booleano, lista_o_mensaje).
    """
    try:
        exito_datos, resultado = obtener_pagos()
        if not exito_datos:
            # Si hay error, 'resultado' contiene el mensaje de error de datos.py
            return False, resultado
        
        # Retorna el listado listo
        return True, resultado
    except Exception as e:
        return False, f"Error inesperado en la lógica al listar: {e}"
