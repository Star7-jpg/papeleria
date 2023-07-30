from .db import get_connection

mydb = get_connection()

class Brand:

    def __init__(self, nombre, id_marca=None):
        self.id_marca = id_marca
        self.nombre = nombre
        
    def save(self):
        # Create a New Object in DB
        if self.id_marca is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO brand(nombre) VALUES(%s)"
                val = (self.nombre)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_marca = cursor.lastrowid
                return self.id_marca
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE brand SET nombre = %s WHERE id_marca = %s"
                val = (self.nombre, self.id_marca)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_marca
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM brand WHERE id_marca = { self.id_marca }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_marca
            
    @staticmethod
    def get(id_marca):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre FROM brand WHERE id_marca = { id_marca }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            nombre = Brand(result["nombre"], id_marca)
            return nombre
        
    @staticmethod
    def get_all():
        brand = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_marca, nombre FROM brand"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                brand.append(Brand(item["nombre"], item["id_marca"]))
            return brand
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_marca) FROM brand"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_marca } - { self.nombre }"