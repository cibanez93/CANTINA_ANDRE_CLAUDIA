import sqlite3

conn=sqlite3.connect("cantina_db.db") # Indicamos la ruta donde queremos conectarnos
cursor=conn.cursor #inicializar una conexión

def crear_usuario(nombre,apellido,correo_electronico,contraseña):
    try:
        cursor.execute("INSERT INTO usuarios (nombre,apellido,correo_electronico,contraseña) VALUES (?,?,?,?)") #consulta de SQL
        conn.commit() # confirmar la conexión
        return True # significa para indicarle que salio todo bien la inserccion de datos
    except sqlite3.Integrity.Error: 
        return False #Significa para indicarle que salio todo mal!!!

def modificar_usuario(id_usuario,nombre,apellido,correo_electronico,contraseña)
    try:
        cursor.execute("UPDATE usuarios SET id nombre=?,apellido=?,correo_electronico=?,contraseña=? WHERE id = ?")
        conn.commit() # confirmar la conexión
        return True # significa para indicarle que salio todo bien la inserccion de datos
    except sqlite3.Integrity.Error: 
        return False #Significa para indicarle que salio todo mal!!!

def eliminar_usuario(id_usuario):
    try:
        cursor.execute("DELETE FROM usuario WHERE id = ?")
        conn.commit()
        return True
    except sqlite3.Integrity.Error:
        return False
    
def crear_reservar(id_usuario,fecha,hora,silla):
    try:
        cursor.execute("INSERT INTO reservas (id_usuario,fecha,hora,silla) VALUES (?,?,?,?)")
        conn.commit()
        return True
    except sqlite3.Integrity.Error:
        return False 

def modificar_reservar(id_reserva,hora,silla):
    try:
        cursor.execute("UPDATE reservas SET hora=?,silla=? WHERE id = ?")
        conn.commit()
        return True
    except sqlite3.Integrity.Error:
        return False    

def eliminar_reservar(id_reserva,hora,silla):
    try:
        cursor.execute("DELETE FROM reservas WHERE id = ?")
        conn.commit()
        return True
    except sqlite3.Integrity.Error:
        return False  

        