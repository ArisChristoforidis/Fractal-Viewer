# Christoforidis Aris

import OpenGL.GL as gl
from OpenGL.GL import shaders, GL_VERTEX_SHADER, GL_FRAGMENT_SHADER

class ShaderProgram:
    ''' Creates a shader program by compiling the shaders in the given paths. '''
    
    def __init__(self, vertexShaderPath: str, fragmentShaderPath: str):
        # Get the source code from the two files.
        vertexShaderSource = self.readShaderFromFile(vertexShaderPath)
        fragmentShaderSource = self.readShaderFromFile(fragmentShaderPath)

        # Compile the shaders.
        vertexShader = shaders.compileShader(vertexShaderSource,GL_VERTEX_SHADER)
        fragmentShader = shaders.compileShader(fragmentShaderSource,GL_FRAGMENT_SHADER)

        # Create the program.
        self.shader = shaders.compileProgram(vertexShader,fragmentShader)

        # Use shader.
        gl.glUseProgram(self.shader)


    def readShaderFromFile(self,path: str) -> str:
        ''' Reads the source code of a shader file and returns its contents as a string. '''
        shaderFile = open(path)
        source = shaderFile.read()
        return source

    def setUniform1i(self,uniformName : str, x : int):
        ''' Sets the value of an int uniform on the shader program. '''
        uniform = gl.glGetUniformLocation(self.shader, uniformName)
        #gl.glUseProgram(self.shader)
        gl.glUniform1i(uniform, x)



    def setUniform2f(self,uniformName: str, x: float, y: float):
        ''' Sets the value of a vec2 uniform on the shader program. '''
        uniform = gl.glGetUniformLocation(self.shader, uniformName)
        #gl.glUseProgram(self.shader)
        gl.glUniform2f(uniform, x, y)

    def setUniform3f(self,uniformName: str, x: float, y: float, z: float):
        ''' Sets the value of a vec3 uniform on the shader program. '''
        uniform = gl.glGetUniformLocation(self.shader, uniformName)
        #gl.glUseProgram(self.shader)
        gl.glUniform3f(uniform, x, y, z)



