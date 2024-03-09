#mainEjercicio.py
import math
class ClassFigura:
    
    def __init__(self,lado, pi=4.1416):
        pass
    
    def area(self):
        pass
    
    
    def perimetro(self):
        pass
    
class Cuadrado(ClassFigura):
    
    def __init__(self, lado):
        self.nombre= __class__.__name__ #guarda el nombre de la clase
        self.lado=lado
            
    def area(self):
        return self.lado*self.lado
    
    def perimetro(self):
        return 4*self.lado            
    
    def __str__(self):#redeine el objeto para que muestre los datos y no el espacio en memoria.
        return f'{self.nombre} Lado: {self.lado}'    
    
class Circulo(ClassFigura):
    
    def __init__(self, radio):
        self.nombre= __class__.__name__
        self.radio=radio
        
    def area(self):
        return math.pi*self.radio*self.radio
    
    def perimetro(self):
        return 2*math.pi * self.radio
    
    def __str__(self):
        return f'{self.nombre} Radio: {self.radio}'   

def mostrarDatos(ClassFigura):
    print(ClassFigura)
    print("Area: ", ClassFigura.area())
    print("Perimetro: ",ClassFigura.perimetro())