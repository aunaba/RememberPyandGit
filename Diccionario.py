Persona={
    'nombre': 'Juan',
    'apellido':'Tabares',
    'edad':'27',
    'elementos':['casa','carro']
}
#print(f"nombre: {Persona['nombre']}, apelido: {Persona['apellido']}, Edad:{Persona ['edad']}")
#print(Persona)
#print(Persona['elementos'][1])
#Puedo introducir la lista que está dentro del diccionario a una variable

#Para agregar un elemento a la lista se hace de la siguiente manera:
Persona['direccion']='street'
#print(Persona)

#El método items devuelve tuplas
print(Persona.items())