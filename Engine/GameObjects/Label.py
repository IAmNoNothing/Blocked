import pygame as pg

from Engine.GameObjects.GameObject import GameObject
from Engine.Application import Application


class Label(GameObject):

    AutoCollider = True

    def __init__(self, application: Application, text: str, font_size: int, collider, **kwargs):
        if type(collider) is bool:
            collider = pg.Rect(0, 0, font_size * len(text) / 2, font_size)
        super().__init__(application, collider, **kwargs)
        self.text = text
        self.font_size = font_size
        self.application = application
        self.font: pg.font.Font
        self.font = self.application.get_font(kwargs.get("font_name"), font_size)
        self.properties = kwargs
        self.surface = self.render()

    def render(self):
        return self.font.render(self.text, self.properties.get("alias", True), self.color)

    def draw(self):
        pg.draw.rect(self.application.screen, 'red', self.collider)
        self.application.screen.blit(self.surface, self.collider)
