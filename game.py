import pygame
import os
# from inimigos.gato import Gato

class Game:
    def __init__(self, win):
        self.w = 1350
        self.h = 700
        self.win = win
        self.bg = pygame.image.load(os.path.join('imagens', 'fundo.png'))
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
        self.gatos = []

    def draw(self):
        self.win.blit(self.bg, (0,0))

        pygame.display.update()
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
        
        pygame.quit()
    
    def move(self):
        for gato in self.gatos:
            gato.move()
    
if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1350, 700))
    game = Game(win)
    game.run()
    pass
    