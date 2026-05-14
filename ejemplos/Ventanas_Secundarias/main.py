import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("300x200")
        
        ttk.Label(self, text="Ventana Principal", font=("Arial", 14)).pack(pady=20)
        
        self.lbl_resultado = ttk.Label(self, text="Esperando datos...")
        self.lbl_resultado.pack(pady=10)
        
        ttk.Button(self, text="Abrir Ventana Secundaria", command=self.abrir_secundaria).pack(pady=10)

    def abrir_secundaria(self):
        # Crear la ventana secundaria (Toplevel)
        ventana_hija = tk.Toplevel(self)
        ventana_hija.title("Ventana Secundaria")
        ventana_hija.geometry("250x150")
        
        # Obligar a que la ventana hija esté siempre por encima de la principal y no permita interactuar con la de atrás
        ventana_hija.grab_set() 
        
        ttk.Label(ventana_hija, text="Ingresa un dato:").pack(pady=10)
        entrada = ttk.Entry(ventana_hija)
        entrada.pack(pady=5)
        
        # Función para enviar el dato de vuelta a la ventana principal
        def enviar_dato():
            texto = entrada.get()
            self.lbl_resultado.config(text=f"Recibido: {texto}")
            ventana_hija.destroy() # Cierra la ventana secundaria
            
        ttk.Button(ventana_hija, text="Enviar", command=enviar_dato).pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
