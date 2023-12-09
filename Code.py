from pygame import *

win_width = 1300
win_height = 700
game = True
time_delay = 15
clock = time.Clock()
scores = 0

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, width,height,player_x_speed,player_y_speed,player_type="None"):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(width,height))
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
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
                self.rect.y -= self.y_speed
            if keys_pressed[K_s] and self.rect.y < win_height-50:
                self.rect.y += self.y_speed
            if keys_pressed[K_a] and self.rect.x > 0:
                self.rect.x -= self.x_speed
            if keys_pressed[K_d] and self.rect.x < win_width-50:
                self.rect.x += self.x_speed
        elif self.player_type == 2:
            if keys_pressed[K_UP] and self.rect.x >0:
                self.rect.y -= self.y_speed
            if keys_pressed[K_DOWN] and self.rect.y < win_height-50:
                self.rect.y += self.y_speed
            if keys_pressed[K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.x_speed
            if keys_pressed[K_RIGHT] and self.rect.x < win_width-50:
                self.rect.x += self.x_speed

class Ball(GameSprite):
    def update(self):
        if self.rect.x > 0 and self.rect.x < win_width - self.width:
            self.rect.x += self.x_speed
        if self.rect.x <= 0:
            self.x_speed *= -1
            self.rect.x += self.x_speed
            global scores 
            scores -= 1

        if self.rect.x >= win_width - self.width:
            self.x_speed *= -1
            self.rect.x += self.x_speed
            scores += 1

        if self.rect.y > 0 and self.rect.y < win_height - self.height:
            
            self.rect.y += self.y_speed
        else:
            self.y_speed *= -1
            self.rect.y += self.y_speed


        self.rect.y += self.y_speed
            




window = display.set_mode((win_width,win_height))
background = transform.scale(image.load("Black.jpg"),(win_width,win_height))
player1 = Player("White.jpg",25,win_height/2,15,100,20,20,1)
player2 = Player("White.jpg",win_width-40,win_height/2,15,100,20,20,2)
ball = Ball("White.jpg",win_width/2,win_height/2,25,25,5,5)


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

    if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
        ball.x_speed *= -1
    ball.update()
    ball.reset()
    

    display.update()
    time.delay(time_delay)
