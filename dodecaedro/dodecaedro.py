import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def Dodecahedron():
    vertices = []
    phiaa = 52.62263590
    phibb = 10.81231754
    r = 1.0
    phia = math.pi*phiaa/180.0
    phib = math.pi*phibb/180.0
    phic = math.pi*(-phibb)/180.0
    phid = math.pi*(-phiaa)/180.0
    the72 = math.pi*72.0/180
    theb = the72/2.0
    the = 0.0

    for i in range(5):
        vertices.append((r*math.cos(the)*math.cos(phia), r*math.sin(the)*math.cos(phia), r*math.sin(phia)))
        the = the+the72

    the=0.0

    for i in range(5, 10):
        vertices.append((r*math.cos(the)*math.cos(phib), r*math.sin(the)*math.cos(phib), r*math.sin(phib)))
        the = the+the72

    the = theb

    for i in range(10, 15):
        vertices.append((r*math.cos(the)*math.cos(phic), r*math.sin(the)*math.cos(phic), r*math.sin(phic)))
        the = the+the72

    the = theb

    for i in range(15, 20):
        vertices.append((r*math.cos(the)*math.cos(phid), r*math.sin(the)*math.cos(phid), r*math.sin(phid)))
        the = the+the72

    def poligono(v1, v2, v3, v4, v5):
        glBegin(GL_POLYGON)
        glColor3fv(cores[random.choice(range(len(cores)))])
        glVertex3fv(vertices[v1])
        glVertex3fv(vertices[v2])
        glVertex3fv(vertices[v3])
        glVertex3fv(vertices[v4])
        glVertex3fv(vertices[v5])
        glEnd()

    poligono(0,1,2,3,4)
    poligono(0,1,6,10,5)
    poligono(1,2,7,11,6)
    poligono(2,3,8,12,7)
    poligono(3,4,9,13,8)
    poligono(4,0,5,14,9)
    poligono(15,16,11,6,10)
    poligono(16,17,12,7,11)
    poligono(17,18,13,8,12)
    poligono(18,19,14,9,13)
    poligono(19,15,10,5,14)
    poligono(15,16,17,18,19)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Dodecahedron()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Dodecaedro")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



