#Definición de variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#condición antispam
racha_forzar = 0

#solicitud del nombre
agente = input("Nombre del agente: ").strip()

while not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ").strip()

#Comienzo del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    #Bloquear por alarma
    if alarma and tiempo <= 3:
        print("DERROTA (bloqueo)")
        break

    print("\n--- ESTADO ---")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    #solicito opción y valido que sea del 1 al 3
    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error. Indique una opción válida: ")

    #opción 1
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
            continue

        #riesgo de alarma
        if energia < 40:
            num = input("Riesgo! Elija número (1-3): ")
            while not num.isdigit() or int(num) < 1 or int(num) > 3:
                num = input("Error. Elija un número del 1 al 3: ")

            if num == "3":
                alarma = True
                print("Se activó la alarma!")

        #abrir cerradura
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta!")

    #Opción 2
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  #corta la racha

        print("Hackeando")

        for i in range(4):
            codigo_parcial += "A"
            print("Progreso:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("Cerradura abierta por hackeo")

    # opcion 3
    elif opcion == "3":
        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
        #para cortar racha
        racha_forzar = 0 

        print("Descansaste.")

#Resultados
if cerraduras_abiertas == 3:
    print("VICTORIA. ¡Abriste la bóveda!")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")