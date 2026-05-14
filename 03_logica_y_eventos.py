"""
Paso 3: Lógica y Eventos
Finalmente, le damos "vida" a la aplicación.
Conectamos una función (lógica) a la acción de presionar el botón (evento).
"""
import tkinter as tk

def saludar():
    """
    Esta función se ejecuta SOLO cuando el usuario hace clic en el botón.
    """
    # 1. Obtenemos el estado actual del componente Entry
    nombre = entrada_nombre.get()
    
    # 2. Modificamos el estado (la propiedad 'text') del componente Label
    if nombre != "":
        etiqueta_saludo.config(text=f"¡Hola, {nombre}!")
    else:
        etiqueta_saludo.config(text="¡Por favor, ingresa tu nombre!")

# --- CONFIGURACIÓN DE VENTANA ---
ventana = tk.Tk()
ventana.title("Aplicación Interactiva")
ventana.geometry("400x250")

# --- CREACIÓN DE COMPONENTES ---
etiqueta_instruccion = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_instruccion.pack(pady=10)

entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# --- CONECTANDO EVENTOS ---
# El parámetro 'command' enlaza el clic del botón con la función 'saludar'
boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=15)

etiqueta_saludo = tk.Label(ventana, text="", font=("Arial", 14, "bold"), fg="blue")
etiqueta_saludo.pack(pady=10)

ventana.mainloop()
