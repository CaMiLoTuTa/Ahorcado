"""Implementación del juego del Ahorcado utilizando Tkinter."""

from tkinter import messagebox, simpledialog
from categorias_y_dibujos_ahorcado import dibujos, categorias


class Ahorcado:
    """Representa los atributos que contiene el juego ahorcado hola hola hola hola hola hola hola
    hola hola"""

    nombre_categoria = [
        "PROGRAMACIÓN",
        "COSAS",
        "CIUDADES",
        "ANIMALES",
        "NOMBRES",
        "GENERAL",
    ]

    def __init__(self) -> None:
        """Inicializa el juego del Ahorcado"""
        self._categoria = categorias[5]
        self._palabra = self._categoria.pop()
        self._longitud_palabra = len(self.palabra)
        self._palabra_mostrar = "_" * self.longitud_palabra
        self._intentos = 7
        self._letras_erradas = ""

    @property
    def categoria(self):
        """Obtiene la categoria actual.

        Devuelve:
            set: La categoria actual.
        """
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        """Establece la categoria actual.

        Args:
            categoria (set): La nueva categoria.

        Devuelve:
            None.
        """
        self._categoria = categoria
        self._palabra = self._categoria.pop()

    @property
    def palabra(self):
        """Obtiene la palabra actual.

        Devuelve:
            str: La palabra actual.
        """
        return self._palabra

    @property
    def longitud_palabra(self):
        """Obtiene la longitud de la palabra actual.

        Devuelve:
            int: La longitud de la palabra actual.
        """
        return self._longitud_palabra

    @property
    def palabra_mostrar(self):
        """Obtiene la visualización actual de la palabra con guiones bajos.

        Devuelve:
            str: La visualización actual de la palabra con guiones bajos.
        """
        return self._palabra_mostrar

    @palabra_mostrar.setter
    def palabra_mostrar(self, palabra_mostrar):
        """Establece la visualización actual de la palabra con guiones bajos.

        Args:
            palabra_mostrar (str): La nueva visualización.

        Devuelve:
            None.
        """
        self._palabra_mostrar = palabra_mostrar

    @property
    def intentos(self):
        """Obtiene los intentos restantes.

        Devuelve:
            int: Los intentos restantes.
        """
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        """Establece los intentos restantes.

        Args:
            intentos (int): Los nuevos intentos restantes.

        Devuelve:
            None.
        """

        self._intentos = intentos

    @property
    def letras_erradas(self):
        """Obtiene las letras erradas.

        Devuelve:
            String: texto con todas las letras en las que se equivoco el usuario
        """
        return self._letras_erradas

    @letras_erradas.setter
    def letras_erradas(self, letras_erradas):
        """Establece las letras falladas.

        Args:
            letras_erradas (String): texto con todas las letras .

        Devuelve:
            None.
        """
        self._letras_erradas = letras_erradas

    # * MÉTODOS DE EJECUCIÓN

    def seleccionar_categoria(self):
        """El usuario escoge la categoria que desea."""

        numero_categoria = simpledialog.askinteger(
            "CATEGORÍA",
            f"{'AHORCADO'.center(
                40, '°')}\n\n0)PROGRAMACIÓN\n1)COSAS\n2)CIUDADES\n3)ANIMALES"
            + "\n4)NOMBRES\n5)GENERAL",
        )
        if numero_categoria == 5:
            return

        while numero_categoria < 0 or numero_categoria > 4:
            messagebox.showerror(
                "CATEGORÍA DESCONOCIDA", "La categoría que ingresó no es válida."
            )
            numero_categoria = simpledialog.askinteger(
                "CATEGORÍA",
                f"{'AHORCADO'.center(
                    40, '°')}\n\n0)PROGRAMACIÓN\n1)COSAS\n2)CIUDADES\n3)ANIMALES"
                + "\n4)NOMBRES\n5)GENERAL",
            )

        categoria = categorias[numero_categoria]
        self.categoria = categoria

    def pedir_letra(self):
        """Pide y valida la entrada de una letra

        Returns:
            string: letra en minúsculas
        """
        letra = simpledialog.askstring("LETRA", f"{self.datos()}Ingrese una letra: ")

        while not letra.isalpha() or len(letra) > 1:
            messagebox.showerror("ENTRADA INCORRECTA", "Sólo se aceptan letras")
            letra = simpledialog.askstring(
                "LETRA", f"{self.datos()}Ingrese una letra: "
            )

        return letra.lower()

    def letra_en_palabra(self, letra):
        """Verifica si la letra recibida se encuentra en la palabra.

        Args:
            letra string: se recibe una letra, CHAR

        Returns:
            bool: Devuelve si la palabra contiene la letra recibida.
        """
        try:
            self.palabra.index(letra)
            return True

        except ValueError:
            return False

    def mostrar_letra(self):
        """Sobre-escribe las letras en la posición correcta y resta un correctas."""
        letra = self.pedir_letra()
        if self.letra_en_palabra(letra):
            posiciones = [i for i, x in enumerate(self.palabra) if x == letra]

            for pos in posiciones:
                self.palabra_mostrar = (
                    self.palabra_mostrar[:pos] + letra + self.palabra_mostrar[pos + 1 :]
                )
        else:
            self.intentos -= 1
            self.acumular_letras_erradas(letra)

    def tiene_intentos(self):
        """Comprueba si el usuario tiene mas de 0 intentos

        Returns:
            bool: devuelve si los intentos son más de 0.
        """
        return self.intentos > 0

    def verificar_victoria(self):
        """Comprueba si el usuario ha acertado con la palabra completa.

        Returns:
            bool: verifica si la palabra es igual a la palabra que se esta descubriendo.
        """
        return self.palabra == self.palabra_mostrar

    def datos(self):
        """Genera un texto con toda la informacion del juego en proceso.

        Returns:
            string: Texto con todas las características actuales del juego.
        """
        texto = "AHORCADO".center(40, "°") + "\n"
        texto += (
            f"{Ahorcado.nombre_categoria[categorias.index(self.categoria)]}".center(
                65, " "
            )
        )
        texto += "\n\n"
        texto += f"{dibujos[self.intentos]}"
        texto += f"{self.palabra_mostrar.upper().center(60, ' ')}"
        texto += "\n\n"
        texto += f"LETRAS ERRADAS: {self.letras_erradas.upper().center(30, ' ')}"
        texto += "\n\n"

        return texto

    def mostrar_victoria(self):
        """Muestra el mensaje de victoria por pantalla."""
        messagebox.showinfo(
            "YOU WIN",
            f"{'AHORCADO'.center(40, '°')}\nHAS GANADO, LA PALABRA ES: {
                self.palabra.upper()}",
        )

    def mostrar_derrota(self):
        """Muestra el mensaje de derrota por pantalla."""
        messagebox.showinfo(
            "YOU LOSE",
            f"{'AHORCADO'.center(40, '°')}\n{
                dibujos[0]}LA PALABRA CORRECTA ES: "
            + f"{self.palabra.upper()}",
        )

    def acumular_letras_erradas(self, letra_errada):
        """Va acumulando las letras que no se encuentran en el palabra.

        Args:
            letra_errada (String): letra equivocada.
        """
        self.letras_erradas += f"{letra_errada.upper()}-"


def jugar():
    """Inicializa el juego ahorcado, ejecutando sus métodos."""
    juego = Ahorcado()
    juego.seleccionar_categoria()

    while True:
        juego.mostrar_letra()

        if not juego.tiene_intentos():
            juego.mostrar_derrota()
            return
        if juego.verificar_victoria():
            juego.mostrar_victoria()
            return


while True:
    if not messagebox.askyesno("INICIAR JUEGO", "Iniciar un nuevo juego"):
        messagebox.showinfo("GAME OVER", "¡GRACIAS POR JUGAR!")
        break

    jugar()
