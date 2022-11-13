import pygame as pg
from entity import Entity


class Tile(Entity):
    def __init__(self, groups: tuple, image: pg.Surface, pos: tuple):
        super(Tile, self).__init__(groups, image, pos)
