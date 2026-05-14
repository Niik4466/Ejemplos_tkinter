# Ejemplo Práctico: Uso de Frames y Pestañas (Notebook)

En este ejemplo vamos a aplicar los conceptos de interfaces gráficas para resolver un problema común: **Organizar múltiples vistas en una sola ventana** utilizando pestañas, logrando un comportamiento muy similar a un "TabHost" en el desarrollo móvil o de escritorio avanzado.

A continuación, destacaremos los hitos más importantes de esta implementación.

---

## 1. Implementación del Controlador de Pestañas (Notebook)

Si revisas el archivo `main.py`, notarás que utilizamos un componente principal llamado `ttk.Notebook`.
* **El `Notebook`:** Actúa como el contenedor principal o "director" que se encarga de gestionar qué contenido se muestra actualmente en pantalla dependiendo de la pestaña que el usuario seleccione.

### ¿Cuáles son las ventajas de usar `ttk.Notebook`?
1. **Organización del Espacio:** Permite tener una ventana de tamaño reducido pero con una gran cantidad de información u opciones, divididas en secciones lógicas.
2. **Navegación Intuitiva:** Los usuarios están acostumbrados a las interfaces basadas en pestañas (como los navegadores web), por lo que reduce la curva de aprendizaje de tu aplicación.
3. **Escalabilidad Visual:** Si el día de mañana necesitas agregar una nueva sección de "Configuración", simplemente añades una nueva pestaña sin tener que rediseñar toda la ventana.

---

## 2. Creación de Vistas Independientes (Frames)

Dentro de la ventana principal, no colocamos los *widgets* (botones, textos) directamente en el `Notebook`. En su lugar, utilizamos `ttk.Frame`.
* **Los `Frames`:** Son contenedores invisibles. Cada Frame actúa como un "lienzo en blanco" dedicado exclusivamente a una de las pestañas.

### ¿Por qué separar el contenido en Frames?
Al separar la interfaz en múltiples `Frames` (`frame1`, `frame2`, `frame3`), logramos modularidad dentro de la misma vista. 
El contenido de la "Vista 1" no interfiere con el de la "Vista 2". Cada Frame tiene su propio sistema de empaquetado (`pack()`, `grid()`, o `place()`) independiente de los demás, lo que evita que la interfaz se desordene al agregar más elementos.

---

## 3. Integración de Vistas y Controlador

Una vez creados los Frames, el paso crítico es vincularlos al controlador de pestañas. Esto se logra mediante el método `add()`:

```python
self.notebook.add(self.frame1, text="Vista 1")
```

Este comando le indica al `Notebook` que debe crear una nueva pestaña visible con el texto "Vista 1" y que, al ser clickeada, el contenido a mostrar será todo lo que hayamos empaquetado dentro de `self.frame1`.

---

## 4. Población de Contenido por Vista

Finalmente, cada Frame se llena con sus propios widgets (`Label`, `Button`, `Entry`, `Checkbutton`). Fíjate que el primer argumento de cada widget no es `self` (la ventana principal), sino el Frame correspondiente (`self.frame1`, `self.frame2`, etc.):

```python
tk.Button(self.frame1, text="Acción en Vista 1", command=lambda: print("Click en Vista 1")).pack(pady=10)
```

Esto asegura que el botón pertenezca exclusivamente a la primera pestaña y desaparezca cuando cambies a la segunda.

### 🔧 ¡Pruébalo tú mismo!
Intenta interactuar con el código y modificar la interfaz para poner en práctica lo aprendido:
1. **Agrega una nueva vista:** Crea un `self.frame4`, agrégalo al `notebook` con el texto "Configuración" y añádele un par de botones.
2. **Experimenta con el diseño:** Cambia el `pack()` de los elementos dentro de `frame2` para usar `.grid()` y organizar las etiquetas y entradas de texto como si fuera un formulario ordenado.
3. **Pestañas deshabilitadas:** Investiga en la documentación de `tkinter` cómo hacer que una de las pestañas (por ejemplo, la Vista 3) inicie en un estado deshabilitado (`state="disabled"`) hasta que se cumpla alguna condición.
