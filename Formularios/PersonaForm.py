
import tkinter as tk
from tkinter import ttk

class PersonaForm():
    def __init__(self):      
        self.ventanaPersona = tk.Tk()
        self.ventanaPersona.title('Formulario Personas')
        self.ventanaPersona.geometry('800x600')
        self.agregar()
        self.ventanaPersona.mainloop()
    
    def agregar(self):
        self.lblTitulo = ttk.Label(text='Gestión Personas',font=('Roboto',28))
        self.lblTitulo.grid(column=1,row=0,padx=5,pady=10)