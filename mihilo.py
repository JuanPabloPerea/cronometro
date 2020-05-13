import threading
import time

decsegundos = 0
segundos = 0
minutos = 0
horas = 0


cont = True


while(cont == True):
    
    if(decsegundos == 100):

        decsegundos = 0
        segundos = segundos + 1

    if(segundos == 60):

        segundos = 0
        minutos = minutos + 1
    

    if(minutos == 60):

        minutos = 0
        horas = horas + 1
            

    decsegundos = decsegundos + 1
                
    time.sleep(0.1)
    
    print(segundos)



print(decsegundos)
print(segundos)
print(minutos)
print(horas)
