# Fractal Viewer

This is a simple python project that allows you to view fractals. It also provides a base for drawing custom fractals using the fragment shader.


## Prerequisites

This project uses NumPy, Pygame and PyOpenGL. You can install these packages with pip:

```
pip install numpy pygame pyopengl
```
    

## Usage

Start the program by running the following command:

```
python fractal_viewer.py
```

A Pygame window should appear. You can use the __Arrow Keys__ to move around and the __[W,S]__ keys to zoom in/out.


## How it works

1. The Pygame window is created.
2. A quad is drawn over the entire viewing area.
3. Every frame, the fragment shader is used to draw the fractal on the quad.


## Configuration

### Iteration control

You can control the number of iterations that the fractal calculation will execute for by configuring the variables at the top of the `fractal_viewer.py` file.

If you want to simply change the number of iterations, you can do so by changing the following variable:

```python
DEFAULT_ITERATIONS = 500
```

Alternatively the program can automatically determine the iteration count for a given depth. This allows for continuous zooming on the fractal without loss of quality. 

__WARNING: This mode is can cause significant performance drops.__

To minimize its effect, I have provided the ability to set the minimum and maximum number of iterations that the calculation will perform:

```python
AUTO_UPDATE_ITERATIONS = False # Set to True for near-infinite zoom.

MIN_ITERATIONS = 1
MAX_ITERATIONS = 1000 # Set this math.inf to functionally remove the constraint. 
```

If you want to further adjust the iteration count in this mode, you can write your own formula to calculate the number of iterations inside the `getIterationCount()` function.

### Camera controls

You can adjust the camera properties, such as the pan or zoom speed on the `Camera` class inside the `camera.py` script.

```python
def __init__():
    ...
    self.movementSpeed = 0.3 # Pan speed.
    ...

def move():
    ...
    # Zoom in/out speed. Don't use large values.
    if keys[pg.K_w]: self.scale *=  0.999
    if keys[pg.K_s]: self.scale *=  1.001
    ...
```

### Creating fractals

Before you can create your own fractals, you should familiarize yourself with the way shaders work and communicate with the main program. You will probably not be interacting with the `vertex.shader` file at all, but you need to understand how the `fragment.shader` functions. You can read up on fragment shaders [here](https://thebookofshaders.com/01/).

After you do that, you should have no problem editing the `fragment.shader` file to draw your own fractals. Simply replace the sample `mandelbrot()` function with one of your own.

The fragment shader should output a vec4 variable which represents a color value, so you have to use the value returned from the fractal function to get a color. The `getPointColor()` function does just that.

## License

Distributed under the MIT License. See `LICENSE.md` for details.

## Acknowledgments

[The Art of Code](https://www.youtube.com/channel/UCcAlTqd9zID6aNX3TzwxJXg)

[The Cherno Project](https://www.youtube.com/user/TheChernoProject)

[The Book of Shaders](https://thebookofshaders.com/)

[Coding Game - Adding colors to the Mandelbrot Set](https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/adding-some-colors)