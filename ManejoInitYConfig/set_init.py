import configparser

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : '../chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.google.com'}

with open('configuracion.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig)