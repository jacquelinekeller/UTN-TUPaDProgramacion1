#Defino valores para las variables
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
max_intentos = 3

#Solicito datos para el ingreso utilizando el contador de intentos
while intentos < max_intentos:
    usuario = input("Ingrese usuario: ").strip().lower()
    clave = input("Ingrese clave: ").strip()

#Fijo la condición que las variables sean true
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")

        #Si se ingresan bien los datos, se pasa al menú
        while True:
            print("")
            print("1) Estado")
            print("2) Cambiar clave")
            print("3) Mensaje")
            print("4) Salir")

            opcion = input("Opción: ")

            #Valido que sea número
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
                continue

            opcion = int(opcion)

            # Valido que elija dentro del rango
            if opcion < 1 or opcion > 4:
                print("Error: opción fuera de rango.")
                continue

            #Opciones del menú
            if opcion == 1:
                print("Estado: Inscripto")

            elif opcion == 2:
                nueva_clave = input("Ingrese nueva clave: ")
                confirmar = input("Confirme nueva clave: ")

                #Si elige esta opción valido el valor de la nueva clave
                if len(nueva_clave) < 6:
                    print("Error: la clave debe tener al menos 6 caracteres")
                elif nueva_clave != confirmar:
                    print("Error: las claves no coinciden")
                else:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito")

            elif opcion == 3:
                print("¡Vamos que ya queda menos!")

            elif opcion == 4:
                print("Ha salido del sistema.")
                break #Para salir del sistema

        break #Para salir del login

#Si no se cumplen las condiciones de ingreso, muestro la cantidad de intentos
#Vuelvo a solicitar los valores
    else:
        intentos += 1
        restantes = max_intentos - intentos

        if restantes > 0:
            print(f"Incorrecto, le quedan {restantes} intentos")
        else:
            print("Cuenta bloqueada") #se cumplieron la cantidad de intentos
