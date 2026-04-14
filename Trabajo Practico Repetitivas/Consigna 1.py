#Solicito el nombre del cliente
nombre = input("Cliente nombre: ").strip()

#Valido que se ingrese un nombre y que solo contenga letras
while nombre == "" or not nombre.isalpha():
    print("Error. Por favor ingrese un nombre en letras y sin vacios")
    nombre = input("Cliente nombre: ").strip()

#Defino una variable para la cantidad de productos
cant_str = input("Ingresa cantidad de productos: ").strip()

#Valido que el usuario ingrese un entero mayor a cero
while not cant_str.isdigit() or int(cant_str) <= 0:
    print("Error. Por favor ingrese un número entero mayor a 0")
    cant_str = input("Ingresa cantidad de productos: ").strip()

#Paso a número el string de la variable
cant_int = int(cant_str)

#Solicito el precio del producto
for i in range (1, cant_int+1):
    precio_str = input(f"Producto {i}  - Precio: $").strip()
    

#Valido la condición del precio como número entero mayor a cero
    while not precio_str.isdigit() or int(precio_str) <=0:
        print("Error. Por favor ingrese un número entero mayor a 0")
        precio_str = input(f"Producto {i}  - Precio: $ ").strip()

#Convierto el string en número
    precio_int = int(precio_str)

#Defino variables descuento
    total_sindesc = 0
    total_condesc = 0

    desc = input("Tiene descuento? Responda S/N: ").strip().lower()

#Valido que solo se pueda contestar S/N
    while desc != "s" and desc != "n":
        print("Error. Por favor conteste S para si o N para no")
        desc = input("Tiene descuento? Responda S/N: ").strip().lower()

    total_sindesc = precio_int

#Calculo el precio con descuento    
    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_condesc += precio_final

ahorro = total_sindesc - total_condesc
promedio = total_condesc / cant_int

print()
print(f"Total sin descuento: ${total_sindesc:.2f}")
print(f"Total con descuento: ${total_condesc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: {promedio:.2f}")