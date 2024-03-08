#Comunmente se usa en funciones factoriales

def factorial(numero):
    if numero > 1:
        numero = numero * factorial(numero-1)
    return numero

#numero=int(input('Ingrese número: '))
#print(factorial(numero))

def contador_atras(numero):
    numero-=1
    if(numero>0):
        print(numero)
        contador_atras(numero)
    else:
        print("Fin")
    
    print(f"Liberación: {numero}")
    
contador_atras(5)