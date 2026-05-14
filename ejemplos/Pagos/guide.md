# Ejemplo Práctico: Gestión de Pagos (Arquitectura 3 Capas y Validaciones Dinámicas)

En este ejemplo vamos a aplicar conceptos de diseño de software e interfaces gráficas para resolver un problema de almacenamiento de datos. El objetivo principal es construir una aplicación utilizando el patrón de **Arquitectura de 3 Capas** y técnicas avanzadas de `Tkinter` sin el uso de clases.

A continuación, destacaremos los hitos y técnicas más importantes de esta implementación.

---

## 1. Arquitectura de 3 Capas

A diferencia de escribir todo el código en un solo archivo, hemos dividido la aplicación en tres módulos con responsabilidades únicas y claramente definidas:

### Capa de Datos (`datos.py`)
Es la única capa que interactúa directamente con el sistema de archivos (nuestra base de datos en formato `data.csv`).
* **Responsabilidad:** Crear el archivo, agregar nuevas filas y leer los registros existentes.
* **Manejo de Errores:** Captura excepciones propias del sistema operativo (como `PermissionError` si el archivo está abierto por otro programa) y devuelve tuplas `(exito, mensaje)` de manera segura, evitando que la aplicación sufra "crashes".

### Capa de Lógica de Negocio (`logica.py`)
Actúa como intermediario o puente entre los datos y la interfaz gráfica.
* **Responsabilidad:** Validar las reglas de negocio (por ejemplo, asegurarse de que los campos no estén vacíos, o que el monto sea efectivamente un número mayor a cero).
* **Flujo:** Recibe la solicitud de la interfaz, valida la consistencia de los datos, y luego autoriza a la capa de datos para que los guarde permanentemente.

### Capa de Presentación (`presentacion.py`)
Maneja única y exclusivamente la Interfaz Gráfica de Usuario (GUI).
* **Responsabilidad:** Construir ventanas, botones y recibir interacciones del usuario. La interfaz no sabe *cómo* ni *dónde* se guardan los datos, simplemente le delega la orden a la capa lógica y reacciona mostrando *pop-ups* de éxito o error al usuario.

---

## 2. Técnicas Avanzadas de Tkinter

Para este proyecto prescindimos de la Programación Orientada a Objetos y utilizamos un enfoque 100% funcional, integrando algunos trucos visuales interesantes:

### a) Variables de Control y Rastreo en Tiempo Real (`StringVar` y `trace_add`)
En lugar de limitarnos a leer el texto final con un `entry.get()`, vinculamos nuestros campos de texto a variables dinámicas `tk.StringVar()`.
* **Observador (Trace):** Utilizamos el método `.trace_add("write", funcion_callback)`. Esto nos permite ejecutar una función específica cada vez que el usuario teclea, borra o pega texto en las casillas.
* **Validación Visual Interactiva:** Gracias a este rastreo, implementamos que el botón "Guardar Pago" cambie de rojo a verde de manera automática justo en el momento en que detecta que todos los campos del formulario han sido completados.

### b) Destrucción y Reutilización de Ventana (`winfo_children`)
Para movernos entre el menú, el formulario y la tabla, no creamos múltiples ventanas emergentes del sistema operativo, lo cual sería molesto para el usuario.
* Usamos la técnica de **limpieza de lienzo**. La función `limpiar_ventana` utiliza `ventana.winfo_children()` para identificar todo lo que hay en pantalla y destruirlo con `.destroy()`, permitiendo volver a pintar nuevos elementos sobre la misma ventana base.

### c) Uso de Tablas de Datos (`ttk.Treeview`)
En la vista de lectura de datos, implementamos un widget más robusto llamado `Treeview` que permite mostrar la información en un formato de tabla estructurada.
* **Poblado Dinámico:** Cada vez que el usuario ingresa a esta vista, la interfaz solicita la lista actualizada a la lógica y rellena el `Treeview` insertando los datos como si fueran filas, asegurando que la tabla jamás muestre información desactualizada.

---

### 🔧 ¡Pruébalo tú mismo!
Intenta interactuar con el código y modificar la aplicación para poner en práctica lo aprendido:
1. **Agrega un Nuevo Campo:** Implementa un campo "Categoría" (Ej: Efectivo, Tarjeta, Transferencia) a tu base de datos. Recuerda que al usar Arquitectura de 3 Capas, deberás modificar `presentacion.py`, `logica.py` y `datos.py` para que el flujo completo funcione.
2. **Mejora el Treeview:** Investiga en la documentación cómo añadir barras de desplazamiento (Scrollbars) al `Treeview` por si algún día tienes 1000 registros y la ventana no alcanza a mostrarlos todos.
3. **Filtros Personalizados:** Añade una nueva pestaña o botón en `presentacion.py` que permita "Buscar pagos por un RUT específico". Tendrás que crear una nueva función en `logica.py` que filtre la lista que devuelve `obtener_pagos()` antes de enviarla a la interfaz.
