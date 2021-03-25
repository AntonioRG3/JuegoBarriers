import threading
from random import randint
import numpy as np
import time

class Jugador(threading.Thread):
    def __init__(self,player, name):
        threading.Thread.__init__(self)
        self.jugador=player #Dorsal del jugador, 1, 2 o 3
        self.nombre=name #Nombre del jugador
        self.numero=0 #Iniciamos la variable del número del jugador

    def run(self):
        while(1):
            self.numero=randint(0,100) #El jugador escoge el número aleatorio
            bdirector.wait() #El director espera a que los 3 jugadores hayan obtenido un número
            bjugadores.wait() #Los jugadores esperan a que el director nos dé el número ganador
            if(director.num_ganador==self.numero): #Si mi número era el ganador, imprimo lo siguiente por pantalla
                print("Soy el "+self.nombre+" y he ganado con el número: " + str(self.numero))
            else: #Si mi número no era el ganador, imprimo lo siguiente por pantalla
                print("Soy el "+self.nombre+" y he perdido con el "+str(self.numero)+", el ganador ha sido el número: "+str(director.num_ganador))
            time.sleep(5)#Dejo 5 segundos entre partida y partida para cotejar el resultado

class Director(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.nombre=name #Nombre del director
        self.numeros=list(range(3)) #Lista donde meter los 3 números de los jugadores
        self.num_ganador=-1 #Iniciamos la variable donde indicar el número ganador
    def run(self):
        while(1):
            bdirector.wait() #El director espera a que los 3 jugadores hayan obtenido un número
            self.consigo_los_numeros() #Meto los 3 números en la variable lista interna del director
            self.num_ganador=self.numero_victorioso() #Obtengo el número victorioso
            bjugadores.wait() #Los jugadores esperan a la decisión del director
        
    def consigo_los_numeros(self): #Relleno la lista con los números de los jugadores
        self.numeros[0]=jugador1.numero
        self.numeros[1]=jugador2.numero
        self.numeros[2]=jugador3.numero

    def numero_victorioso(self): #Si uno de los números es mayor que los otros dos, devuelvo ese
        if((self.numeros[0]>self.numeros[1])and(self.numeros[0]>self.numeros[2])):
            return self.numeros[0]
        elif((self.numeros[1]>self.numeros[0])and(self.numeros[1]>self.numeros[2])):
            return self.numeros[1]
        else:
            return self.numeros[2]


#Creamos los jugadores
jugador1=Jugador(1,"jugador 1")
jugador2=Jugador(2,"jugador 2")
jugador3=Jugador(3,"jugador 3")

#Creamos al director
director=Director("Director")

#Creamos dos barreras
bjugadores=threading.Barrier(4) 
bdirector=threading.Barrier(4)  

jugador1.start()
jugador2.start()
jugador3.start()

director.start()