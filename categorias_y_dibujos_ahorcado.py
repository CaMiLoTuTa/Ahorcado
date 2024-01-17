""" Este módulo contiene las categorias de las palabras y los dibujos del juego ahorcado
    """

palabras_categoria_programacion = {
    "python",
    "programacion",
    "desarrollo",
    "computadora",
    "tecnologia",
    "inteligencia",
    "artificial",
    "algoritmo",
    "datos",
    "estructura",
    "codigo",
    "variable",
    "funcion",
    "interfaz",
    "biblioteca",
    "framework",
    "proyecto",
    "ingenieria",
    "software",
    "hardware",
    "programador",
    "ingeniero",
    "terminal",
    "depuracion",
    "abstraccion",
    "orientacion",
    "internet",
    "seguridad",
    "teclado",
    "mouse",
    "javascript",
    "backend",
    "frontend",
    "repositorio",
    "version",
    "control",
    "implementacion",
    "herencia",
    "polimorfismo",
    "encapsulamiento",
    "analisis",
    "diseño",
    "ciclo",
    "eficiencia",
    "optimizacion",
    "complejidad",
    "debugging",
}
palabras_categoria_cosas = {
    "telefono",
    "computadora",
    "coche",
    "bicicleta",
    "television",
    "refrigerador",
    "ventilador",
    "reloj",
    "gafas",
    "libro",
    "camara",
    "cuchillo",
    "silla",
    "mesa",
    "boligrafo",
    "cuaderno",
    "zapatos",
    "sombrero",
    "laptop",
    "piano",
    "guitarra",
    "horno",
    "lavadora",
    "secadora",
    "maleta",
    "paraguas",
    "brujula",
    "telescopio",
    "microscopio",
    "planta",
    "lampara",
    "llavero",
    "candado",
    "espejo",
    "cepillo",
    "peine",
    "bolsa",
    "globo",
}
palabras_categoria_ciudades = {
    "paris",
    "londres",
    "tokio",
    "roma",
    "berlin",
    "moscu",
    "beijing",
    "amsterdam",
    "mexico",
    "toronto",
    "dubai",
    "madrid",
    "singapur",
    "seul",
    "cairo",
    "nairobi",
    "lisboa",
    "bangkok",
    "casablanca",
    "estambul",
    "atenas",
    "hanoi",
    "ottawa",
    "delhi",
    "jakarta",
    "mumbai",
    "saopaulo",
    "lima",
    "bogota",
    "caracas",
    "sydney",
    "dakar",
    "viena",
}
palabras_categoria_animales = {
    "leon",
    "elefante",
    "tigre",
    "jirafa",
    "mono",
    "serpiente",
    "tortuga",
    "pinguino",
    "ballena",
    "delfin",
    "tiburon",
    "aguila",
    "loro",
    "tucan",
    "cocodrilo",
    "rinoceronte",
    "hipopotamo",
    "gato",
    "perro",
    "raton",
    "conejo",
    "pajaro",
    "oveja",
    "caballo",
    "vaca",
    "gallina",
    "pez",
    "abeja",
    "mariposa",
    "araña",
    "camaleon",
    "ciervo",
    "pato",
    "foca",
    "koala",
    "panda",
    "zorro",
}
palabras_categoria_nombres = {
    "juan",
    "maria",
    "carlos",
    "ana",
    "luis",
    "elena",
    "pedro",
    "clara",
    "jorge",
    "natalia",
    "fernando",
    "lucia",
    "daniel",
    "sofia",
    "roberto",
    "victoria",
    "alberto",
    "carmen",
    "raul",
    "silvia",
    "sergio",
    "andrea",
    "pablo",
    "adriana",
    "manuel",
    "isabel",
    "eduardo",
    "patricia",
    "gabriel",
    "valeria",
    "alejandro",
    "laura",
    "javier",
    "veronica",
    "ricardo",
    "marta",
    "oscar",
    "monica",
    "felipe",
    "elisa",
}


palabras_categoria_general = set(
    list(palabras_categoria_programacion)
    + list(palabras_categoria_cosas)
    + list(palabras_categoria_ciudades)
    + list(palabras_categoria_animales)
    + list(palabras_categoria_nombres)
)

categorias = [
    palabras_categoria_programacion,
    palabras_categoria_cosas,
    palabras_categoria_ciudades,
    palabras_categoria_animales,
    palabras_categoria_nombres,
    palabras_categoria_general,
]


dibujos = [
    """
--------
|      |
|      O
|      /|\\
|      / \\
|
----------
""",
    """
--------
|      
|      O
|      /|\\
|      / \\
|
----------
""",
    """
--------
|      
|      O
|       |\\
|      / \\
|
----------
""",
    """
--------
|      
|      O
|       | 
|      / \\
|
----------
""",
    """
--------
|      
|      O
|       | 
|        \\
|
----------
""",
    """
--------
|      
|      O
|       | 
|        
|
----------
""",
    """
--------
|      
|      O
|        
|        
|
----------
""",
    """
--------
|      
|       
|        
|        
|
----------
""",
]
