'''
Imprimir numeros impares de N a 1
Descripciòn: Escribe un programa que soliciite un numero N al usuario 
e imprima tods los numeros impares desde N hasta 1 en orden descendente

'''

n = int(input("Por favor ingrese un numero: "))
for i in range(n,0,-1):
    if i%2 !=0:
        print(i)
        
    
