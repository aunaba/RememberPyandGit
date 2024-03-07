class Player:
    
    #Atributo de objeto de clase
    membresia=True
    
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def ejecutar(self):
        print('Run')
        return 'ok'
    
    def datos(self):
        print(f"Mi nombre es {self.nombre}")
        
    def getMembresia(self):
        if Player.membresia:
            print("ok")
        else:
            print("No membresía")
        
    @classmethod  #se debe agregar la referencia a la clase con el parámetro 'cls'
    def agregar_datos(cls, score):
        return score
    
    @staticmethod  #A este tipo de metodo no se necesita pasar la clase
    def agregar_datos2(score):
        return score
    
        
        
        
        
        
        
        
        
        
        
        
#Los atributos de las variables creadas en la función constructora, los envio desde el archivo main.py