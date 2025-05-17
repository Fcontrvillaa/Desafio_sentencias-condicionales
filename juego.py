import random
import sys

jugador = sys.argv[1]

opciones = ["piedra", "papel", "tijera"]

if jugador not in opciones:
    print(" Opcion no valida. Debe ser piedra, papel o tijera")
    sys.exit(1)
else:
    computador = random.choices(opciones)
    computador = computador[0]

    print(f"El jugador eligio {jugador}")
    print(f"El computador eligio {computador}")

if jugador == computador:
    print("Empate")

elif (jugador == "piedra" and computador == "tijera") or \
        (jugador == "papel" and computador == "piedra") or \
        (jugador == "tijera" and computador == "papel"):
    print (" Ganaste!!")

else:
    print(" Perdiste. ")