# Ejemplo Práctico: Eventos (Bind) y Funciones Anónimas (Lambda)

En este ejemplo abordaremos dos conceptos fundamentales para darle dinamismo avanzado a nuestras interfaces: Las **funciones Lambda** para pasar argumentos a botones, y la captura de **Eventos** (`bind`) como clics especiales o teclas del teclado.

A continuación, destacaremos los hitos más importantes de esta implementación.

---

## 1. El Problema con los Botones (y cómo `lambda` lo soluciona)

Cuando le asignamos un comando a un botón en Tkinter, debemos pasarle el **nombre** de la función sin paréntesis:
`command=self.mi_funcion` 
(Correcto: el botón la ejecutará al ser presionado).

Si le ponemos paréntesis y parámetros: `command=self.mi_funcion("hola")`, **la función se ejecuta inmediatamente** al arrancar el programa, sin esperar a que nadie presione el botón.

### ¿Qué es `lambda` y cómo ayuda?
Una expresión `lambda` es una forma rápida de crear una pequeña función anónima (sin nombre) en una sola línea.
Al escribir `command=lambda: self.saludar("¡Hola!")`, estamos diciéndole al botón: *"Cuando te presionen, ejecuta esta funcioncita anónima, y esa funcioncita es la que se encargará de llamar a saludar() con el parámetro 'Hola'"*.
Esto nos permite reutilizar una misma función (`saludar`) pasándole distintos textos, ahorrándonos tener que crear funciones separadas (`saludar_ingles()`, `saludar_frances()`, etc.).

---

## 2. Captura de Eventos mediante `.bind()`

Los botones de Tkinter solo reaccionan al clic normal (botón izquierdo del mouse). Pero ¿qué pasa si queremos que el programa responda cuando el usuario presiona "Enter", o cuando hace doble clic en el fondo de la aplicación?

Para eso utilizamos el método `.bind("<Evento>", función)`.
* **`<Return>`:** Representa la tecla Enter del teclado. En este ejemplo, la vinculamos a la entrada de texto para que el programa detecte cuando terminaste de escribir.
* **`<Double-Button-1>`:** Representa un doble clic del botón izquierdo del mouse.

### El Parámetro del Evento
Cualquier función que sea llamada mediante `.bind()` (como `al_presionar_enter`) **automáticamente recibe un argumento extra** por parte de Tkinter: el objeto del evento (que contiene información como en qué coordenadas del mouse ocurrió, qué tecla se presionó, etc.). Es por esto que nuestra función está definida como `def al_presionar_enter(self, evento):`.

También podemos ver en el código fuente cómo usamos `lambda evento:` directamente dentro del `.bind()` para resolver funciones rápidas en una línea y recibir el parámetro de evento sin que tire un error.

### 🔧 ¡Pruébalo tú mismo! (Desafío)
Intenta interactuar con el código y extender sus capacidades:
1. Agrega un botón nuevo que reciba un parámetro y haga un cálculo matemático usando una función y un `lambda` (ej: pasar un número para calcular su cuadrado).
2. Vincula el evento `<FocusIn>` al campo de texto (Entry), para que usando `lambda` imprima en la consola "Escribiendo..." justo en el momento en que el usuario hace clic dentro de la caja de texto.
