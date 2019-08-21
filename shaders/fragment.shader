// Christoforidis Aris

#version 330 core

out vec4 FragColor;
  
uniform vec2 resolution;
uniform vec3 cameraPos;
uniform vec2 scale;

uniform int iterations;

in vec4 gl_FragCoord;

vec3 hsv2rgb(vec3 val){
    //Converts an HSV vector to an RGB vector
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(val.xxx + K.xyz) * 6.0 - K.www);
    return val.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), val.y);
}

vec4 getPointColor(int escapeValue) {
    int hue = int(255.0 * float(escapeValue) / float(iterations));
    int saturation = 255;
    int value = 0;
    if( escapeValue < iterations) {
        value = 255;
    }
    vec3 rgb = hsv2rgb(vec3(hue,saturation,value));
    return vec4(rgb,1.0);
}

int mandelbrot(vec2 p){

    vec2 c = (p - 0.5) * scale - cameraPos.xy;

    //p.x = cameraPos.x + (p.x - 0.5) * scale.x; 
    //p.y = cameraPos.y + (p.y - 0.5) * scale.y; 

    //p.x = (p.x -0.5) * scale  - cameraPos.x;
    //p.y = (p.y -0.5) * scale  - cameraPos.y;

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
    vec2 point = (gl_FragCoord.xy + cameraPos.xy)/resolution.xy;
    vec2 cameraOffset = cameraPos.xy/resolution.xy;
    int value =  mandelbrot(point);
    FragColor = getPointColor(value);
    /*
    if(value == iterations){
        FragColor = vec4(0.0,0.0,0.0,0.0);
    }else {
        FragColor = vec4(1.0,1.0 * value/iterations,1.0 * value/iterations,1.0);
        //FragColor = vec4(cameraPos.x,cameraPos.y,cameraPos.z,1.0);

    }
    */
} 