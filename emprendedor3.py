# AUTORA: CLAUDIA PIRELA  FECHA: 23-02-23
# ACTIVIDAD 2 caso 2: Rentabilidad
"""
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula 
original de utilidades donde el usuario ingrese el precio de suscripción P, el número de 
usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año 
anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades 
actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos 
decimales.
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺T

"""
# DATOS DE ENTRADA
print("DATOS DE ENTRADA, recuerde el número de usuario es un número entero y números con decimales use el punto")
si_no=input("Leiste la advertencia para los DATOS DE ENTRADA (si o no)")
# se debe validar la respuesta y ejecutar la acción dependiendo de la respuesta

num_usuario_normal=int(input("Ingrese el número de usuario normales: "))
precio_susc=float(input("Ingrese el precio de suscripción (CLP):"))
gasto_total=float(input("Ingrese el gasto total (CLP):"))
utilid_anterior=float(input("Ingrese las utilidades del año anterior (CLP):"))

#CÁLCULOS para USUARIO NORMAL
utilidades_actual= (precio_susc * num_usuario_normal) - gasto_total
print(f"Las utilidades actuales con los usuarios normales es de: {utilidades_actual:.2f} CLP")

#CÁLCULOS para hallar la razón entre las utilidades actuales y las del año anterior
razon= (utilidades_actual /utilid_anterior)

print(f"La razón entre las utilidades actuales y las del año anterior es de: {razon:.2f}")

#realizado por: Claudia Pirela 23-2-23