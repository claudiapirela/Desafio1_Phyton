# AUTORA: CLAUDIA PIRELA  FECHA: 23-02-23
# ACTIVIDAD 2 caso 1: Rentabilidad
"""
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente 
para calcular las utilidades de un proyecto. Para ello utiliza input() para solicitar 
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺T

"""
# DATOS DE ENTRADA
print("DATOS DE ENTRADA, recuerde el número de usuario es un número entero y números con decimales use el punto")
si_no=input("Leiste la advertencia para los DATOS DE ENTRADA (si o no)")
# se debe validar la respuesta y ejecutar la acción dependiendo de la respuesta

num_usuario=int(input("Ingrese el número de usuario: "))
precio_susc=float(input("Ingrese el precio de suscripción (CLP):"))
gasto_total=float(input("Ingrese el gasto total (CLP):"))

#CÁLCULAR LA UTILIDAD
utilidades= (precio_susc * num_usuario) - gasto_total

#mostrar resultado
print(f"Las utilidades actuales son de: {utilidades:.2f} CLP")

#realizado por: Claudia Pirela 23-2-23


