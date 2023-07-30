from .db import get_connection

mydb = get_connection()

class Product:

    def __init__(self, nombre, precio, descripcion, id_marca, id_categoria, id_producto=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.id_marca = id_marca
        self.id_categoria = id_categoria
        
    def save(self):
        # Create a New Object in DB
        if self.id_producto is None:
            with mydb.cursor() as cursor:
                sql = "INSERT INTO product(nombre, precio, descripcion, id_marca, id_categoria) VALUES(%s,%s,%s,%s,%s)"
                val = (self.nombre, self.precio, self.descripcion, self.id_marca, self.id_categoria)
                cursor.execute(sql, val)
                mydb.commit()
                self.id_producto = cursor.lastrowid
                return self.id_producto
        # Update an Object
        else:
            with mydb.cursor() as cursor:
                sql = "UPDATE product SET nombre = %s, precio = %s, descripcion = %s, id_marca = %s, id_categoria = %s WHERE id_producto = %s"
                val = (self.nombre, self.precio, self.descripcion, self.id_marca, self.id_categoria, self.id_producto)
                cursor.execute(sql, val)
                mydb.commit()
                return self.id_producto
            
    def delete(self):
        with mydb.cursor() as cursor:
            sql = f"DELETE FROM product WHERE id_producto = { self.id_producto }"
            cursor.execute(sql)
            mydb.commit()
            return self.id_producto
            
    @staticmethod
    def get(id_producto):
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT nombre, precio, descripcion, id_marca, id_categoria FROM product WHERE id_producto = { id_producto }"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
            nombre = Product(result["nombre"], result["precio"], result["descripcion"], result["id_marca"], result["id_categoria"], id_producto)
            return nombre
        
    @staticmethod
    def get_all():
        product = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = f"SELECT id_producto, nombre, precio, descripcion, id_marca, id_categoria FROM product"
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result:
                product.append(Product(item["nombre"], item["precio"], item["descripcion"],item["id_marca"],item["id_categoria"],item["id_producto"]))
            return product
    
    @staticmethod
    def count_all():
        with mydb.cursor() as cursor:
            sql = f"SELECT COUNT(id_producto) FROM product"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0]
        
    def __str__(self):
        return f"{ self.id_producto } - { self.nombre } - { self.precio } - { self.descripcion } - { self.id_marca } - { self.id_categoria }"