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
'''#2
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
import random

pares=[]
impares=[]
tupla=(1,2,3,4,5,6,7,8,9)

nrandom=random.randint(1,100)

print(f"Número random: {nrandom}")
for nramdom in tupla:
    n=tupla*nrandom
if n / 2 == 0:
    pares.append()
elif n/ 2 != 0:
    impares.append()

print(f"{tupla} x {nrandom} = {n}")
print(pares,impares)