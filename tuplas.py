"""tupla-no se modifica"""

tupla_colores = ("verde","azul","amarillo")

for color in tupla_colores:
    print(color)

"""Diccionarios-indexados-clave-valor"""

diccio_colores = {"azul":"blue","amarillo":"yellow","rojo":"red"}

print(diccio_colores["amarillo"])

"recorrido-diccionario"

for clave, valor in diccio_colores.items():
    print(clave,valor)
