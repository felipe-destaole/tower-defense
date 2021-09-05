import pygame,random,math
pygame.init()

# our game window
window = pygame.display.set_mode((800,600),pygame.NOFRAME)
pygame.display.set_caption("Tower Defense Game")

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)




def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))
        smallText = pygame.font.SysFont("Candarai.ttf",40)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        window.blit(textSurf, textRect)
        
    #------------------------------------------------------



hit = pygame.mixer.Sound("hit.wav")
buysound = pygame.mixer.Sound("Item2A.wav")

pygame.mixer.set_num_channels(64)




bonus = pygame.mixer.Sound("bonus.wav")

mens = pygame.mixer.Sound("Menu2A.wav")




    # the buttons for the shop MENUUUU
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False

    def draw(self,window,outline=None):
                #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                    
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
                
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
                #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                    
        return False

    def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):            
            if not self.over:
                click.play()
                self.over = True
        else:
            self.over = False



# THIS IS THE RESTART WHEN THE PLAYER HEALTH IS ALMOST DEAD LOL
# you lose screen
whs = (255,255,255)
def text_objects(text, font):
    textSurface = font.render(text, True, whs)
    return textSurface, textSurface.get_rect()
 




music = pygame.mixer.music.load("song2.flac")


music2 = pygame.mixer.Sound("gam2.wav")



click = pygame.mixer.Sound("click.wav")




def text_objects(text, font):
    black = (255,255,255)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((255,255,155))
    for alpha in range(0, 100):
        fade.set_alpha(alpha)
        window.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(15)

def game_intro():
    pygame.mixer.music.play(-1)



                    

    class intro():
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.bg = [pygame.image.load("nam" + str(i) + ".jpg") for i in range(1, 209)]
            self.rect = pygame.Rect(x,y,height,width)
            self.fps = 50
            self.next_frame_time = 0
            self.clock = pygame.time.Clock()
            self.direction = "intros"
            self.anim_index = 0
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "intros":
                self.clock.tick(self.fps)
                image_list = self.bg

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 1990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


    white = 255,255,255
    bg = intro(400,219,00,200,white)



    class load:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
            self.health = 10
            self.hitbox = (self.x, self.y + 30, 46,60)
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            self.hitbox = (self.x, self.y + 30, 206,60)
            pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 510, 50)) # NEW
            pygame.draw.rect(window, (52, 152, 219), (self.hitbox[0], self.hitbox[1] - 40, 10 - (5 * (10 - self.health)), 50))



    load1 = load(150,530,10,10,white)

    font = pygame.font.Font("abya.ttf", 40)
    score = 0
    scoretext = font.render("" + str(score), True, (255,255,255))
    scorerect = scoretext.get_rect()
    scorerect.center = ((400,550))

    
    # the background image
    def redraw():
        bg.draw()
        load1.draw()
        window.blit(scoretext,scorerect)


        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 190
    time = 0
    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()

        if load1.health < 110:
            load1.health += 0.5
            score += 0.5
            scoretext = font.render(str(score) + "%" , True, (255,255,255))
            scorerect = scoretext.get_rect()
            scorerect.center = ((400,550))
        else:
            time += 1
            if time > 60:
                fade(800,800)
                main_game_loop()

        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()







 

def main_game_loop():

    colors = 255,23,56

    class intro2():
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.bg = [pygame.image.load("n (" + str(i) + ").png") for i in range(1, 60)]
            self.rect = pygame.Rect(x,y,height,width)
            self.fps = 50
            self.next_frame_time = 0
            self.clock = pygame.time.Clock()
            self.direction = "intros"
            self.anim_index = 0
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "intros":
                self.clock.tick(self.fps)
                image_list = self.bg

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 1990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


    class Wave:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
            self.font = pygame.font.Font("abya.ttf", 30)
            self.cash = 1
            self.cashtext = self.font.render("" + str(self.cash), True, (0, 0,15))
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.cashtext,self.rect)

    white = 255,255,255
    wh = (255,255,255)
    Wave1 = Wave(730,540,50,50,wh)



    bg1 = intro2(400,219,00,200,white)

    over1 = pygame.image.load("arr.png")
    bu1 = button((colors),350,285,150,30, '')
    bu3 = button((colors),350,370,150,30, '')
    bu4 = button((colors),350,420,150,30, '')
    buttons = [bu1,bu3,bu4]

    # the background image
    over11 = False
    def redraw():
        bg1.draw()

        
        pos = pygame.mouse.get_pos()
        if bu1.isOver(pos):
            window.blit(over1,(bu1.x + 150,bu1.y + 5))

        if bu3.isOver(pos):
            window.blit(over1,(bu3.x + 165,bu3.y + 10))

        if bu4.isOver(pos):
            window.blit(over1,(bu4.x + 130,bu4.y + 1))

        Wave1.draw()
        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 60

    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bu1.isOver(pos):
                    mens.play()
                    fade(800,800)
                    game()
                if bu3.isOver(pos):
                    mens.play()
                    fade(800,800)
                    how_to_play()

                if bu4.isOver(pos):
                    mens.play()
                    fade(800,800)
                    how_to_play2()


        pos = pygame.mouse.get_pos()

        bu1.playSoundIfMouseIsOver(pos, mouseisover)
        bu3.playSoundIfMouseIsOver(pos, mouseisover)
        bu4.playSoundIfMouseIsOver(pos, mouseisover)


        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()










def play_again():


    colors = (255,255,255)

    bgimage = pygame.image.load("play.png")
    over1 = pygame.image.load("arr.png")
    bu1 = button((colors),350,235,150,30, '')
    buttons = [bu1]

    # the background image
    over11 = False
    def redraw():
        window.blit(bgimage,(0,0))

        
        pos = pygame.mouse.get_pos()
        if bu1.isOver(pos):
            window.blit(over1,(bu1.x + 150,bu1.y + 5))

        
        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 60

    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bu1.isOver(pos):
                    mens.play()
                    fade(800,800)
                    game()

        pos = pygame.mouse.get_pos()

        bu1.playSoundIfMouseIsOver(pos, mouseisover)

        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()




def how_to_play():

    colors = 255,23,56

    class intro2():
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.bg = [pygame.image.load("d (" + str(i) + ").png") for i in range(1, 60)]
            self.rect = pygame.Rect(x,y,height,width)
            self.fps = 50
            self.next_frame_time = 0
            self.clock = pygame.time.Clock()
            self.direction = "intros"
            self.anim_index = 0
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "intros":
                self.clock.tick(self.fps)
                image_list = self.bg

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 1990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


    white = 255,255,255
    bg1 = intro2(400,219,00,200,white)

    over1 = pygame.image.load("arr.png")
    bu1 = button((colors),10,445,150,150, '')
    buttons = [bu1]

    # the background image
    over11 = False
    def redraw():
        bg1.draw()

        
        pos = pygame.mouse.get_pos()
        if bu1.isOver(pos):
            window.blit(over1,(bu1.x + 150,bu1.y + 55))

        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 60

    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bu1.isOver(pos):
                    mens.play()
                    fade(800,800)
                    main_game_loop()

        pos = pygame.mouse.get_pos()

        bu1.playSoundIfMouseIsOver(pos, mouseisover)

        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()












        
def how_to_play():

    colors = 255,23,56

    class intro2():
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.bg = [pygame.image.load("d (" + str(i) + ").png") for i in range(1, 60)]
            self.rect = pygame.Rect(x,y,height,width)
            self.fps = 50
            self.next_frame_time = 0
            self.clock = pygame.time.Clock()
            self.direction = "intros"
            self.anim_index = 0
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "intros":
                self.clock.tick(self.fps)
                image_list = self.bg

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 1990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


    white = 255,255,255
    bg1 = intro2(400,219,00,200,white)

    over1 = pygame.image.load("arr.png")
    bu1 = button((colors),10,445,150,150, '')
    buttons = [bu1]

    # the background image
    over11 = False
    def redraw():
        bg1.draw()

        
        pos = pygame.mouse.get_pos()
        if bu1.isOver(pos):
            window.blit(over1,(bu1.x + 150,bu1.y + 55))

        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 60

    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bu1.isOver(pos):
                    mens.play()
                    fade(800,800)
                    main_game_loop()

        pos = pygame.mouse.get_pos()

        bu1.playSoundIfMouseIsOver(pos, mouseisover)

        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()








def how_to_play2():

    colors = 255,23,56

    class intro2():
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.bg = [pygame.image.load("y (" + str(i) + ").png") for i in range(1, 60)]
            self.rect = pygame.Rect(x,y,height,width)
            self.fps = 50
            self.next_frame_time = 0
            self.clock = pygame.time.Clock()
            self.direction = "intros"
            self.anim_index = 0
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "intros":
                self.clock.tick(self.fps)
                image_list = self.bg

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 1990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


    white = 255,255,255
    bg1 = intro2(400,219,00,200,white)

    over1 = pygame.image.load("arr.png")
    bu1 = button((colors),10,445,150,150, '')
    buttons = [bu1]

    # the background image
    over11 = False
    def redraw():
        bg1.draw()

        
        pos = pygame.mouse.get_pos()
        if bu1.isOver(pos):
            window.blit(over1,(bu1.x + 150,bu1.y + 55))

        
    red = (200,0,0)
    green = (255,250,250)
    bright_red = (255,250,0)
    bright_green = (0,255,0)
    clock = pygame.time.Clock()

    mouseisover = True
    FPS = 60

    intro = True
    while intro:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bu1.isOver(pos):
                    fade(800,800)
                    main_game_loop()

        pos = pygame.mouse.get_pos()

        bu1.playSoundIfMouseIsOver(pos, mouseisover)

        redraw()



        
        clock.tick(FPS)



                    
 


    # ---------------------------------------------------------------------





      

        pygame.display.update()


def game():
    pygame.mixer.music.fadeout(1000)
    musicplay = False
    music2.play(-1)

    global pause
    #---------------------------------------------------


            
    
    class button():
        def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.over = False

        def draw(self,window,outline=None):
                    #Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                        
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
                    
            if self.text != '':
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(self.text, 1, (255,255,255))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def isOver(self, pos):
                    #Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
                        
            return False

        def playSoundIfMouseIsOver(self, pos, sound):
            if self.isOver(pos):            
                if not self.over:
                    click.play()
                    self.over = True
            else:
                self.over = False


    colors = 255,23,56


    # our drawn towers:
    class towerdrawn1:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("to1.png"),
                          pygame.image.load("to2.png"),
                          pygame.image.load("to3.png"),
                          pygame.image.load("to4.png"),
                          pygame.image.load("to5.png"),
                          pygame.image.load("to6.png"),
                          pygame.image.load("to7.png"),
                          pygame.image.load("to8.png"),
                          pygame.image.load("to9.png")
                         ]

            self.walk = [pygame.transform.scale(image,(image.get_width()-20,image.get_height()-20)) for image in self.walk]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
                     
            self.direction = "walk"
            self.anim_index = 0
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk


            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hit
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 6990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)



    class towerdrawn2:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("tos1.png"),
                          pygame.image.load("tos2.png"),
                          pygame.image.load("tos3.png"),
                          pygame.image.load("tos4.png"),
                          pygame.image.load("tos5.png"),
                          pygame.image.load("tos6.png"),
                          pygame.image.load("tos7.png"),
                          pygame.image.load("tos8.png"),
                          pygame.image.load("tos9.png")
                         ]

            self.walk = [pygame.transform.scale(image,(image.get_width()-20,image.get_height()-20)) for image in self.walk]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "walk"
            self.anim_index = 0
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk


            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hit
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 6990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)

            


    class towerdrawn3:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("tol1.png"),
                          pygame.image.load("tol2.png"),
                          pygame.image.load("tol3.png"),
                          pygame.image.load("tol4.png"),
                          pygame.image.load("tol5.png"),
                          pygame.image.load("tol6.png"),
                          pygame.image.load("tol7.png"),
                          pygame.image.load("tol8.png"),
                          pygame.image.load("tol9.png")
                         ]

            self.walk = [pygame.transform.scale(image,(image.get_width()-20,image.get_height()-20)) for image in self.walk]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "walk"
            self.anim_index = 0
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk


            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hit
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 6990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)




    class towerdrawn4:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("tow1.png"),
                          pygame.image.load("tow2.png"),
                          pygame.image.load("tow3.png"),
                          pygame.image.load("tow4.png"),
                          pygame.image.load("tow5.png"),
                          pygame.image.load("tow6.png"),
                          pygame.image.load("tow7.png"),
                          pygame.image.load("tow8.png"),
                          pygame.image.load("tow9.png")
                         ]

            self.walk = [pygame.transform.scale(image,(image.get_width()-20,image.get_height()-20)) for image in self.walk]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "walk"
            self.anim_index = 0
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk


            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hit
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 6990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]

            player_image = image_list[self.anim_index]
            self.hitbox = (self.x, self.y + 30, 46,60)

            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)


            

    white = 255,255,255




    colors = (155,255,255)
    greenbutton1 = button((colors),700,35,80,30, '')
    exit2 = button((colors),655,36,30,30, '')


    drawtower1 = button((colors),120,553,65,30, '')
    drawtower2 = button((colors),280,553,65,30, '')
    drawtower3 = button((colors),450,553,65,30, '')
    drawtower4 = button((colors),620,553,65,30, '')

    SHOP_UPGRADE = button((colors),700,110,80,30, '')
    exit3 = button((colors),655,110,30,30, '')



    # my upgrade buttons
    upgrade1 = button((colors),120,553,65,30, '')
    upgrade2 = button((colors),280,553,65,30, '')
    upgrade3 = button((colors),450,553,65,30, '')
    upgrade4 = button((colors),620,553,65,30, '')





    attack1 = button((colors),80,423,100,100, '')
    attack2 = button((colors),80,170,100,100, '')
    attack3 = button((colors),230,80,100,100, '')
    attack4 = button((colors),380,250,100,100, '')
    attack5 = button((colors),560,53,100,100, '')


    attack6 = button((colors),80,423,100,100, '')
    attack7 = button((colors),80,170,100,100, '')
    attack8 = button((colors),230,80,100,100, '')
    attack9 = button((colors),380,250,100,100, '')
    attack10 = button((colors),560,53,100,100, '')



    attack11 = button((colors),80,423,100,100, '')
    attack12 = button((colors),80,170,100,100, '')
    attack13 = button((colors),230,80,100,100, '')
    attack14 = button((colors),380,250,100,100, '')
    attack15 = button((colors),560,53,100,100, '')



    attack16 = button((colors),80,423,100,100, '')
    attack17 = button((colors),80,170,100,100, '')
    attack18 = button((colors),230,80,100,100, '')
    attack19 = button((colors),380,250,100,100, '')
    attack20 = button((colors),560,53,100,100, '')


    pausees = button((colors),280,553,70,30, '')
    main_lol = button((colors),30,553,70,30, '')

    
    soly = [main_lol,pausees,exit3,SHOP_UPGRADE,exit2,greenbutton1]
    holy = [upgrade1,upgrade2,upgrade3,upgrade4]
    moly = [drawtower1,drawtower2,drawtower3,drawtower4]
            
    # add the other buttons for the other towers

    buttons = [main_lol,pausees,upgrade1,upgrade2,upgrade3,upgrade4,SHOP_UPGRADE,exit3,greenbutton1,exit2,drawtower1,drawtower2,drawtower3,drawtower4,attack1,attack2,attack3,attack4,attack5,attack6,attack7,attack8,attack9,attack10,attack11,attack12,attack13,attack14,attack15,attack16,attack17,attack18,attack19,attack20]









    pause = False


    def text_objects(text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()


    def unpause():
        global pause
        pause = False
        





    def paused():
        
        class button():
            def __init__(self, color, x,y,width,height, text=''):
                self.color = color
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.text = text
                self.over = False

            def draw(self,window,outline=None):
                        #Call this method to draw the button on the screen
                if outline:
                    pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                            
                pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
                        
                if self.text != '':
                    font = pygame.font.SysFont('comicsans', 60)
                    text = font.render(self.text, 1, (255,255,255))
                    window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

            def isOver(self, pos):
                        #Pos is the mouse position or a tuple of (x,y) coordinates
                if pos[0] > self.x and pos[0] < self.x + self.width:
                    if pos[1] > self.y and pos[1] < self.y + self.height:
                        return True
                            
                return False

            def playSoundIfMouseIsOver(self, pos, sound):
                if self.isOver(pos):            
                    if not self.over:
                        click.play()
                        self.over = True
                else:
                    self.over = False




        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((700/2),(600/2))
        window.blit(TextSurf, TextRect)


        red = 255,255,255
        button1 = button(red,430,553,70,30,'')

        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if button1.isOver(pos):
                        click.play()
                        unpause()

       
            #gameDisplay.fill(white)
            green = (0, 0,15)
            pygame.display.update()
            clock.tick(15)






    # the buttons for the shop MENUUUU
    class move:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            pygame.draw.rect(window,self.color,self.rect)


    black = (0, 0, 0)      
    white = (250,250,250)
    check1 = move(20,-590,50,940,white)

    check11 = move(20,90,50,240,white)

    check2 = move(20,370,240,40,white)

    check3 = move(270,230,50,160,white)

    check4 = move(270,170,310,50,white)

    check5 = move(580,170,50,170,white)

    check6 = move(570,370,80,50,white)

    void = move(-4,-450,90,500,black)

    towerhit1 = move(660,350,80,80,white)




    class Wave:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
            self.font = pygame.font.Font("abya.ttf", 40)
            self.cash = 1
            self.cashtext = self.font.render("" + str(self.cash), True, (88, 214, 141))
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.cashtext,self.rect)


    Wave1 = Wave(207,24,50,50,white)


    moves = [Wave1,towerhit1,check1,check2,check3,check4,check5,check6,check11]


    # our fps
    fps = 60
    clock = pygame.time.Clock()



    class bg:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.speed = 2
            self.image = pygame.image.load("map.png")
            self.rect = pygame.Rect(x,y,height,width)
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.image,self.rect)

    white = (255,255,255)
    bg1 = bg(0,0,0,0,white)



    class shop:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.image = pygame.image.load("shop.png")
            self.rect = pygame.Rect(x,y,height,width)
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.image,self.rect)

    shop1 = shop(0,9100,50,0,white)



    class upgrade:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.image = pygame.image.load("upgrade.png")
            self.rect = pygame.Rect(x,y,height,width)
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.image,self.rect)

    upgrade21 = upgrade(0,9100,50,0,white)




    # my tower health
    class tower:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color  = color
            self.rect = pygame.Rect(x,y,height,width)
            self.hitbox = (self.x, self.y + 30, 46,60)
            self.health = 10
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            self.hitbox = (self.x + 32, self.y + 34, 46,60)
            pygame.draw.rect(window, (80, 161, 6), (self.hitbox[0], self.hitbox[1] - 90, 268 - (5 * (10 - self.health)), 39))

    srs = 80,161,6
    tower1 = tower(500,505,50,50,srs)

    class money:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
            self.font = pygame.font.Font("abya.ttf", 40)
            self.cash = 9
            self.cashtext = self.font.render("" + str(self.cash), True, (88, 214, 141))
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.cashtext,self.rect)


    money1 = money(380,24,50,50,white)


    class towertext:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.rect = pygame.Rect(x,y,height,width)
            self.font = pygame.font.Font("abya.ttf", 40)
            self.health_text = 100
            self.cashtext = self.font.render(str(self.health_text)  + "%" ,  True, (155,224,53))
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            window.blit(self.cashtext,self.rect)

    towertext1 = towertext(630,447,50,50,white)









    # our monster class
    class monster:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("monsta" + str(i) + ".png") for i in range(1, 5)]
            

            self.hite = [pygame.image.load("mhit" + str(i) + ".png") for i in range(1, 3)]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "hit"
            self.direction = "walk"
            self.anim_index = 0
            self.health = 10
            self.hit = False
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.cols = (self.x, self.y + 30, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk

          
            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hite
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 2990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]
            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)
            player_image = image_list[self.anim_index]
            if self.hit:
                self.hitbox = (self.x, self.y + 30, 60,60)
                pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 40, 10)) # NEW
                pygame.draw.rect(window, (169, 50, 38), (self.hitbox[0], self.hitbox[1] - 40, 40 - (5 * (10 - self.health)), 10))
                self.cols = (self.x, self.y + 30, 46,60)






    # our monster class
    class lime:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("h" + str(i) + ".png") for i in range(1, 7)]
            

            self.hite = [pygame.image.load("hurt" + str(i) + ".png") for i in range(1, 3)]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "hit"
            self.direction = "walk"
            self.anim_index = 0
            self.health = 10
            self.hit = False
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.cols = (self.x, self.y + 30, 46,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk

          
            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hite
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 2990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]
            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)
            player_image = image_list[self.anim_index]
            if self.hit:
                self.hitbox = (self.x, self.y + 30, 60,60)
                pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 40, 10)) # NEW
                pygame.draw.rect(window, (169, 50, 38), (self.hitbox[0], self.hitbox[1] - 40, 40 - (5 * (10 - self.health)), 10))
                self.cols = (self.x, self.y + 30, 46,60)






    # our monster class
    class turtle:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("tut" + str(i) + ".png") for i in range(1, 5)]
            

            self.hite = [pygame.image.load("hurtut" + str(i) + ".png") for i in range(1, 3)]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "hit"
            self.direction = "walk"
            self.anim_index = 0
            self.health = 10
            self.hit = False
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.cols = (self.x, self.y + 30, 60,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk

          
            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hite
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 2990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]
            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)
            player_image = image_list[self.anim_index]
            if self.hit:
                self.hitbox = (self.x, self.y + 30, 60,60)
                pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 40, 10)) # NEW
                pygame.draw.rect(window, (169, 50, 38), (self.hitbox[0], self.hitbox[1] - 40, 40 - (5 * (10 - self.health)), 10))
                self.cols = (self.x, self.y + 30, 46,60)













   # our monster class
    class orc:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("hy" + str(i) + ".png") for i in range(1, 7)]
            self.walk = [pygame.transform.scale(image,(image.get_width()+30,image.get_height()+30)) for image in self.walk]

            

            self.hite = [pygame.image.load("hurtut" + str(i) + ".png") for i in range(1, 3)]
            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "hit"
            self.direction = "walk"
            self.anim_index = 0
            self.health = 10
            self.hit = False
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.cols = (self.x, self.y + 30, 60,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk

          
            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hite
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 2990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]
            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)
            player_image = image_list[self.anim_index]
            if self.hit:
                self.hitbox = (self.x, self.y + 30, 60,60)
                pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 40, 10)) # NEW
                pygame.draw.rect(window, (169, 50, 38), (self.hitbox[0], self.hitbox[1] - 40, 40 - (5 * (10 - self.health)), 10))
                self.cols = (self.x, self.y + 30, 46,60)








   # our monster class
    class boss:
        def __init__(self,x,y,height,width,color):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.color = color
            self.walk = [pygame.image.load("boss" + str(i) + ".png") for i in range(1, 24)]
            self.walk = [pygame.transform.scale(image,(image.get_width()//4,image.get_height()//4)) for image in self.walk]

            

            self.hite = [pygame.image.load("bosshurt" + str(i) + ".png") for i in range(1, 13)]
            self.hite = [pygame.transform.scale(image,(image.get_width()//4,image.get_height()//4)) for image in self.hite]

            self.next_frame_time = 0
            self.fps = 60
            self.speed = 3
            self.clock = pygame.time.Clock()
            self.direction = "hit"
            self.direction = "walk"
            self.anim_index = 0
            self.health = 10
            self.hit = False
            self.hitbox = (self.x + -18, self.y, 46,60)
            self.cols = (self.x, self.y + 30, 60,60)
            self.rect = pygame.Rect(x,y,height,width)
        def get_rect(self):
            self.rect.topleft = (self.x,self.y)
            return self.rect
             

                
        def draw(self):
            self.rect.topleft = (self.x,self.y)
            if self.direction == "walk":
                self.clock.tick(self.fps)
                image_list = self.walk

          
            elif self.direction == "hit":
                self.clock.tick(self.fps)
                image_list = self.hite
                
                    

                    # Is it time to show the next animation frame?
            time_now = pygame.time.get_ticks()
            if ( time_now > self.next_frame_time ):
                        # set the time for the next animation-frame
                inter_frame_delay = 2990 // self.fps   
                self.next_frame_time = time_now + inter_frame_delay  # in the future
                        # move the current image to the next (with wrap-around)
                self.anim_index += 1
                if self.anim_index >= len( image_list ):
                    self.anim_index = 0
                                
            if self.anim_index >= len(image_list):
                self.anim_index = 0
            player_image = image_list[self.anim_index]
            player_rect = player_image.get_rect(center = self.get_rect().center)
            player_rect.centerx += 0
            player_rect.centery += -20
            window.blit(player_image, player_rect)
            player_image = image_list[self.anim_index]
            if self.hit:
                self.hitbox = (self.x, self.y + 30, 60,60)
                pygame.draw.rect(window, (23, 32, 42), (self.hitbox[0], self.hitbox[1] - 40, 40, 10)) # NEW
                pygame.draw.rect(window, (169, 50, 38), (self.hitbox[0], self.hitbox[1] - 40, 40 - (5 * (10 - self.health)), 10))
                self.cols = (self.x, self.y + 30, 46,60)




    

    monsters = []
    limes = []
    turtles = []
    orcs = []
    bosses = []
    level = ["  m                                                                     ",
             "                                                                      ",
             "    m                                                                      ",
             " m                                                                      ",
             "                                                                        ",
             "   m                                                                   ",
             "                                                                      ",
             "    m                                                                    ",
             " m                                                                     ","                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "   m                                                                     ",
             "                                                                        ",
             "m                                                                     ",
             "                                                                       ",
             "    m                                                                    ",
             "                                                                        ",
             " m                                                                      ",
             "                                                                     ",
             "                                                                        ",
             " m                                                                      ",

             "   m                                                                     ",
             "                                                                     ",
             "m                                                                      ",
      
             ]

    level2 = ["  m                                                                     ",
             "                                                                      ",
             "                                                                       ",
             "   m                                                                      ",
             "                                                                      ",
             " m                                                                     ",
             "                                                                      ",
             "m                                                                    ",
             "                                                                      ","                                                                      ",
             "   m                                                                   ",
             "                                                                      ",
             "  m                                                                     ",
             "                                                                        ",
             "m                                                                     ",
             "                                                                      ",
             "                                                                   ",
             "   m                                                                     ",
             "                                                                       ",
             "  m                                                                     ",
             "                                                                    ",
             " m                                                                      ",

             "   m                                                                     ",
             "                                                                     ",
             " m                                                                      ",
      
             ]



    level3 = ["  m                                                                     ",
             "                                                                      ",
             "                                                                       ",
             " m                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "  m                                                                    ",
             "                                                                      ","                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "  m                                                                     ",
             "                                                                        ",
             "    m                                                                     ",
             "                                                                      ",
             "                                                                   ",
             " m                                                                     ",
             "                                                                       ",
             "   m                                                                     ",
             "                                                                    ",
             " m                                                                      ",

             "m                                                                     ",
             "                                                                     ",
             "  m                                                                      ",
      
             ]





    level4 = ["  m                                                                     ",
             "                                                                      ",
             "                                                                       ",
             " m                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "  m                                                                    ",
             "                                                                      ","                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "  m                                                                     ",
             "                                                                        ",
             "    m                                                                     ",
             "                                                                      ",
             "                                                                   ",
             " m                                                                     ",
             "                                                                       ",
             "   m                                                                     ",
             "                                                                    ",
             " m                                                                      ",

             "m                                                                     ",
             "                                                                     ",
             "  m                                                                      ",
      
             ]







    level5 = ["                                                                       ",
             "m                                                                   ",
             "                                                                       ",
             "                                                                       ",
             "                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "                                                                      ","                                                                      ",
             "                                                                      ",
             "                                                                      ",
             "                                                                       ",
             "                                                                        ",
             "                                                                         ",
             "                                                                      ",
             "                                                                   ",
             "                                                                      ",
             "                                                                       ",
             "                                                                        ",
             "                                                                    ",
             "                                                                       ",

             "                                                                     ",
             "                                                                    ",
             "                                                                        ",
      
             ]

    
    for iy, row in enumerate(level):
        for ix, col in enumerate(row):
            if col == "m":
                new_platforms = monster(ix*9.8, iy*-29, 60,60,(255,255,255))
                monsters.append(new_platforms)

    for iy, row in enumerate(level2):
        for ix, col in enumerate(row):
            if col == "m":
                new_platforms = lime(ix*9.8, iy*-29, 60,60,(255,255,255))
                limes.append(new_platforms)




    for iy, row in enumerate(level3):
        for ix, col in enumerate(row):
            if col == "m":
                new_platforms = turtle(ix*9.8, iy*-29, 60,60,(255,255,255))
                turtles.append(new_platforms)





    for iy, row in enumerate(level4):
        for ix, col in enumerate(row):
            if col == "m":
                new_platforms = orc(ix*9.8, iy*-29, 60,60,(255,255,255))
                orcs.append(new_platforms)
                


    for iy, row in enumerate(level5):
        for ix, col in enumerate(row):
            if col == "m":
                new_platforms = boss(ix*9.8, iy*-29, 60,60,(255,255,255))
                bosses.append(new_platforms)

                           
    # scores


    # auto cash timer

            



    # our invisible score
    font = pygame.font.Font("abya.ttf", 60)
    score = 0
    scoretext = font.render("Enemys ?/" + str(score), True, (255,255,255))
    scorerect = scoretext.get_rect()
    scorerect.center = ((620,150))


    # our tower mouse image
    Tower_image = pygame.image.load('tower1.png').convert_alpha()
    Tower_image = pygame.transform.scale(Tower_image,(Tower_image.get_width()-40,Tower_image.get_height()-40))

    # our tower mouse image
    Tower_image2 = pygame.image.load('tower2.png').convert_alpha()
    Tower_image2 = pygame.transform.scale(Tower_image2,(Tower_image2.get_width()-40,Tower_image2.get_height()-40))


    # our tower mouse image
    Tower_image3 = pygame.image.load('tower3.png').convert_alpha()
    Tower_image3 = pygame.transform.scale(Tower_image3,(Tower_image3.get_width()-40,Tower_image3.get_height()-40))


    # our tower mouse image
    Tower_image4 = pygame.image.load('tower4.png').convert_alpha()
    Tower_image4 = pygame.transform.scale(Tower_image4,(Tower_image4.get_width()-40,Tower_image4.get_height()-40))



    # this here will be our shooting bullets
    class enemyboolss:
        def __init__(self, x, y,color, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.health = 10
            self.hitbox = (self.x + -20, self.y + 30, 5, 5)
               #-------------------------------------------------------
                # Make a Reference Copy of the bitmap for later rotation
            self.shootsright = pygame.image.load("50.png")

            self.shootsright = pygame.transform.scale(self.shootsright,(self.shootsright.get_width()//5,self.shootsright.get_height()//5))        
         

            self.image = self.shootsright
            self.rect  = self.image.get_rect(center = (self.x, self.y))
            self.look_at_pos = (self.x, self.y)

            self.angle = 15
            self.hitbox = (self.x + 20, self.y, 18,10)
            self.isLookingAtPlayer = False
            self.look_at_pos = (x,y)
        def draw(self,window):
            self.rect.topleft = (self.x,self.y)
            self.rect = self.shootsright.get_rect(center = (self.x, self.y))

            dx = self.look_at_pos[0] - self.rect.centerx
            dy = self.look_at_pos[1] - self.rect.centery 
            angle = (380/math.pi) * math.atan2(dx, dy)
            self.image = pygame.transform.rotate(self.shootsright, angle)
            self.rect  = self.image.get_rect(center = self.rect.center)

            window.blit(self.image, self.rect)



            self.rect.topleft = (self.x,self.y)
            player_rect = self.shootsright.get_rect(center = self.rect.center) 
            player_rect.centerx += 0 # 10 is just an example
            player_rect.centery += 0 # 15 is just an example
            self.hitbox = (self.x -10, self.y + 8, 15, 15) # NEW

        def lookAt( self, coordinate ):
            self.look_at_pos = coordinate





    # this here will be our shooting bullets
    class enemyboolss2:
        def __init__(self, x, y,color, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.health = 10
            self.hitbox = (self.x + -20, self.y + 30, 5, 5)
               #-------------------------------------------------------
                # Make a Reference Copy of the bitmap for later rotation
            self.shootsright = pygame.image.load("45.png")

            self.shootsright = pygame.transform.scale(self.shootsright,(self.shootsright.get_width()//5,self.shootsright.get_height()//5))        
         

            self.image = self.shootsright
            self.rect  = self.image.get_rect(center = (self.x, self.y))
            self.look_at_pos = (self.x, self.y)

            self.angle = 15
            self.hitbox = (self.x + 20, self.y, 18,10)
            self.isLookingAtPlayer = False
            self.look_at_pos = (x,y)
        def draw(self,window):
            self.rect.topleft = (self.x,self.y)
            self.rect = self.shootsright.get_rect(center = (self.x, self.y))

            dx = self.look_at_pos[0] - self.rect.centerx
            dy = self.look_at_pos[1] - self.rect.centery 
            angle = (380/math.pi) * math.atan2(dx, dy)
            self.image = pygame.transform.rotate(self.shootsright, angle)
            self.rect  = self.image.get_rect(center = self.rect.center)

            window.blit(self.image, self.rect)



            self.rect.topleft = (self.x,self.y)
            player_rect = self.shootsright.get_rect(center = self.rect.center) 
            player_rect.centerx += 0 # 10 is just an example
            player_rect.centery += 0 # 15 is just an example
            self.hitbox = (self.x -10, self.y + 8, 15, 15) # NEW

        def lookAt( self, coordinate ):
            self.look_at_pos = coordinate






    # this here will be our shooting bullets
    class enemyboolss3:
        def __init__(self, x, y,color, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.health = 10
            self.hitbox = (self.x + -20, self.y + 30, 5, 5)
               #-------------------------------------------------------
                # Make a Reference Copy of the bitmap for later rotation
            self.shootsright = pygame.image.load("49.png")

            self.shootsright = pygame.transform.scale(self.shootsright,(self.shootsright.get_width()//5,self.shootsright.get_height()//5))        
         

            self.image = self.shootsright
            self.rect  = self.image.get_rect(center = (self.x, self.y))
            self.look_at_pos = (self.x, self.y)

            self.angle = 15
            self.hitbox = (self.x + 20, self.y, 18,10)
            self.isLookingAtPlayer = False
            self.look_at_pos = (x,y)
        def draw(self,window):
            self.rect.topleft = (self.x,self.y)
            self.rect = self.shootsright.get_rect(center = (self.x, self.y))

            dx = self.look_at_pos[0] - self.rect.centerx
            dy = self.look_at_pos[1] - self.rect.centery 
            angle = (380/math.pi) * math.atan2(dx, dy)
            self.image = pygame.transform.rotate(self.shootsright, angle)
            self.rect  = self.image.get_rect(center = self.rect.center)

            window.blit(self.image, self.rect)



            self.rect.topleft = (self.x,self.y)
            player_rect = self.shootsright.get_rect(center = self.rect.center) 
            player_rect.centerx += 0 # 10 is just an example
            player_rect.centery += 0 # 15 is just an example
            self.hitbox = (self.x -10, self.y + 8, 15, 15) # NEW

        def lookAt( self, coordinate ):
            self.look_at_pos = coordinate







    # this here will be our shooting bullets
    class enemyboolss4:
        def __init__(self, x, y,color, xspeed, yspeed):
            self.x = x
            self.y = y
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.health = 10
            self.hitbox = (self.x + -20, self.y + 30, 5, 5)
               #-------------------------------------------------------
                # Make a Reference Copy of the bitmap for later rotation
            self.shootsright = pygame.image.load("51.png")

            self.shootsright = pygame.transform.scale(self.shootsright,(self.shootsright.get_width()//5,self.shootsright.get_height()//5))        
         

            self.image = self.shootsright
            self.rect  = self.image.get_rect(center = (self.x, self.y))
            self.look_at_pos = (self.x, self.y)

            self.angle = 15
            self.hitbox = (self.x + 20, self.y, 18,10)
            self.isLookingAtPlayer = False
            self.look_at_pos = (x,y)
        def draw(self,window):
            self.rect.topleft = (self.x,self.y)
            self.rect = self.shootsright.get_rect(center = (self.x, self.y))

            dx = self.look_at_pos[0] - self.rect.centerx
            dy = self.look_at_pos[1] - self.rect.centery 
            angle = (380/math.pi) * math.atan2(dx, dy)
            self.image = pygame.transform.rotate(self.shootsright, angle)
            self.rect  = self.image.get_rect(center = self.rect.center)

            window.blit(self.image, self.rect)



            self.rect.topleft = (self.x,self.y)
            player_rect = self.shootsright.get_rect(center = self.rect.center) 
            player_rect.centerx += 0 # 10 is just an example
            player_rect.centery += 0 # 15 is just an example
            self.hitbox = (self.x -10, self.y + 8, 15, 15) # NEW

        def lookAt( self, coordinate ):
            self.look_at_pos = coordinate




    shootsright = []

    shootsright2 = []

    shootsright3 = []

    shootsright4 = []

    shootsright5 = []


    shootsright6 = []

    shootsright7 = []

    shootsright8 = []

    shootsright9 = []

    shootsright10 = []


    shootsright11 = []

    shootsright12 = []

    shootsright13 = []

    shootsright14 = []

    shootsright15 = []
                
                
                

    shootsright16 = []

    shootsright17 = []

    shootsright18 = []

    shootsright19 = []

    shootsright20 = []

    example_list = [ [shootsright,shootsright2] ]

    
    particles = []
    visible = False

    place_tower = False

    place_tower2 = False

    place_tower3 = False

    place_tower4 = False

    def bullet_draw():
        # enemy bullets
        for shootss in shootsright:
            shootss.draw(window)
        for shootss2 in shootsright2:
            shootss2.draw(window)
        for shootss3 in shootsright3:
            shootss3.draw(window)
        for shootss4 in shootsright4:
            shootss4.draw(window)
        for shootss5 in shootsright5:
            shootss5.draw(window)


        # enemy bullets
        for shootss6 in shootsright6:
            shootss6.draw(window)
        for shootss7 in shootsright7:
            shootss7.draw(window)
        for shootss8 in shootsright8:
            shootss8.draw(window)
        for shootss9 in shootsright9:
            shootss9.draw(window)
        for shootss10 in shootsright10:
            shootss10.draw(window)



        # enemy bullets
        for shootss11 in shootsright11:
            shootss11.draw(window)
        for shootss12 in shootsright12:
            shootss12.draw(window)
        for shootss13 in shootsright13:
            shootss13.draw(window)
        for shootss14 in shootsright14:
            shootss14.draw(window)
        for shootss15 in shootsright15:
            shootss15.draw(window)


        # enemy bullets

        for shootss16 in shootsright16:
            shootss16.draw(window)
        for shootss17 in shootsright17:
            shootss17.draw(window)
        for shootss18 in shootsright18:
            shootss18.draw(window)
        for shootss19 in shootsright19:
            shootss19.draw(window)

        for shootss20 in shootsright20:
            shootss20.draw(window)

    def enemydraw():

        
        for lime in limes:
            lime.draw()
            
        for monster in monsters:
            monster.draw()


        for turtle in turtles:
            turtle.draw()


        for orc in orcs:
            orc.draw()


        for boss in bosses:
            boss.draw()



    def redraw():

        for move in moves:
            move.draw()


        towerhit1.draw()       
        window.fill((35, 155, 86))



        
        bg1.draw()
        
        enemydraw()


        money1.draw()

        upgrade21.draw()
        shop1.draw()


        # DRAW OUR VOID
        #    to hide our enemys:
        void.draw()

        
        tower1.draw()

        # my tower health
        towertext1.draw()
        
        bullet_draw()



    # display our towers
        if place_tower:
            pos = pygame.mouse.get_pos()
            window.blit(Tower_image, Tower_image.get_rect(center = pos))

        if place_tower2:
            pos = pygame.mouse.get_pos()
            window.blit(Tower_image2, Tower_image2.get_rect(center = pos))

        if place_tower3:
            pos = pygame.mouse.get_pos()        
            window.blit(Tower_image3, Tower_image3.get_rect(center = pos))

        if place_tower4:
            pos = pygame.mouse.get_pos()        
            window.blit(Tower_image4, Tower_image4.get_rect(center = pos))


        for towerdrawn1 in particles:
            towerdrawn1.draw()

        Wave1.draw()



        
    def bullet_right():
        for shootss in shootsright:
            shootss.x -= bg1.speed
         
        for shootss2 in shootsright2:
            shootss2.x -= bg1.speed

        for shootss3 in shootsright3:
            shootss3.x -= bg1.speed

        for shootss4 in shootsright4:
            shootss4.x -= bg1.speed

        for shootss5 in shootsright5:
            shootss5.x -= bg1.speed

        for shootss6 in shootsright6:
            shootss6.x -= bg1.speed
         
        for shootss7 in shootsright7:
            shootss7.x -= bg1.speed

        for shootss8 in shootsright8:
            shootss8.x -= bg1.speed

        for shootss9 in shootsright9:
            shootss9.x -= bg1.speed

        for shootss10 in shootsright10:
            shootss10.x -= bg1.speed

         
        for shootss11 in shootsright11:
            shootss11.x -= bg1.speed

        for shootss12 in shootsright12:
            shootss12.x -= bg1.speed

        for shootss13 in shootsright13:
            shootss13.x -= bg1.speed

        for shootss14 in shootsright14:
            shootss14.x -= bg1.speed

        for shootss15 in shootsright15:
            shootss15.x -= bg1.speed



# -------------------------------------- enemy camera movement
    def enemy_right():
        for monster in monsters:
            monster.x -= bg1.speed

        for lime in limes:
            lime.x -= bg1.speed

        for turtle in turtles:
            turtle.x -= bg1.speed

        for orc in orcs:
            orc.x -= bg1.speed

        for boss in bosses:
            boss.x -= bg1.speed
            

    def enemy_left():
        for monster in monsters:
            monster.x += bg1.speed

        for lime in limes:
            lime.x += bg1.speed

        for turtle in turtles:
            turtle.x += bg1.speed

        for orc in orcs:
            orc.x += bg1.speed

        for boss in bosses:
            boss.x += bg1.speed

            
    def enemy_up():
        for monster in monsters:
            monster.y += bg1.speed

        for lime in limes:
            lime.y += bg1.speed

        for turtle in turtles:
            turtle.y += bg1.speed

        for orc in orcs:
            orc.y += bg1.speed

        for boss in bosses:
            boss.y += bg1.speed

            

    def enemy_down():
        for monster in monsters:
            monster.y -= bg1.speed

        for lime in limes:
            lime.y -= bg1.speed

        for turtle in turtles:
            turtle.y -= bg1.speed

        for orc in orcs:
            orc.y -= bg1.speed

        for boss in bosses:
            boss.y -= bg1.speed

# -------------------------------------- enemy camera movement

        

    def bullet_left():
        for shootss in shootsright:
            shootss.x += bg1.speed

        for shootss2 in shootsright2:
            shootss2.x += bg1.speed

        for shootss3 in shootsright3:
            shootss3.x += bg1.speed

        for shootss4 in shootsright4:
            shootss4.x += bg1.speed

        for shootss5 in shootsright5:
            shootss5.x += bg1.speed

        
        for shootss6 in shootsright6:
            shootss6.x += bg1.speed
         
        for shootss7 in shootsright7:
            shootss7.x += bg1.speed

        for shootss8 in shootsright8:
            shootss8.x += bg1.speed

        for shootss9 in shootsright9:
            shootss9.x += bg1.speed

        for shootss10 in shootsright10:
            shootss10.x += bg1.speed

         
        for shootss11 in shootsright11:
            shootss11.x += bg1.speed

        for shootss12 in shootsright12:
            shootss12.x += bg1.speed

        for shootss13 in shootsright13:
            shootss13.x += bg1.speed

        for shootss14 in shootsright14:
            shootss14.x += bg1.speed

        for shootss15 in shootsright15:
            shootss15.x += bg1.speed


            
    def bullet_up():
        for shootss in shootsright:
            shootss.y += bg1.speed
         
        for shootss2 in shootsright2:
            shootss2.y += bg1.speed


        for shootss3 in shootsright3:
            shootss3.y += bg1.speed

        for shootss4 in shootsright4:
            shootss4.y += bg1.speed

        for shootss5 in shootsright5:
            shootss5.y += bg1.speed

            


        for shootss6 in shootsright6:
            shootss6.y += bg1.speed
         
        for shootss7 in shootsright7:
            shootss7.y += bg1.speed

        for shootss8 in shootsright8:
            shootss8.y += bg1.speed

        for shootss9 in shootsright9:
            shootss9.y += bg1.speed

        for shootss10 in shootsright10:
            shootss10.y += bg1.speed

         
        for shootss11 in shootsright11:
            shootss11.y += bg1.speed

        for shootss12 in shootsright12:
            shootss12.y += bg1.speed

        for shootss13 in shootsright13:
            shootss13.y += bg1.speed

        for shootss14 in shootsright14:
            shootss14.y += bg1.speed

        for shootss15 in shootsright15:
            shootss15.y += bg1.speed

            
    def bullet_down():
        for shootss in shootsright:
            shootss.y -= bg1.speed


        for shootss2 in shootsright2:
            shootss2.y -= bg1.speed
         

        for shootss3 in shootsright3:
            shootss3.y -= bg1.speed

        for shootss4 in shootsright4:
            shootss4.y -= bg1.speed

        for shootss5 in shootsright5:
            shootss5.y -= bg1.speed

            





        for shootss6 in shootsright6:
            shootss6.y -= bg1.speed
         
        for shootss7 in shootsright7:
            shootss7.y -= bg1.speed

        for shootss8 in shootsright8:
            shootss8.y -= bg1.speed

        for shootss9 in shootsright9:
            shootss9.y -= bg1.speed

        for shootss10 in shootsright10:
            shootss10.y -= bg1.speed

         
        for shootss11 in shootsright11:
            shootss11.y -= bg1.speed

        for shootss12 in shootsright12:
            shootss12.y -= bg1.speed

        for shootss13 in shootsright13:
            shootss13.y -= bg1.speed

        for shootss14 in shootsright14:
            shootss14.y -= bg1.speed

        for shootss15 in shootsright15:
            shootss15.y -= bg1.speed
            
    def keyevents():
        if keys[pygame.K_RIGHT]:
            bg1.x -= bg1.speed

            enemy_right()

            # tower bullets
            bullet_right()

          


            # OUR INVISIBLE MOVING RECT 
            for move in moves:
                move.x -= bg1.speed

            # our money rect
            money1.x -= bg1.speed

            # OUR BUTTONS
            for button in buttons:
                button.x -= bg1.speed

            # our shop stop it from scrolling
            shop1.x -= bg1.speed

            # my tower health
            towertext1.x -= bg1.speed
            
            # my tower actual health bar
            tower1.x -= bg1.speed

            # our void TO HIDE OUR ENEMYAS
            void.x -= bg1.speed
            
            for shootss in shootsright:
                shootss.x -= bg1.speed
                
            # our  particles for our first 10 dollar tower image
            for towerdrawn1 in particles:
                towerdrawn1.x -= bg1.speed


                        
            upgrade21.x -= bg1.speed

            
        if keys[pygame.K_LEFT]:
            bg1.x += bg1.speed

            # my tower bullets
            bullet_left()
             
            enemy_left()
                
            for move in moves:
                move.x += bg1.speed

            money1.x += bg1.speed

            # OUR BUTTONS
            for button in buttons:
                button.x += bg1.speed

            # our shop stop it from scrolling
            shop1.x += bg1.speed


            # my tower health
            towertext1.x += bg1.speed
            # my tower actual health bar
            tower1.x += bg1.speed


            # our void TO HIDE OUR ENEMYAS
            void.x += bg1.speed

                
            # our  particles for our first 10 dollar tower image
            for towerdrawn1 in particles:
                towerdrawn1.x += bg1.speed

            upgrade21.x += bg1.speed
                
        if keys[pygame.K_UP]:
            bg1.y += bg1.speed


            # shooOOT
            bullet_up()


            enemy_up()

            for move in moves:
                move.y += bg1.speed

            money1.y += bg1.speed

            # OUR BUTTONS
            for button in buttons:
                button.y += bg1.speed

            # our shop stop it from scrolling
            shop1.y += bg1.speed
            
            # my tower health
            towertext1.y += bg1.speed
            # my tower actual health bar
            tower1.y += bg1.speed            


            # our void TO HIDE OUR ENEMYAS
            void.y += bg1.speed
                

            # our  particles for our first 10 dollar tower image
            for towerdrawn1 in particles:
                towerdrawn1.y += bg1.speed


            upgrade21.y += bg1.speed

        if keys[pygame.K_DOWN]:
            bg1.y -= bg1.speed

            # all my tower bullets
            bullet_down()

             


            enemy_down()

            for move in moves:
                move.y -= bg1.speed

            money1.y -= bg1.speed
            
            # OUR BUTTONS
            for button in buttons:
                button.y -= bg1.speed

            # our shop stop it from scrolling
            shop1.y -= bg1.speed

            # my tower health
            towertext1.y -= bg1.speed

            # my tower actual health bar
            tower1.y -= bg1.speed


            # our void TO HIDE OUR ENEMYAS
            void.y -= bg1.speed

            # our  particles for our first 10 dollar tower image
            for towerdrawn1 in particles:
                towerdrawn1.y -= bg1.speed

            upgrade21.y -= bg1.speed

      

    def checkpoints():
        if check1.rect.colliderect(monster.rect):
            monster.y += 0.6

                
        if check2.rect.colliderect(monster.rect):
            monster.x += 0.6

        if check3.rect.colliderect(monster.rect):
            monster.y -= 0.6

        if check4.rect.colliderect(monster.rect):
            monster.x += 0.6

        if check5.rect.colliderect(monster.rect):
            monster.y += 0.6

        if check6.rect.colliderect(monster.rect):
            monster.x += 0.6



        # what happens if our monster hits our tower?
        if towerhit1.rect.colliderect(monster.rect):        
            if tower1.health > -42:
                monster.hit = False
                tower1.health -= 2
                towertext1.health_text -= 2
                towertext1.cashtext = towertext1.font.render(str(towertext1.health_text)  + "%" ,  True, (88, 214, 141))
                monster.x = void.x + 20 
                monster.y = void.y + 200






    def checkpoints2():
        if check1.rect.colliderect(lime.rect):
            lime.y += 0.6

                
        if check2.rect.colliderect(lime.rect):
            lime.x += 0.6

        if check3.rect.colliderect(lime.rect):
            lime.y -= 0.6

        if check4.rect.colliderect(lime.rect):
            lime.x += 0.6

        if check5.rect.colliderect(lime.rect):
            lime.y += 0.6

        if check6.rect.colliderect(lime.rect):
            lime.x += 0.6



        # what happens if our monster hits our tower?
        if towerhit1.rect.colliderect(lime.rect):        
            if tower1.health > -42:
                lime.hit = False
                tower1.health -= 1
                towertext1.health_text -= 1
                towertext1.cashtext = towertext1.font.render(str(towertext1.health_text)  + "%" ,  True, (88, 214, 141))
                lime.x = void.x + 20 
                lime.y = void.y + 200






    def checkpoints3():
        if check1.rect.colliderect(turtle.rect):
            turtle.y += 0.3

                
        if check2.rect.colliderect(turtle.rect):
            turtle.x += 0.3

        if check3.rect.colliderect(turtle.rect):
            turtle.y -= 0.3

        if check4.rect.colliderect(turtle.rect):
            turtle.x += 0.3

        if check5.rect.colliderect(turtle.rect):
            turtle.y += 0.3

        if check6.rect.colliderect(turtle.rect):
            turtle.x += 0.3



        # what happens if our monster hits our tower?
        if towerhit1.rect.colliderect(turtle.rect):        
            if tower1.health > -42:
                lime.hit = False
                tower1.health -= 5
                towertext1.health_text -= 5
                towertext1.cashtext = towertext1.font.render(str(towertext1.health_text)  + "%" ,  True, (88, 214, 141))
                turtle.x = void.x + 20 
                turtle.y = void.y + 200









    def checkpoints4():
        if check1.rect.colliderect(orc.rect):
            orc.y += 0.8

                
        if check2.rect.colliderect(orc.rect):
            orc.x += 0.8

        if check3.rect.colliderect(orc.rect):
            orc.y -= 0.8

        if check4.rect.colliderect(orc.rect):
            orc.x += 0.8

        if check5.rect.colliderect(orc.rect):
            orc.y += 0.8

        if check6.rect.colliderect(orc.rect):
            orc.x += 0.8



        # what happens if our monster hits our tower?
        if towerhit1.rect.colliderect(orc.rect):        
            if tower1.health > -42:
                lime.hit = False
                tower1.health -= 1
                towertext1.health_text -= 1
                towertext1.cashtext = towertext1.font.render(str(towertext1.health_text)  + "%" ,  True, (88, 214, 141))
                orc.x = void.x + 20 
                orc.y = void.y + 200














    def checkpoints5():
        if check1.rect.colliderect(boss.rect):
            boss.y += 0.7

                
        if check2.rect.colliderect(boss.rect):
            boss.x += 0.7

        if check3.rect.colliderect(boss.rect):
            boss.y -= 0.7

        if check4.rect.colliderect(boss.rect):
            boss.x += 0.7

        if check5.rect.colliderect(boss.rect):
            boss.y += 0.7

        if check6.rect.colliderect(boss.rect):
            boss.x += 0.7



        # what happens if our monster hits our tower?
        if towerhit1.rect.colliderect(boss.rect):        
            if tower1.health > -42:
                lime.hit = False
                tower1.health -= 100
                towertext1.health_text -= 1
                towertext1.cashtext = towertext1.font.render(str(towertext1.health_text)  + "%" ,  True, (88, 214, 141))
                orc.x = void.x + 20 
                orc.y = void.y + 200























# for the lime enemies:
    def boss_collid1():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 160:
            for boss in bosses:
                for shootss in shootsright:
                    if boss.rect.colliderect(shootss.hitbox):
                        boss.hit = True
                        hit.play
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -=  00.1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss in shootsright:
                    if boss.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for boss in bosses:
                for shootss2 in shootsright2:
                    if boss.rect.colliderect(shootss2.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -=  00.1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss2 in shootsright2:
                    if boss.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for boss in bosses:
                for shootss3 in shootsright3:
                    if boss.rect.colliderect(shootss3.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss3 in shootsright3:
                    if boss.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for boss in bosses:
                for shootss4 in shootsright4:
                    if boss.rect.colliderect(shootss4.hitbox):
                        boss.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss4 in shootsright4:
                    if boss.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for boss in bosses:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        bosses.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss5 in shootsright5:
                    if boss.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def boss_collid2():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 0:
            
            for boss in bosses:
                for shootss6 in shootsright6:
                    if boss.rect.colliderect(shootss6.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss6 in shootsright6:
                    if boss.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for boss in bosses:
                for shootss7 in shootsright7:
                    if boss.rect.colliderect(shootss7.hitbox):
                        boss.hit = True
                        hit.play
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss7 in shootsright7:
                    if boss.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for boss in bosses:
                for shootss8 in shootsright8:
                    if boss.rect.colliderect(shootss8.hitbox):
                        turtle.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss8 in shootsright8:
                    if boss.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for boss in bosses:
                for shootss9 in shootsright9:
                    if boss.rect.colliderect(shootss9.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss9 in shootsright9:
                    if boss.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for boss in bosses:
                for shootss10 in shootsright10:
                    if boss.rect.colliderect(shootss10.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 00.5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss11 in shootsright10:
                    if boss.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def boss_collid3():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x + 170:
            for boss in bosses:
                for shootss11 in shootsright11:
                    if boss.rect.colliderect(shootss11.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 2
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss11 in shootsright11:
                    if boss.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for boss in bosses:
                for shootss12 in shootsright12:
                    if boss.rect.colliderect(shootss12.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 2
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss12 in shootsright12:
                    if boss.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for boss in bosses:
                for shootss13 in shootsright13:
                    if boss.rect.colliderect(shootss13.hitbox):
                        monster.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 2
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss13 in shootsright13:
                    if boss.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for boss in bosses:
                for shootss14 in shootsright14:
                    if boss.rect.colliderect(shootss14.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 2
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss14 in shootsright14:
                    if boss.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for boss in bosses:
                for shootss15 in shootsright15:
                    if boss.rect.colliderect(shootss15.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 2
                            
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss15 in shootsright15:
                    if boss.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def boss_collid4():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x + 330:
            for boss in bosses:
                for shootss16 in shootsright16:
                    if boss.rect.colliderect(shootss16.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 9
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss16 in shootsright16:
                    if boss.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for boss in bosses:
                for shootss17 in shootsright17:
                    if boss.rect.colliderect(shootss17.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 9
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss17 in shootsright17:
                    if boss.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for boss in bosses:
                for shootss18 in shootsright18:
                    if boss.rect.colliderect(shootss18.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss18 in shootsright18:
                    if boss.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for boss in bosses:
                for shootss19 in shootsright19:
                    if boss.rect.colliderect(shootss19.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss19 in shootsright19:
                    if boss.rect.colliderect(shootss19.hitbox):
                        shootsright20.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for boss in bosses:
                for shootss20 in shootsright20:
                    if boss.rect.colliderect(shootss20.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 5
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss20 in shootsright20:
                    if boss.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))


















# for the lime enemies:
    def boss_upgrade1():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 9000:
            for boss in bosses:
                for shootss in shootsright:
                    if boss.rect.colliderect(shootss.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 0.9
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss in shootsright:
                    if boss.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for boss in bosses:
                for shootss2 in shootsright2:
                    if boss.rect.colliderect(shootss2.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 0.9
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss2 in shootsright2:
                    if boss.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for boss in bosses:
                for shootss3 in shootsright3:
                    if boss.rect.colliderect(shootss3.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 0.9
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            money1.cash += 1
                            boss.health += 8
                            boss.hit = False


            for boss in bosses:
                for shootss3 in shootsright3:
                    if boss.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for boss in bosses:
                for shootss4 in shootsright4:
                    if boss.rect.colliderect(shootss4.hitbox):
                        boss.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 0.9
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss4 in shootsright4:
                    if boss.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for boss in bosses:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        bosses.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 0.9
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss5 in shootsright5:
                    if boss.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def boss_upgrade2():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 9000:
            
            for boss in bosses:
                for shootss6 in shootsright6:
                    if boss.rect.colliderect(shootss6.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss6 in shootsright6:
                    if boss.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for boss in bosses:
                for shootss7 in shootsright7:
                    if boss.rect.colliderect(shootss7.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss7 in shootsright7:
                    if boss.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for boss in bosses:
                for shootss8 in shootsright8:
                    if boss.rect.colliderect(shootss8.hitbox):
                        turtle.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss8 in shootsright8:
                    if boss.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for boss in bosses:
                for shootss9 in shootsright9:
                    if boss.rect.colliderect(shootss9.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss9 in shootsright9:
                    if boss.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for boss in bosses:
                for shootss10 in shootsright10:
                    if boss.rect.colliderect(shootss10.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 1
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss11 in shootsright10:
                    if boss.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def boss_upgrade3():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x - 9000:
            for boss in bosses:
                for shootss11 in shootsright11:
                    if boss.rect.colliderect(shootss11.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 3
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss11 in shootsright11:
                    if boss.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for boss in bosses:
                for shootss12 in shootsright12:
                    if boss.rect.colliderect(shootss12.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 3
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss12 in shootsright12:
                    if boss.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for boss in bosses:
                for shootss13 in shootsright13:
                    if boss.rect.colliderect(shootss13.hitbox):
                        monster.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 3
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss13 in shootsright13:
                    if boss.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for boss in bosses:
                for shootss14 in shootsright14:
                    if boss.rect.colliderect(shootss14.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 3
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss14 in shootsright14:
                    if boss.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for boss in bosses:
                for shootss15 in shootsright15:
                    if boss.rect.colliderect(shootss15.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 3
                            
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss15 in shootsright15:
                    if boss.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def boss_upgrade4():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x - 9000:
            for boss in bosses:
                for shootss16 in shootsright16:
                    if boss.rect.colliderect(shootss16.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 8
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 9
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss16 in shootsright16:
                    if boss.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for boss in bosses:
                for shootss17 in shootsright17:
                    if boss.rect.colliderect(shootss17.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 8
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 9
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss17 in shootsright17:
                    if boss.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for boss in bosses:
                for shootss18 in shootsright18:
                    if boss.rect.colliderect(shootss18.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 8
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss18 in shootsright18:
                    if boss.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for boss in bosses:
                for shootss19 in shootsright19:
                    if boss.rect.colliderect(shootss19.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 8
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss19 in shootsright19:
                    if boss.rect.colliderect(shootss19.hitbox):
                        shootsright20.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for boss in bosses:
                for shootss20 in shootsright20:
                    if boss.rect.colliderect(shootss20.hitbox):
                        boss.hit = True
                        hit.play()
                        boss.direction = "hit"
                        if boss.health > 2:
                            boss.health -= 8
                        else:
                            boss.x = void.x + 20 
                            boss.y = void.y + 200
                            boss.health += 8
                            money1.cash += 1
                            boss.hit = False


            for boss in bosses:
                for shootss20 in shootsright20:
                    if boss.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))













































# for the lime enemies:
    def orc_collid1():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 160:
            for orc in orcs:
                for shootss in shootsright:
                    if orc.rect.colliderect(shootss.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -=  0.1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss in shootsright:
                    if orc.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for orc in orcs:
                for shootss2 in shootsright2:
                    if orc.rect.colliderect(shootss2.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -=  0.1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss2 in shootsright2:
                    if orc.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for orc in orcs:
                for shootss3 in shootsright3:
                    if orc.rect.colliderect(shootss3.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss3 in shootsright3:
                    if orc.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for orc in orcs:
                for shootss4 in shootsright4:
                    if orc.rect.colliderect(shootss4.hitbox):
                        orc.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss4 in shootsright4:
                    if orc.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for orc in orcs:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def orc_collid2():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 0:
            
            for orc in orcs:
                for shootss6 in shootsright6:
                    if orc.rect.colliderect(shootss6.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss6 in shootsright6:
                    if orc.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for orc in orcs:
                for shootss7 in shootsright7:
                    if orc.rect.colliderect(shootss7.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss7 in shootsright7:
                    if orc.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for orc in orcs:
                for shootss8 in shootsright8:
                    if orc.rect.colliderect(shootss8.hitbox):
                        turtle.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss8 in shootsright8:
                    if orc.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for orc in orcs:
                for shootss9 in shootsright9:
                    if orc.rect.colliderect(shootss9.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss9 in shootsright9:
                    if orc.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for orc in orcs:
                for shootss10 in shootsright10:
                    if orc.rect.colliderect(shootss10.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 0.3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss11 in shootsright10:
                    if orc.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def orc_collid3():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x + 170:
            for orc in orcs:
                for shootss11 in shootsright11:
                    if orc.rect.colliderect(shootss11.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss11 in shootsright11:
                    if orc.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for orc in orcs:
                for shootss12 in shootsright12:
                    if orc.rect.colliderect(shootss12.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss12 in shootsright12:
                    if orc.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for orc in orcs:
                for shootss13 in shootsright13:
                    if orc.rect.colliderect(shootss13.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss13 in shootsright13:
                    if orc.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for orc in orcs:
                for shootss14 in shootsright14:
                    if orc.rect.colliderect(shootss14.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 1
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss14 in shootsright14:
                    if orc.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for orc in orcs:
                for shootss15 in shootsright15:
                    if orc.rect.colliderect(shootss15.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 1
                            
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss15 in shootsright15:
                    if orc.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def orc_collid4():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x + 330:
            for orc in orcs:
                for shootss16 in shootsright16:
                    if orc.rect.colliderect(shootss16.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 10
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 9
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss16 in shootsright16:
                    if orc.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for orc in orcs:
                for shootss17 in shootsright17:
                    if orc.rect.colliderect(shootss17.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 10
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 9
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss17 in shootsright17:
                    if orc.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for orc in orcs:
                for shootss18 in shootsright18:
                    if orc.rect.colliderect(shootss18.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss18 in shootsright18:
                    if orc.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for orc in orcs:
                for shootss19 in shootsright19:
                    if orc.rect.colliderect(shootss19.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss19 in shootsright19:
                    if orc.rect.colliderect(shootss19.hitbox):
                        shootsright20.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for orc in orcs:
                for shootss20 in shootsright20:
                    if orc.rect.colliderect(shootss20.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss20 in shootsright20:
                    if orc.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))




























# for the lime enemies:
    def orc_upgrade1():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 9000:
            for orc in orcs:
                for shootss in shootsright:
                    if orc.rect.colliderect(shootss.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -=  2
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss in shootsright:
                    if orc.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for orc in orcs:
                for shootss2 in shootsright2:
                    if orc.rect.colliderect(shootss2.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -=  2
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss2 in shootsright2:
                    if orc.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for orc in orcs:
                for shootss3 in shootsright3:
                    if orc.rect.colliderect(shootss3.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 2
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            money1.cash += 1
                            orc.health += 8
                            orc.hit = False


            for orc in orcs:
                for shootss3 in shootsright3:
                    if orc.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for orc in orcs:
                for shootss4 in shootsright4:
                    if orc.rect.colliderect(shootss4.hitbox):
                        orc.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 2
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss4 in shootsright4:
                    if orc.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for orc in orcs:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 2
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss5 in shootsright5:
                    if orc.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def orc_upgrade2():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 9000:
            for orc in orcs:
                for shootss6 in shootsright6:
                    if orc.rect.colliderect(shootss6.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss6 in shootsright6:
                    if orc.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for orc in orcs:
                for shootss7 in shootsright7:
                    if orc.rect.colliderect(shootss7.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss7 in shootsright7:
                    if orc.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for orc in orcs:
                for shootss8 in shootsright8:
                    if orc.rect.colliderect(shootss8.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss8 in shootsright8:
                    if orc.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for orc in orcs:
                for shootss9 in shootsright9:
                    if orc.rect.colliderect(shootss9.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for turtle in turtles:
                for shootss9 in shootsright9:
                    if orc.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for orc in orcs:
                for shootss10 in shootsright10:
                    if orc.rect.colliderect(shootss10.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 3
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss11 in shootsright10:
                    if orc.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def orc_upgrade3():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x - 9000:
            for orc in orcs:
                for shootss11 in shootsright11:
                    if orc.rect.colliderect(shootss11.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 5
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 5
                            orc.hit = False


            for orc in orcs:
                for shootss11 in shootsright11:
                    if orc.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for orc in orcs:
                for shootss12 in shootsright12:
                    if orc.rect.colliderect(shootss12.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 5
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss12 in shootsright12:
                    if orc.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for orc in orcs:
                for shootss13 in shootsright13:
                    if orc.rect.colliderect(shootss13.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 5
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss13 in shootsright13:
                    if orc.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for orc in orcs:
                for shootss14 in shootsright14:
                    if orc.rect.colliderect(shootss14.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 5
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss14 in shootsright14:
                    if orc.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for orc in orcs:
                for shootss15 in shootsright15:
                    if orc.rect.colliderect(shootss15.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 2:
                            orc.health -= 5
                            
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss15 in shootsright15:
                    if orc.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def orc_upgrade4():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x - 9000:
            for orc in orcs:
                for shootss16 in shootsright16:
                    if orc.rect.colliderect(shootss16.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 10
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 9
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss16 in shootsright16:
                    if orc.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for orc in orcs:
                for shootss17 in shootsright17:
                    if orc.rect.colliderect(shootss17.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 10
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 9
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss17 in shootsright17:
                    if orc.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for orc in orcs:
                for shootss18 in shootsright18:
                    if orc.rect.colliderect(shootss18.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss18 in shootsright18:
                    if orc.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for orc in orcs:
                for shootss19 in shootsright19:
                    if orc.rect.colliderect(shootss19.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss19 in shootsright19:
                    if orc.rect.colliderect(shootss19.hitbox):
                        shootsright19.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for orc in orcs:
                for shootss20 in shootsright20:
                    if orc.rect.colliderect(shootss20.hitbox):
                        orc.hit = True
                        hit.play()
                        orc.direction = "hit"
                        if orc.health > 13:
                            orc.health -= 9
                        else:
                            orc.x = void.x + 20 
                            orc.y = void.y + 200
                            orc.health += 8
                            money1.cash += 1
                            orc.hit = False


            for orc in orcs:
                for shootss20 in shootsright20:
                    if orc.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))















# for the lime enemies:
    def bullet_collisions9():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 160:
            for turtle in turtles:
                for shootss in shootsright:
                    if turtle.rect.colliderect(shootss.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -=  0.1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss in shootsright:
                    if turtle.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for turtle in turtles:
                for shootss2 in shootsright2:
                    if turtle.rect.colliderect(shootss2.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -=  0.1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss2 in shootsright2:
                    if turtle.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for turtle in turtles:
                for shootss3 in shootsright3:
                    if turtle.rect.colliderect(shootss3.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss3 in shootsright3:
                    if turtle.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for turtle in turtles:
                for shootss4 in shootsright4:
                    if turtle.rect.colliderect(shootss4.hitbox):
                        turtle.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss4 in shootsright4:
                    if turtle.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for turtle in turtles:
                for shootss5 in shootsright5:
                    if turtle.rect.colliderect(shootss5.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss5 in shootsright5:
                    if turtle.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def bullet_collisions10():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 0:
            
            for turtle in turtles:
                for shootss6 in shootsright6:
                    if turtle.rect.colliderect(shootss6.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.3
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss6 in shootsright6:
                    if turtle.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for turtle in turtles:
                for shootss7 in shootsright7:
                    if turtle.rect.colliderect(shootss7.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.3
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss7 in shootsright7:
                    if turtle.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for turtle in turtles:
                for shootss8 in shootsright8:
                    if turtle.rect.colliderect(shootss8.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.3
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss8 in shootsright8:
                    if turtle.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for turtle in turtles:
                for shootss9 in shootsright9:
                    if turtle.rect.colliderect(shootss9.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.3
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss9 in shootsright9:
                    if turtle.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for turtle in turtles:
                for shootss10 in shootsright10:
                    if turtle.rect.colliderect(shootss10.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.3
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss11 in shootsright10:
                    if turtle.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def bullet_collisions11():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x + 170:
            for turtle in turtles:
                for shootss11 in shootsright11:
                    if turtle.rect.colliderect(shootss11.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss11 in shootsright11:
                    if turtle.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for turtle in turtles:
                for shootss12 in shootsright12:
                    if turtle.rect.colliderect(shootss12.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss12 in shootsright12:
                    if turtle.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for turtle in turtles:
                for shootss13 in shootsright13:
                    if turtle.rect.colliderect(shootss13.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss13 in shootsright13:
                    if turtle.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for turtle in turtles:
                for shootss14 in shootsright14:
                    if turtle.rect.colliderect(shootss14.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 1
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss14 in shootsright14:
                    if turtle.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for turtle in turtles:
                for shootss15 in shootsright15:
                    if turtle.rect.colliderect(shootss15.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 1
                            
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss15 in shootsright15:
                    if turtle.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def bullet_collisions12():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x + 330:
            for turtle in turtles:
                for shootss16 in shootsright16:
                    if turtle.rect.colliderect(shootss16.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 9
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss16 in shootsright16:
                    if turtle.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for turtle in turtles:
                for shootss17 in shootsright17:
                    if turtle.rect.colliderect(shootss17.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 9
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss17 in shootsright17:
                    if turtle.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for turtle in turtles:
                for shootss18 in shootsright18:
                    if turtle.rect.colliderect(shootss18.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss18 in shootsright18:
                    if turtle.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for turtle in turtles:
                for shootss19 in shootsright19:
                    if turtle.rect.colliderect(shootss19.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss19 in shootsright19:
                    if turtle.rect.colliderect(shootss19.hitbox):
                        shootsright19.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for turtle in turtles:
                for shootss20 in shootsright20:
                    if turtle.rect.colliderect(shootss20.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss20 in shootsright20:
                    if turtle.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))

























# for the lime enemies:
    def towerups001():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 9000:
            for turtle in turtles:
                for shootss in shootsright:
                    if turtle.rect.colliderect(shootss.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -=  0.5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss in shootsright:
                    if turtle.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for turtle in turtles:
                for shootss2 in shootsright2:
                    if turtle.rect.colliderect(shootss2.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -=  0.5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss2 in shootsright2:
                    if turtle.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for turtle in turtles:
                for shootss3 in shootsright3:
                    if turtle.rect.colliderect(shootss3.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            money1.cash += 1
                            turtle.health += 8
                            turtle.hit = False


            for turtle in turtles:
                for shootss3 in shootsright3:
                    if turtle.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for turtle in turtles:
                for shootss4 in shootsright4:
                    if turtle.rect.colliderect(shootss4.hitbox):
                        turtle.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss4 in shootsright4:
                    if turtle.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for turtle in turtles:
                for shootss5 in shootsright5:
                    if turtle.rect.colliderect(shootss5.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss5 in shootsright5:
                    if turtle.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def towerups002():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 9000:
            
            for turtle in turtles:
                for shootss6 in shootsright6:
                    if turtle.rect.colliderect(shootss6.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss6 in shootsright6:
                    if turtle.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for turtle in turtles:
                for shootss7 in shootsright7:
                    if turtle.rect.colliderect(shootss7.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss7 in shootsright7:
                    if turtle.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for turtle in turtles:
                for shootss8 in shootsright8:
                    if turtle.rect.colliderect(shootss8.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss8 in shootsright8:
                    if turtle.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for turtle in turtles:
                for shootss9 in shootsright9:
                    if turtle.rect.colliderect(shootss9.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss9 in shootsright9:
                    if turtle.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for turtle in turtles:
                for shootss10 in shootsright10:
                    if turtle.rect.colliderect(shootss10.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 2:
                            turtle.health -= 0.9
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss11 in shootsright10:
                    if turtle.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def towerups003():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x - 9000:
            for turtle in turtles:
                for shootss11 in shootsright11:
                    if turtle.rect.colliderect(shootss11.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss11 in shootsright11:
                    if turtle.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for turtle in turtles:
                for shootss12 in shootsright12:
                    if turtle.rect.colliderect(shootss12.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss12 in shootsright12:
                    if turtle.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for turtle in turtles:
                for shootss13 in shootsright13:
                    if turtle.rect.colliderect(shootss13.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss13 in shootsright13:
                    if turtle.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for turtle in turtles:
                for shootss14 in shootsright14:
                    if turtle.rect.colliderect(shootss14.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss14 in shootsright14:
                    if turtle.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for turtle in turtles:
                for shootss15 in shootsright15:
                    if turtle.rect.colliderect(shootss15.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 5
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss15 in shootsright15:
                    if turtle.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def towerups004():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x - 9000:
            for turtle in turtles:
                for shootss16 in shootsright16:
                    if turtle.rect.colliderect(shootss16.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 9
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss16 in shootsright16:
                    if turtle.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for turtle in turtles:
                for shootss17 in shootsright17:
                    if turtle.rect.colliderect(shootss17.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 9
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss17 in shootsright17:
                    if turtle.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for turtle in turtles:
                for shootss18 in shootsright18:
                    if turtle.rect.colliderect(shootss18.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss18 in shootsright18:
                    if turtle.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for turtle in turtles:
                for shootss19 in shootsright19:
                    if turtle.rect.colliderect(shootss19.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss19 in shootsright19:
                    if turtle.rect.colliderect(shootss19.hitbox):
                        shootsright19.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for turtle in turtles:
                for shootss20 in shootsright20:
                    if turtle.rect.colliderect(shootss20.hitbox):
                        turtle.hit = True
                        hit.play()
                        turtle.direction = "hit"
                        if turtle.health > 13:
                            turtle.health -= 10
                        else:
                            turtle.x = void.x + 20 
                            turtle.y = void.y + 200
                            turtle.health += 8
                            money1.cash += 1
                            turtle.hit = False


            for turtle in turtles:
                for shootss20 in shootsright20:
                    if turtle.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))










































# for the lime enemies:
    def bullet_collisions5():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        
        if upgrade1.x == drawtower2.x - 160:
            for lime in limes:
                for shootss in shootsright:
                    if lime.rect.colliderect(shootss.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.3
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            money1.cash += 2
                            lime.health += 8
                            lime.hit = False


            for lime in limes:
                for shootss in shootsright:
                    if lime.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))




            # bullet 2 collid
            for lime in limes:
                for shootss2 in shootsright2:
                    if lime.rect.colliderect(shootss2.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.3
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            money1.cash += 2
                            lime.health += 8
                            lime.hit = False


            for lime in limes:
                for shootss2 in shootsright2:
                    if lime.rect.colliderect(shootss2.hitbox):
                        shootsright2.pop(shootsright2.index(shootss2))




            # bullet 2 collid
            for lime in limes:
                for shootss3 in shootsright3:
                    if lime.rect.colliderect(shootss3.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.3
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            money1.cash += 2
                            lime.health += 8
                            lime.hit = False


            for lime in limes:
                for shootss3 in shootsright3:
                    if lime.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for lime in limes:
                for shootss4 in shootsright4:
                    if lime.rect.colliderect(shootss4.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.3
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss4 in shootsright4:
                    if lime.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))




            # bullet 2 collid
            # bullet 1 collid
            for lime in limes:
                for shootss5 in shootsright5:
                    if lime.rect.colliderect(shootss5.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.3
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss5 in shootsright5:
                    if lime.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def bullet_collisions6():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 0:
            
            for lime in limes:
                for shootss6 in shootsright6:
                    if lime.rect.colliderect(shootss6.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss6 in shootsright6:
                    if lime.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for lime in limes:
                for shootss7 in shootsright7:
                    if lime.rect.colliderect(shootss7.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss7 in shootsright7:
                    if lime.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))




            # bullet 1 collid
            for lime in limes:
                for shootss8 in shootsright8:
                    if lime.rect.colliderect(shootss8.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss8 in shootsright8:
                    if lime.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for lime in limes:
                for shootss9 in shootsright9:
                    if lime.rect.colliderect(shootss9.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss9 in shootsright9:
                    if lime.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



                # bullet 1 collid
            for lime in limes:
                for shootss10 in shootsright10:
                    if lime.rect.colliderect(shootss10.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 0.5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss11 in shootsright10:
                    if lime.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def bullet_collisions7():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x + 170:
            for lime in limes:
                for shootss11 in shootsright11:
                    if lime.rect.colliderect(shootss11.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss11 in shootsright11:
                    if lime.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))




            # bullet 1 collid
            for lime in limes:
                for shootss12 in shootsright12:
                    if lime.rect.colliderect(shootss12.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss12 in shootsright12:
                    if lime.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))

                        

            for lime in limes:
                for shootss13 in shootsright13:
                    if lime.rect.colliderect(shootss13.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss13 in shootsright13:
                    if lime.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))

                        



            # bullet 1 collid
            for lime in limes:
                for shootss14 in shootsright14:
                    if lime.rect.colliderect(shootss14.hitbox):
                        lime.hit = True
                        hit.play
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss14 in shootsright14:
                    if lime.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))

                        
            # bullet 1 collid
            # bullet 1 collid
            for lime in limes:
                for shootss15 in shootsright15:
                    if lime.rect.colliderect(shootss15.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss15 in shootsright15:
                    if lime.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))

        # ------------------------------ my second shooting image bullets




    def bullet_collisions8():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        # bullet 1 collid
        if upgrade4.x == drawtower2.x + 330:
            for lime in limes:
                for shootss16 in shootsright16:
                    if lime.rect.colliderect(shootss16.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 9
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss16 in shootsright16:
                    if lime.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))

                        
            # bullet 1 collid
            for lime in limes:
                for shootss17 in shootsright17:
                    if lime.rect.colliderect(shootss17.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 9
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss17 in shootsright17:
                    if lime.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid

            for lime in limes:
                for shootss18 in shootsright18:
                    if lime.rect.colliderect(shootss18.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 9
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss18 in shootsright18:
                    if lime.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))






            # bullet 1 collid
            for lime in limes:
                for shootss19 in shootsright19:
                    if lime.rect.colliderect(shootss19.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 9
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss19 in shootsright19:
                    if lime.rect.colliderect(shootss19.hitbox):
                        shootsright20.pop(shootsright19.index(shootss19))





            # bullet 1 collid
            for lime in limes:
                for shootss20 in shootsright20:
                    if lime.rect.colliderect(shootss20.hitbox):
                        lime.hit = True
                        hit.play()
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 9
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 200
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False


            for lime in limes:
                for shootss20 in shootsright20:
                    if lime.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))



# UPGRADE 2--------------------------------------------------------
    def towerups00():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade1.x == drawtower2.x - 9000:
            for lime in limes:
                for shootss in shootsright:
                    if lime.rect.colliderect(shootss.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 1.7
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            money1.cash += 2
                            lime.health += 8
                            lime.hit = False



            for lime in limes:
                for shootss in shootsright:
                    if lime.rect.colliderect(shootss.rect):
                        shootsright16.pop(shootsright.index(shootss))


            collid_1 = True
            for lime in limes:
                for shootss2 in shootsright2:
                    if lime.rect.colliderect(shootss2.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 1.4
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss2 in shootsright2:
                    if lime.rect.colliderect(shootss2.rect):
                        shootsright2.pop(shootsright2.index(shootss2))



            collid_1 = True
            for lime in limes:
                for shootss3 in shootsright3:
                    if lime.rect.colliderect(shootss2.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 1.7
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss2 in shootsright3:
                    if lime.rect.colliderect(shootss3.rect):
                        shootsright2.pop(shootsright2.index(shootss3))




            collid_1 = True
            for lime in limes:
                for shootss4 in shootsright4:
                    if lime.rect.colliderect(shootss4.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 1.7
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss4 in shootsright4:
                    if lime.rect.colliderect(shootss4.rect):
                        shootsright4.pop(shootsright4.index(shootss4))




            collid_1 = True
            for lime in limes:
                for shootss5 in shootsright5:
                    if lime.rect.colliderect(shootss5.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 1.7
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss5 in shootsright5:
                    if lime.rect.colliderect(shootss5.rect):
                        shootsright5.pop(shootsright5.index(shootss5))






    def towerups11():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade2.x == drawtower2.x - 9000:
            for lime in limes:
                for shootss6 in shootsright6:
                    if lime.rect.colliderect(shootss6.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 8
                            money1.cash += 2
                            lime.hit = False



            for lime in limes:
                for shootss6 in shootsright6:
                    if lime.rect.colliderect(shootss6.rect):
                        shootsright6.pop(shootsright.index(shootss6))


            collid_1 = True
            for lime in limes:
                for shootss7 in shootsright7:
                    if lime.rect.colliderect(shootss7.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss7 in shootsright7:
                    if lime.rect.colliderect(shootss7.rect):
                        shootsright7.pop(shootsright7.index(shootss7))



            collid_1 = True
            for lime in limes:
                for shootss8 in shootsright8:
                    if lime.rect.colliderect(shootss8.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 2
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 5
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss9 in shootsright9:
                    if lime.rect.colliderect(shootss9.rect):
                        shootsright9.pop(shootsright9.index(shootss8))




            collid_1 = True
            for lime in limes:
                for shootss10 in shootsright10:
                    if lime.rect.colliderect(shootss10.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 4:
                            lime.health -= 5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 5
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss10 in shootsright4:
                    if lime.rect.colliderect(shootss10.rect):
                        shootsright10.pop(shootsright10.index(shootss4))




            collid_1 = True
            for lime in limes:
                for shootss11 in shootsright11:
                    if lime.rect.colliderect(shootss11.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 2:
                            lime.health -= 5
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 5
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss11 in shootsright11:
                    if lime.rect.colliderect(shootss11.rect):
                        shootsright11.pop(shootsright11.index(shootss11))









    def towerups22():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade3.x == drawtower2.x - 9000:
            for lime in limes:
                for shootss12 in shootsright12:
                    if lime.rect.colliderect(shootss12.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 13
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            money1.cash += 2
                            lime.health += 8
                            lime.hit = False



            for lime in limes:
                for shootss12 in shootsright12:
                    if lime.rect.colliderect(shootss12.rect):
                        shootsright12.pop(shootsright.index(shootss12))


            collid_1 = True
            for lime in limes:
                for shootss13 in shootsright13:
                    if lime.rect.colliderect(shootss13.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 13
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss13 in shootsright13:
                    if monster.rect.colliderect(shootss13.rect):
                        shootsright12.pop(shootsright13.index(shootss13))



            collid_1 = True
            for lime in limes:
                for shootss14 in shootsright14:
                    if lime.rect.colliderect(shootss14.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss14 in shootsright14:
                    if lime.rect.colliderect(shootss14.rect):
                        shootsright8.pop(shootsright14.index(shootss8))




            collid_1 = True
            for lime in limes:
                for shootss15 in shootsright15:
                    if lime.rect.colliderect(shootss15.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss15 in shootsright15:
                    if lime.rect.colliderect(shootss15.rect):
                        shootsright15.pop(shootsright15.index(shootss15))




            collid_1 = True
            for lime in limes:
                for shootss16 in shootsright16:
                    if lime.rect.colliderect(shootss16.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 6
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 1
                            lime.hit = False

            for lime in limes:
                for shootss16 in shootsright16:
                    if lime.rect.colliderect(shootss16.rect):
                        shootsright16.pop(shootsright16.index(shootss16))


    def towerups33():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade4.x == drawtower2.x - 9000:

            collid_1 = True
            for lime in limes:
                for shootss17 in shootsright17:
                    if lime.rect.colliderect(shootss17.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss17 in shootsright17:
                    if lime.rect.colliderect(shootss17.rect):
                        shootsright17.pop(shootsright17.index(shootss17))



            collid_1 = True
            for lime in limes:
                for shootss18 in shootsright18:
                    if lime.rect.colliderect(shootss18.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss18 in shootsright18:
                    if lime.rect.colliderect(shootss18.rect):
                        shootsright18.pop(shootsright18.index(shootss18))




            collid_1 = True
            for lime in limes:
                for shootss19 in shootsright19:
                    if lime.rect.colliderect(shootss19.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss19 in shootsright19:
                    if lime.rect.colliderect(shootss19.rect):
                        shootsright19.pop(shootsright19.index(shootss19))




            collid_1 = True
            for lime in limes:
                for shootss20 in shootsright20:
                    if lime.rect.colliderect(shootss20.rect):
                        hit.play()
                        lime.hit = True
                        lime.direction = "hit"
                        if lime.health > 13:
                            lime.health -= 10
                        else:
                            lime.x = void.x + 20 
                            lime.y = void.y + 150
                            lime.health += 6
                            money1.cash += 2
                            lime.hit = False

            for lime in limes:
                for shootss20 in shootsright20:
                    if lime.rect.colliderect(shootss20.rect):
                        shootsright20.pop(shootsright20.index(shootss20))










# -------------------------------------------------- BULLET COLISIOn 2





              
    def bullet_collisions():
        
        
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade1.x == drawtower2.x - 160:
            for monster in monsters:
                for shootss in shootsright:
                    if monster.rect.colliderect(shootss.hitbox):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False
                        



            for monster in monsters:
                for shootss in shootsright:
                    if monster.rect.colliderect(shootss.hitbox):
                        shootsright.pop(shootsright.index(shootss))





            # bullet 2 collid
            for monster in monsters:
                for shootss2 in shootsright2:
                    if monster.rect.colliderect(shootss2.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False


            for monster in monsters:
                for shootss2 in shootsright2:
                    if monster.rect.colliderect(shootss2.hitbox):
                        monster.hit = True
                        shootsright2.pop(shootsright2.index(shootss2))





            # bullet 2 collid
            for monster in monsters:
                for shootss3 in shootsright3:
                    if monster.rect.colliderect(shootss3.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False


            for monster in monsters:
                for shootss3 in shootsright3:
                    if monster.rect.colliderect(shootss3.hitbox):
                        shootsright3.pop(shootsright3.index(shootss3))





            # bullet 2 collid
            for monster in monsters:
                for shootss4 in shootsright4:
                    if monster.rect.colliderect(shootss4.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False


            for monster in monsters:
                for shootss4 in shootsright4:
                    if monster.rect.colliderect(shootss4.hitbox):
                        shootsright4.pop(shootsright4.index(shootss4))





            # bullet 2 collid
            for monster in monsters:
                for shootss5 in shootsright5:
                    if monster.rect.colliderect(shootss5.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False


            for monster in monsters:
                for shootss5 in shootsright5:
                    if monster.rect.colliderect(shootss5.hitbox):
                        shootsright5.pop(shootsright5.index(shootss5))






    def bullet_collisions2():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade2.x == drawtower2.x - 0:
            for monster in monsters:
                for shootss6 in shootsright6:
                    if monster.rect.colliderect(shootss6.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 0.5
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False


            for monster in monsters:
                for shootss6 in shootsright6:
                    if monster.rect.colliderect(shootss6.hitbox):
                        shootsright6.pop(shootsright6.index(shootss6))


            # bullet 1 collid
            for monster in monsters:
                for shootss7 in shootsright7:
                    if monster.rect.colliderect(shootss7.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss7 in shootsright7:
                    if monster.rect.colliderect(shootss7.hitbox):
                        shootsright7.pop(shootsright7.index(shootss7))



            # bullet 1 collid
            for monster in monsters:
                for shootss8 in shootsright8:
                    if monster.rect.colliderect(shootss8.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss8 in shootsright8:
                    if monster.rect.colliderect(shootss8.hitbox):
                        shootsright8.pop(shootsright8.index(shootss8))




            # bullet 1 collid
            for monster in monsters:
                for shootss9 in shootsright9:
                    if monster.rect.colliderect(shootss9.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss8 in shootsright9:
                    if monster.rect.colliderect(shootss9.hitbox):
                        shootsright9.pop(shootsright9.index(shootss9))



            # bullet 1 collid
            for monster in monsters:
                for shootss10 in shootsright10:
                    if monster.rect.colliderect(shootss10.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss10 in shootsright10:
                    if monster.rect.colliderect(shootss10.hitbox):
                        shootsright10.pop(shootsright10.index(shootss10))

                    
    # ------------------------------ my second shooting image bullets


    def bullet_collisions3():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade3.x == drawtower2.x + 170:
            for monster in monsters:
                for shootss11 in shootsright11:
                    if monster.rect.colliderect(shootss11.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss11 in shootsright10:
                    if monster.rect.colliderect(shootss11.hitbox):
                        shootsright11.pop(shootsright11.index(shootss11))


            # bullet 1 collid
            for monster in monsters:
                for shootss12 in shootsright12:
                    if monster.rect.colliderect(shootss12.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss12 in shootsright12:
                    if monster.rect.colliderect(shootss12.hitbox):
                        shootsright12.pop(shootsright12.index(shootss12))



            # bullet 1 collid
            for monster in monsters:
                for shootss13 in shootsright13:
                    if monster.rect.colliderect(shootss13.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss13 in shootsright13:
                    if monster.rect.colliderect(shootss13.hitbox):
                        shootsright13.pop(shootsright13.index(shootss13))




            # bullet 1 collid
            for monster in monsters:
                for shootss14 in shootsright14:
                    if monster.rect.colliderect(shootss14.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss14 in shootsright14:
                    if monster.rect.colliderect(shootss14.hitbox):
                        shootsright14.pop(shootsright14.index(shootss14))


            # bullet 1 collid
            for monster in monsters:
                for shootss15 in shootsright15:
                    if monster.rect.colliderect(shootss15.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 4
                            money1.cash += 2
                            monster.hit = False



            for monster in monsters:
                for shootss15 in shootsright15:
                    if monster.rect.colliderect(shootss15.hitbox):
                        shootsright15.pop(shootsright15.index(shootss15))
        # ------------------------------ my second shooting image bullets




    def bullet_collisions4():
        hit  = pygame.mixer.Sound("hit.wav")
        # bullet 1 collid
        if upgrade4.x == drawtower2.x + 330:
            for monster in monsters:
                for shootss16 in shootsright16:
                    if monster.rect.colliderect(shootss16.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 5
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss16 in shootsright16:
                    if monster.rect.colliderect(shootss16.hitbox):
                        shootsright16.pop(shootsright16.index(shootss16))


            # bullet 1 collid
            for monster in monsters:
                for shootss17 in shootsright17:
                    if monster.rect.colliderect(shootss17.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss17 in shootsright17:
                    if monster.rect.colliderect(shootss17.hitbox):
                        shootsright17.pop(shootsright17.index(shootss17))

            # bullet 1 collid
            for monster in monsters:
                for shootss18 in shootsright18:
                    if monster.rect.colliderect(shootss18.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False
                            

            for monster in monsters:
                for shootss18 in shootsright18:
                    if monster.rect.colliderect(shootss18.hitbox):
                        shootsright18.pop(shootsright18.index(shootss18))




            # bullet 1 collid
            for monster in monsters:
                for shootss19 in shootsright19:
                    if monster.rect.colliderect(shootss19.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss19 in shootsright19:
                    if monster.rect.colliderect(shootss19.hitbox):
                        shootsright19.pop(shootsright19.index(shootss19))



            # bullet 1 collid
            for monster in monsters:
                for shootss20 in shootsright20:
                    if monster.rect.colliderect(shootss15.hitbox):
                        monster.hit = True
                        hit.play()
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 200
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False


            for monster in monsters:
                for shootss20 in shootsright20:
                    if monster.rect.colliderect(shootss20.hitbox):
                        shootsright20.pop(shootsright20.index(shootss20))

                    
    # ------------------------------ my second shooting image bullets

                    
                    
    particles = []
                        
    # our main loop
    cashtimer = 0


    tos = 0





    def towerups():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade1.x == drawtower2.x - 9000:
            for monster in monsters:
                for shootss in shootsright:
                    if monster.rect.colliderect(shootss.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            money1.cash += 2
                            monster.health += 8
                            monster.hit = False



            for monster in monsters:
                for shootss in shootsright:
                    if monster.rect.colliderect(shootss.rect):
                        shootsright16.pop(shootsright.index(shootss))


            collid_1 = True
            for monster in monsters:
                for shootss2 in shootsright2:
                    if monster.rect.colliderect(shootss2.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1.4
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss2 in shootsright2:
                    if monster.rect.colliderect(shootss2.rect):
                        shootsright2.pop(shootsright2.index(shootss2))



            collid_1 = True
            for monster in monsters:
                for shootss3 in shootsright3:
                    if monster.rect.colliderect(shootss2.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1.4
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss2 in shootsright3:
                    if monster.rect.colliderect(shootss3.rect):
                        shootsright2.pop(shootsright2.index(shootss3))




            collid_1 = True
            for monster in monsters:
                for shootss4 in shootsright4:
                    if monster.rect.colliderect(shootss4.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1.4
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss4 in shootsright4:
                    if monster.rect.colliderect(shootss4.rect):
                        shootsright4.pop(shootsright4.index(shootss4))




            collid_1 = True
            for monster in monsters:
                for shootss5 in shootsright5:
                    if monster.rect.colliderect(shootss5.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 1.4
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss5 in shootsright5:
                    if monster.rect.colliderect(shootss5.rect):
                        shootsright5.pop(shootsright5.index(shootss5))






    def towerups1():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade2.x == drawtower2.x - 9000:
            for monster in monsters:
                for shootss6 in shootsright6:
                    if monster.rect.colliderect(shootss6.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 2
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False



            for monster in monsters:
                for shootss6 in shootsright6:
                    if monster.rect.colliderect(shootss6.rect):
                        shootsright6.pop(shootsright.index(shootss6))


            collid_1 = True
            for monster in monsters:
                for shootss7 in shootsright7:
                    if monster.rect.colliderect(shootss7.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 2
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss7 in shootsright7:
                    if monster.rect.colliderect(shootss7.rect):
                        shootsright7.pop(shootsright7.index(shootss7))



            collid_1 = True
            for monster in monsters:
                for shootss8 in shootsright8:
                    if monster.rect.colliderect(shootss8.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 2
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss9 in shootsright9:
                    if monster.rect.colliderect(shootss9.rect):
                        shootsright9.pop(shootsright9.index(shootss8))




            collid_1 = True
            for monster in monsters:
                for shootss10 in shootsright10:
                    if monster.rect.colliderect(shootss10.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 4:
                            monster.health -= 2
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss10 in shootsright4:
                    if monster.rect.colliderect(shootss10.rect):
                        shootsright10.pop(shootsright10.index(shootss4))




            collid_1 = True
            for monster in monsters:
                for shootss11 in shootsright11:
                    if monster.rect.colliderect(shootss11.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 2:
                            monster.health -= 2
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss11 in shootsright11:
                    if monster.rect.colliderect(shootss11.rect):
                        shootsright11.pop(shootsright11.index(shootss11))









    def towerups2():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade3.x == drawtower2.x - 9000:
            for monster in monsters:
                for shootss12 in shootsright12:
                    if monster.rect.colliderect(shootss12.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 13
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 8
                            money1.cash += 2
                            monster.hit = False



            for monster in monsters:
                for shootss12 in shootsright12:
                    if monster.rect.colliderect(shootss12.rect):
                        shootsright12.pop(shootsright.index(shootss12))


            collid_1 = True
            for monster in monsters:
                for shootss13 in shootsright13:
                    if monster.rect.colliderect(shootss13.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 13
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss13 in shootsright13:
                    if monster.rect.colliderect(shootss13.rect):
                        shootsright12.pop(shootsright13.index(shootss13))



            collid_1 = True
            for monster in monsters:
                for shootss14 in shootsright14:
                    if monster.rect.colliderect(shootss14.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 13
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss14 in shootsright14:
                    if monster.rect.colliderect(shootss14.rect):
                        shootsright8.pop(shootsright14.index(shootss8))




            collid_1 = True
            for monster in monsters:
                for shootss15 in shootsright15:
                    if monster.rect.colliderect(shootss15.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 13
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss15 in shootsright15:
                    if monster.rect.colliderect(shootss15.rect):
                        shootsright15.pop(shootsright15.index(shootss15))




            collid_1 = True
            for monster in monsters:
                for shootss16 in shootsright16:
                    if monster.rect.colliderect(shootss16.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 13
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss16 in shootsright16:
                    if monster.rect.colliderect(shootss16.rect):
                        shootsright16.pop(shootsright16.index(shootss16))


    def towerups3():
        hit  = pygame.mixer.Sound("hit.wav")
        if upgrade4.x == drawtower2.x - 9000:

            collid_1 = True
            for monster in monsters:
                for shootss17 in shootsright17:
                    if monster.rect.colliderect(shootss17.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss17 in shootsright17:
                    if monster.rect.colliderect(shootss17.rect):
                        shootsright17.pop(shootsright17.index(shootss17))



            collid_1 = True
            for monster in monsters:
                for shootss18 in shootsright18:
                    if monster.rect.colliderect(shootss18.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss18 in shootsright18:
                    if monster.rect.colliderect(shootss18.rect):
                        shootsright18.pop(shootsright18.index(shootss18))




            collid_1 = True
            for monster in monsters:
                for shootss19 in shootsright19:
                    if monster.rect.colliderect(shootss19.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss19 in shootsright19:
                    if monster.rect.colliderect(shootss19.rect):
                        shootsright19.pop(shootsright19.index(shootss19))




            collid_1 = True
            for monster in monsters:
                for shootss20 in shootsright20:
                    if monster.rect.colliderect(shootss20.rect):
                        hit.play()
                        monster.hit = True
                        monster.direction = "hit"
                        if monster.health > 13:
                            monster.health -= 10
                        else:
                            monster.x = void.x + 20 
                            monster.y = void.y + 150
                            monster.health += 6
                            money1.cash += 2
                            monster.hit = False

            for monster in monsters:
                for shootss20 in shootsright20:
                    if monster.rect.colliderect(shootss20.rect):
                        shootsright20.pop(shootsright20.index(shootss20))

# -------------------------------------------------------------------------------
                        


    BULLET_SPEED = 0
    BULLET_SPEED2 = 0
    BULLET_SPEED3 = 0
    timer = 0
    timo = 0

    # upgrade timer
    tic = 0



    hit = True

    loren = 0
    sho = 0

    wow = 0
    stimer = 0      
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if greenbutton1.isOver(pos):
                    click.play()
                    shop1.y = drawtower2.y - 50


                   
                if exit2.isOver(pos):
                    click.play()
                    shop1.y = 9100

                    
                
                if SHOP_UPGRADE.isOver(pos):
                    click.play()
                    upgrade21.y = drawtower2.y - 50


                       
                if exit3.isOver(pos):
                    click.play()
                    upgrade21.y = 9100
                    



                if shop1.y == 9100:
                    if pausees.isOver(pos):
                        click.play()
                        pause = True
                        paused()

                        
                        
                if shop1.y == 9100:                                                            
                    if main_lol.isOver(pos):
                        click.play()
                        fade(800,800)
                        main_game_loop()

                    

    # ---------------------------------------------------- upgrade section

                if upgrade21.y == drawtower2.y - 50:
                    if money1.cash >= 100:
                        if upgrade1.isOver(pos):
                            upgrade1.x = drawtower2.x - 9000
                            money1.cash -= 100
                            bonus.play()


            


                    
                if upgrade21.y == drawtower2.y - 50:
                    if money1.cash >= 500:
                        if upgrade2.isOver(pos):
                            upgrade2.x = drawtower2.x - 9000
                            money1.cash -= 100
                            bonus.play()


                if upgrade21.y == drawtower2.y - 50:
                    if money1.cash >= 700:
                        if upgrade3.isOver(pos):
                            upgrade3.x = drawtower3.x - 9000
                            money1.cash -= 100
                            bonus.play()


                if upgrade21.y == drawtower2.y - 50:
                    if money1.cash >= 1500:
                        if upgrade3.isOver(pos):
                            upgrade3.x = drawtower3.x - 9000
                            money1.cash -= 100
                            bonus.play()

                                
                                    
                    
                # draw our towers
                # draw our tower when its over a pos
                if place_tower == True:
                    if attack1.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn1(drawtower1.x - 50,drawtower1.y - 150,100,100,white))
                        place_tower = False
                        attack1.x = 90000
                        money1.cash -= 10



                if place_tower == True:
                    if attack2.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn1(drawtower1.x - 20,drawtower1.y - 420  ,100,100,white))
                        place_tower = False
                        attack2.x = 90000
                        money1.cash -= 10



                if place_tower == True:
                    if attack3.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn1(drawtower3.x - 200,drawtower3.y - 500  ,100,100,white))
                        place_tower = False
                        attack3.x = 90000
                        money1.cash -= 10


               
                if place_tower == True:
                    if attack4.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn1(drawtower4.x - 230,drawtower4.y - 300  ,100,100,white))
                        place_tower = False
                        attack4.x = 90000
                        money1.cash -= 10
                        

                if place_tower == True:
                    if attack5.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn1(drawtower4.x - 70,drawtower4.y - 490  ,100,100,white))
                        place_tower = False
                        attack5.x = 90000
                        money1.cash -= 10

        # my second placing towers
                if place_tower2 == True:
                    if attack6.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn2(drawtower1.x - 50,drawtower1.y - 150,100,100,white))
                        place_tower2 = False
                        attack6.x = 90000
                        money1.cash -= 500


                if place_tower2 == True:
                    if attack7.isOver(pos):
                        particles.append(towerdrawn2(drawtower1.x - 20,drawtower1.y - 420 ,100,100,white))
                        place_tower2 = False
                        attack7.x = 90000
                        money1.cash -= 500



                if place_tower2 == True:
                    if attack8.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn2(drawtower3.x - 200,drawtower3.y - 500  ,100,100,white))
                        place_tower2 = False
                        attack8.x = 90000
                        money1.cash -= 500


               
                if place_tower2 == True:
                    if attack9.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn2(drawtower4.x - 230,drawtower4.y - 300  ,100,100,white))
                        place_tower2 = False
                        attack9.x = 90000
                        money1.cash -= 500
                        

                if place_tower2 == True:
                    if attack10.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn2(drawtower4.x - 70,drawtower4.y - 490  ,100,100,white))
                        place_tower2 = False
                        attack10.x = 90000
                        money1.cash -= 500
                        

            # our our thir

                if place_tower3 == True:
                    if attack11.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn3(drawtower1.x - 50,drawtower1.y - 150,100,100,white))
                        place_tower3 = False
                        attack11.x = 90000
                        money1.cash -= 700


                if place_tower3 == True:
                    if attack12.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn3(drawtower1.x - 20,drawtower1.y - 420 ,100,100,white))
                        place_tower3 = False
                        attack12.x = 90000
                        money1.cash -= 700



                if place_tower3 == True:
                    if attack13.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn3(drawtower3.x - 200,drawtower3.y - 500  ,100,100,white))
                        place_tower3 = False
                        attack13.x = 90000
                        money1.cash -= 700


               
                if place_tower3 == True:
                    if attack14.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn3(drawtower4.x - 230,drawtower4.y - 300  ,100,100,white))
                        place_tower3 = False
                        attack14.x = 90000
                        money1.cash -= 700

                if place_tower3 == True:
                    if attack15.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn3(drawtower4.x - 70,drawtower4.y - 490  ,100,100,white))
                        place_tower3 = False
                        attack15.x = 90000
                        money1.cash -= 700


                        

            # our last p[lacing towers

                if place_tower4 == True:
                    if attack16.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn4(drawtower1.x - 50,drawtower1.y - 150,100,100,white))
                        place_tower4 = False
                        attack16.x = 90000
                        money1.cash -= 1500


                if place_tower4 == True:
                    if attack17.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn4(drawtower1.x - 20,drawtower1.y - 420 ,100,100,white))
                        place_tower4 = False
                        attack17.x = 90000
                        money1.cash -= 1500



                if place_tower4 == True:
                    if attack18.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn4(drawtower3.x - 200,drawtower3.y - 500  ,100,100,white))
                        place_tower4 = False
                        attack18.x = 90000
                        money1.cash -= 1500


               
                if place_tower4 == True:
                    if attack19.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn4(drawtower4.x - 230,drawtower4.y - 300  ,100,100,white))
                        place_tower4 = False
                        attack19.x = 90000
                        money1.cash -= 1500
                        

                if place_tower4 == True:
                    if attack20.isOver(pos):
                        buysound.play()
                        particles.append(towerdrawn4(drawtower4.x - 70,drawtower4.y - 490  ,100,100,white))
                        place_tower4 = False
                        attack20.x = 90000
                        money1.cash -= 1500





                                
    #------------------------------------------------------------------------------------------------------------


                # if we click any of our buttons and we have the right
                # amount of money do this

                if shop1.y == drawtower2.y -50:
                    if money1.cash >= 10:
                        if drawtower1.isOver(pos): 
                            place_tower = True
                            place_tower2 = False
                            place_tower3 = False
                            place_tower4 = False
                            
                    
                if shop1.y == drawtower2.y -50:
                    if money1.cash >= 500:
                        if drawtower2.isOver(pos): 
                            place_tower = False
                            place_tower2 = True
                            place_tower3 = False
                            place_tower4 = False
                                                    



                if shop1.y == drawtower2.y -50:
                    if money1.cash >= 700:
                        if drawtower3.isOver(pos): 
                            place_tower = False
                            place_tower2 = False
                            place_tower3 = True
                            place_tower4 = False

                                                 
                            
                if shop1.y == drawtower2.y -50:
                    if money1.cash >= 1500:
                        if drawtower4.isOver(pos): 
                            place_tower = False
                            place_tower2 = False
                            place_tower3 = False
                            place_tower4 = True
                            



     
        for shootss in shootsright:
            shootss.x += shootss.xspeed
            shootss.y += shootss.yspeed

            if shootss.x > 900 or shootss.x < 0 or shootss.y > 900 or shootss.y < 0: 
                shootsright.pop(shootsright.index(shootss))


        if attack1.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-200)
                            start_y = round(drawtower2.y+ drawtower2.height-140)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss2 in shootsright2:
            shootss2.x += shootss2.xspeed
            shootss2.y += shootss2.yspeed

            if shootss2.x > 900 or shootss2.x < 0 or shootss2.y > 900 or shootss2.y < 0: 
                shootsright2.pop(shootsright2.index(shootss2))


        if attack2.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright2) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright2.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))





        for shootss3 in shootsright3:
            shootss3.x += shootss3.xspeed
            shootss3.y += shootss3.yspeed

            if shootss3.x > 900 or shootss3.x < 0 or shootss3.y > 900 or shootss3.y < 0: 
                shootsright3.pop(shootsright3.index(shootss3))

        if attack3.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright3) < 1:
                            BULLET_SPEED3 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright3.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss4 in shootsright4:
            shootss4.x += shootss4.xspeed
            shootss4.y += shootss4.yspeed

            if shootss4.x > 900 or shootss4.x < 0 or shootss4.y > 900 or shootss4.y < 0: 
                shootsright4.pop(shootsright4.index(shootss4))
                

        if attack4.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check3.rect)  or monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright4) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright4.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss5 in shootsright5:
            shootss5.x += shootss5.xspeed
            shootss5.y += shootss5.yspeed

            if shootss5.x > 900 or shootss5.x < 0 or shootss5.y > 900 or shootss5.y < 0: 
                shootsright5.pop(shootsright5.index(shootss5))
                

        if attack5.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright5) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright5.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))


     #------------------------------------------------------------------------------------------------- MY SeCOND

        for shootss6 in shootsright6:
            shootss6.x += shootss6.xspeed
            shootss6.y += shootss6.yspeed

            if shootss6.x > 900 or shootss6.x < 0 or shootss6.y > 900 or shootss6.y < 0: 
                shootsright6.pop(shootsright6.index(shootss6))

        
        if attack6.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright6) < 1:
                            BULLET_SPEED =  10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright6.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss7 in shootsright7:
            shootss7.x += shootss7.xspeed
            shootss7.y += shootss7.yspeed

            if shootss7.x > 900 or shootss7.x < 0 or shootss7.y > 900 or shootss7.y < 0: 
                shootsright7.pop(shootsright7.index(shootss7))


        if attack7.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright7) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright7.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        for shootss8 in shootsright8:
            shootss8.x += shootss8.xspeed
            shootss8.y += shootss8.yspeed

            if shootss8.x > 900 or shootss8.x < 0 or shootss8.y > 900 or shootss8.y < 0: 
                shootsright8.pop(shootsright8.index(shootss8))

        if attack8.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright8) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright8.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss9  in shootsright9:
            shootss9.x += shootss9.xspeed
            shootss9.y += shootss9.yspeed

            if shootss9.x > 900 or shootss9.x < 0 or shootss9.y > 900 or shootss9.y < 0: 
                shootsright9.pop(shootsright9.index(shootss9))
                

        if attack9.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check3.rect) or monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright9) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright9.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss10 in shootsright10:
            shootss10.x += shootss10.xspeed
            shootss10.y += shootss10.yspeed

            if shootss10.x > 900 or shootss10.x < 0 or shootss10.y > 900 or shootss10.y < 0: 
                shootsright10.pop(shootsright10.index(shootss10))
                

        if attack10.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright10) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright10.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





     #------------------------------------------------------------------------------------------------- MY SeCOND

        for shootss11 in shootsright11:
            shootss11.x += shootss11.xspeed
            shootss11.y += shootss11.yspeed

            if shootss11.x > 900 or shootss11.x < 0 or shootss11.y > 900 or shootss11.y < 0: 
                shootsright11.pop(shootsright11.index(shootss11))

        
        if attack11.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright11) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright11.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss12 in shootsright12:
            shootss12.x += shootss12.xspeed
            shootss12.y += shootss12.yspeed

            if shootss12.x > 900 or shootss12.x < 0 or shootss12.y > 900 or shootss12.y < 0: 
                shootsright12.pop(shootsright12.index(shootss12))


        if attack12.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright12) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright12.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))





        for shootss13 in shootsright13:
            shootss13.x += shootss13.xspeed
            shootss13.y += shootss13.yspeed

            if shootss13.x > 900 or shootss13.x < 0 or shootss13.y > 900 or shootss13.y < 0: 
                shootsright13.pop(shootsright13.index(shootss8))

        if attack13.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright13) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright13.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss14  in shootsright14:
            shootss14.x += shootss14.xspeed
            shootss14.y += shootss14.yspeed

            if shootss14.x > 900 or shootss14.x < 0 or shootss14.y > 900 or shootss14.y < 0: 
                shootsright14.pop(shootsright14.index(shootss14))
                

        if attack14.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check3.rect) or monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright14) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright14.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss15 in shootsright15:
            shootss15.x += shootss15.xspeed
            shootss15.y += shootss15.yspeed

            if shootss15.x > 900 or shootss15.x < 0 or shootss15.y > 900 or shootss15.y < 0: 
                shootsright15.pop(shootsright15.index(shootss10))
                

        if attack15.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright15) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright15.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))












     #------------------------------------------------------------------------------------------------- MY SeCOND

        for shootss16 in shootsright16:
            shootss16.x += shootss16.xspeed
            shootss16.y += shootss16.yspeed

            if shootss16.x > 900 or shootss16.x < 0 or shootss16.y > 900 or shootss16.y < 0: 
                shootsright16.pop(shootsright16.index(shootss16))

        
        if attack16.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright16) < 1:
                            BULLET_SPEED =  10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright16.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss17 in shootsright17:
            shootss17.x += shootss17.xspeed
            shootss17.y += shootss17.yspeed

            if shootss17.x > 900 or shootss17.x < 0 or shootss17.y > 900 or shootss17.y < 0: 
                shootsright17.pop(shootsright17.index(shootss17))


        if attack17.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright17) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright17.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))





        for shootss18 in shootsright18:
            shootss18.x += shootss18.xspeed
            shootss18.y += shootss18.yspeed

            if shootss18.x > 900 or shootss18.x < 0 or shootss18.y > 900 or shootss18.y < 0: 
                shootsright18.pop(shootsright18.index(shootss18))

        if attack18.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright18) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright18.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss19  in shootsright19:
            shootss19.x += shootss19.xspeed
            shootss19.y += shootss19.yspeed

            if shootss19.x > 900 or shootss19.x < 0 or shootss19.y > 900 or shootss19.y < 0: 
                shootsright19.pop(shootsright19.index(shootss19))
                

        if attack19.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check3.rect) or monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright19) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright19.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        for shootss20 in shootsright20:
            shootss20.x += shootss20.xspeed
            shootss20.y += shootss20.yspeed

            if shootss20.x > 900 or shootss20.x < 0 or shootss20.y > 900 or shootss20.y < 0: 
                shootsright20.pop(shootsright20.index(shootss10))
                

        if attack20.x >= bg1.x + 9000:
            for monster in monsters:
                if monster.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright20) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = monster.x
                            target_y = monster.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright20.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))
                                
























        if attack1.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-200)
                            start_y = round(drawtower2.y+ drawtower2.height-140)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack2.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright2) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright2.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack3.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright3) < 1:
                            BULLET_SPEED3 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright3.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack4.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check3.rect)  or lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright4) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright4.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack5.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright5) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright5.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))


     #------------------------------------------------------------------------------------------------- MY SeCOND

        
        if attack6.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright6) < 1:
                            BULLET_SPEED =  10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright6.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))



        if attack7.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright7) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright7.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack8.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright8) < 1:
                            BULLET_SPEED3 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright8.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))


        if attack9.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check3.rect) or lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright9) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright9.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack10.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright10) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright10.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        
        if attack11.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright11) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright11.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack12.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright12) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright12.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack13.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright13) < 1:
                            BULLET_SPEED3 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright13.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




                

        if attack14.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check3.rect) or lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright14) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright14.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack15.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright15) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright15.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))












     #------------------------------------------------------------------------------------------------- MY SeCOND



        
        if attack16.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright16) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright16.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))







        if attack17.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright17) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright17.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack18.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright18) < 1:
                            BULLET_SPEED3 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright18.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack19.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check3.rect) or lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright19) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright19.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack20.x >= bg1.x + 9000:
            for lime in limes:
                if lime.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright20) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = lime.x
                            target_y = lime.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright20.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))
































        if attack1.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-200)
                            start_y = round(drawtower2.y+ drawtower2.height-140)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack2.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright2) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright2.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack3.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright3) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright3.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack4.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check3.rect)  or turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright4) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright4.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack5.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright5) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright5.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))


     #------------------------------------------------------------------------------------------------- MY SeCOND

        
        if attack6.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright6) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright6.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))



        if attack7.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright7) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright7.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack8.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright8) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright8.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))


        if attack9.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check3.rect) or turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright9) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright9.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack10.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright10) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright10.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        
        if attack11.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright11) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright11.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack12.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright12) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright12.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack13.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright13) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright13.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




                

        if attack14.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check3.rect) or turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright14) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright14.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack15.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright15) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright15.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))












     #------------------------------------------------------------------------------------------------- MY SeCOND



        
        if attack16.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright16) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright16.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))







        if attack17.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright17) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright17.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack18.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright18) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright18.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack19.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check3.rect) or turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright19) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright19.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack20.x >= bg1.x + 9000:
            for turtle in turtles:
                if turtle.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright20) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = turtle.x
                            target_y = turtle.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright20.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))



























        if attack1.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-200)
                            start_y = round(drawtower2.y+ drawtower2.height-140)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack2.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright2) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright2.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack3.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright3) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright3.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack4.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check3.rect)  or orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright4) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright4.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack5.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright5) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright5.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))


     #------------------------------------------------------------------------------------------------- MY SeCOND

        
        if attack6.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright6) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright6.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))



        if attack7.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright7) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright7.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack8.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright8) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright8.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))


        if attack9.x >= bg1.x + 9000:
            for orc in orcs:
                if turtle.rect.colliderect(check3.rect) or orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright9) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright9.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack10.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright10) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright10.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        
        if attack11.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright11) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright11.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack12.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright12) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright12.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack13.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright13) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright13.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




                

        if attack14.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check3.rect) or orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright14) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright14.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack15.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright15) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright15.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))












     #------------------------------------------------------------------------------------------------- MY SeCOND



        
        if attack16.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright16) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright16.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))







        if attack17.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright17) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright17.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack18.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright18) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright18.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack19.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check3.rect) or orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright19) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright19.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack20.x >= bg1.x + 9000:
            for orc in orcs:
                if orc.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright20) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = orc.x
                            target_y = orc.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright20.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))
































        if attack1.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-200)
                            start_y = round(drawtower2.y+ drawtower2.height-140)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack2.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright2) < 1:
                            BULLET_SPEED2 =  10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright2.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack3.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright3) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright3.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack4.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check3.rect)  or boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright4) < 1:
                            BULLET_SPEED4 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright4.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack5.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright5) < 1:
                            BULLET_SPEED5 =  10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright5.append(enemyboolss(start_x,start_y,(0,0,0),dir_x, dir_y))


     #------------------------------------------------------------------------------------------------- MY SeCOND

        
        if attack6.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright6) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright6.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))



        if attack7.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright7) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright7.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack8.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright8) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright8.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))


        if attack9.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check3.rect) or boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright9) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright9.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack10.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright10) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright10.append(enemyboolss2(start_x,start_y,(0,0,0),dir_x, dir_y))





        
        if attack11.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright11) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright11.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack12.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright12) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright12.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack13.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright13) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright13.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))




                

        if attack14.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check3.rect) or boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright14) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright14.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack15.x >= bg1.x + 9000:
            for boss in boss:
                if bosses.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright15) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright15.append(enemyboolss3(start_x,start_y,(0,0,0),dir_x, dir_y))












     #------------------------------------------------------------------------------------------------- MY SeCOND



        
        if attack16.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check2.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright16) < 1:
                            BULLET_SPEED = 10
                            timer = 0
                            start_x = round(drawtower1.x+drawtower1.width-70)
                            start_y = round(drawtower1.y+ drawtower1.height-100)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED * delta_x / distance
                            dir_y = BULLET_SPEED * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright16.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))







        if attack17.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check11.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright17) < 1:
                            BULLET_SPEED2 = 10
                            timer = 0
                            start_x = round(drawtower2.x+drawtower2.width-180)
                            start_y = round(drawtower2.y+ drawtower2.height-390)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED2 * delta_x / distance
                            dir_y = BULLET_SPEED2 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright17.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))





        if attack18.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright18) < 1:
                            BULLET_SPEED3 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-190)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED3 * delta_x / distance
                            dir_y = BULLET_SPEED3 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright18.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))






        if attack19.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check3.rect) or boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright19) < 1:
                            BULLET_SPEED4 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width-100)
                            start_y = round(drawtower3.y+ drawtower3.height-250)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED4 * delta_x / distance
                            dir_y = BULLET_SPEED4 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright19.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




        if attack20.x >= bg1.x + 9000:
            for boss in bosses:
                if boss.rect.colliderect(check4.rect):
                    timer += 1
                    if timer > 60:
                       if  len(shootsright20) < 1:
                            BULLET_SPEED5 = 10
                            timer = 0
                            start_x = round(drawtower3.x+drawtower3.width+30)
                            start_y = round(drawtower3.y+ drawtower3.height-470)
                            target_x = boss.x
                            target_y = boss.y
                            delta_x, delta_y = target_x - start_x, target_y - start_y
                            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
                            dir_x = BULLET_SPEED5 * delta_x / distance
                            dir_y = BULLET_SPEED5 * delta_y / distance
                            distance = math.sqrt(dir_x**2 + dir_y**2)
                            if distance > 0:
                                shootsright20.append(enemyboolss4(start_x,start_y,(0,0,0),dir_x, dir_y))




















                                
    # UPGRADE BUTTONS
        upgrade1.x = drawtower2.x - 160
        upgrade2.x = drawtower2.x - 0
        upgrade3.x = drawtower2.x + 170
        upgrade4.x = drawtower2.x + 330





        bullet_collisions()

        # --------------------- upgrades FOR mY TOWER 1
        towerups()

        # --------------------- timer before the next button appears

                            



        bullet_collisions2()
        towerups1()

        
        bullet_collisions3()
        towerups2()
        
        bullet_collisions4()
        towerups3()
                


        bullet_collisions5()
        towerups00()
        bullet_collisions6()
        towerups11()
        bullet_collisions7()
        towerups22()
        bullet_collisions8()
        towerups33()


        bullet_collisions9()
        towerups001()
        bullet_collisions10()
        towerups002()
        bullet_collisions11()
        towerups003()
        bullet_collisions12()
        towerups004()


        orc_collid1()
        orc_upgrade1()
        
        orc_collid2()
        orc_upgrade2()
        
        orc_collid3()
        orc_upgrade3()
        
        orc_collid4()
        orc_upgrade4()


        boss_collid1()
        boss_upgrade1()
        boss_collid2()
        boss_upgrade2()
        boss_collid3()
        boss_upgrade3()
        boss_collid4()
        boss_upgrade4()



        # COLLISIONS WITH DIFFERENT BULLETS 



        for monster in monsters:    
            if monster.direction == "hit":
                tos += 1
                if tos >= 5:
                    tos = 0 
                    monster.direction = "walk"
            

        for lime in limes:    
            if lime.direction == "hit":
                tos += 1
                if tos >= 5:
                    tos = 0 
                    lime.direction = "walk"

        for turtle in turtles:    
            if turtle.direction == "hit":
                tos += 1
                if tos >= 5:
                    tos = 0 
                    turtle.direction = "walk"
                    
            


        for orc in orcs:    
            if orc.direction == "hit":
                tos += 1
                if tos >= 5:
                    tos = 0 
                    orc.direction = "walk"



        for boss in bosses:    
            if boss.direction == "hit":
                tos += 1
                if tos >= 5:
                    tos = 0 
                    boss.direction = "walk"

                    

        # WHAT HAPPENS  if we have 10$ cash and we click or drawbutton1?
        if money1.cash >= 10:
            score += 1                
            scoretext = font.render("Enemys ?/" + str(score), True, (255,255,255))
            scorerect.center = ((620,150))
        
        for monster in monsters:
            monster.drection = "walk"
            checkpoints()
            



        
        sho += 1
        if sho > 15:
            loren += 1
     
                

        for lime in limes:
            lime.drection = "walk"
            if loren > 2035:
                checkpoints2()





        for turtle in turtles:
            turtle.direction = "walk"
            if loren > 5035:
                checkpoints3()

        for orc in orcs:
            orc.direction = "walk"
            if loren > 7035:
                checkpoints4()


        for boss in bosses:
            boss.direction = "walk"
            if loren > 12035:
                checkpoints5()
    

        if loren == 2035:
            Wave1.cash += 1
            Wave1.cashtext = Wave1.font.render("" + str(Wave1.cash), True, (88, 214, 141))


        if loren == 5035:
            Wave1.cash += 1
            Wave1.cashtext = Wave1.font.render("" + str(Wave1.cash), True, (88, 214, 141))


        if loren == 7035:
            Wave1.cash += 1
            Wave1.cashtext = Wave1.font.render("" + str(Wave1.cash), True, (88, 214, 141))


        if loren == 12035:
            Wave1.cash += 1
            Wave1.cashtext = Wave1.font.render("" + str(Wave1.cash), True, (88, 214, 141))


        # this will give use cash every 50 secondes

        cashtimer += 1
        if cashtimer >= 60:
            money1.cash += 1
            money1.cashtext = money1.font.render("" + str(money1.cash), True, (88, 214, 141))
            cashtimer = 0



        if upgrade21.y == drawtower2.y - 50:
            pausees.x = 9100
        else:
            pausees.x = 280


        keys = pygame.key.get_pressed()
        keyevents()


            
        if tower1.health <= -40:
            play_again()


            
        redraw()
        pygame.display.update()
        
    pygame.quit()
game_intro()
