import pygame as pg


from Engine.Application import Application


class GameObject:
    def __init__(self, application: Application, collider: pg.Rect, **kwargs):
        self.color = kwargs.get("color", (0, 0, 0))
        self.collider = pg.Rect(collider)
        self.application = application

    def draw(self):
        pg.draw.rect(self.application.screen, self.color, self.collider)
    
    def set_pos(self, x, y):
        self.collider.x = x
        self.collider.y = y

    def set_size(self, w, h):
        self.collider.w = w
        self.collider.h = h
