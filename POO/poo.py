class Class_Persona:
    #Se puden crear objetos con atributos sin datos iniciales
    #Conectado a instancia sin función constructora
    '''nombre= None
    edad=None
    movil=None'''
    
    #Puedo poner los datos privados para que no puedan modificarse desde ningún archivo fuera de la clase usando la expresión __nombreObjeto = None, ejm:
    
    __nombre=None
    __edad=None
    __movil=None
    
    #Atributos con datos inicializados:
    #Constructores.
    #Recibe self, que llama cualquier variable de la clase y atributos que quiero inicializar
    def __init__(self,nom,ed,mov ):
        self.__nombre =nom
        self.__edad=ed
        self.__movil=mov
        #al crear ésta función o constructor no es necesario tener variables globales por que se detecta automaticaente el constructor _init_()
        #Al tener éste objeto, se deben enviar los parámetros
        
                
    def getDatos(self):
        print('Nombre: ', self.__nombre)
        print('Edad: ', self.__edad)
        print('Movil: ', self.__movil)


#Como se ha creado un constructor _init_():, es necesario enviar los datos a la clase, por lo cual de ésta manera genera un error.  
'''per1 = Class_Persona() #Instancia de la clase conectada a atributos si datos iniciales
per1.nombre='Juan'
per1.edad=27
per1.movil=323123456

per2=Class_Persona()
per2.nombre='Carol'
per2.edad=23
per2.movil=3001234567'''


'''per1=Class_Persona('Juan',27,323123456)
per2=Class_Persona('Carol', 23,3001234567)
per3=Class_Persona('Noa',5,30054321)

#Devolver los datos
per1.getDatos()
print('*'*10)
per2.getDatos()
print('*'*10)
per3.getDatos()'''