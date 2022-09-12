#Ejercicio1
contador = 0
while True:
    numero = int(input("Ingrese numero par"))
    contador = contador + 1
    if numero % 2 == 0:
        print("El numero es par")
        break
    else:
        print("El numero es impar")
    break


#Ejercicio2
numero1 = int(input("Ingrese primer numero"))
numero2 = int(input("Ingrese segundo numero"))
contador = 0
opciones = int(input("1-suma 2-resta 3-multiplicacion 4-division"))
while True:
    contador = contador + 1
    if opciones == 1:
        print(numero1 + numero2)
        break
    elif opciones == 2:
        print(numero1 - numero2)
    elif opciones == 3:
        print(numero1 * numero2)
    elif opciones == 4:
        print(numero1 / numero2)
    else:
        print("numero incorrecto")



#Ejercicio3
email = input("ingresar email")
if "@" in email:
    print("Es un email")
else:
    print("no es un email")



#Ejercicio4
listaDeNumeros = [1,2,3,4,5,6,7,8]
cantidad = 0
for numeros in listaDeNumeros:
    cantidad += 1
print(cantidad)


#Ejercicio5
listaDeNumeros = [1,2,3,4,5,6,7,8]
total = 0
for numeros in listaDeNumeros:
    total+= numeros
print(total)


#Ejercicio6
listaDeNumeros = [1,2,3,4,5,6,7,8]
total = 0
for numeros in listaDeNumeros:
    total+= numeros
print(int(total/ len(listaDeNumeros)))


#Ejercicio7
listaDeNumeros = [1,2,3,4,5,6,7,8]
maximo = 0
for numero in listaDeNumeros:
    if maximo < numero:
        maximo = numero
print(maximo)


#Ejercicio8
listaDeNumeros = [1,2,3,4,5,6,7,8]
minimo = max(listaDeNumeros)
for numero in listaDeNumeros:
    if minimo > numero:
        minimo = numero
print(minimo)