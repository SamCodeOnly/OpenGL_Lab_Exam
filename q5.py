import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def draw_Triangle():
    glColor3f(1,0,1)
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f( 0.0, 0.5)
    glVertex2f( 0.5, 0.0)
    glVertex2f(-0.5, 0.0)
    glEnd()



def main():
    pygame.init()
    display = (600,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL )
    pygame.display.set_caption("Triangle")

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_Triangle()
        pygame.display.flip()

main()