#break se usa para hacer un corte 
lista=[1,2,3,4,5]
n=1
#En este caso no pasaría a la instrucción n+=1 y se detiene al contar 1
'''while n <= len(lista):
    print(n)
    break
    n+=1
'''
'''while True:
    respuesta=input('ingrese un mensaje: ')
    if(respuesta=='bye'):
        print("Adios")
        break'''

#Continue se va a la siguiente interación hasta que se cumppla la condición
'''while n <= len(lista):
    print(n)
    n+=1
    if n==3:
        continue
    print('no es 3')
'''
#pass se usa cuando hay una función o una parte del código sin terminar, se usa pass para que la ejecución del código continúe sin problemas.

