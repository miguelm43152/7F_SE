
CLAYMORE = "Claymore"
SPEAR = "Spear"
SWORD = "Sword"

class Arma:
            
        def __init__(self, nombre, ataque, tipo):
  
            self.nombre = nombre
            self.ataque = ataque
            self.tipo = tipo;


        def imprime_datos(self):
            print('Nombre:', self.nombre, '\nAtaque:', self.ataque, "\ntipo", self.tipo)

        def get_ataque(self):
            return self.ataque
        
        def get_tipo(self):
            return self.tipo

arma1 = Arma( "Lynel sword", 24, SWORD)

arma2 = Arma( "Knights Halverd", 13, SPEAR)

arma3 = Arma( "Soldiers Broadsword", 14, SWORD)

arma4 = Arma( "ThunderSpear", 22, SPEAR)

arma5 = Arma( "Royal Claymore", 52, CLAYMORE)

lista = []
lista.append( arma1 )
lista.append( arma2 )
lista.append( arma3 )
lista.append( arma4 )
lista.append( arma5 )


print( "Lista desordenada:\n")
for i in range(len(lista)): ## empieza desde el numero 1 hasta el 10 con incrementos de 1
    lista[i].imprime_datos()



def bubbleSort_ataque(nlist):
    for passnum in range( len(nlist) - 1, 0 , -1):

        for i in range( passnum):

            if nlist[i].get_ataque() > nlist[i+1].get_ataque():
                temp = nlist[i]
                nlist[i] = nlist[ i + 1]
                nlist[ i + 1 ] = temp

def bubbleSort_tipo(nlist):
    for passnum in range( len(nlist) - 1, 0 , -1):

        for i in range( passnum):

            if nlist[i].get_tipo() > nlist[i+1].get_tipo():
                temp = nlist[i]
                nlist[i] = nlist[ i + 1]
                nlist[ i + 1 ] = temp

bubbleSort_tipo(lista)

print( "\nLista ordenada por tipo:\n")
for i in range(len(lista)): ## empieza desde el numero 1 hasta el 10 con incrementos de 1
    lista[i].imprime_datos()

bubbleSort_ataque(lista)

print( "\nLista ordenada por daño:\n")
for i in range(len(lista)): ## empieza desde el numero 1 hasta el 10 con incrementos de 1
    lista[i].imprime_datos()
