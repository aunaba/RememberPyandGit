es_amigo=True
es_familiar=False

'''if es_amigo:
    print("Es amigo")
elif es_familiar:
    print("Es familiar")
elif es_amigo and es_familiar: 
    print("es amigo y familiar")
else:
    print("no es amigo ni familiar")

#Operador ternario
#Condición_verdadera if condicion else condicion false
mensaje="Es amigo" if es_amigo else "No es amigo"
'''
#is vs ==
a=[]
b=a
c=[1]
d=[1]
print(True == 1)
print(''==1)
print([]==1)
print(10==10.0)
print(a==b)
print([]==[])
print(c==d)

print()

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print(a is b)
print([] is [])
print(c is d)