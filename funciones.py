


#funciones básocas
'''
def saludar(nombre):
    return(f'Hola {nombre} desde la funcion saludar')
    

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

    
saludo=saludar("Juan")
print(saludo)

suma=sumar(2,3)
print(f'la suma es igual a {suma}')'''

'''#funciones con argumentos indefinidos
def sumar(*args):
    suma =0
    for n in args:
        suma+=n
    return suma
    
#argumentos indefinidos con keyword o palabra clave
def persona(**kwargs):
    dato=''
    return kwargs
    

suma=sumar(2,3,3,2,10)
print(f'la suma es igual a {suma}')

datos=persona(nombre='Juan', ciudad='Medellín', pareja='Carol')
print (f"Los datos son: {datos}")'''

#tambien puedo unir los dos tipos de datos:
def sumar(*args, **kwargs):
    suma =0
    for n in args:
        suma+=n
    return suma, kwargs


suma, datos=sumar(2,3,3,2,10,nombre='Juan', ciudad='Medellín', pareja='Carol')
print(f'la suma es igual a {suma}')
print(f"Los datos de la persona son: {datos}")