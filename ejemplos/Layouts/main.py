import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Layouts (Grid y Pack)")
        
        # Frame superior usando PACK
        self.frame_top = ttk.Frame(self)
        self.frame_top.pack(fill='x', pady=10)
        
        ttk.Label(self.frame_top, text="Bienvenido al Formulario", font=("Arial", 16)).pack()
        ttk.Label(self.frame_top, text="Este título usa pack()").pack()

        # Frame central usando GRID (como una tabla)
        self.frame_grid = ttk.Frame(self)
        self.frame_grid.pack(pady=20)
        
        # Fila 0
        ttk.Label(self.frame_grid, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.frame_grid).grid(row=0, column=1, padx=5, pady=5)
        
        # Fila 1
        ttk.Label(self.frame_grid, text="Apellido:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.frame_grid).grid(row=1, column=1, padx=5, pady=5)
        
        # Botones inferiores usando PACK alineados a la izquierda
        self.frame_bottom = ttk.Frame(self)
        self.frame_bottom.pack(pady=10)
        
        ttk.Button(self.frame_bottom, text="Aceptar").pack(side="left", padx=5)
        ttk.Button(self.frame_bottom, text="Cancelar").pack(side="left", padx=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()
