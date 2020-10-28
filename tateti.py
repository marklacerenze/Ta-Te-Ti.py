import random as R 

#LEER UN ENTERO CON CONTROL DE ERROR DE TIPO DE DATO
def leerInt(cartel,desde=-9999999999,hasta=9999999999):
    salir = False
    numero = 0
    while not salir:
        try:
            numero = int(input(cartel))
            if numero < desde or  numero > hasta:
                print("ERROR ==> numero fuera de rango\n")
            else:
                salir = True
        except:
            print("ERROR ==> Ingrese un numero entero\n")
    return numero


class Ficha:
    def __init__(self,caracter):
        self.caracter = caracter
    
    def __str__(self):
        return '['+self.caracter+']'


class Tablero:

    def __init__(self,filas=3,columnas=3):
        self.cf = filas
        self.cc = columnas
        self.mat = []
        for f in range(self.cf):
            col = []
            for c in range(self.cc):
                col.append(Ficha(' '))
            self.mat.append(col)

    def __str__(self):
        cadena = ""
        for f in range(self.cf):
            for c in range(self.cc):
                cadena += str(self.mat[f][c])
            cadena += "\n" 
        return cadena

    def poner(self,f,c,ficha):
        self.mat[f][c] = ficha

    def ver(self,f,c):
        return self.mat[f][c]
    
    def existe(self,ficha):
        for f in range(self.cf):
            for c in range(self.cc):
                
                if str(ficha) == str(self.mat[f][c]):
                    return True
        return False

    def filaIgual(self,fila,ficha):
        for c in range(self.cc):
            if ficha != self.mat[fila][c]:
                return False
        return True
    
    def columnaIgual(self,columna,ficha):
        for f in range(self.cf):
            if ficha != self.mat[f][columna]:
                return False
        return True

    def digonalIgual(self,ficha):
        for x in range(self.cf):
            if self.mat[x][x] != ficha:
                return False
        return True

    def digonalSecIgual(self,ficha):
        f = 0
        c = self.cc-1
        while f < self.cf:
            if self.mat[f][c] != ficha:
                return False
            f += 1
            c -= 1
        return True
    

class Jugador(object):
    
    def __init__(self,nombre,ficha):
        self.nombre = nombre
        self.ficha = ficha


    def __str__(self):
        return self.nombre + " ==> "+str(self.ficha)

    def jugar(self,tablero):
        pass


class Humano(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def jugar(self,tablero):
        salir = False
        while not salir:
            fila = leerInt("Fila: ",0,tablero.cf-1)
            columna = leerInt("Columna: ",0,tablero.cc-1)
            if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
                salir = True
        return Coordenada(fila,columna)


class Computadora(Jugador):

    def __init__(self,nombre,ficha):
        Jugador.__init__(self,nombre,ficha)

    def jugar(self,tablero):
        salir = False
        while not salir:
            fila = R.randint(0,tablero.cf-1)
            columna = R.randint(0,tablero.cc-1)
            if str(tablero.ver(fila,columna)) == str(Ficha(' ')):
                salir = True
        return Coordenada(fila,columna)

class Coordenada:
    def __init__(self,fila=0,columna=0):
        self.fila = fila
        self.columna = columna


class Tateti:

    def __init__(self,jug1,jug2):
        self.jug1 = jug1
        self.jug2 = jug2
        self.tablero = Tablero()

    def jugarTateti(self):
        
        if R.randint(0,1) == 0:
            jugAux = self.jug1
        else:
            jugAux = self.jug2

        ganar = False
        print(str(self.tablero))
        
        while not ganar and self.tablero.existe(Ficha(' ')):
            print("JUEGA: " + str(jugAux))
            coor = jugAux.jugar(self.tablero)
            self.tablero.poner(coor.fila,coor.columna,jugAux.ficha)
            print(str(self.tablero))
            if self.esTateti(jugAux.ficha):
                ganar = True
            else:
                jugAux = self.elOtro(jugAux)
        if ganar:
            print("Ganador: " + str(jugAux))
        else:
            print("Empate!!!!!!!") 

    def elOtro(self,humano):
        if humano == self.jug2:
            return self.jug1
        return self.jug2

    def esTateti(self,ficha):
        for fila in  range(self.tablero.cf):
            if self.tablero.filaIgual(fila,ficha):
                return True
        for columna in range(self.tablero.cc):
            if self.tablero.columnaIgual(columna,ficha):
                return True
        return self.tablero.digonalIgual(ficha) or self.tablero.digonalSecIgual(ficha)     


def main():

    """
    h = Humano("Juan",Ficha('O'))
    c = Computadora("CompuJuan",Ficha('X'))

    print(str(h))
    print(str(c))
    t = Tablero()
    t.poner(0,0,Ficha('X'))
    t.poner(1,1,Ficha('X'))
    t.poner(2,2,Ficha('X'))
    print(str(t))
    """
    juego = Tateti(Humano("Juan",Ficha('X')),Computadora("CompuPinchame",Ficha('O')))
    juego.jugarTateti()


main()
