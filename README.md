# Fractal Viewer

This is a simple python project that allows you to view fractals. It also provides a base for drawing custom fractals using the fragment shader.


## Prerequisites

This project uses NumPy, Pygame and PyOpenGL. You can install these packages with pip:

```console
pip install numpy pygame pyopengl
```
    

## Usage

Start the program by running the following command:

```console
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

If you want to further adjust the iteration count in this mode, you can write your own formula to calculate the number of iterations inside the *getIterationCount()* function.

### Camera controls

You can adjust the camera properties, such as the pan or zoom speed inside the `camera.py` script.

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
