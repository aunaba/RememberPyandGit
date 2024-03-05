'''
1. Una tienda ofrece descuento de por consumos, aplica tax de 15%.
Determinar monto del descuento, tax e importe a pagar.

Consumo:                            Descuento:
Hasta $100.00                           10%
Mayor a $100.00                         20%
Mayor a $200.00                         30%

'''

def descuentos(consumo):
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
    return descuento

def impuesto(total):
    return total*(tax/100)

tax=15
consumo=(float(input("Ingresar valor del consumo: ")))

if (consumo>0):
    descuento=descuentos(consumo)
    total=consumo-descuento
    valImpuesto=impuesto(total)
    importe=total+valImpuesto
    
    print(f"El descuento es de: ${descuento}")
    print(f"Valor sin taxes: {total}")
    print(f"El importe a pagar más taxes es: {importe}")
    print(f"El valor a pagar es: ${importe}, el descuento aplicado es: ${descuento}, tax: {tax}%= {valImpuesto}")
else:
    print("Valor incorrecto")