from Engine.Application import Application
from Engine.GameObjects.Label import Label
# from Engine.Functions import clamp

import pygame as pg


class Block:
    def __init__(self, application: Application, text: str = '', collider: tuple | pg.Rect = None, **kwargs):
        self.application = application
        self.text = text
        self.label = Label(self.application, self.text, 15, collider=Label.AutoCollider)
        self.collider = collider

        self.color = kwargs.get('color')

    def draw(self):
        pg.draw.rect(self.application.screen, self.color, (self.collider.left, self.collider.top, 40, self.collider.h))
