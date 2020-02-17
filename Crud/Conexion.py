import psycopg2


class Conexion:
    __instance = None
    conn = None
    cursor = None

    def __init__(self):
        self.conn = psycopg2.connect(
            database="crud",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432",
        )

        Conexion.__instance = self

    @staticmethod
    def get_instance():
        if Conexion.__instance is None:
            Conexion()
        return Conexion.__instance

    def execute_update(self, sql, data):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql, data)
            self.conn.commit()
            return True
        except Exception as ex:
            print(ex.args)
            self.conn.rollback()
            return False
        finally:
            self.cursor.close()

    def execute_query(self, sql, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql, id)
            return self.cursor.fetchall()
        finally:
            self.cursor.close()