"""
Paso 1: La Ventana Básica
Este script muestra lo mínimo necesario para crear y mantener abierta 
una ventana en Tkinter.
"""
import tkinter as tk

# 1. Crear el objeto de la ventana principal
ventana = tk.Tk()

# 2. Configurar propiedades de la ventana
ventana.title("Mi Primera Ventana")
ventana.geometry("400x250") # Define el tamaño: Ancho x Alto

# 3. Iniciar el bucle principal de la aplicación (mainloop)
# Esto es vital: mantiene la ventana abierta y escuchando eventos (clics, teclas, etc.)
ventana.mainloop()
