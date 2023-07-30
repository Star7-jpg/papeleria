from .db import get_connection

mydb = get_connection()

class User:

    def __init__(self, nombre, ape_paterno, ape_materno, nom_usuario, contrasenia, id_usuario=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.nom_usuario = nom_usuario
        self.contrasenia = contrasenia
        
    def save(self):
        # Create a New Object in DB
        if self.id_usuario is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO user(nombre, ape_paterno, ape_materno, nom_usuario, contrasenia) VALUES(%s,%s,%s,%s,%s)"
                val = (self.nombre, self.ape_paterno, self.ape_materno, self.nom_usuario, self.contrasenia)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_usuario = cursor.lastrowid
                return self.id_usuario
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE user SET nombre = %s, ape_paterno = %s, ape_materno = %s, nom_usuario = %s, contrasenia = %s WHERE id_usuario = %s"
                val = (self.nombre, self.ape_paterno, self.ape_materno, self.nom_usuario, self.contrasenia, self.id_usuario)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_usuario
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM user WHERE id_usuario = { self.id_usuario }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_usuario
            
    @staticmethod
    def get(id_usuario):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, ape_paterno, ape_materno, nom_usuario, contrasenia FROM user WHERE id_usuario = { id_usuario }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            nombre = User(result["nombre"], result["ape_paterno"], result["ape_materno"], result["nom_usuario"], result["contrasenia"], id_usuario)
            return nombre
        
    @staticmethod
    def get_all():
        user = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_usuario, nombre, ape_paterno, ape_materno, nom_usuario, contrasenia FROM user"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                user.append(User(item["nombre"], item["ape_paterno"], item["ape_materno"],item["nom_usuario"],item["contrasenia"],item["id_usuario"]))
            return user
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_usuario) FROM user"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_usuario } - { self.nombre } - { self.ape_paterno } - { self.ape_materno } - { self.nom_usuario } - { self.contrasenia }"