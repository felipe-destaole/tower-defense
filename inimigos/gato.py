import pygame
import os
from .inimigo import Inimigo


imgs = []
for x in range(6):
    nome_arquivo = 'tile{:0>3}.png'.format(str(x))
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("imagens/inimigos/gato", nome_arquivo)),
        (64, 64)))

class Gato(Inimigo):
    def __init__(self):
        super().__init__()
        self.width = 64
        self.height = 64
        self.images = imgs
        self.image = imgs[0]
        self.max_health = 100
        self.vel = 3