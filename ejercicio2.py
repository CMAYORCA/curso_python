'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''



num1 = float(input("Por favor ingresa el primer numero: "))
num2 = float(input("Por favor ingresa el primer numero: ")) 
suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
div = num1/num2
divEntera = num1 // num2
modulo = num1%num2
print (f"Suma: {suma}")
print (f"Resta: {suma}")
print (f"Multiplicacion: {multiplicacion}")
print (f"Division: {div}")
print (f"Division Entera: {divEntera}")
print (f"Modulo {modulo}")
