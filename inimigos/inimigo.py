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
        self.path = [(100, 100), (200, 200), (300, 300), (400, 400)]
        self.path_pos = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]

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

        if self.path_pos + 1 >= len(self.path):
            self.x, self.y = (-10, 355)
        else:
            self.x, self.y = self.path[self.path_pos + 1]
