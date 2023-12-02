from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x) ,player_y, width,height,min_x):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.min_x = min_x
        self.max_x = max_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.x >0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height-50:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width-50:
            self.rect.x += self.speed
