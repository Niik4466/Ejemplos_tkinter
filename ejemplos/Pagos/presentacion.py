import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from logica import registrar_pago, listar_pagos
from datos import initialize_file

def limpiar_ventana(ventana):
    """Elimina todos los widgets (hijos) actuales de la ventana."""
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_menu_principal(ventana):
    """Construye la vista del menú principal."""
    limpiar_ventana(ventana)
    
    label_titulo = tk.Label(ventana, text="Sistema de Pagos de Tiendas", font=("Helvetica", 18, "bold"))
    label_titulo.pack(pady=50)
    
    btn_ingresar = tk.Button(ventana, text="Ingresar Datos", font=("Helvetica", 12), width=20, height=2,
                            command=lambda: mostrar_vista_ingresar(ventana))
    btn_ingresar.pack(pady=10)
    
    btn_ver = tk.Button(ventana, text="Ver Datos", font=("Helvetica", 12), width=20, height=2,
                        command=lambda: mostrar_vista_ver(ventana))
    btn_ver.pack(pady=10)

def mostrar_vista_ingresar(ventana):
    """Construye la vista del formulario para ingresar datos."""
    limpiar_ventana(ventana)
    
    label_titulo = tk.Label(ventana, text="Ingresar Nuevo Pago", font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=20)
    
    # Frame del formulario
    form_frame = tk.Frame(ventana)
    form_frame.pack(pady=10)
    
    # Variables de control
    var_rut = tk.StringVar()
    var_fecha = tk.StringVar()
    var_monto = tk.StringVar()
    var_lugar = tk.StringVar()

    # Etiquetas y campos de entrada
    tk.Label(form_frame, text="RUT:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_rut = tk.Entry(form_frame, textvariable=var_rut, font=("Helvetica", 12))
    entry_rut.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(form_frame, text="FECHA (DD/MM/YYYY):", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_fecha = tk.Entry(form_frame, textvariable=var_fecha, font=("Helvetica", 12))
    entry_fecha.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(form_frame, text="MONTO:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_monto = tk.Entry(form_frame, textvariable=var_monto, font=("Helvetica", 12))
    entry_monto.grid(row=2, column=1, padx=10, pady=10)
    
    tk.Label(form_frame, text="LUGAR (Tienda):", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_lugar = tk.Entry(form_frame, textvariable=var_lugar, font=("Helvetica", 12))
    entry_lugar.grid(row=3, column=1, padx=10, pady=10)
    
    def intentar_guardar():
        rut = var_rut.get().strip()
        fecha = var_fecha.get().strip()
        monto = var_monto.get().strip()
        lugar = var_lugar.get().strip()
        
        try:
            exito, mensaje = registrar_pago(rut, fecha, monto, lugar)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                # Limpiar formulario
                var_rut.set("")
                var_fecha.set("")
                var_monto.set("")
                var_lugar.set("")
            else:
                messagebox.showerror("Error", mensaje)
        except Exception as e:
            messagebox.showerror("Error Crítico", f"Error de sistema no manejado: {e}")
            
    # Botones
    btn_guardar = tk.Button(ventana, text="Guardar Pago", font=("Helvetica", 12), bg="red", command=intentar_guardar)
    btn_guardar.pack(pady=20)
    
    def validar_campos(*args):
        if var_rut.get().strip() and var_fecha.get().strip() and var_monto.get().strip() and var_lugar.get().strip():
            btn_guardar.config(bg="lightgreen")
        else:
            btn_guardar.config(bg="red")
            
    var_rut.trace_add("write", validar_campos)
    var_fecha.trace_add("write", validar_campos)
    var_monto.trace_add("write", validar_campos)
    var_lugar.trace_add("write", validar_campos)
    
    btn_volver = tk.Button(ventana, text="Volver al Menú", font=("Helvetica", 10),
                            command=lambda: mostrar_menu_principal(ventana))
    btn_volver.pack(pady=5)

def mostrar_vista_ver(ventana):
    """Construye la vista de la tabla para visualizar datos."""
    limpiar_ventana(ventana)
    
    label_titulo = tk.Label(ventana, text="Registros de Pagos", font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=10)
    
    # Tabla Treeview
    columns = ("RUT", "FECHA", "MONTO", "LUGAR")
    tree = ttk.Treeview(ventana, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
        
    tree.pack(fill="both", expand=True, padx=20, pady=10)
    
    btn_volver = tk.Button(ventana, text="Volver al Menú", font=("Helvetica", 10),
                            command=lambda: mostrar_menu_principal(ventana))
    btn_volver.pack(pady=10)
    
    # Cargar datos al iniciar esta vista
    try:
        exito, resultado = listar_pagos()
        if exito:
            for p in resultado:
                tree.insert("", tk.END, values=(p.get('RUT', ''), p.get('FECHA', ''), p.get('MONTO', ''), p.get('LUGAR', '')))
        else:
            messagebox.showerror("Error de Carga", resultado)
    except Exception as e:
        messagebox.showerror("Error Crítico", f"Fallo al cargar datos de la vista: {e}")

def iniciar_app():
    """Inicializa y arranca la aplicación de Tkinter."""
    # Inicializar base de datos primero y atrapar errores iniciales (como permisos o carpetas)
    exito_bd, mensaje_bd = initialize_file()
    
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Pagos")
    ventana.geometry("600x450")
    
    if not exito_bd:
        messagebox.showerror("Error Crítico Base de Datos", mensaje_bd)
        # Se avisa al usuario, pero se permite mostrar el menú (las acciones darán error manejado)
    
    mostrar_menu_principal(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_app()
