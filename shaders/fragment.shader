// Christoforidis Aris

#version 330 core

out vec4 FragColor;
  
uniform vec2 resolution;
uniform vec2 cameraPos;
uniform vec2 scale;

uniform int iterations;

in vec4 gl_FragCoord;

vec3 hsv2rgb(vec3 val){
    //Converts an HSV vector to an RGB vector.
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(val.xxx + K.xyz) * 6.0 - K.www);
    return val.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), val.y);
}

vec4 getPointColor(int escapeValue) {
    // Calculates a vec4 color value for a given integer.
    float hue = float(1.0 * float(escapeValue) / float(iterations));
    float saturation = 1.0;
    float value = 0;
    if( escapeValue < iterations) {
        value = 1.0;
    }
    vec3 rgb = hsv2rgb(vec3(hue,saturation,value));
    return vec4(rgb,1.0);
}

int mandelbrot(vec2 p){
    // Calculates the mandelbrot set.
    vec2 c = (p - 0.5) * scale - cameraPos.xy;
    vec2 z = c;
    
    int i;
    for(i=0;i<iterations;i++) {
        z = vec2(z.x*z.x - z.y*z.y, 2*z.x*z.y) + c;

        // Define infinity here. The number on the right hand side does not need to be very big.
        if(length(z) > 2) break;
    }
    return i;
}

void main() {
    //Calculate the point position.
    vec2 point = (gl_FragCoord.xy)/resolution.xy;
    int value =  mandelbrot(point);
    FragColor = getPointColor(value);
} 