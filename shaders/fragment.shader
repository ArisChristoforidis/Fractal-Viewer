// Christoforidis Aris

#version 330 core

out vec4 FragColor;
  
uniform vec2 resolution;

in vec4 gl_FragCoord;

void main() {
    vec2 pos = gl_FragCoord.xy/resolution.xy;
    FragColor = vec4(pos.x,pos.y,1.0,0.0);
} 