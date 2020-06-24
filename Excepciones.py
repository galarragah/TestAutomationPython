class matematica:
    def sumar(self, nr1, nr2):
        try:
            if nr1<0:
                raise Exception("LOS NUMEROS TIENEN QUE SER POSITIVOS")
        except:
            return ('NO SE PUEDE COLOCAR NUMEROS MENOR AL CERO AL PRIMERO')
        else:
            return nr1 + nr2

    def restar(self, nr1, nr2):
        return nr1 - nr2

    def multiplicar(self, nr1, nr2):
        try:
            if not type(nr1) is int:
                raise TypeError ('Solo integer')
        except TypeError:
            return ('NO SE PUEDE MULTIPLICAR')
        else:
            return nr1 * nr2

    def dividir(self, nr1, nr2):
        n1 = nr1 - 5
        n2 = nr2 - 3
        n3 = 0.0
        try:
            n3 = n1/n2
        except ZeroDivisionError: # SIN COLOCAR LA EXCEPCION CORRE PARA TODAS
            return 'No se puede dividir por cero'
        except TypeError:
            return 'Debe ingresar numeros'
        else:
            return n3
        finally:
            print("IMPRIMO PORQUE SI")

class mapas:
    def get_item(self,mapa, item):
        try:
            return mapa[item]
        except KeyError:
            print('NO EXISTE LA KEY')
mi_calculadora = matematica()

#(mi_calculadora.dividir(5,3))
#print((mi_calculadora.sumar(-3,4)))
#print((mi_calculadora.multiplicar(2.3,3)))

mi_mapa = mapas()
print(mi_mapa.get_item({'id': 0, 'nombre':'Pablo'}, 'id'))



