# Ejemplo Práctico: Ventanas Secundarias (Toplevel)

En este ejemplo vamos a aprender cómo crear **ventanas emergentes o secundarias** en nuestra aplicación, separadas de la ventana principal, y cómo enviar información de una a otra.

A continuación, destacaremos los hitos más importantes de esta implementación.

---

## 1. El Componente `Toplevel`

Cuando iniciamos una aplicación de Tkinter, creamos la ventana principal con `tk.Tk()`. **Solo puede haber un `tk.Tk()` por programa.** 
Si queremos abrir otra ventana, debemos instanciar `tk.Toplevel(parent)`.

* La ventana `Toplevel` se comporta igual que la principal: puedes agregarle *widgets*, configurarle tamaño (`geometry`) y título.
* Cuando el usuario hace clic en "Abrir Ventana", nuestro programa ejecuta la función `abrir_secundaria()`, la cual crea y dibuja el `Toplevel`.

---

## 2. Gestión de Enfoque con `grab_set()`

En interfaces gráficas, a veces queremos que una ventana secundaria actúe como un "diálogo modal" (como cuando un programa te pregunta "¿Estás seguro que quieres salir?"). 
* Al utilizar el método `ventana_hija.grab_set()`, "atrapamos" todos los eventos del usuario (clics, teclado).
* Esto **obliga** al usuario a interactuar con la ventana hija antes de poder volver a hacer clic en la ventana principal.

---

## 3. Comunicación entre Ventanas y `destroy()`

Una duda muy común es cómo pasar un dato ingresado en la segunda ventana a la primera.
En este código, lo resolvemos creando la función `enviar_dato()` *dentro* de la función `abrir_secundaria()`. 

Al hacerlo así, la función interna tiene acceso tanto al campo de texto de la ventana hija (`entrada.get()`) como a la etiqueta de la ventana principal (`self.lbl_resultado.config()`).
Una vez enviado el texto, ejecutamos `ventana_hija.destroy()` para cerrar y destruir únicamente la ventana secundaria.

### 🔧 ¡Pruébalo tú mismo!
Intenta interactuar con el código para explorar este concepto:
1. Comenta (usando `#`) la línea `ventana_hija.grab_set()`. Abre la ventana secundaria e intenta hacer clic en la ventana principal. ¿Qué diferencia notas?
2. Agrega un botón en la ventana secundaria que diga "Cancelar" y que simplemente ejecute el comando para destruirla (`destroy()`) sin enviar ningún dato.
