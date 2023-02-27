# AUTORA: CLAUDIA PIRELA  FECHA: 23-02-23
# ACTIVIDAD 1: Velocidad de Escape
"""
Se solicita crear un script escape.py que permita calcular la velocidad de escape 
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada 
deben ingresarse de manera interactiva utilizando la función input()
El programa debe especificar claramente el formato en el que se deben entregar los 
datos de entrada con instrucciones apropiadas"""

# CARGAR LA LIBRERIA MATH
import math

# DATOS DE ENTRADA
print("Programa para Calcular la Velocidad de Escape de un planeta")
print("DATOS DE ENTRADA: por favor, no ingrese las unidades,  solo los valores numéricos, use el punto para números con decimales.")

s_n=bool(input("Leyó la información para ingresar los datos? (True o False)"))
radio=float(input("Ingrese el radio del planeta en Kilometros (Km): "))
constante_g=float(input("Ingrese la constante gravitacional, es 9.8 (m/s^2): "))
# Validar la constante
if constante_g!=9.8:
    constante_g=float(input("Ingrese la constante gravitacional, es 9.8 (m/s^2): "))

# si es igual continuar, de lo contrario volver a pedir el dato, esto debería estar en un repita hasta que sea correcto

# CALCULOS
# CONVERTIR Km a m se multiplica por 1000
radio_m= radio * 1000

# CALCULAR 2*g*radio_m
raiz=2*constante_g*radio_m

# CALCULAR la Velocidad con la raiz cuadrada
Ve = math.sqrt(raiz)

#MOSTRAR EL RESULTADO DE LA VELOCIDAD DE ESCAPE con 1 decimal.
print(f"La velocidad de Escape del planeta es: {Ve:.1f} [m/s]")

#realizado por: Claudia Pirela 23-2-23
