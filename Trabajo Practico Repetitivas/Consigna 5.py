#Solicito nombre y valido que tenga solo letras
print("\n--- BIENVENIDO A LA ARENA ---")
nombre = input("\nNombre del Gladiador: ").strip()

while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. ").strip()

#Defino las variables del juego
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12

print("\n === INICIO DEL COMBATE ===")
#defino condición base ganar/perder
while vida_jugador > 0 and vida_enemigo > 0:
    #mensaje con hp
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    #condicional opción del 1 al 3
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    #para ataque pesado (sin uso de ñ)
    if opcion == "1":
        if vida_enemigo < 20:
            danio = int(danio_jugador * 1.5)  #para evitar decimales
        else:
            danio = danio_jugador

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    #para ráfaga veloz
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    #para curar
    elif opcion == "3":
        if pociones > 0:
            vida_jugador = min(vida_jugador + 30, 100) #para no superar los 100 HP
            pociones -= 1
            print("Te curaste 30 puntos de vida")
        else:
            print("¡No quedan pociones!")

    #ataque enemigo
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")
    #Mensaje de turno
    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

#resultado
if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")