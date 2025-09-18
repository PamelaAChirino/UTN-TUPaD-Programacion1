
 #1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for  num in range(101):
   print(num)
#2) Desarrolle un programa que solicite al usuario un número entero y determine la
#cantidad de dígitos que contiene

num=int(input("Ingrese un número entero"))
dig= len(str(abs(num)))
print(f"La cantidad dígitos de {num} es {dig}")

#Con bucle
num=int(input("Ingrese un número entero"))

n= abs(num)
cantidad_de_digitos=0
if n==0:
  cantidad_de_digitos=1
else:
  cantidad_de_digitos=0
  while n>0:
    n//=10
    cantidad_de_digitos+=1
print(f"La cantidad de dígitos de número {num} es {cantidad_de_digitos}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre
#dos valores dados por el usuario,excluyendo esos dos valores.
print("Ingrese los números entre los que desea sumar los números enteros")
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
suma_total=0
if(num1>num2):
  valor_final=num1
  valor_inicial=num2
else:
  valor_final=num2
  valor_inicial=num1

for num in range(valor_inicial+1, valor_final, 1):
  suma_total+=num

print(f"La suma total es: {suma_total}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume
#en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el
#usuario ingrese un 0

repeticiones=int(input("Ingrese la cantidad de numeros que quiere ingresar:"))
cont=1
suma_total=0

while repeticiones>0:
  num=int(input(f"Ingrese número {cont}: "))

  if(num==0):
    break
  suma_total+=num
  repeticiones-=1
  cont+=1
print(f"La suma total es:{suma_total}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final el programa debe mostrarcuantos intentos fueron necesarios para
#acertar el número
import random
num_usuario=int(input("Adivine el número aleatorio: "))
num_aleatorio=random.randint(0,9)
cont=0;
while num_usuario != num_aleatorio:
  cont+=1
  num_usuario=int(input("Por favor, vuelva a intentarlo: "))

print(f"La cantidad de intento fue de  {cont} veces")
#6) Desarrolla un programa que imprima por pantalla todos los números pares
#comprendidos entre 0 y 100, en orden decreciente

for num in range(100,0, -2):
  print(num)
#7) Crea un programa que calcule la suma de todos los números comprendidos entre
#0 y un número entero positivo indicado por el usuario
num=int(input("Ingrese un número entero positivo: "))

n= abs(num)
suma_total=0;
for i in range(0,n,1):
  suma_total+=i
print(f"La suma total entre 0 y {n}: {suma_total}")

#8) Escriba un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos números enteros son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota:Para probar el programa puedes usar una cantidad menor, pero debe
#estar preparado para procesar 100 números con un solo cambio)
repeticiones= 10
pares=0
impares=0
negativos=0
positivos=0

for i in range(1,repeticiones):
  num=int(input("Ingrese un número entero: "))
  if(num % 2 ==0):
    pares+=1
  else:
    impares+=1
  if(num>0):
    positivos+=1
  else:
    negativos+=1
  
  print(f"La cantidad de números pares son: {pares}")
  print(f"La cantidad de números impres son: {impares}")
  print(f"La cantidad de números positivos son: {positivos}")
  print(f"La cantidad de números negatvos son: {negativos}")
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego
#calcule la media de esos valores.(Nota: puedes probar el programa con una cantidad menos, pero debe
#poder procesar 100 números cambiando un solo valor)
suma = 0

for i in range(1, 10):
    numero = int(input(f"Ingresa el número {i} de 100: "))
    suma += numero 

media = suma / 10

print(f"\nLa media de los números ingresados es: {media}")

#10)Escriba un programa que invierta el orden de los dígitos de un número ingresado
#por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# Programa que invierte un número con operaciones matemáticas

numero = int(input("Ingrese un número entero: "))

n = abs(numero)
invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10               

if numero < 0:
    invertido = -invertido

print(f"El número invertido es: {invertido}")