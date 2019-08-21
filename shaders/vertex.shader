// Christoforidis Aris

#version 330 core
layout (location = 0) in vec2 aPos; // the position variable has attribute position 0
  

void main() {
    gl_Position = vec4(aPos, 0.0 , 1.0); // see how we directly give a vec2 to vec4's constructor
}