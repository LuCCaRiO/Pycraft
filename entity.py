import pygame as pg
from abc import ABC, abstractmethod


class Entity(pg.sprite.Sprite, ABC):
    def __init__(self, groups: tuple, image: pg.Surface, pos: pg.math.Vector2):
        super(Entity, self).__init__(groups)
        self.image: pg.Surface = image
        self.rect: pg.Rect = self.image.get_rect(topleft=pos)
