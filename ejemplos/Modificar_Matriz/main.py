import tkinter as tk
from tkinter import messagebox
import gestor_matriz # Importamos nuestro módulo de lógica

RUTA_CSV = "matriz.csv"

# Variables globales para guardar el estado de la aplicación
entradas_matriz = []

def cargar_y_mostrar():
    """Se encarga de pedir la matriz a la lógica y dibujarla en pantalla."""
    global entradas_matriz
    
    try:
        # 1. Leer y validar los datos usando nuestro módulo
        # Aquí es donde capturamos los posibles errores
        matriz = gestor_matriz.cargar_matriz(RUTA_CSV)
        
        # 2. Limpiar la interfaz (si había componentes anteriores dibujados)
        for widget in frame_matriz.winfo_children():
            widget.destroy()
            
        entradas_matriz = []
        
        # 3. Crear la cuadrícula de Entrys
        for i in range(len(matriz)):
            fila_entradas = []
            for j in range(len(matriz[i])):
                # Creamos un Entry para cada celda de la matriz
                entry = tk.Entry(frame_matriz, width=5, justify="center")
                entry.insert(0, str(matriz[i][j]))
                entry.grid(row=i, column=j, padx=5, pady=5)
                fila_entradas.append(entry)
                
            entradas_matriz.append(fila_entradas)
            
        # Habilitamos el botón de guardar porque ahora sí hay datos
        btn_guardar.config(state="normal")
        messagebox.showinfo("Éxito", "Matriz cargada correctamente.")
        
    except FileNotFoundError as e:
        # Si el archivo no existe, mostramos error rojo
        messagebox.showerror("Error de Archivo", str(e))
    except ValueError as e:
        # Si la matriz no es AxA o tiene strings, mostramos alerta amarilla
        messagebox.showwarning("Error de Formato", str(e))
    except Exception as e:
        messagebox.showerror("Error Inesperado", str(e))

def guardar_cambios():
    """Recoge los datos de la interfaz, los valida y los envía al módulo para guardar."""
    nueva_matriz = []
    
    # 1. Validar desde la interfaz que el usuario no haya escrito letras
    for i in range(len(entradas_matriz)):
        fila_valores = []
        for j in range(len(entradas_matriz[i])):
            texto_ingresado = entradas_matriz[i][j].get()
            try:
                valor_entero = int(texto_ingresado)
                fila_valores.append(valor_entero)
            except ValueError:
                # Mostrar ventana de error si escribe texto en vez de número
                messagebox.showerror(
                    "Error de Ingreso", 
                    f"El valor '{texto_ingresado}' en la celda ({i+1}, {j+1}) no es un entero."
                )
                return # Cortar la función aquí para no guardar datos corruptos
        nueva_matriz.append(fila_valores)
        
    # 2. Si todo es válido, enviamos los datos a la Lógica
    try:
        gestor_matriz.guardar_matriz(RUTA_CSV, nueva_matriz)
        messagebox.showinfo("Guardado", "La matriz se ha actualizado en el archivo CSV.")
    except Exception as e:
        messagebox.showerror("Error al Guardar", str(e))

# --- INTERFAZ GRÁFICA PRINCIPAL ---
def main():
    global frame_matriz, btn_guardar
    # 1. Crear la instancia de la ventana
    ventana = tk.Tk()
    # 2. Configurar propiedades de la ventana
    ventana.title("Editor de Matriz")
    ventana.geometry("350x350")

    # Etiqueta de título
    titulo = tk.Label(ventana, text="Modificador de Matrices", font=("Arial", 14, "bold"))
    titulo.pack(pady=10)

    # Botón para cargar
    btn_cargar = tk.Button(ventana, text="Cargar Matriz CSV", command=cargar_y_mostrar)
    btn_cargar.pack(pady=5)

    # Frame (Contenedor) para agrupar las celdas usando .grid() en lugar de .pack()
    frame_matriz = tk.Frame(ventana)
    frame_matriz.pack(pady=10)

    # Botón para guardar (inicia deshabilitado hasta que se cargue una matriz)
    btn_guardar = tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios, state="disabled")
    btn_guardar.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
