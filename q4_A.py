import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *





def main():
    pygame.init()
    canvas = (500,400)
    pygame.display.set_mode(canvas, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('My Canvas Question Number 4 A')

    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    print("white")
                    # canvas.fill((255,0,255))
            


        pygame.display.flip()
        pygame.time.wait(10)
main()


# yaredmgmt@gmail.com