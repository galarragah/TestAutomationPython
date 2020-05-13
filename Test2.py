
'''
nombre_alumno = input("Ingrese su nombre: ")
apellido_alumno = input("Ingrese su apellido: ")
nota_matematica = int(input("Ingrese la nota de matematica: "))
nota_literatura = int(input("Ingrese la nota de literatura: "))
nota_fisica = int(input("Ingrese la nota de fisica: "))

def calcular_promedio(nota_matematica,nota_literatura,nota_fisica):
    nota_final = (nota_matematica+nota_literatura+nota_fisica)/3
    return nota_final

promedio = calcular_promedio(nota_matematica,nota_literatura,nota_fisica)
if promedio > 6:
    print(nombre_alumno + apellido_alumno)
    print(promedio)
    print("APROBADO")
    if promedio >= 9:
        print("ALUMNO DESTACADO")
elif promedio < 4:
    print(nombre_alumno + apellido_alumno)
    print(promedio)
    print("INSUFICIENTE")
elif promedio >= 4 or 5.9:
    print(nombre_alumno + apellido_alumno)
    print(promedio)
    print("A RECUPERATORIO")
    '''


    

