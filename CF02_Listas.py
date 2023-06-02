#PD: normalmente se usan lista que almacenen 1 solo tipo de valor

#definir listas
lista1 = list()
lista2 = []

print()

#Mostrar elementos
lista1 = ["Gaston", "Farias", 28, 1.74, True]
print(lista1)

print()

#indices
print("primer elemento (lista1[0])", lista1[0])
print("cuarto elemento (lista1[3])", lista1[4])

print()

#indices negativos
print("primer elemento (lista1[-4])", lista1[-5])
print("cuarto elemento (lista1[-1])", lista1[-1])

print()

#Cambair valor
print("lista1[2]",lista1[2])
lista1 [2] = 29
print("lista1[2]",lista1[2])

print()

#Crear sub lista (desde 0 hasta 4 NO INCLUSIVE)
lista2 = lista1 [0:4]
print("lista2 =",lista2)
#[ a : b ] Desde a hasta b
#[ a :   ] Desde a hasta terminar
#[   : b ] Desde los primerso hasta el indicen b
#[ a : b : c] Desde a hasta b con salto c
#[::-1] Invierte la lista

print()

#Añadir elemento a lista
lista3 = list()
print(lista3)
lista3.append("Buenas!")
print(lista3)
lista3.append("Como va?")
print(lista3)

#Longitu de una lista
logitud_de_lista = len(lista3)
print("Dimension de la lista anterior = ", logitud_de_lista)

print()

#Inserta elementos
#lista.insert( posicion , elemento)
lista4 = [ "a", "b", "c", "d", "e" ]
print(lista4)
lista4.insert(0, "g")
print(lista4)
lista4.insert(2, "s")
print(lista4)

print()

#extender / combinar listas
lista5 = [ "f", "h", "i", "j", "k"]
print("lista5",lista5)
lista4.extend(lista5)
print("lista4",lista4)

print()

#Remover elemento 1
lista4.remove("g")
print("lista4",lista4)

print()

#remover elemento 2
del lista4[0]
print("lista4",lista4)

print()

#Eliminar todos los elemntos
lista4.clear()
print("lista4",lista4)

print()

#ordenar
listaInt = [20, 43 , 500, 1, 7, 1000, 264, 8, 3]
listaInt2 = list()
print(listaInt)

print()

listaInt.sort()
listaInt2 = listaInt
print("De menor a mayor",listaInt2)                   
print("Menor numero", listaInt[0])
print("Mayor numero", listaInt[-1])

print()

listaInt.sort(reverse = True)
listaInt2 = listaInt
print("De mayor a menor", listaInt2)     
print("Menor numero", listaInt[-1])
print("Mayor numero", listaInt[0])

print()

#Maximos y minimos
listaInt = [20, 43 , 500, 1, 7, 1000, 264, 8, 3]
print("min(listaInt)",min(listaInt))
print("max(listaInt)",max(listaInt))

#Se encuentra el valor?
listaInt = [20, 43 , 500, 1, 7, 1000, 264, 8, 3]
print("43 SI esta en la lista?", 43 in listaInt)

#Se encuentra el valor?
listaInt = [20, 43 , 500, 1, 7, 1000, 264, 8, 3]
print("11 NO esta en la lista?", 11 not in listaInt)

print()

#Ubicacion del numero 43
listaInt = [20, 43 , 500, 1, 7, 1000, 264, 8, 3]
print("En que posicionse encuentra el numero 43 ->", listaInt.index(43)) 
#PD : .index solo busa y encuentra el primero
#PD : si elnuemro bsucado no esta, .index tirara error

print()

#Matrices 2col x 3fila
listaInt = [1, 2, 3]
listaInt2 = [4, 5, 6]
matriz = [listaInt, listaInt2]
print("Mostrar Matriz",matriz)
print("Mostrar valor matriz[0][1] ->", matriz[0][1])