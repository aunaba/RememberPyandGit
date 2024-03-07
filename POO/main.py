# MÓDULOS
from poo import Class_Persona
from player import Player
#Instancia de la clase Class_Persona() en el archivo poo.py
'''per1=Class_Persona('Juan',27,323123456)
per2=Class_Persona('Carol', 23,3001234567)
per3=Class_Persona('Noa',5,30054321)
'''
'''
#Devolver los datos
per1.getDatos()
print('*'*10)
per2.getDatos()
print('*'*10)
per3.getDatos()'''

'''#la función type(), devuelve el tipo de dato
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Hola'))
print(type([]))
print(type(()))
print(type({}))
'''

#Clase Player()
player1=Player('Juan', 27)
player2=Player('Carol', 23)
print(player1.nombre)
print(Player.membresia)
print(Player.agregar_datos(1000))
print(Player.agregar_datos2(2000))


