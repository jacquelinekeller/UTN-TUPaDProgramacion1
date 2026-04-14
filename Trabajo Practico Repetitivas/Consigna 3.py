#Solicito nombre y defino la condición de solo letras
operador = input("Indique su nombre: ").strip()

while not operador.isalpha():
    print("Error. Ingrese solo letras: ")
    operador = input("Ingrese su nombre: ").strip()

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""
opción = ""

#Se despliega el menú para el usuario y valido que solo pueda poner un número
while opción != "5":
    print("\n MENÚ: ")
    print("1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del día")
    print("4- Ver resumen general")
    print("5- Cerrar sistema")

#Valido que la opción ingresada sea válida
    opción = input("Opción: ").strip()
    while not opción.isdigit() or int(opción) < 1 or int(opción) > 5:
        opción = input("Error. Ingrese una opción del 1 al 5: ")

#Defino variables para la opción 1
    if opción == "1":
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error, indique 1 para Lunes o 2 para Martes").strip()

        nombre = input("Indique su nombre: ").strip()
        while not nombre.isalpha():
            nombre = input("Error. Ingrese solo letras: ").strip()

#Asigno los turnos según el día elegido
        asignado = False #bandera para agregar un mensaje de turno asignado
        if dia == "1": #día lunes
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                    print("El paciente ya tiene turno ese día.")
            elif lunes1 == "":
                    lunes1 = nombre
                    asignado = True
            elif lunes2 == "":
                    lunes2 = nombre
                    asignado = True
            elif lunes3 == "":
                    lunes3 = nombre
                    asignado = True
            elif lunes4 == "":
                    lunes4 = nombre
                    asignado = True
            else:
                    print("No hay turnos disponibles.")
   
        else: #día martes
            if nombre in (martes1, martes2, martes3):
                    print("El paciente ya tiene turno ese día.")
            elif martes1 == "":
                    martes1 = nombre
                    asignado = True
            elif martes2 == "":
                    martes2 = nombre
                    asignado = True
            elif martes3 == "":
                    martes3 = nombre
                    asignado = True
            else:
                    print("No hay turnos disponibles.")
  
        if asignado: #Mensaje agregado
                    print("Turno asignado correctamente.")
    #Opción para cancelar turnos
    elif opción == "2": #valido que pueda ingresar 1 o 2
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error. Indique 1 para Lunes o 2 para Martes: ").strip()
        
        #valido que solo pueda ingresar letras
        nombre = input("Nombre: ").strip()
        while not nombre.isalpha():
            nombre = input("Error. Ingrese solo letras: ").strip()
        #Asignación del día
        cancelado = False #bandera para mensaje de cancelación
        if dia == "1": #dia lunes
            if lunes1 == nombre:
                lunes1 = ""
                cancelado = True
            elif lunes2 == nombre:
                lunes2 = ""
                cancelado = True
            elif lunes3 == nombre:
                lunes3 = ""
                cancelado = True
            elif lunes4 == nombre:
                lunes4 = ""
                cancelado = True
        
        else: #dia martes
            if martes1 == nombre:
                martes1 = ""
                cancelado = True
            elif martes2 == nombre:
                martes2 = ""
                cancelado = True
            elif martes3 == nombre:
                martes3 = ""
                cancelado = True
    
        if not cancelado:
             print("Nombre no encontrado.")
        else:
             print("Turno cancelado.")
    
    #Opción de ver agenda
    elif opción == "3": #valido que solo pueda ingresar 1 o 2
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error. Indique 1 para Lunes o 2 para Martes: ").strip()

        #Muestro la agenda con el nombre del turno ocupado, sino que se encuentra "Libre"
        if dia == "1":
            print("Lunes: ")
            print("1:", lunes1 if lunes1 else "(Libre)")
            print("2:", lunes2 if lunes2 else "(Libre)")
            print("3:", lunes3 if lunes3 else "(Libre)")
            print("4:", lunes4 if lunes4 else "(Libre)")
        else:
            print("Martes: ")
            print("1:", martes1 if martes1 else "(Libre)")
            print("2:", martes2 if martes2 else "(Libre)")
            print("3:", martes3 if martes3 else "(Libre)")

    #Promedio de ocupación de turnos
    elif opción == "4":
        ocup_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocup_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        print("Lunes:", ocup_lunes, "ocupados,", 4 - ocup_lunes, "libres")
        print("Martes:", ocup_martes, "ocupados,", 3 - ocup_martes, "libres")

        if ocup_lunes > ocup_martes:
            print("Más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Más turnos: Martes")
        else:
            print("Igual cantidad.")

    #Opción de cerrar el sistema
    elif opción == "5":
        print("Cerrando sistema.")