"""
Diseña un programa para calcular el cociente y residuo de una división mediante restas sucesivas.
750722
"""
#Entrada
dividendo = int(input("Introduzca el dividendo: "))
divisor = int(input("Introduzca el divisor: "))

#Proceso
def division_con_restas_sucesivas(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    residuo = dividendo
    return cociente, residuo
cociente, residuo = division_con_restas_sucesivas(dividendo, divisor)

#Salida
print(f"El cociente es {cociente}")
print(f"El residuo es {residuo}")

