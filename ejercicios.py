'''
1. Una tienda ofrece descuento de 10% por consumos de hasta $100.00 y 20% por consumos mayores, para ambos casos se aplica tax de 15%.
Determinar monto del descuento, tax e importe a pagar.

2. La tienda amplia sus ofertas a las siguientes escalas de consumo:
Consumo:                            Descuento:
Hasta $100.00                           10%
Mayor a $100.00                         20%
Mayor a $200.00                         30%

3. Guardar resultado de pares e impares en listas:
Crear 2 listas y una tupla que tendrán números de 1 a 9.
La primera lista guardará los números pares y la segunda los impares, ambas estarán vacías.
Después multiplicar cada uno de los números de la tupla por un número aleatorio entre 1 y 100, si el resultado es par, guarda ese número en la lista de los pares y si es impar en la lista de los impares. Muestra en consola: -La multiplicación que se produce junto con su resultado con el formato:
2 x 3 = 6 y la lista de pares e impares.

'''
#1
'''
tax=15
consumo=float(input("Valor del consumo del cliente: "))
importe=0.0


if consumo >0 and consumo <= 100.00:
    descuento= consumo * 0.10
    descAplicado="10%"
elif consumo>100.00:
    descuento= consumo*0.20
    descAplicado="20%"
else:
    descuento=0
    print("Ingrese un consumo válido")
    
print(f"El descuento es de: ${descuento}")
total=consumo-descuento
print(f"Valor {total}")
importe=(total*tax/100)+total
print(f"El valor a pagar es: ${importe}, el descuento aplicado es: {descAplicado}, tax: {tax}%.")
'''

#2
'''
tax=15
consumo=float(input("Valor del consumo del cliente: "))
importe=0.0


if consumo >0 and consumo <= 100.00:
    descuento= consumo * 0.10
    descAplicado="10%"
elif consumo>100.00 and consumo <= 200:
    descuento= consumo*0.20
    descAplicado="20%"
elif consumo>200:
    descuento= consumo*0.30
    descAplicado="30%"
else:
    descuento=0
    print("Ingrese un consumo válido")
    
print(f"El descuento es de: ${descuento}")
total=consumo-descuento
print(f"Valor {total}")
importe=(total*tax/100)+total
print(f"El valor a pagar es: ${importe}, el descuento aplicado es: {descAplicado}, tax: {tax}%.")
'''

#3
'''import random

pares=[]
impares=[]
tupla=(1,2,3,4,5,6,7,8,9)



for n in tupla:
    nrandom=random.randint(1,100)
    result= n*nrandom
    print(f"Número random: {nrandom}")
    print(f"{n} x {nrandom} = {result}")
    
    if result % 2 == 0:
        pares.append(result)
    elif result % 2 != 0:
        impares.append(result)

print(f"Lista de pares: {pares}, Lista de impares: {impares}")'''

#4
'''
Una lotería genera 6 números aleatorios del 1 al 35, estos números deben guardarse en una lista; dentro de la lista no deben reperirse números, si se repite un número este debe volver a generarse y guardar en la lista.
Mostrar los 6 números ganadores de la lotería de forma ordenada.
'''

import random


numeros_loteria=[]

for n in range(0,6):
    numero=random.randint(1,35)
    while numero in numeros_loteria:
        numero=random.randint(1,35)
    numeros_loteria.append(numero)

print("Los números de la lotería ganadores son: " , numeros_loteria)