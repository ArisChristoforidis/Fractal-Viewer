# Christoforidis Aris

import OpenGL.GL as gl
from OpenGL.GL import GL_QUADS,GL_TRIANGLES,GL_LINES,GL_COLOR_BUFFER_BIT,GL_DEPTH_BUFFER_BIT
import OpenGL.GLU as glu

from mesh import Mesh

def clearScreen():
    gl.glClear(GL_COLOR_BUFFER_BIT)

def render3D(mesh: Mesh):
    ''' Renders a 3D mesh on the screen. '''
    gl.glBegin(GL_TRIANGLES)
    for indicePair in mesh.indices:
        for index in indicePair:
            vertex = mesh.vertices[index]
            gl.glVertex3fv(vertex)

def render2D(mesh: Mesh,shader):
    ''' Renders a 2D mesh on the screen. '''

    gl.glUseProgram(shader)

    gl.glBegin(GL_TRIANGLES)
    for indicePair in mesh.indices:
        for index in indicePair:
            vertex = mesh.vertices[index]
            gl.glVertex2fv(vertex)