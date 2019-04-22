"""Funciones de las cadenas"""

cadenaHola = "Holi mundo mi querida sasha"

print(len(cadenaHola))

"""mayusculas"""

print(cadenaHola.upper())

mayusculas = cadenaHola.upper()

print(mayusculas)

"""minusculas"""

print(mayusculas.lower())

"""lista de palabras"""

print(mayusculas.split())

"""formato"""

nombre = "liz"
edad = 26
print("Buenos días a ti, {} feliz cumpleaños No. {}".format(nombre,edad))
print(f"Buenos tardes a ti, {nombre} feliz cumpleaños No. {edad}")


division = 3/4
print("división igual a {div:1}".format(div = division))
