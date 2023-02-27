# AUTORA: CLAUDIA PIRELA  FECHA: 23-02-23
# ACTIVIDAD 2 caso 2: Rentabilidad
"""
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados, 
los usuarios normales y los usuarios premium a los cuales se les cobrará una 
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que 
permita considerar el caso recién expuesto. Para ello modifica la fórmula de utilidades 
en la cual se solicite mediante input() los parámetros de entrada precios de 
suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺T

"""
# DATOS DE ENTRADA
print("DATOS DE ENTRADA, recuerde el número de usuario es un número entero y números con decimales use el punto")
si_no=input("Leiste la advertencia para los DATOS DE ENTRADA (si o no)")
# se debe validar la respuesta y ejecutar la acción dependiendo de la respuesta

num_usuario_normal=int(input("Ingrese el número de usuario normales: "))
num_usuario_premium=int(input("Ingrese el número de usuario premium: "))
precio_susc=float(input("Ingrese el precio de suscripción (CLP):"))
gasto_total=float(input("Ingrese el gasto total (CLP):"))

#CÁLCULOS para USUARIO NORMAL
utilidades_normal= (precio_susc * num_usuario_normal) - gasto_total
print(f"Las utilidades con los usuarios normales es de: {utilidades_normal:.2f} CLP")

#CÁLCULOS para USUARIO PREMIUM se les cobrará una suscripción un 50% mayor (SE DEBE SUMAR AL PRECIO)
precio_susc_premium= (precio_susc * 50 /100)+ precio_susc
utilidades_premium= (precio_susc_premium * num_usuario_premium) - gasto_total
print(f"Las utilidades con los usuarios premium es de: {utilidades_premium:.2f} CLP")

#realizado por: Claudia Pirela 23-2-23