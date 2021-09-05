import pygame
import os

VERMELHO = (255, 0, 0)
VERMELHO2 = (240, 0, 0)

class Inimigo:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.images = []
        self.image = pygame.image.load(os.path.join('imagens','h1.png')).convert_alpha()
        self.health = 1
        self.max_health = 50
        self.vel = 3
        self.path = [(10,10), (20,20), (30,30), (40,40),]
        self.path_pos = 0
    
    def draw(self, win):
        """
        Desenha o inimigo na tela

        Args:
            win: Janela
        """
        self.img = self.images[self.animation_count]
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))
        
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
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos+1]
        
        
        
