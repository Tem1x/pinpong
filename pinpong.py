from pygame import *
speed_x = 3
speed_y = 3
#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

Raketka_1 = Player('red.png', 20, 200, 30, 120, 5)
Raketka_2 = Player('blue.png', 550, 200, 30, 120, 5)
ball = GameSprite("ball.png", 250, 300, 50, 50, 10)
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        Raketka_1.update_r()
        Raketka_2.update_l()
        Raketka_1.reset()
        Raketka_2.reset()
        ball.reset()
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(Raketka_1, ball) or  sprite.collide_rect(Raketka_2, ball):
        speed *= -1
    display.update()
    clock.tick(FPS)
