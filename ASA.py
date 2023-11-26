from TipoToken import TipoToken

class Celda:
    def __init__(self, contenido):
        self.contenido = contenido  
class ASA:
    def __init__(self, tokens):
        aux = [Celda([None]) for _ in range(20)]
        # aux = [[None] for _ in range(20)]
        self.tabla = [aux.copy() for _ in range(28)]  # Se declara la tabla de análisis sintáctico
        # self.tabla = [[None] * 20 for _ in range(28)]  # Se declara la tabla de análisis sintáctico
        self.i = 0
        self.hay_errores = False
        self.preanalisis = tokens[self.i]
        self.tokens = tokens

        