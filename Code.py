from pygame import *

win_width = 700
win_height = 500
game = True
time_delay = 15
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width,height,player_speed,player_type):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_type = player_type
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if self.player_type == 1:
            if keys_pressed[K_w] and self.rect.x >0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < win_height-50:
                self.rect.y += self.speed
            if keys_pressed[K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys_pressed[K_d] and self.rect.x < win_width-50:
                self.rect.x += self.speed
        elif self.player_type == 2:
            if keys_pressed[K_UP] and self.rect.x >0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < win_height-50:
                self.rect.y += self.speed
            if keys_pressed[K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys_pressed[K_RIGHT] and self.rect.x < win_width-50:
                self.rect.x += self.speed
            




window = display.set_mode((win_width,win_height))
background = transform.scale(image.load("Black.jpg"),(win_width,win_height))
player1 = Player("White.jng",100,win_height/2,50,100,20,1)
player2 = Player("White.jng",win_width-100,win_height/2,50,100,20,2)


while game:

    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    player1.update()
    player1.reset()
    player2.update()
    player2.reset()

    display.update()
    time.delay(time_delay)
