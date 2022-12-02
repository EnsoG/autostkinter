from dataclasses import dataclass
from conexion import DataBase

class Auto():
    #método o función para añadir un nuevo auto
    def add(self,patente,marca,modelo):
        #abre la conexión a base de datos
        db = DataBase()
        #consulta sql que permite guardar un nuevo auto
        query = "INSERT INTO automovil VALUES('{}','{}','{}')"\
                .format(patente,marca,modelo)
        #ejecutar la consulta
        db.cursor.execute(query)
        #permite guardar los cambios en la base de datos
        db.conn.commit()
        #cerrar la conexión a la base de datos
        db.conn.close()
    
    def get_all(self):
        db = DataBase()
        query = "SELECT * FROM automovil"
        db.cursor.execute(query)
        db.conn.close()
        #devolver todos los datos resultantes de la consulta
        return db.cursor.fetchall()
    def delete(self,patente):
        db = DataBase()
        query = "DELETE FROM automovil WHERE patente='{}'".format(patente)
        db.cursor.execute(query)
        db.conn.commit()
        db.conn.close()

    def update(self,patente,marca,modelo):
        db = DataBase()
        query = "UPDATE automovil SET marca ='{}', modelo='{}' WHERE patente = '{}'" \
            .format(marca,modelo,patente)
        db.cursor.execute(query)
        db.conn.commit()
        db.conn.close()
    
    def verificar(self,patente):
        db = DataBase()
        query = f"SELECT * FROM automovil WHERE patente ='{patente}'"
        db.cursor.execute(query)
        auto = db.cursor.fetchone()
        db.conn.close()
        if auto:
            return True
        return False