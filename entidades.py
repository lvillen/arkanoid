import pygame as pg

class Pelota:
    def __init__(self, x, y, vx, vy, color, escala):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.escala = escala

        self.imagen = pg.Surface((self.escala, self.escala))
        self.imagen.fill(self.color)
        
        self.rect = pg.Rect(self.x, self.y, self.escala, self.escala)