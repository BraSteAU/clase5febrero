#Retorno y parametros.
#Las funciones pueden recibir datos de entrada y devolver valores procesados(retornos)

#Crear una funcion que reciba una lista de ventas mensuales y clacule, el total vendido, el mes con mayores ventas 
#y el mes con menores ventas.

def analizarVentas(ventas):
    total=sum(ventas)
    max_venta=max(ventas)
    min_venta=min(ventas)

    return total, ventas.index(max_venta),ventas.index(min_venta)

#datos de ventas mensuales

ventas_mensuales=[1500,3200,1800,4000,2510,2100,3400,1480,4500,4300,5000,6000]
total,mes_max,mes_min=analizarVentas(ventas_mensuales)

print(f"Total vendido en el año fue: ${total}")
print(f"El mes con mayores ventas fue el numero: {mes_max+1} con ${ventas_mensuales[mes_max]}")
print(f"El mes con menores ventas fue el numero: {mes_min+1} con ${ventas_mensuales[mes_min]}")
