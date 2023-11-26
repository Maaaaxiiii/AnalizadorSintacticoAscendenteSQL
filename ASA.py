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
        
        # Definición de reglas
        self.regla0 = ["Q", "select", "D", "from", "T"]
        self.regla1 = ["D", "distinct", "P"]
        self.regla2 = ["D", "P"]
        self.regla3 = ["P", "*"]
        self.regla4 = ["P", "A"]
        self.regla5 = ["A", "A", ",", "A1"]
        self.regla6 = ["A", "A1"]
        self.regla7 = ["A1", "id", "A2"]
        self.regla8 = ["A2", ".", "id"]
        self.regla9 = ["A2"]
        self.regla10 = ["A1", "id"]
        self.regla11 = ["T", "T", ",", "T1"]
        self.regla12 = ["T", "T1"]
        self.regla13 = ["T1", "id", "T2"]
        self.regla14 = ["T2", "id"]
        self.regla15 = ["T1", "id"]
        self.regla16 = []

        # Inicialización de la tabla
        self.inicializar_tabla()

    def inicializar_tabla(self):
        self.tabla[1][7] = Celda(["acc"])
        self.tabla[2][2] = Celda(["s", "12"])
        self.tabla[2][3] = Celda(["s", "14"])
        self.tabla[2][5] = Celda(["s", "18"])
        self.tabla[2][9] = Celda(["3"])
        self.tabla[2][10] = Celda(["23"])
        self.tabla[2][11] = Celda(["15"])
        self.tabla[2][12] = Celda(["22"])
        self.tabla[3][1] = Celda(["s", "4"])
        self.tabla[4][4] = Celda(["s", "6"])
        self.tabla[4][5] = Celda(["s", "7"])
        self.tabla[4][15] = Celda(["5"])
        self.tabla[5][4] = Celda(["s", "10"])
        self.tabla[5][7] = Celda(["r", "0"])
        self.tabla[6][4] = Celda(["r", "12"])
        self.tabla[6][7] = Celda(["r", "12"])
        self.tabla[7][5] = Celda(["s", "9"])
        self.tabla[7][17] = Celda(["8"])
        self.tabla[8][4] = Celda(["r", "13"])
        self.tabla[8][7] = Celda(["r", "13"])
        self.tabla[9][4] = Celda(["r", "14"])
        self.tabla[9][7] = Celda(["r", "14"])
        self.tabla[10][5] = Celda(["s", "7"])
        self.tabla[10][16] = Celda(["11"])
        self.tabla[11][4] = Celda(["r", "11"])
        self.tabla[11][7] = Celda(["r", "11"])
        self.tabla[12][3] = Celda(["s", "14"])
        self.tabla[12][5] = Celda(["s", "18"])
        self.tabla[12][10] = Celda(["13"])
        self.tabla[12][11] = Celda(["15"])
        self.tabla[12][12] = Celda(["22"])
        self.tabla[13][1] = Celda(["r", "1"])
        self.tabla[14][1] = Celda(["r", "3"])
        self.tabla[15][1] = Celda(["r", "4"])
        self.tabla[15][4] = Celda(["s", "16"])
        self.tabla[16][5] = Celda(["s", "18"])
        self.tabla[16][12] = Celda(["17"])
        self.tabla[17][1] = Celda(["r", "5"])
        self.tabla[17][4] = Celda(["r", "5"])
        self.tabla[18][6] = Celda(["s", "20"])
        self.tabla[18][13] = Celda(["19"])
        self.tabla[19][1] = Celda(["r", "7"])
        self.tabla[19][4] = Celda(["r", "7"])
        self.tabla[20][5] = Celda(["s", "21"])
        self.tabla[21][1] = Celda(["r", "8"])
        self.tabla[21][4] = Celda(["r", "8"])
        self.tabla[22][1] = Celda(["r", "6"])
        self.tabla[22][4] = Celda(["r", "6"])
        self.tabla[23][1] = Celda(["r", "2"])
        self.tabla[0][0] = Celda(["s", "2"])
        self.tabla[0][8] = Celda(["1"])
        self.tabla[18][1] = Celda(["r", "10"])
        self.tabla[18][4] = Celda(["r", "10"])
        self.tabla[7][4] = Celda(["r", "15"])
        self.tabla[7][7] = Celda(["r", "15"])
        self.tabla[4][16] = Celda(["24"])
        self.tabla[24][4] = Celda(["r", "12"])
        self.tabla[24][7] = Celda(["r", "12"])
        
    def reducciones(self, aux):
      reglas = {
        "0": self.regla0,
        "1": self.regla1,
        "2": self.regla2,
        "3": self.regla3,
        "4": self.regla4,
        "5": self.regla5,
        "6": self.regla6,
        "7": self.regla7,
        "8": self.regla8,
        "9": self.regla9,
        "10": self.regla10,
        "11": self.regla11,
        "12": self.regla12,
        "13": self.regla13,
        "14": self.regla14,
        "15": self.regla15,
        "16": self.regla16,
      }
      return reglas.get(aux, self.regla16)


    def buscar(self, A):
      mapeo = {
        "Q": 8,
        "D": 9,
        "P": 10,
        "A": 11,
        "A1": 12,
        "A2": 13,
        "A3": 14,
        "T": 15,
        "T1": 16,
        "T2": 17,
        "T3": 18,
      }
      return mapeo.get(A, -1)
  
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

        
