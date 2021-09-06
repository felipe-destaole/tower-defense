import pygame
import os
import math

VERMELHO = (255, 0, 0)
VERMELHO2 = (240, 0, 0)


class Inimigo:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.images = []
        self.image = pygame.image.load(
            os.path.join("imagens", "ren.png")
        ).convert_alpha()
        self.health = 1
        self.max_health = 50
        self.vel = 3
        self.path = [(33, 378), (213, 375), (218, 178), (488, 180), (495, 443), (859, 451), (858, 315), (1321, 308)]
        self.path_pos = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.flipped = False

    def draw(self, win):
        """
        Desenha o inimigo na tela

        Args:
            win: Janela
        """
        self.img = self.images[self.animation_count]
        win.blit(
            self.img,
            (
                self.x - self.img.get_width() / 2,
                self.y - self.img.get_height() / 2 - 35,
            ),
        )

    def health_bar(self, win):
        """Desenha a barra de vida dos inimigos"""
        pass

    def move(self):
        """Move o inimigo"""
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1360, 310)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1