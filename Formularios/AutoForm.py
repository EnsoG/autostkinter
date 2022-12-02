from cProfile import label
from distutils.cmd import Command
from email import message
from mailbox import mbox
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from Clases.AutoClass import Auto
from Formularios.PersonaForm import PersonaForm

class AutoForm():
    #constructor que genera la ventana o formulario
    def __init__(self):        
        self.auto = Auto()
        #generar el formulario
        self.ventanaAuto = tk.Tk()
        #titulo de la ventana
        self.ventanaAuto.title('Formulario Autos')
        #tamaño de la ventana
        self.ventanaAuto.geometry('800x600')
        self.agregar()
        self.listar_autos()
        #asignar al tree view el evento double click para seleccionar
        self.tabla.bind('<Double-1>',self.seleccionar_click)
        self.menu_opciones()
        self.ventanaAuto.config(menu=self.menu)
        #mostrar la ventana 
        self.ventanaAuto.mainloop()
    
    def agregar(self):
        #titulo para el formulario - fila 0
        self.lblTitulo = ttk.Label(text='Gestión Autos',font=('Roboto',28))
        self.lblTitulo.grid(column=1,row=0,padx=5,pady=10)

        #patente fila 1 - label - entry
        ##label
        self.lblPatente = ttk.Label(text='Patente',font=('Arial',16))
        self.lblPatente.grid(column=0,row=1,padx=5,pady=5)
        ###Entry
        self.patente = tk.StringVar() #es una variable de tipo string que pertenece a Tkinter
        self.entryPatente = ttk.Entry(textvariable=self.patente)
        self.entryPatente.grid(column=1,row=1,padx=5,pady=5,ipadx=30)

        #marca fila 2 - label y entry
        ##label
        self.lblMarca = ttk.Label(text='Marca',font=('Arial',16))
        self.lblMarca.grid(column=0,row=2,padx=5,pady=5)
        ###Entry
        self.marca = tk.StringVar() #es una variable de tipo string que pertenece a Tkinter
        self.entryMarca = ttk.Entry(textvariable=self.marca)
        self.entryMarca.grid(column=1,row=2,padx=5,pady=5,ipadx=30)

        #modelo fila 3 - label y entry
        ##label
        self.lblModelo = ttk.Label(text='Modelo',font=('Arial',16))
        self.lblModelo.grid(column=0,row=3,padx=5,pady=5)
        ###Entry
        self.modelo = tk.StringVar() #es una variable de tipo string que pertenece a Tkinter
        self.entryModelo = ttk.Entry(textvariable=self.modelo)
        self.entryModelo.grid(column=1,row=3,padx=5,pady=5,ipadx=30)

        #botón para guardar
        self.btnGuardar = ttk.Button(text='Guardar',command=self.guardar)
        self.btnGuardar.grid(column=3,row=1,padx=5,pady=5)
        #botón limpiar
        self.btnLimpiar = ttk.Button(text='Limpiar',command=self.limpiar)
        self.btnLimpiar.grid(column=3,row=2,padx=5,pady=5)
        #botón eliminar
        self.btnEliminar = ttk.Button(text='Eliminar',command=self.eliminar)
        self.btnEliminar.grid(column=4,row=1,padx=5,pady=5)
        self.btnEliminar.config(state='disabled')
        #botón eliminar
        self.btnModificar = ttk.Button(text='Modificar',command=self.modificar)
        self.btnModificar.grid(column=4,row=2,padx=5,pady=5)
        self.btnModificar.config(state='disabled')
        #treeview o tabla
        self.tabla = ttk.Treeview(columns=('#0','#1'))
        #self.tabla.grid(column=1,row=5)
        #place sirve para posicionar los elementos dentro del formulario
        self.tabla.place(x=5,y=180)
        #encabezados a la tabla o treeview
        self.tabla.heading('#0',text='PATENTE')
        #ancho de la columna
        self.tabla.column('#0',width=90)
        self.tabla.heading('#1',text='MARCA')
        self.tabla.heading('#2',text='MODELO')
        
    def guardar(self):
        error = ''
        if self.patente.get() == '':
            error += 'Debe ingresar Patente \n'
        elif self.auto.verificar(self.patente.get()):
            error += 'La patente ya está ingresada \n'
        if self.marca.get()=='':
            error += 'Debe ingresar Marca \n'
        if self.modelo.get() == '':
            error += 'Debe ingresar Modelo'
        if error != '':
            mb.showerror('Error',error)
        else:
            self.auto.add(self.patente.get(),self.marca.get(),self.modelo.get())
            mb.showinfo('Guardado','El auto se ha registrado con éxito!!!')
            self.limpiar()
            self.listar_autos()
    
    def limpiar(self):
        self.patente.set('')
        self.marca.set('')
        self.modelo.set('')
        #habilita el entry patente
        self.entryPatente.config(state='enabled')
        self.btnEliminar.config(state='disabled')
        self.btnModificar.config(state='disabled')

    def listar_autos(self):
        #trae la lista de autos desde la clase 
        lista_autos = self.auto.get_all()
        #captura los registros en el treeview
        registros = self.tabla.get_children()
        #for recorre los registro del treeview y luego los elimina
        for r in registros:
            self.tabla.delete(r)
        #for para recorrer la lista de autos y mostrarla en el treeview
        for a in lista_autos:
            self.tabla.insert('',0,text=a[0],values=(a[1],a[2]))    
     
    def seleccionar_click(self,event):
        #indica que elementos de treeview selecciona
        elemento = self.tabla.identify('item',event.x,event.y)
        #asigna al entry patente el elemento seleccionado 
        self.patente.set(self.tabla.item(elemento,'text'))
        self.marca.set(self.tabla.item(elemento,'values')[0])
        self.modelo.set(self.tabla.item(elemento,'values')[1])
        #bloquea la patente para que no se pueda escribir
        self.entryPatente.config(state='disabled')
        self.btnEliminar.config(state='enabled')
        self.btnModificar.config(state='enabled')
    def eliminar(self):
        if mb.askyesno(message='¿Está seguro de eliminar la patente ' + self.patente.get() 
        + ' ?',title='ELIMINAR'):
            self.auto.delete(self.patente.get())
            mb.showinfo('Eliminación','El registro se ha eliminado con éxito')
            self.limpiar()
            self.listar_autos()

    def modificar(self):
        error = ''
        if self.marca.get()=='':
            error += 'Debe ingresar Marca \n'
        if self.modelo.get() == '':
            error += 'Debe ingresar Modelo'
        if error != '':
            mb.showerror('Error',error)
        else:
            if mb.askyesno(message='¿Está seguro de modificar la patente ' + self.patente.get() 
            + ' ?',title='ELIMINAR'):
                self.auto.update(self.patente.get(),self.marca.get(),self.modelo.get())
                mb.showinfo('Modificar','El registro se ha modificado con éxito')
                self.limpiar()
                self.listar_autos()
    
    def menu_opciones(self):
        #instancia la barra de menú de tkinter
        self.menu = Menu(self.ventanaAuto)
        #indicamos donde estará el menú
        #menú inicio
        self.menuinicio = Menu(self.menu,tearoff=0)
        self.menuinicio.add_command(label='Ir a Personas',command=self.ir_persona)
        self.menuinicio.add_command(label='Ir a Asignación',command=self.ir_asignacion)
        self.menuinicio.add_command(label='Salir',command=self.salir)
        self.menu.add_cascade(label='Inicio',menu=self.menuinicio)
        #menú ayuda
        self.menuayuda = Menu(self.menu,tearoff=0)
        self.menuayuda.add_command(label='Acerca de',command=self.mensaje)
        self.menuayuda.add_command(label='Limpiar',command=self.limpiar)
        self.menu.add_cascade(label='Ayuda',menu=self.menuayuda)
    
    def salir(self):
        if mb.askyesno('SALIR','¿Esta seguro que desea salir de la aplicación?'):
            self.ventanaAuto.destroy()

    def mensaje(self):
        mb.showinfo('Información','Aplicación desarrollada en POO - por los alumnos de primer año')
    def ir_persona(self):
        self.ventanaAuto.destroy()
        self.formPersona = PersonaForm()
    def ir_asignacion(self):
        pass