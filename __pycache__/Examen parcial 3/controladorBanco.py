from tkinter import messagebox
import sqlite3

class controladorBD:
    
    def __init__ (self):
        pass
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub/POO182/__pycache__/Examen parcial 3/BD_BANCO2.db")
            print ("conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print ("no se pudo conectar")
            
    def Guardar (self, nom, cuenta, saldo):
        #llamar metodo conexion
        conx = self.conexionBD()
        
        #validar vacíos
        if (nom == "" or cuenta == "" or saldo == ""):
            messagebox.showwarning ("Warning", "Formulario incompleto")
            conx.close()
            
        else:
            cursor = conx.cursor()
            datos = (nom, cuenta, saldo)
            sqlInsert = "insert into TBCuentas(Nombre, Cuenta, Saldo) values (?, ?, ?)"
            
            #ejecutar insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Registro guardado")
            
    def consultarRegistros(self):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        try: 
                #4. Preparar lo necesario
            cursor = conx.cursor()
            sqlSelect = "select * from TBCuenta"
                
                #5. Ejecutar y cerrar conexión
            cursor.execute(sqlSelect)
            RSregistro = cursor.fetchall()
            conx.close()
            return RSregistro
                
        except sqlite3.OperationalError:
            print ("Error de consulta todos los usuarios")
            
    def ActualizarNom(self, id, nom):
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
                sqlSelect = "UPDATE TBCuentas SET Nombre = ? WHERE IDCuenta = ?"
                actualizar = (nom, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar nombre")
    
    def ActualizarSaldo(self, id, saldo):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or saldo == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y nombre")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE TBCuenta SET Saldo = ? WHERE IDCuenta = ?"
                actualizar = (saldo, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar nombre")
                
    def ActualizarCuenta(self, id, cuenta):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or cuenta == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y nombre")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE TBCuentas SET Cuenta = ? WHERE IDCuenta = ?"
                actualizar = (cuenta, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error para actualizar nombre")
    