from tkinter import *
#se crea un objeto de tipo Tk
window = Tk()

# Nombre que va a llevar la ventana
window.title("primera Ventana")

# se da dimensiones a la ventyana
window.geometry('350x200')

# objeto labe,(en la ventana en que va, texto)
lbl = Label(window, text="Hello")

# posicion de el label
lbl.grid(column=0,row=0)

def clicked():
    lbl.configure(text="button was clicked")

# objeto boton,(en ventana, la accion, el resultado haber oprimido el boton)
btn = Button(window, text="click", command=clicked)

# posicion en la ventana
btn.grid(column=1, row=180)

# llamado de la ventana, sin esta linea de codigo el usuario no ve nada
window.mainloop() 

