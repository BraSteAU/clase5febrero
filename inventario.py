#funcion con paso por referencia(lista mutable)
#cuando una funcion recibe una lista como parametro, puede modificarla directamente
#
#ejemplo 2: crear una funcion que reciba un inventario de productos y permita actualizar cantidades segun las compras


def actualizar_inventario(inventario,producto,cantidad_comprada):
    if producto in inventario:
        inventario[producto]-=cantidad_comprada
        if inventario[producto]<0:
            inventario[producto]=0
    
    else:
        print("Producto no encontrado en el inventario")

#Inventario de prueba
inventario={
    "laptop":10,
    "mouse":25,
    "teclado":15,
    "monitores":8
}
producto_solicitado=input("Ingrese el producto comprado: ")
cantidad=int(input(f"Ingrese la cantidad de {producto_solicitado} comprada: "))

actualizar_inventario(inventario,producto_solicitado,cantidad)
print("Inventario actualizado: ",inventario)
