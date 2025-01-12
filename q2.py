import pygame
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

matrix = np.array([
    [1,1,1,1],
    [1,1,1,1],
])

matrix2 = np.array([
    [1,1,1,1],
    [1,1,1,1],
])



# def compute_cross_product(matrix1, matrix2):
#     return matrix1 @ matrix2
z = np.dot(matrix, matrix2)
print(z)

# def main():
#     pygame.init()
#     display = (800,600)
#     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
#     pygame.display.set_caption('Pyramid')

#     # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

#     # glTranslatef(0.1, 0.1, -5)

#     # glRotatef(0, 0, 0, 0)

    

#     # while True:
        
#     #     for event in pygame.event.get():
#     #         if event.type == pygame.QUIT:
#     #             pygame.quit()
#     #             quit()

#     #     glRotatef(1,2,1,1)
#     #     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     #     Pyramid()
#     #     pygame.display.flip()
#     #     pygame.time.wait(10)
# main()
