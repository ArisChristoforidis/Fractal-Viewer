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
DEFAULT_ITERATIONS = 255
AUTO_UPDATE_ITERATIONS = True

MIN_ITERATIONS = 1
MAX_ITERATIONS = m.inf



vertices = np.array([
    -1.0,-1.0,
    -1.0, 1.0,
     1.0,-1.0,
     1.0, 1.0
],dtype='f')

indices = np.array([
    0,1,2,
    1,2,3
],dtype=np.int32)

def handleEvents():
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

def getIterationCount(scale):
    ''' Calculates the number of iterations needed to continue getting good data from the fractal. '''
    iterations = int(DEFAULT_ITERATIONS / (scale * 10))
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
            shaderprogram.setUniform3f("cameraPos",camera.position[0],camera.position[1],camera.position[2])
        
        if zoom:    
            shaderprogram.setUniform2f("scale",camera.scaleVector[0],camera.scaleVector[1])
            
            if AUTO_UPDATE_ITERATIONS:
                iterations = getIterationCount(camera.scale)
                shaderprogram.setUniform1i("iterations",iterations)

        renderer.clearScreen()
        
        # Render the quads
        renderer.render2D(mesh,shaderprogram.shader)
        
        # Swap buffers.
        pygame.display.flip()
        

if __name__ == "__main__":
    main()