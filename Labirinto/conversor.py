import numpy as np


def prox(arq):
    for l in arq:
        for n in l.strip().split(" "):
            yield n

class Parede:

    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final
    
    def __str__(self):
        str1 = ','.join(str(e)  for e in self.inicio)
        str2 = ','.join(str(e) for e in self.final)
        return "Inicio : " + str1 + "\n" + "Final : " + str2
   

arq = open('labirinto.pgm','r')

it = prox(arq)

p2 = it.next()
#print p2

w = int(it.next())
#print w

h = int(it.next())
#print h

m = int(it.next())
#print m

table = np.zeros([h, w])

for linha in range(0,h):
    #print "------------------------------------------------------------"
    for coluna in range(0,w):
        cor = int(it.next())
        if cor < 10:
            #print "*",
            table[linha,coluna] = 1
        else:
            #print "-",
            table[linha,coluna] = 0
    #print ""
    # print "-----------------------------------------------------------"
#print table[6]

arq.close()

anterior = 0
inicio = [0,0]
fim = [0,0]
paredes = []

for linha in range(0,h):
    for coluna in range(0,w):
        if table[linha,coluna] == 1:
            if anterior != 1:
                anterior = 1
                inicio = [linha,coluna]
                #print inicio
        else:
            if anterior == 1:
                anterior = 0
                fim = [linha, coluna-1]
                #print fim
                paredes.append(Parede(inicio,fim))

for i in range(0,len(paredes)):
    print '------------'
    print 'PAREDE' , i
    print paredes[i]
    print '------------\n'
          

