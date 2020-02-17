from tkinter import *
from tkinter import ttk

from Personas import Personas
from DaoPersonas import DaoPersonas
class Main:

    def __init__(self, window):
        self.wind = window
        self.wind.title("Personas")

        frame = LabelFrame(self.wind, text='CRUD Personas')
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        Label(frame, text='Id: ').grid(row=1, column=0)
        self.id = Entry(frame)
        self.id.grid(row=1, column=1)

        Label(frame, text='Nombre').grid(row=2, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=2, column=1)

        Label(frame, text='direccion: ').grid(row=3, column=0)
        self.direcc = Entry(frame)
        self.direcc.grid(row=3, column=1)

        ttk.Button(frame, text='Agregar persona', command=lambda: self.add()).grid(row=6, columnspan=2, sticky=W + E)
        ttk.Button(frame, text='Eliminar persona', command=lambda: self.delete()).grid(row=7, columnspan=2, sticky=W + E)
        ttk.Button(frame, text='Actualizar persona', command=lambda: self.update()).grid(row=8, columnspan=2, sticky=W + E)

        self.tabla = ttk.Treeview(height=10, columns=("#0", "#1"))
        self.tabla.grid(row=4, column=0, columnspan=2)
        self.tabla.heading('#0', text='Id', anchor=CENTER)
        self.tabla.heading('#1', text='Nombre', anchor=CENTER)
        self.tabla.heading('#2', text='Direccion', anchor=CENTER)
        self.fill_table()

    def update(self):
        ref = DaoPersonas()
        persona = Personas(self.id.get(), self.nombre.get(), self.direcc.get())

        ref.update(persona)

        self.clear()
        self.fill_table()

    def delete(self):
        ref = DaoPersonas()

        ref.delete(self.id.get())

        self.clear()
        self.fill_table()

    def add(self):
        ref = DaoPersonas()
        persona = Personas(self.id.get(), self.nombre.get(), self.direcc.get())

        ref.insert(persona)

        self.clear()
        self.fill_table()

    def fill_table(self):
        personas = DaoPersonas().find_all()

        for persona in personas:
            self.tabla.insert('', 'end', text=persona.id, values=(persona.nombre, persona.direccion))

    def clear(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)


if __name__ == '__main__':
    window = Tk()
    aplicacion = Main(window)
    window.mainloop()
