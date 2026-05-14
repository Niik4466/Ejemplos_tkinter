import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eventos y Funciones Lambda")
        self.geometry("350x300")
        
        # --- Uso de Lambdas ---
        ttk.Label(self, text="Botones con Lambda", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Sin lambda, no podemos pasar parámetros fácilmente a la función del botón
        # Con lambda, pasamos distintos saludos usando la misma función
        ttk.Button(self, text="Saludar Español", command=lambda: self.saludar("¡Hola!")).pack(pady=5)
        ttk.Button(self, text="Saludar Inglés", command=lambda: self.saludar("Hello!")).pack(pady=5)
        ttk.Button(self, text="Saludar Francés", command=lambda: self.saludar("Bonjour!")).pack(pady=5)
        
        ttk.Separator(self, orient='horizontal').pack(fill='x', pady=15)
        
        # --- Uso de Eventos (Bind) ---
        ttk.Label(self, text="Eventos del Teclado (Bind)", font=("Arial", 12, "bold")).pack(pady=5)
        ttk.Label(self, text="Escribe y presiona la tecla ENTER:").pack()
        
        self.entrada = ttk.Entry(self)
        self.entrada.pack(pady=5)
        
        # Vinculamos la tecla Enter (Return) a una función
        self.entrada.bind("<Return>", self.al_presionar_enter)
        
        # Vinculamos doble clic en la ventana, usamos un lambda también aquí para ignorar el argumento de evento
        self.bind("<Double-Button-1>", lambda evento: messagebox.showinfo("Clic", "¡Doble clic en la ventana!"))

    def saludar(self, mensaje):
        messagebox.showinfo("Saludo", mensaje)

    def al_presionar_enter(self, evento):
        # La función llamada por un bind() recibe siempre un parámetro 'evento'
        texto = self.entrada.get()
        messagebox.showinfo("Enter presionado", f"Escribiste: {texto}")
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
