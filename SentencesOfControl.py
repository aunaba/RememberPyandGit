#if condición
#       instrucción
#        ...
#else
#       instrucción
#---
#
#elif
#
#bucles
##
#for
#While
'''
n=int(input('In number: '))
if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f"El número {n} es par positivo.")      
        else:
            print(f"El número {n} es impar positivo.")
    elif n % 2 == 0:
            print(f"El número {n} es par negativo.")      
    else:
            print(f"El número {n} es impar negativo.")
else:
    print(f"El número {n} es neutro")

vocal=input("Ingrese una letra: ")
if vocal=='a':
    print(f"La letra ingresada {vocal} es una vocal.")
elif vocal=='e':
    print(f"La letra ingresada {vocal} es una vocal.")
elif vocal=='i':
    print(f"La letra ingresada {vocal} es una vocal.")
elif vocal=='o':
    print(f"La letra ingresada {vocal} es una vocal.")
elif vocal=='u':
    print(f"La letra ingresada {vocal} es una vocal.")
else:
    print(f"La letra ingresada '{vocal}' es una consonante.")
    '''

'''
#while
#Suma los primeros n números
num=int(input("Ingresa un número para sumar hasta el: "))
cont=1
suma=0
while cont <= num:
    suma+=cont
    cont+=1
print(f"La suma de los primeros {num} números es: ",suma)
'''

'''n=int(input("Ingresa cuantos números vamos a comparar: "))
menor = 0
i=1
while i<=n:
    numero=int(input(f"Ingresa el número {i}: "))
    if (i==1):
        menor=numero
    elif(numero<menor):
        menor=numero
    i+=1
print(menor)
    '''

#for

#la setencia for itera sobre items de un rango

elementos=['uno', 'dos', 'tres']
for L in elementos:
   # print(L)
    print(L, len(elementos))