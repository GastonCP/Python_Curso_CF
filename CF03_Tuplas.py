#TUPLAS
#Inmutables una vez definidas
# Python accede mas rapidamente que las listas.

print()
#Crear, definir y mostrar tupla
tupla = ("texto", 10, 3.14, True, [1, 2, 3], (4, 5, 6))
print(tupla)
print(type(tupla))

print()
#indices de la tupla
print("tupla[0]",tupla[0])
print("tupla[2]",tupla[2])
print("tupla[4]",tupla[4])
print("tupla[-1]",tupla[-1])

print()
#Crear sub Tupla
subTupla = tupla[1:3]
subTupla2 = tupla[4:]
print("subTupla",subTupla)
print("subTupla2",subTupla2)

print()
#Crear tupla a partir de una lista
lista1 = list()
lista1 = [1,2,3,4,5]
print(type(lista1),lista1)
tupla = tuple(lista1)
print(type(tupla),tupla)
#PD tambien se puede hacer vicebersa

print()
#Asignar valores deuna tupla 1
tupla2 = (1,2,3,4)
a, b, c, d = tupla2
print(a)
print(b)
print(c)
print(d)

print()
#Asignar valores deuna tupla 2
tupla2 = (1,2,3,4)
a, b, *omitir = tupla2
print(a)
print(b)
print(omitir)

print()
#Asignar valores deuna tupla 3
tupla2 = (1,2,3,4,5,6,7,8,9,10)
uno, dos, *_, nueve, diez = tupla2
print(uno)
print(dos)
print(nueve)
print(diez)
# * -> Lista
# _ -> Omitir

print()
#Comprimir valores
lista1 = [1,2,3,4,5,"a","b","c"]
tupla1 = (6,7,8,9,0)
resultado1 = zip (tupla1, lista1)
print("resultado1",resultado1)
resultado1 = tuple(resultado1)
print("resultado1",resultado1)



