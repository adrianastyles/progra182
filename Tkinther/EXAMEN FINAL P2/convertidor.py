from tkinter import messagebox

class Convertidor1:
    
    def RomanosAArabigo (self, nRomano):
        if (nRomano == ""):
            messagebox.showerror("Warning", "Ingrese un número")
        else:
            romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            op = 0
            for i in range(0, len(nRomano)):
                if (i == 0 or romanos[nRomano[i]] <= romanos[nRomano[i - 1]]):
                    op += romanos[nRomano[i]]
                else:
                    op += romanos[nRomano[i]] - 2 * romanos[nRomano[i - 1]]
            if (op <= 50):
                messagebox.showinfo ("Coversión exitosa", "El número es: " + str(op))
            else:
                messagebox.showerror("Warning", "Ingrese un número menor a 50")
            
    def ArabigoaRomano(self, nArabigo):
        if (nArabigo == ""):
            messagebox.showerror ("Warning", "Ingrese un número")
        else:
            m = ["", "M", "MM", "MMM"]
            c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
            x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  
            miles = m[nArabigo // 1000]
            centenas = c[(nArabigo % 1000) // 100]
            decimas = x[(nArabigo % 100) // 10]
            unidades = i[nArabigo % 10]
  
            s = (miles + centenas + decimas + unidades)
            
            if (nArabigo <= 50):
                messagebox.showinfo("Conversión exitosa", "El número es: " + s)
            else:
                messagebox.showerror("Warning", "Ingrese un número menor a 50")