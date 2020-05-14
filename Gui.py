from tkinter import Tk,Label,Button,Frame

proceso=0
segundos = 0
minutos = 0
horas = 0

def iniciar(contador=0):


    global proceso
    global segundos
    global minutos
    global horas

    # mostramos la variable contandor
    time['text'] = str(horas) + ":" + str(minutos) + ":" + str(segundos) + ":" + str(contador)

    if(contador == 100):

        contador = 0
        segundos = segundos + 1

    if(segundos == 60):

        segundos = 0
        minutos = minutos + 1


    if(minutos == 60):

        minutos = 0
        horas = horas + 1

    # hacemos un llamamient a la funcion mostrarContador pasando el
    # contador mas uno
    proceso=time.after(1, iniciar, (contador+1))

def parar():

    global proceso
    global segundos
    global minutos
    global horas

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


