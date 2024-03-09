#1.Crear un módulo donde se tenga 3 clases: Figura, Cuadradro y circulo.
#2.Figura es padre de la clase Cuadrado y Circulo.
#3. Las clases deben imprementar dos funciones que permitan calcular el área y perímetro.
#4. Que el calculo se muestre por medio de un menú de opciones desde un archivo principal.
from ejercicioFun import Cuadrado, Circulo, mostrarDatos

def main():
    
    while True:
        menu="""
        Menú de opciones
        =================================
        |Calcúle el área y perímetro de:|
        |Seleccione un número:          |
        |1. Cuadrado.                   |
        |2. Circulo.                    |
        |3. Salir.                      |
        =================================
        Ingrese su opción: 
        """
        opcion=input(menu)
        
        if opcion == '1':
            print('Cuadrado')
            lado=float(input("Ingrese el lado del cuadrado: "))
            cuadrado= Cuadrado(lado)
            mostrarDatos(cuadrado)
        elif opcion=='2':
            radio=float(input("Ingree el radio del circulo: "))
            circulo= Circulo(radio)
            mostrarDatos(circulo)
        elif opcion == '3':
            print("Salir")
            break        
        else:
            print("Ingrese una opción valida.")
        
    
        
main()