# Christoforidis Aris

import numpy as np
import math as m

import pygame
from pygame.locals import *

import OpenGL.GL as gl
import OpenGL.GLU as glu

import renderer
from mesh import Mesh
from shader import ShaderProgram

from camera import Camera2D

# The window dimensions. [WIDTH, HEIGHT]
DIMENSIONS = [800, 600]

# The initial number of iterations to be performed for the calculation of the fractal.
DEFAULT_ITERATIONS = 500
AUTO_UPDATE_ITERATIONS = False

MIN_ITERATIONS = 1
MAX_ITERATIONS = 1000#m.inf

# The coordinates of the quad that the shader is displayed on.
vertices = np.array([
    -1.0,-1.0,
    -1.0, 1.0,
     1.0,-1.0,
     1.0, 1.0
],dtype='f')

# Index directions for creating the quad by forming triangles.
indices = np.array([
    0,1,2,
    1,2,3
],dtype=np.int32)

def handleEvents():
    ''' Handles pygame window events. '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def setupWindow():
    ''' Initializes pygame and configures window and camera parameters. '''
    pygame.init()
    display = (DIMENSIONS[0],DIMENSIONS[1])
    pygame.display.set_caption("OpenGL Fractals")
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glu.gluOrtho2D(-1,1,-1,1)
    gl.glViewport(0,0,DIMENSIONS[0],DIMENSIONS[1])

    gl.glClearColor(0.0,0.0,0.0,1.0)


def getIterationCount(scale):
    ''' 
    Calculates the number of iterations needed to continue getting good data from the fractal.
    Note that as the depth increases, this tends to get very expensive and can be the cause of 
    significant performance drops.
    '''

    # A very simple formula to calculate iterations needed for the given scale.
    iterations = int(DEFAULT_ITERATIONS / (scale * 10))

    # Constrain the number of iterations to be in the range [MIN_ITERATIONS, MAX_ITERATIONS]
    iterations = int(np.clip(iterations,MIN_ITERATIONS,MAX_ITERATIONS))
    return iterations


def main():
    setupWindow()
    
    mesh = Mesh(vertices,indices)
    
    camera = Camera2D(DIMENSIONS[0],DIMENSIONS[1])

    # Create the shader program and configure its uniforms.
    shaderprogram = ShaderProgram("shaders/vertex.shader","shaders/fragment.shader")
    shaderprogram.setUniform2f("resolution",DIMENSIONS[0],DIMENSIONS[1])
    shaderprogram.setUniform2f("scale",camera.scaleVector[0],camera.scaleVector[1])
    shaderprogram.setUniform1i("iterations",DEFAULT_ITERATIONS)

    while True:
        handleEvents()

        pan,zoom = camera.move()
        
        if pan:
            shaderprogram.setUniform2f("cameraPos",camera.position[0],camera.position[1])
        
        if zoom:    
            shaderprogram.setUniform2f("scale",camera.scaleVector[0],camera.scaleVector[1])
            
            if AUTO_UPDATE_ITERATIONS:
                iterations = getIterationCount(camera.scale)
                shaderprogram.setUniform1i("iterations",iterations)

        renderer.clearScreen()
        
        # Render the quads.
        renderer.render2D(mesh,shaderprogram.shader)
        
        # Swap buffers.
        pygame.display.flip()
        

if __name__ == "__main__":
    main()