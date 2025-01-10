#TEORIA PARTE 1
persona={"nombre":"Juan", "edad":25, "ciudad":"Lima", "correo": "cesar@mail.to"}

print("Nombre: " ,persona["nombre"])
print("Edad: ",persona["edad"])
print("ciudad: ",persona["ciudad"])
print(persona["ciudad"])

if "nombre" in persona:
    print("la clave se encuentra")
else:
    print("No se encuentra la clave")
    
#AGREGAR
persona["telefono"]="975444664"
print(persona)

#ELIMINAR
persona={"nombre":"Juan", "edad":25, "ciudad":"Lima", "correo": "cesar@mail.to"}
del persona["correo"]
print(persona)

#ITERAR
for clave,valor in persona.items():
    print(f"{clave}:{valor}")
    