from Conexion import Conexion
from Personas import Personas


class DaoPersonas:
    INSERT = "INSERT INTO public.personas (id, nombre, direccion) VALUES(%s, %s, %s)"
    UPDATE = "UPDATE personas SET nombre = %s, direccion = %s WHERE id = %s"
    DELETE = "DELETE FROM public.personas WHERE id = %s"
    FIND = "SELECT * FROM personas WHERE id = %s"
    FINDALL = "SELECT * FROM personas ORDER BY id"

    connection = Conexion.get_instance()

    def insert(self, entity: Personas):
        return self.connection.execute_update(self.INSERT,
                                              (entity.id, entity.nombre, entity.direccion))

    def update(self, entity: Personas):
        return self.connection.execute_update(self.UPDATE,
                                              (entity.nombre, entity.direccion, entity.id))

    def delete(self, id):
        return self.connection.execute_update(self.DELETE,
                                              (id))

    def find(self, id):
        persona = None

        data = self.connection.execute_query(self.FIND, (id,))

        for row in data:
            persona = Personas(row[0], row[1], row[2])

        return persona

    def find_all(self):
        personas = []

        data = self.connection.execute_query(self.FINDALL, ())

        for row in data:

            id = row[0]
            nombre = row[1]
            direccion = row[2]

            persona = Personas(id, nombre, direccion)

            personas.append(persona)

        return personas
