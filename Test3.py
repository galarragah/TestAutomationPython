#cliente = {'nombre':'Hector','edad':22,'entrenamientos':['trotar','correr','pesas']}
#print(cliente['nombre'])
#print(cliente['edad'])
#print(cliente['entrenamientos'])

#archivo = open('mi_archivo.txt','w')
#archivo.write("Hola mundo \n")
#archivo.write('Python')
#dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
#for i in dias:
#    archivo.write(i+'\n')
#archivo.close()

#----------------------
#archivo = open('mi_archivo.txt','r')
#print(archivo.read(5))
#print(archivo.read())
#while True:
#    linea = archivo.readline() 
#    print(linea)
#    if not linea:
#        break
#print(linea)
#archivo.close()
#---------------

#def datos():
#    nombre = input("Nombre: ")

#    return nombre


#def imprimir_datos(nombre):
#    print("\n Imprimio el nombre: "+nombre)

#mis_datos = datos()
#imprimir_datos(mis_datos)

'''
class Vehiculo:
    def __init__(self,marca,modelo,color,velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.color = color 
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0

class Motor:
    def __init__(self,peso,cilindros,potencia):
        self.peso = peso
        self.cilindros = cilindros
        self.potencia = potencia

    def limpiar_motor(self):
        print("LIMOIANDO MOTOR")        


class Auto (Vehiculo,Motor):
    def __init__(self,marca,modelo,color,velocidad_maxima,patente,peso,cilindros,potencia): #constructor
        #atributos
        self.patente = patente
        Vehiculo.__init__(self,marca,modelo,color,velocidad_maxima)
        Motor.__init__(self,peso,cilindros,potencia)

    def __str__(self):
        return "Auto marca " + self.marca +" con una velocidad de "+str(self.velocidad)+" con una patente de "+self.patente

    def acelerar(self,velocidad): #metodos
        self.velocidad += velocidad
        print(self.velocidad)

    def frenar(self,velocidad):
        self.velocidad -= velocidad
        print(self.velocidad)
     
    def arrancar(self):
        print("ARRCANDO")

    def apagar(self):
        print("APAGADO")

    
mi_auto = Auto("Toyota",'H5423','Rojo',200,'HectorCompany',300,5,5000)

print(mi_auto.marca)
print(mi_auto.color)

mi_auto.arrancar()
mi_auto.acelerar(10)
mi_auto.acelerar(30)
mi_auto.frenar(5)
mi_auto.frenar(5)
mi_auto.frenar(1)
print(mi_auto.cilindros)
mi_auto.apagar

print(mi_auto)

'''
