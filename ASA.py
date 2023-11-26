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
    def parse(self):
        pila = []
        a = self.preanalisis.buscar()
        s = 0

        while True:
            if pila:
                s = pila[-1]
            else:
                pila.append(s)

            if self.tabla[s][a] is not None and self.tabla[s][a].contenido[0] == "s":  # Manejo de Desplazamientos
                pila.append(int(self.tabla[s][a].contenido[1]))
                self.i += 1
                self.preanalisis = self.tokens[self.i]
                a = self.preanalisis.buscar()
            elif self.tabla[s][a] is not None and self.tabla[s][a].contenido[0] == "r":  # Manejo de Reducciones
                produccion = self.reducciones(self.tabla[s][a].contenido[1])
                tam = len(produccion) - 1
                A = produccion[0]

                for _ in range(tam):
                    pila.pop()

                #print(f"{self.tabla[s][a].contenido[1]}){A}->", end="")
                #for i in range(1, tam + 1):
                #    print(produccion[i], end="")
                #print("")

                
                pila.append(int(self.tabla[pila[-1]][self.buscar(A)].contenido[0]))
                
            elif self.tabla[s][a] is not None and self.tabla[s][a].contenido[0] == "acc":
                break
            else:
                self.hay_errores = True
                break

        if self.preanalisis.tipo == TipoToken.EOF and not self.hay_errores:
            print("Consulta correcta")
            return True
        else:
            print("Se encontraron errores")
            return False

        
