import pygame
import os
from inimigos.gato import Gato

class Game:
    def __init__(self, win):
        self.w = 1350
        self.h = 700
        self.win = win
        self.bg = pygame.image.load(os.path.join('imagens', 'fundo.png'))
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
        gato = Gato()
        self.gatos: list[Gato] = [gato]

    def draw(self):
        self.win.blit(self.bg, (0,0))
        for gato in self.gatos:
            gato.draw(win)

        pygame.display.update()
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
        
            for gato in self.gatos:
                gato.move()
        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1350, 700))
    game = Game(win)
    game.run()
    pass
    