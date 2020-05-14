from tkinter import Tk,Label,Button,Frame
 
proceso=0
segundo = 0
minuto  = 0
hora = 0

def iniciar(decsegundo=0):
    
    global proceso
    global segundo
    global minuto
    global hora
 
    # mostramos la variable contandor
    time['text'] = str(hora) + ":" + str(minuto) + ":" + str(segundo) + ":" + str(decsegundo)

    if(decsegundo == 100):

        decsegundo = 0
        segundo = segundo + 1

    if(segundo == 60):

        segundo = 0
        minuto = minuto + 1
    

    if(minuto == 60):

        minuto = 0
        hora = hora + 1
 
    # hacemos un llamamient a la funcion mostrarContador pasando el
    # contador mas uno
    proceso=time.after(1, iniciar, (decsegundo+1))
 
def parar():
    
    global proceso
    global segundo
    global minuto
    global hora
    
    time.after_cancel(proceso)
 
root = Tk()
root.title('Cronometro')

 
time = Label(root, fg='red', width=20, font=("","18"))
time.pack()
 
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
frame.pack()
 
root.mainloop()

