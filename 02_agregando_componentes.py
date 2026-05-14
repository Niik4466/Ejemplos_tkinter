"""
Paso 2: Agregando Componentes (Widgets)
Aquí añadimos elementos visuales a nuestra ventana.
Nota que aún no tienen "vida" (el botón no hace nada si lo presionas).
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Componentes Básicos")
ventana.geometry("400x250")

# --- COMPONENTES (WIDGETS) ---

# 1. Etiqueta (Label) - Para mostrar texto fijo
etiqueta_instruccion = tk.Label(ventana, text="Ingresa tu nombre:")
# .pack() sirve para colocar el componente en la ventana. pady da un margen vertical.
etiqueta_instruccion.pack(pady=10) 

# 2. Entrada de texto (Entry) - Para que el usuario escriba
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# 3. Botón (Button) - Para que el usuario haga clic
# Por ahora, es un botón "tonto", no hace nada.
boton_saludar = tk.Button(ventana, text="Saludar")
boton_saludar.pack(pady=15)

# 4. Etiqueta de resultado (Label) - Inicialmente vacía
etiqueta_saludo = tk.Label(ventana, text="", font=("Arial", 14, "bold"), fg="blue")
etiqueta_saludo.pack(pady=10)

ventana.mainloop()
