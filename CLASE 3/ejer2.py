''''''
'''
 Calcular el producto de los números entre A y B
Descripción: Solicita dos números A y B (donde A < B) y calcula el producto de todos los números en ese rango, incluyendo A y B.

'''


a = int(input("Por favor ingrese un numero: "))
b = int(input("Por favor ingrese un numero: "))
producto = 1
for i in range(a,b+1):
    producto *=i
    
print(f"el producto de los numeros {a} y {b} es: {producto}")
