class Personas:
    id = 0
    nombre = ""
    direccion = ""

    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return "Id: {} Nombre: {}".format(self.id, self.nombre)


