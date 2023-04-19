from tkinter import messagebox
import sqlite3


class controladorBDBanco:
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub/POO182/__pycache__/Examen parcial 3/BD_BANCO1.db")
            print ("conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print ("No se pudo conectar")
    
    def Guardar (self, nom, nocuenta, saldo):
        
        conx = self.conexionBD()
        
        if (nom == "" or nocuenta == "" or saldo == ""):
            messagebox.showwarning ("Warning", "Formulario incompleto")
            conx.close()
            
        else:
            cursor = conx.cursor()
            datos = (nom, nocuenta, saldo)
            sqlInsert = "insert into TBCuentas (Nombre, NoCuenta, Saldo) values (?, ?, ?)"
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Registro guardado")