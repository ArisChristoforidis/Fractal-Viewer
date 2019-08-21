# Christoforidis Aris

import OpenGL.GL as gl
from OpenGL.GL import GL_QUADS,GL_TRIANGLES,GL_LINES,GL_COLOR_BUFFER_BIT,GL_DEPTH_BUFFER_BIT,GL_UNSIGNED_INT
import OpenGL.GLU as glu

from mesh import Mesh

def clearScreen():
    gl.glClearColor(0.0,0.0,0.0,1.0)
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
    gl.glBindVertexArray(mesh.VAO)
    gl.glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

