import tkinter as tk


class ControlIngresosEgresosApp:
    def __init__(self):
        self.ingresos = 0
        self.egresos = 0
        
        self.root = tk.TK()
        self.root.title("Ingresos y Egresos Master Car")
        
#creacion de widgets
        self.ingresos_label = tk.Label(self.root, text='Ingresos')
        self.ingresos_entry = tk.Entry(self.root)
        self.ingresos_button = tk.Button(self.root, text='Registrar Ingreso', command=self.registrar_ingresos)
        
        self.egresos_label = tk.Label(self.root, text='Egresos')
        self.egresos_entry = tk.Entry(self.root)
        self.egresos_button = tk.Button(self.root, text='Registrar Egreso', command=self.registrar_egresos)
        
        self.balance_label = tk.Label(self.root, text='balance: $0')
        
#posicionar widgets
        
        self.ingresos_label.grid(row=0, column=0)
        self.ingresos_entry.grid(row=0, column=1)
        self.ingresos_button.grid(row=0, column=2)
        
        self.egresos_label.grid(row=1, column=0)
        self.egresos_entry.grid(row=1, column=1)
        self.egresos_button.grid(row=1, column=2)
        
        self.balance_label.grid(row=2, columnspan=3)
        
    def registrar_ingreso(self):
        ingreso = float(self.ingresos_entry.get())
        self.ingreso += ingreso
        self.actualizar_balance()
        
    def registrar_egreso(self):
        egreso = float(self.egresos_entry.get())
        self.egresos += egreso
        self.actualizar_balance()
        
    def actualizar_balance(self):
        balance = self.ingresos - self.egresos
        self.balance_label.config(text=f'Balance: ${balance:.2f}')

    def run(self):
        self.root.mainloop()
        
if __name__ == '_main_':
    app = ControlIngresosEgresosApp()
    app.run()
                         
                                             