# Christoforidis Aris

import OpenGL.GL as gl
from OpenGL.GL import GL_QUADS,GL_TRIANGLES,GL_LINES,GL_COLOR_BUFFER_BIT,GL_DEPTH_BUFFER_BIT,GL_UNSIGNED_INT
import OpenGL.GLU as glu

from mesh import Mesh

def clearScreen():
    ''' Clears the screen. '''
    gl.glClear(GL_COLOR_BUFFER_BIT)


def render2D(mesh: Mesh,shader):
    ''' Renders a 2D mesh on the screen. '''
    gl.glUseProgram(shader)
    gl.glBindVertexArray(mesh.VAO)
    gl.glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

