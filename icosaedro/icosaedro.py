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

cores = ( (1,0,1),(1,0.5,0),(0,1,0.5),(1,1,1),(1,0.5,1),(1,0,1),(0.5,1,0.5),(1,0,0.5) )

def Icosahedron():
    vertices = []
    phiaa  = 26.56505
    r = 1.0
    phia = math.pi*phiaa/180.0
    theb = math.pi*36.0/180.0
    the72 = math.pi*72.0/180
    vertices.append((0.0, 0.0, r))
    the = 0.0

    for i in range(1, 6):
        vertices.append((r*math.cos(the)*math.cos(phia), r*math.sin(the)*math.cos(phia), r*math.sin(phia)))
        the = the+the72

    the=theb

    for i in range(6, 11):
        vertices.append((r*math.cos(the)*math.cos(-phia), r*math.sin(the)*math.cos(-phia), r*math.sin(-phia)))
        the = the+the72

    vertices.append((0.0, 0.0, -r))

    def poligono(v1, v2, v3):
        glBegin(GL_POLYGON)
        glColor3fv(cores[random.choice(range(len(cores)))])
        glVertex3fv(vertices[v1])
        glVertex3fv(vertices[v2])
        glVertex3fv(vertices[v3])
        glEnd()

    poligono(0,1,2)
    poligono(0,2,3)
    poligono(0,3,4)
    poligono(0,4,5)
    poligono(0,5,1)
    poligono(11,6,7)
    poligono(11,7,8)
    poligono(11,8,9)
    poligono(11,9,10)
    poligono(11,10,6)
    poligono(1,2,6)
    poligono(2,3,7)
    poligono(3,4,8)
    poligono(4,5,9)
    poligono(5,1,10)
    poligono(6,7,2)
    poligono(7,8,3)
    poligono(8,9,4)
    poligono(9,10,5)
    poligono(10,6,1)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Icosahedron()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Icosaedro")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()



