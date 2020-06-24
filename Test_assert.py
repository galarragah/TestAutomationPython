from selenium import webdriver
import unittest
import time

class PruebasStandards(unittest.TestCase):

    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b,"Los elementos no son iguales")#NOS INDICA QUE LO QUE ESTA DENTRO DEL PARENTESIS SON IGUALES  TRUE

    def test_sumaII(self):
        a = 5 + 1
        b = 1 + 2
        self.assertNotEqual(a,b)#NOS INDICA QUE LO QUE ESTA DENTRO DEL PARENTESIS ES DIFERENTE

    def test_algo_verdadero(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a==b,"A y B no son iguales")

    def test_algo_falso(self):
        self.assertFalse(2+1 == 4) # TIENE QUE SER FALSO

    def test_algo_mayor(self):
        a = 5
        b = 3
        self.assertTrue(a>b)

    def test_algo_mayorII(self):
        a = 5
        b = 3
        self.assertGreater(a,b)

    def test_algo_mayor_igual(self):
        a = 5
        b = 3
        self.assertGreaterEqual(a,b)

    def test_algo_menor(self):
         a = 5
         b = 8 
         self.assertLess(a,b)

    def test_algo_menor_igual(self):
        a = 7
        b = 8
        self.assertLessEqual(a, b)

    def test_comparar_lista(self):
        a = [1,2, "fruta"]
        b = [1,2, "fruta"]
        self.assertListEqual(a,b)

    def test_comparar_tuplas(self):
        a = (1,2,3)
        b = (1,2,3)
        self.assertTupleEqual(a,b)

    def test_comparar_dicccionarios(self):
        a = {id: 1, "Nombre": "Hector", "Apellido": "Galarraga"}
        b = {id: 1, "Nombre": "Hector", "Apellido": "Galarraga"}
        self.assertDictEqual(a,b)



if __name__ == '__main__':
    unittest.main()


