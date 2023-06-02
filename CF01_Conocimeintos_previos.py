# LINEA DE COMENTARIO 

""" COMENTARIO QUE POSEE
                SALTOS DE LINEA"""

#Mostrar en Pantalla
print("print(""Nuevo Curso."")", " -> ", "Nuevo Curso.")

#variables
varaible = "variable"
print(varaible)

#contatnes (por convencion)
CONSTANTE = "Constante"
print(CONSTANTE)

#Tipos de datos
texto : str = "Cadena de texto."
print(texto)
print(("Tipo de variable texto", type(texto)))

numeroEntero  : int = 10
print(numeroEntero)
print(("Tipo de variable numeroEntero", type(numeroEntero)))

numeroDecimal : float = 3.14
print(numeroDecimal)
print(("Tipo de variable numeroDecimal", type(numeroDecimal)))
#pueden almacenar distintos tipos de datos (tipado dinamico)

print()
#Operaciones
numeroI1 = 10
numeroI2 = 3
print("Suma ", numeroI1, "+", numeroI2, "=", numeroI1 + numeroI2)
print("Resta ", numeroI1, "-", numeroI2, "=", numeroI1 - numeroI2)
print("Multiplicacion ", numeroI1, "*", numeroI2, "=", numeroI1 * numeroI2)
print("Division resultado entero ", numeroI1, "//", numeroI2, "=", numeroI1 // numeroI2)
print("Division resultado decimal ", numeroI1, "/", numeroI2, "=", numeroI1 / numeroI2)
print("Resto de division ", numeroI1, "%", numeroI2, "=", numeroI1 % numeroI2)

print()
#Operadores relcionales

#Operadores logicos (and, or, not)


#Tipo de valor de la variable



#ingreso de distintos tipos de datos y confirmacion
edad = int(input("Ingrese su edad -> "))
altura = float(input("Ingrese su altura -> "))
autorizacion = input ("Confirmacion de datos (si/no)")
autorizacion = autorizacion == "si"

#Crear Multiples variables en linea
nombre, apellido, titulo = "Gaston", "Farias", "Tecnico Programador"