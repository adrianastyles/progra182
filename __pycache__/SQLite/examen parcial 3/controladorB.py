from tkinter import messagebox
import sqlite3


class controladorBDBanco:
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub/POO182/__pycache__/SQLite/examen parcial 3/BD_Banco.db")
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
            sqlInsert = "insert into TBCUENTAS (Nombre, NCuenta, Saldo) values (?, ?, ?)"
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Registro guardado")