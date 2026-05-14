import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Frames y Notebook (Tabs)")
        self.geometry("400x300")

        # Crear el Notebook (Tabhost)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Crear los frames
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)

        # Agregar los frames al notebook
        self.notebook.add(self.frame1, text="Vista 1")
        self.notebook.add(self.frame2, text="Vista 2")
        self.notebook.add(self.frame3, text="Vista 3")

        # Contenido del Frame 1
        tk.Label(self.frame1, text="Contenido de la primera vista", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.frame1, text="Acción en Vista 1", command=lambda: print("Click en Vista 1")).pack(pady=10)

        # Contenido del Frame 2
        tk.Label(self.frame2, text="Contenido de la segunda vista", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.frame2, text="Ingresa un dato:").pack()
        tk.Entry(self.frame2).pack(pady=5)

        # Contenido del Frame 3
        tk.Label(self.frame3, text="Contenido de la tercera vista", font=("Arial", 14)).pack(pady=20)
        self.check_var = tk.BooleanVar()
        tk.Checkbutton(self.frame3, text="Aceptar términos", variable=self.check_var).pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
