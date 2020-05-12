from threading import *
def hola():
  print("Hola")
def segundo():
  cont = 10
  segundos = 0
  while(cont != 0):
    print(segundos)
    segundos += 1
    cont -= 1
    if(cont==1):
      cont = 10
    if(segundos==60):
      segundos=0
      t = Timer(0.1,hola)
      t.start()
      t = Timer(0.1,hola)
      t.start()
def para():
  print("sopas")
def reiniciar():
  print("me lleva el demonio")

# Creacion del hilo
t = Timer(1,segundo)   # Timer() recibe como primer parámetro el intervalo de tiempo que será usado
                       # y como segundo parámetro la función a ejecutar. También recibe como 3er parámetro
# Ejecución del Hilo   # argumentos (args) y como 4to parametro argumentos de palabras clave (kwargs)
t.start()              # Por defecto, ambos tienen como valor 'None'

