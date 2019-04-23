"PROGRAMACION ORIENTADA A OBJETOS"

class ClaseSilla:
    color = "verde"
    precio = 100

objetoSilla1 = ClaseSilla()
objetoSilla2 = ClaseSilla()

objetoSilla2.color = "azul"

print(objetoSilla1.color,objetoSilla2.color)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"hola, mi nombre es {self.nombre}, y tengo {self.edad} años")
    

personaReal = Persona("Pancho", 15)

print(personaReal.saludar())
