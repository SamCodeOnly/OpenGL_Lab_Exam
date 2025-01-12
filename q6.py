import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = (
    (1, 1),
    (-1,-1)
)

def draw_line(x1,y1,x2,y2):
    p1 = (x1,y1)
    p2 = (x2,y2)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2fv(p1)
    glVertex2fv(p2)
    glEnd()


def main():
    pygame.init()
    canvas = (500,400)
    pygame.display.set_mode(canvas, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('My Canvas')

    gluPerspective(45, canvas[0]/canvas[1], 0.1, 50.0)

    glTranslate(0.0, 0.0, -5)


    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type = pygame.Keyboard:
            #     if event.keyboard == keyboard.


        draw_line(vertices[0][0],vertices[0][1],vertices[1][0],vertices[1][1])
        pygame.display.flip()
        pygame.time.wait(10)
main()
