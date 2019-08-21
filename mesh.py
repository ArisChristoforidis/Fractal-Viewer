# Christoforidis Aris
import numpy as np
import sys
import OpenGL.GL as gl
from OpenGL.GL import GL_ARRAY_BUFFER,GL_ELEMENT_ARRAY_BUFFER,GL_STATIC_DRAW,GL_FLOAT,GL_FALSE

class Mesh:
    ''' Represents a 2D/3D mesh. '''

    def __init__(self,vertices,indices):

        self.VAO = 0
        self.VBO = 0
        self.EBO = 0

        self.VAO = gl.glGenVertexArrays(1)

        self.VBO = gl.glGenBuffers(1)
        self.EBO = gl.glGenBuffers(1)

        gl.glBindVertexArray(self.VAO)

        gl.glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        gl.glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        gl.glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,self.EBO)
        gl.glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes , indices ,GL_STATIC_DRAW)

        gl.glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
        gl.glEnableVertexAttribArray(0)

        gl.glBindBuffer(GL_ARRAY_BUFFER,0)
        
        gl.glBindVertexArray(0)



