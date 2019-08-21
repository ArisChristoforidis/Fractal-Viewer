import numpy as np
import pygame as pg
import math as m
from pygame.key import *

class Camera2D:
    ''' A 2D Camera. '''

    def __init__(self,screenWidth : int, screenHeight : int):

        self.aspectRatio = screenWidth / screenHeight
        self.scale = 1
        self.scaleVector = np.array([0.0,0.0])
        self.UpdateScaleVector()

        # The starting "position" of the camera.
        self.position = np.array([0.0,0.0,1])

        # The right direction in space.(Positive movement on the x-axis)
        self.right = np.array([-1.0,0.0,0.0])
        # The up direction in space.(Positive movement on the y-axis)
        self.up = np.array([0.0,-1.0,0.0])
        # The forward direction in space.(Negative movement on the z-axis)
        self.forward = np.array([0.0,0.0,-1.0])

        self.lastFrameTicks = 0

        self.movementSpeed = 0.3

    def move(self):
        pan = zoom = False

        velocity = self.movementSpeed * self.getDeltaTime()

        keys = get_pressed()

        # Check if camera was moved.
        pan = keys[pg.K_RIGHT] or keys[pg.K_LEFT] or keys[pg.K_UP] or keys[pg.K_DOWN]
        
        # Check if camera was zoomed in/out.
        zoom = keys[pg.K_w] or keys[pg.K_s]

        if keys[pg.K_RIGHT]: self.position += self.right * velocity * self.scale
        if keys[pg.K_LEFT]: self.position += -self.right * velocity * self.scale
        if keys[pg.K_UP]: self.position +=  self.up * velocity * self.scale
        if keys[pg.K_DOWN]: self.position += -self.up * velocity * self.scale


        if keys[pg.K_w]: self.scale *=  0.995
        if keys[pg.K_s]: self.scale *=  1.0015
        
        if zoom:
            self.UpdateScaleVector()


        return pan,zoom
            

    def UpdateScaleVector(self):
        self.scaleVector[:] = self.scale

        if self.aspectRatio > 1:
            self.scaleVector[1] /= self.aspectRatio
        else:
            self.scaleVector[0] *= self.aspectRatio



    def getDeltaTime(self):
        currentFrameTicks = pg.time.get_ticks()
        deltaTime = (currentFrameTicks - self.lastFrameTicks) / 1000
        self.lastFrameTicks = currentFrameTicks
        return deltaTime
