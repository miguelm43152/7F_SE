#colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]

#print( '\nEl color ' ,colores[3], " se encuentra en la posición 3\n" )

import time
import os

elementos = ["a) carros\n", "b) futbol\n", "c) videojuegos\n", "salir\n"]
respuestas = ["Los carros tienen 4 ruedas", "me encanta el futbol!!!", "Soy malo en los videojuegos :0000", "salir\n"]

input( "Hola, ¿Como te encuentras hoy?\n")

print( "Me alegro mucho :)\n")
time.sleep(1) # Sleep for 1 seconds

pregunta = "¿De que te gustaria hablar hoy\n"

for x in range(len(elementos)):

    pregunta = pregunta + elementos[x]
respuesta = ''

#print(elementos[0][0:5])

while( respuesta != 's'):
    os.system("cls")
    pregunta = ""
    for x in range(len(elementos)):

        pregunta = pregunta + elementos[x]

    respuesta = input(pregunta)

    if respuesta == 's':
        pass
    elif len(respuesta) > 1:

        nuevoIndice = ""
        agregaInfo = ""

        nuevoIndice = ord( elementos[-2][0] ) + 1 #si la entrada es una c, entonces la salida es una d

        nuevoIndice = chr( nuevoIndice)

        nuevoElemento = nuevoIndice + ") " + respuesta + "\n"

        #elementos.append( nuevoElemento )
        elementos.insert(-1,nuevoElemento)
        
        agregaInfo = input( "no se de que me hablas, ¿puedes hablarme mas sobre ello?\n\n")

        #respuestas.append( agregaInfo )
        respuestas.insert(-1,agregaInfo)

    else:
        #print("no es s")
        for x in range(len(elementos)):
            
            if respuesta[0] == elementos[x][0]:
                print(respuestas[x] + "\n\n")
                
print("Hasta pronto!!!! :)\n\n\n")

