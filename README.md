# Guía de Introducción a Tkinter

## ¿Qué es Tkinter?
Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). 
Permite construir aplicaciones de escritorio con ventanas, botones, cuadros de texto y otros componentes interactivos de manera sencilla.

Es ideal para aprender cómo funcionan las aplicaciones gráficas porque viene incluido por defecto con Python, y es una excelente introducción a la **Programación Orientada a Eventos** (donde el programa reacciona a acciones del usuario, como clics de mouse o pulsaciones de teclado).

## ¿Cómo instalamos Tkinter?

La gran ventaja de Tkinter es que **viene incluido por defecto** en la mayoría de las instalaciones de Python. Por lo general, ¡no necesitas usar `pip install` ni descargar nada extra!

Sin embargo, dependiendo de tu sistema operativo, la situación puede variar ligeramente:

* **Windows y macOS:** Tkinter se instala automáticamente junto con Python cuando lo descargas de la página oficial. ¡Ya está listo para usar!
* **Linux (Ubuntu/Debian/Mint):** A veces, por cuestiones de optimización de espacio, no viene en la instalación base de Python. Si al ejecutar un código te arroja un error diciendo que no encuentra el módulo `tkinter`, puedes instalarlo fácilmente abriendo tu terminal y ejecutando:
  ```bash
  sudo apt-get install python3-tk
  ```

**¿Cómo comprobar si ya lo tienes instalado?**
Abre tu terminal o línea de comandos y escribe lo siguiente:
```bash
python -m tkinter
```
*(Nota: En Linux o Mac puede que necesites escribir `python3 -m tkinter`)*

Si al presionar Enter se abre una pequeña ventana gris de demostración, ¡significa que Tkinter está instalado y funcionando correctamente!

---

## Construcción de la Aplicación (Paso a Paso)

A continuación, construiremos nuestra primera aplicación dividiendo el proceso en 3 etapas fundamentales.

### Paso 1: La Ventana Básica (`01_ventana_basica.py`)
Toda aplicación gráfica necesita un contenedor principal: la ventana.

```python
import tkinter as tk

# Se crea la instancia de la ventana
ventana = tk.Tk()
ventana.title("Mi Primera Ventana") # Nombre de la ventana
ventana.geometry("400x250") # Dimensiones de la ventana

# Inicia el ciclo principal
ventana.mainloop()
```
**Linea Clave!:** `mainloop()` es un ciclo infinito que mantiene la ventana dibujada en pantalla y espera a que el usuario interactúe. Si no pones esta línea, el programa terminaría y la ventana se cerraría instantáneamente.

**Codigo**: [01_ventana_basica.py](01_ventana_basica.py)

---

### Paso 2: Agregando Componentes (`02_agregando_componentes.py`)
Una ventana vacía no es muy útil. Los "Componentes" o "Widgets" son los elementos visuales que ponemos dentro de ella.

* **Label:** Muestra texto (etiquetas).
* **Entry:** Un campo de una sola línea para que el usuario escriba.
* **Button:** Un botón clickeable.

```python
etiqueta_instruccion = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_instruccion.pack(pady=10) 
```
**Concepto Clave:** El método `.pack()` es un "gestor de geometría". Si creas un componente pero no llamas a `pack()`, `grid()` o `place()`, el componente **no aparecerá en la ventana**.

**Codigo**: [02_agregando_componentes.py](02_agregando_componentes.py)

---

### Paso 3: Lógica y Eventos (`03_logica_y_eventos.py`)
Tenemos los botones, pero no hacen nada. Necesitamos conectar la **Interfaz** con la **Lógica**.

1. **Crear la función lógica:**
   ```python
   def saludar():
       nombre = entrada_nombre.get() # Obtener estado de un componente
       etiqueta_saludo.config(text=f"¡Hola, {nombre}!") # Modificar estado de otro componente
   ```

2. **Conectar el botón a la función:**
   ```python
   boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
   ```

**Esto es Clave!!:** Nota que pasamos `command=saludar` y **NO** `command=saludar()`. Estamos pasando la función como referencia para que Tkinter sepa *a quién llamar* cuando ocurra el clic, en lugar de ejecutar la función inmediatamente al dibujar el botón.

**Codigo**: [03_logica_y_eventos.py](03_logica_y_eventos.py)

---

## Más Ejemplos y Práctica

Una vez que domines estos 3 pasos básicos, es hora de aplicarlos a problemas reales.

En la carpeta **`ejemplos/`** encontrarás proyectos más avanzados que combinan Tkinter con tecnicas ya vistas y código modular.

**Te recomendamos revisar el ejemplo practico** : [Ejemplo Práctico: Modificador de Matrices CSV](./ejemplos/Modificar_Matriz/guide.md)