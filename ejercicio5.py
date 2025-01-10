'''
Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5.

'''

num= int(input("Introduce un numero: "))
if num%3 == 0 and num%5 == 0:
    print("El numero es divisible entre 3 y 5")
else: 
    print("El numero no es divisible entre 3 y 5")