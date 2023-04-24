from tkinter import messagebox
import random
import tkinter as tk
from tkinter import ttk

class Generador:
        
    def Generador1(self, l, m, c):
        
        if (m == "si" and c == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
            q_list = [random.choice(valores) for i in range(l)]
            messagebox.showinfo("CONTRASEÑA", q_list)
            root = tk.Tk()
            root.title("CONTRASEÑA")
            root.geometry("200x100")
            text = tk.Entry(root)
            text.insert(0, q_list)
            text.place(x=37, y=45)
            root.mainloop()
            
        elif (m == "no" and c == "si"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz<=>@#%&+"
            q_list1 = [random.choice(valores) for i in range(l)]
            messagebox.showinfo("CONTRASEÑA", q_list1)
            root1 = tk.Tk()
            root1.title("CONTRASEÑA")
            root1.geometry("200x100")
            text1 = tk.Entry(root1)
            text1.insert(0, q_list1)
            text1.place(x=37, y=45)
            root1.mainloop()
            
        elif (m == "si" and c == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            q_list2 = [random.choice(valores) for i in range(l)]
            messagebox.showinfo("CONTRASEÑA", q_list2)
            root2 = tk.Tk()
            root2.title("CONTRASEÑA")
            root2.geometry("200x100")
            text2 = tk.Entry(root2)
            text2.insert(0, q_list2)
            text2.place(x=37, y=45)
            root2.mainloop()
            
        elif (m == "no" and c == "no"):
            valores = "0123456789abcdefghijklmnopqrstuvwxyz"
            q_list3 = [random.choice(valores) for i in range(l)]
            messagebox.showinfo("CONTRASEÑA", q_list3)
            root3 = tk.Tk()
            root3.title("CONTRASEÑA")
            root3.geometry("200x100")
            text3 = tk.Entry(root3)
            text3.insert(0, q_list3)
            text3.place(x=37, y=45)
            root3.mainloop()
    
    def Validar1 (self, l, m, c):
        if (m == "si" and c == "si" and l >= 8):
            messagebox.showinfo("CONTRASEÑA", "La contraseña es segura")
        elif (m == "no" and c == "si" and l >= 8):
            messagebox.showinfo("CONTRASEÑA", "La contraseña es media segura")
        elif (m == "si" and c == "no" and l >= 8):
            messagebox.showinfo("CONTRASEÑA", "La contraseña es media segura")
        elif (m == "no" and c == "no" and l < 8):
            messagebox.showinfo("CONTRASEÑA", "La contraseña no es segura")