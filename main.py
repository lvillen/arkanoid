import pygame as pg
import sys
import random
import entidades

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        pg.display.set_caption("Futuro Arkanoid")
        self.pelota = entidades.Pelota(400, 300, 10, 10, (251, 202, 239), 25)
        #TODO Background

    def main_loop(self):
        game_over = False
        while not game_over:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            if self.pelota.x <= 0 or self.pelota.x + self.pelota.escala >= 800: #también self.pelota.rect.right
                self.pelota.vx = -self.pelota.vx
            if self.pelota.y <= 0 or self.pelota.y + self.pelota.escala >= 600: #también self.pelota.rect.bottom
                self.pelota.vy = -self.pelota.vy

            self.pelota.x += self.pelota.vx
            self.pelota.y += self.pelota.vy

            self.pantalla.fill((0, 0, 255))
            self.pantalla.blit(self.pelota.imagen, (self.pelota.x, self.pelota.y))

            pg.display.flip()

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()

