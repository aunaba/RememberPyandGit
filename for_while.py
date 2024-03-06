#función enumerate() funciona con datos iterables
'''for i,char in enumerate('hola'):
#Puedo llamar en for a la tupla, con un solo dato o con ambos datos
    #print(i)
    print(i,char)
'''
'''for i, num in enumerate(list(range(10))):
    print(i,num)
    if (num==8):
        print(f'index of 8 es: {i}')
'''        

#for se ejecuta una cantidad finita de veces
#while se ejecuta hasta que le demos la instrucción
for i in ([1,2,3]):
    print(i)
    if i==3:
        print()
        
        
i=1
while i <=3:
    print(i)
    i+=1