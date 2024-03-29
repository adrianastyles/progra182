from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__ (self):
        pass
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub\POO182/__pycache__/SQLite/database15.db")
            print ("conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print ("no se pudo conectar")
            
    def GuardarUsuario (self, nom, cor, cont):
        #llamar metodo conexion
        conx = self.conexionBD()
        
        #validar vacíos
        if (nom == "" or cor == "" or cont == ""):
            messagebox.showwarning ("Warning", "Formulario incompleto")
            conx.close()
            
        else:
            #realizar insert a la base de datos
            #preparar variables
            cursor = conx.cursor()
            conH = self.encriptarContra(cont)
            datos = (nom, cor, conH)
            sqlInsert = "insert into tbregistrados(nombre, correo, contraseña) values (?, ?, ?)"
            
            #ejecutar insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Usuario guardado")
            
    def encriptarContra (self, cont):
        #preparamos contraseña y la sal para hash
        conPlana = cont
        conPlana = conPlana.encode() #convertir a byte
        sal = bcrypt.gensalt()
        
        #encriptamos
        conHa = bcrypt.hashpw(conPlana, sal)
        print (conHa)
        
        #regresamos la contraseña encriptada
        return conHa
    
    def consultarUsuario(self, id):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == ""):
            messagebox.showwarning ("Warning", "Ingresa un ID")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "select * from tbregistrados where id = " + id
                
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                return RSusuario
                
            except sqlite3.OperationalError:
                print ("Error de consulta")
                
    def consultarTodosLosUsuarios(self):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        try: 
                #4. Preparar lo necesario
            cursor = conx.cursor()
            sqlSelect = "select * from tbregistrados"
                
                #5. Ejecutar y cerrar conexión
            cursor.execute(sqlSelect)
            RSusuario = cursor.fetchall()
            conx.close()
            return RSusuario
                
        except sqlite3.OperationalError:
            print ("Error de consulta todos los usuarios")
    
    def ActualizarUsuariosNom(self, id, nom):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or nom == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y nombre")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE tbregistrados SET nombre = ? WHERE id = ?"
                actualizar = (nom, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar nombre")
    
    def ActualizarUsuariosCor(self, id, cor):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or cor == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y correo")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE tbregistrados SET correo = ? WHERE id = ?"
                actualizar = (cor, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar correo")
                
    def ActualizarUsuariosCon(self, id, con):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or con == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y contraseña")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                conH = self.encriptarContra(con)
                sqlSelect = "UPDATE tbregistrados SET contraseña = ? WHERE id = ?"
                actualizar = (conH, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar contraseña")
            
    def EliminarUsuarios(self, id):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == ""):
            messagebox.showwarning ("Warning", "Ingresa un ID")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "DELETE FROM tbregistrados WHERE id = "+ id
                
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error")