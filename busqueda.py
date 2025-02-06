#Busqueda avanzada en un matriz
#Localizacion de un producto en una tienda

#dada una matriz que representa los estantes de una tienda, buscar un producto y devolver su ubicacion

def buscar_producto(matriz,producto):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==producto:
                return i,j
    return None 

tienda=[
    ["laptop","teclados","mouse"],
    ["monitor","procesador","parlantes"],
    ["impresora","webcam","route"]
]

producto_buscar=input("Ingrese el producto que quiere buscar: ")
ubicacion=buscar_producto(tienda,producto_buscar)

if ubicacion:
    print(f"El producto '{producto_buscar}' esta en la fila {ubicacion[0]+1} y en la columna {ubicacion[1]+1}")
else:
    print(f"El producto '{producto_buscar}' no se encuentra en la tienda")