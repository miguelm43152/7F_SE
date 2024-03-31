print( " Metodos de ordenamiento " )

import random
import math

######################### Clases del programa ############################

class MetodosOrdenamiento():
    
    lista = []

    def __init__(self,tamagno, minval, maxval):

        for i in range( tamagno ):
            self.lista.append( random.randrange(minval,maxval) )

    def actualizaLista(self, listaEntrada):
        for i in range( len( listaEntrada) ):
            self.lista[i] = listaEntrada[i]

    def dameLista(self):
        return self.lista

    ### metodo de ordenamiento burbuja, descomentar print para ver su funcionamiento ###
    def burbuja(self):
        n = len( self.lista )
        for i in range( n - 1, 0 , -1 ):
#            print( " ------- valor de i: " + str(i) + " --------")
            for j in range( 0, i, 1): 
                    if self.lista[ j ] > self.lista[ j + 1 ]: # si el elemento de la derecha es menor que el de la izquierda
                        # entonces lo movemos a la izquierda
                        temp = self.lista[j]
                        self.lista[ j ] = self.lista[ j + 1 ]
                        self.lista[ j + 1 ] = temp
#                    print( "valor de j: " + str(j) + " donde: " + str(self.lista) )


    ### metodo de ordenamiento insercion, descomentar print para ver su funcionamiento ###
    def insercion(yo):
        n = len( yo.lista )
        for i in range( 1, n, 1 ): #empezamos a contar a partir del indice 1 porque el 0 no tiene nada a su izquierda para comparar.
            #print( " ------- valor de i: " + str(i) + " --------")
            for j in range( i, 0, -1 ):
                if yo.lista[j] < yo.lista[j-1]:
                    temp = yo.lista[j]
                    yo.lista[ j ] = yo.lista[ j - 1 ]
                    yo.lista[ j - 1 ] = temp
                else:
                    break;
                
                #print( yo.lista)
                #print( "valor de j: " + str(j) + " donde: " + str(yo.lista) )


    ### metodo de ordenamiento seleccion, descomentar print para ver su funcionamiento ###

    def seleccion(s):
        n = len( s.lista)

        for i in range( n-1 ):
            minval = s.obtenMinimo( s.lista[(i):] ) + i
            temp = s.lista[i]
            s.lista[i] = s.lista[minval]
            s.lista[minval] = temp   

    def obtenMinimo( self, lista ):
        n = len( lista)
        minval = lista[0]
        index = 0
        #print(lista)
        for i in range( n ):
            if lista[i] < minval:
               minval = lista[i]
               index = i
        return index

    @staticmethod       # Todo metodo que use recurrencia DEBE de ser estatico
    def mergeSort( inputList ):
        longitud = len( inputList )

        if( longitud < 2 ):
            return

        mitadIzquierda = []
        mitadDerecha = []

        mitad = math.floor( longitud / 2 )

        for i in range( 0, mitad, 1 ):
            mitadIzquierda.append(  inputList[i] )
        #print( mitadIzquierda )
        for i in range( mitad, longitud, 1 ):
            mitadDerecha.append( inputList[i] )
        #print( mitadDerecha )

        MetodosOrdenamiento.mergeSort( mitadIzquierda )
        MetodosOrdenamiento.mergeSort( mitadDerecha )

        MetodosOrdenamiento.merge( inputList, mitadIzquierda, mitadDerecha)
        #print( "orden: " + str(lista))

    @staticmethod
    def merge( lista ,mitadIzquierda, mitadDerecha):
        longitudIzquierda = len( mitadIzquierda )
        longitudDerecha = len( mitadDerecha )
        longitud = len(lista)

        i = 0; j = 0; k = 0

        while( i < longitudIzquierda and j < longitudDerecha ):
            #print( i < longitudIzquierda and j < longitudDerecha  )
            if(  mitadIzquierda[i] <= mitadDerecha[j] ):
                #print(  mitadIzquierda[i] )
                lista[k] = mitadIzquierda[i]
                i = i + 1
                k = k + 1
            else:
                lista[k] = mitadDerecha[j]
                j = j + 1
                k = k + 1

        while( i < longitudIzquierda ):
            lista[k] = mitadIzquierda[i]
            i = i + 1
            k = k + 1

        while( j < longitudDerecha ):
            lista[k] = mitadDerecha[j]
            j = j + 1
            k = k + 1
######################### Inicio del programa ############################

sort =  MetodosOrdenamiento( 10,0,100 )

print( sort.dameLista() )
#sort.actualizaLista( MetodosOrdenamiento.mergeSort(  sort.dameLista()  ) )
#print( sort.dameLista() )
A = [1,2,3]
B = [3,5,7]
#print( len( A ) )
MetodosOrdenamiento.mergeSort( sort.dameLista()  )
print( sort.dameLista() )

#print( A[0] <= B[0]  )
#print( C)