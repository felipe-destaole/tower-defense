import pygame
import os
import pathlib
from .inimigo import Inimigo

path = pathlib.path(__file__)

gato_0 = pygame.image.load(os.path.join('imagens','tile_000.png')).convert_alpha()
gato_1 = pygame.image.load(os.path.join('imagens','tile_001.png')).convert_alpha()
gato_2 = pygame.image.load(os.path.join('imagens','tile_002.png')).convert_alpha()
gato_3 = pygame.image.load(os.path.join('imagens','tile_003.png')).convert_alpha()
gato_4 = pygame.image.load(os.path.join('imagens','tile_004.png')).convert_alpha()
gato_5 = pygame.image.load(os.path.join('imagens','tile_005.png')).convert_alpha()

class Gato(Inimigo):
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.images = [gato_1,gato_2,gato_3,gato_4,gato_5,gato_0]
        self.image = gato_1
        self.max_health = 100
        self.vel = 3