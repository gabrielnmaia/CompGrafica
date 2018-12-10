from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import numpy as np


def prox(arq):
    for l in arq:
        for n in l.strip().split(" "):
            yield n

class Parede:

    def __init__(self, x0, x1, y0, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

def desenhaParede(x0,xf,z0,zf):
    y0 = 0
    yf = 1.5
    vertices = ((x0,y0,z0),(x0,y0,zf),(x0,yf,zf),(x0,yf,z0),(xf,yf,z0),(xf,y0,z0),(xf,y0,zf),(xf,yf,zf))
    faces = ((0,1,2,3),(3,0,5,4),(4,5,6,7),(4,5,6,7),(6,7,2,1),(4,7,2,3),(5,6,1,0))
    glColor3fv((0,0,1))
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()



def desenhaLabirinto():
    
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
                    paredes.append(Parede(inicio[0],fim[0],inicio[1],fim[1]))

    for i in range(0,len(paredes)):
        desenhaParede(paredes[i].y0/4, paredes[i].y1/4, paredes[i].x0/4, paredes[i].x1/4)

    
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    desenhaLabirinto()
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1200,800)
glutCreateWindow("LABIRINTO")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(1.,1.,1.,1.)
gluPerspective(90,1200.0/800.0,2.0,150.0)
glTranslatef(-40.0,50.0,-60) 
glRotatef(70,10,0,0) 
glutTimerFunc(50,timer,1)
glutMainLoop()
