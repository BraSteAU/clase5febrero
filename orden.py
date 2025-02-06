#ordenamiento avanzado de listas
#recibir una lista d estudiantes con sus calificaciones y ordenarlas de mayor a menor(timesort)

def ordenar_estudiantes(estudiantes):
    estudiantes.sort(key=lambda x: x[1], reverse=False)

estudiantes=[
    ("juan",85),
    ("maria",92),
    ("carlos",78),
    ("ana",95),
    ("pedro",88)
]

ordenar_estudiantes(estudiantes)
print("lista de estudiantes ordenada por nota fina")
for estudiante in estudiantes:
    print(f"{estudiante[0]} - nota: {estudiante[1]}")

