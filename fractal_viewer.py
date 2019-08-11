# Christoforidis Aris

import pygame
from pygame.locals import *

import OpenGL.GL as gl
from OpenGL.GL import GL_COLOR_BUFFER_BIT,GL_DEPTH_BUFFER_BIT
import OpenGL.GLU as glu

import renderer
from mesh import Mesh
from shader import ShaderProgram

# The window dimensions. [WIDTH, HEIGHT]
dimensions = [800, 400]

vertices = [
    [-1,-1],
    [-1, 1],
    [ 1,-1],
    [ 1, 1]
]

edges = [
    [0,1,2],
    [1,2,3]
]

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def setupWindow():
    ''' Initializes pygame and configures window and camera parameters. '''
    pygame.init()
    display = (dimensions[0],dimensions[1])
    pygame.display.set_caption("OpenGL Fractals")
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glu.gluOrtho2D(-1,1,-1,1)
    gl.glViewport(0,0,dimensions[0],dimensions[1])

def main():
    setupWindow()
    
    mesh = Mesh(vertices,edges)
    
    # Create the shader program and configure its uniforms.
    shaderprogram = ShaderProgram("vertex.shader","fragment.shader")
    shaderprogram.setUniform2f("resolution",dimensions[0],dimensions[1])
    
    while True:
        handleEvents()

        renderer.clearScreen()
        
        # Render the quads
        renderer.render2D(mesh,shaderprogram.shader)
        
        # Swap buffers.
        pygame.display.flip()
        

if __name__ == "__main__":
    main()