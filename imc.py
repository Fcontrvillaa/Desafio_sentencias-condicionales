import sys

# --- calcula IMC desde argumentos de línea de comandos ---

# Obtener el peso y la altura de los argumentos
peso = int(sys.argv[1])
altura_cm = float(sys.argv[2])

# Calcular el IMC
imc = peso / ((altura_cm / 100) ** 2)

# Mostrar el resultado
print(f"El IMC es de : {imc:.2f}")
print("-------------------------------")
print(f"Su clasificacion OMS es : ")

# Clasificar según OMS
if imc < 18.5:
    print(" Bajo peso")
elif 18.5 <= imc < 25:
    print(" Adecuado")
elif 25 <= imc < 30:
    print(" Sobre peso")
elif 30 <= imc < 35:
    print(" Obesidad nivel I")
elif 35 <= imc < 40:
    print(" Obesidad nivel II")
elif imc >= 40:
    print(" Obesidad nivel III") 
print("-------------------------------")