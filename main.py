import pygame
import os
pygame.init()

def path_file(file_name):
    folder_path = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder_path, file_name)
    return path


WIN_WIDTH = 900
WIN_HEIGHT = 700
FPS = 40
RED = (100, 0, 0)
BLACK = (0, 0, 0)
GREY = (60, 60, 60)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

fon = pygame.image.load(path_file("fon.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

win_picture = pygame.image.load(path_file("fon.jpg"))
win_picture = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

pygame.mixer.music.load(path_file("fon_muzika.ogg"))
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(10)

music_win = pygame.mixer.Sound(path_file("pobeda.ogg"))

music_lose = pygame.mixer.Sound(path_file("porazhenie.ogg"))
music_lose.set_volume(0.5)

music_shoot = pygame.mixer.Sound(path_file("perezaryadka.ogg"))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def __init__(self, x, y, width, height, img, speed):
        super().__init__(x, y, width, height, img)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIN_WIDTH or self.rect.right < 0:
            self.kill()








class Enemy(GameSprite):
    def __init__(self, x, y, width, height, file_name, speed, direction, min_coord, max_coord):
        super().__init__(x, y, width, height, file_name)
        self.speed = speed
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord

    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed
            if self.direction == "right":
                self.rect.x += self.speed

            if self.rect.right >= self.max_coord:
                self.direction = "left"
            if self.rect.left <= self.min_coord:
                self.direction = "right"

        elif self.direction == "up" or self.direction == "down":
            if self.direction == "down":
                self.rect.y += self.speed
            if self.direction == "up":
                self.rect.y -= self.speed

            if self.rect.top <= self.min_coord:
                self.direction = "down"
            if self.rect.bottom >= self.max_coord:
                self.direction = "up"



            


class Player(GameSprite):
    def __init__(self, x, y, width, height, img):
        super().__init__(x, y, width, height, img)
        self.speed_x = 0
        self.speed_y = 0
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.speed_x > 0 and self.rect.right < WIN_WIDTH or self.speed_x < 0 and self.rect.left > 0:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
                self.rect.right = min(self.rect.right, wall.rect.left)
        elif self.speed_x < 0:
            for wall in walls_touched:
                self.rect.left = max(self.rect.left, wall.rect.right)

        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
        elif self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
   

    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 10, 10, path_file("stenka (2).jpg"), 5)
            bullets.add(bullet)
        if self.direction == "left":
            bullet = Bullet(self.rect.left - 10 , self.rect.centery, 10, 10, path_file("stenka (2).jpg"), -5)
            bullets.add(bullet)


class Button():
    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.font30 = pygame.font.SysFont("arial", 30)
        self.text = self.font30.render(text, True, BLACK)

    def button_show(self, px_x, px_y):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + px_x, self.rect.y + px_y))

button_start = Button(GREY, 50, 50, 100, 50, "start")
button_exit = Button(GREY, 50, 150, 100, 50, "exit")

player = Player(100, 100, 50, 50, path_file("doom_guy__2_-removebg-preview (1).png"))

bullets = pygame.sprite.Group()

enemies = pygame.sprite.Group()

teleport = GameSprite(120, 450, 50, 50, path_file("teleport.jpg"))

enemies = pygame.sprite.Group()
vrag1 = Enemy(350, 80, 50, 50, path_file("vrag-removebg-preview.png"), 4, "up", 200, 400)
enemies.add(vrag1)
vrag2 = Enemy(400, 275, 250, 20, path_file("vrag3.png"), 4, "right", 200, 400)
enemies.add(vrag2)
vrag3 = Enemy(350, 80, 50, 50, path_file("vrag-removebg-preview.png"), 4, "up", 200, 400)
enemies.add(vrag3)
vrag4 = Enemy(350, 80, 50, 50, path_file("vrag-removebg-preview.png"), 4, "right", 200, 400)
enemies.add(vrag4)
vrag5 = Enemy(350, 80, 50, 50, path_file("vrag-removebg-preview.png"), 4, "up", 200, 400)
enemies.add(vrag5)
vrag6 = Enemy(350, 80, 50, 50, path_file("vrag-removebg-preview.png"), 4, "up", 200, 400)
enemies.add(vrag6)

walls = pygame.sprite.Group()
wall_1 = GameSprite(0, 275, 450, 20, path_file("stenka (2).jpg"))
walls.add(wall_1)
wall_2 = GameSprite(250, 0, 10, 200, path_file("stenka (2).jpg"))
walls.add(wall_2)
wall_3 = GameSprite(450, 80, 10, 200, path_file("stenka (2).jpg"))
walls.add(wall_3)
wall_4 = GameSprite(450, 70, 250, 10, path_file("stenka (2).jpg"))
walls.add(wall_4)
wall_5 = GameSprite(700, 80, 10, 200, path_file("stenka (2).jpg"))
walls.add(wall_5)
wall_6 = GameSprite(450, 275, 250, 20, path_file("stenka (2).jpg"))
walls.add(wall_6)
wall_6 = GameSprite(850, 0, 10, 530, path_file("stenka (2).jpg"))
walls.add(wall_6)
wall_7 = GameSprite(620, 530, 230, 10, path_file("stenka (2).jpg"))
walls.add(wall_7)
wall_8 = GameSprite(620, 400, 10, 450, path_file("stenka (2).jpg"))
walls.add(wall_8)
wall_9 = GameSprite(400, 650, 230, 10, path_file("stenka (2).jpg"))
walls.add(wall_9)
wall_10 = GameSprite(400, 500, 10, 200, path_file("stenka (2).jpg"))
walls.add(wall_10)
wall_11 = GameSprite(300, 500, 100, 10, path_file("stenka (2).jpg"))
walls.add(wall_11)
wall_12 = GameSprite(300, 500, 10, 200, path_file("stenka (2).jpg"))
walls.add(wall_12)
wall_13 = GameSprite(190, 600, 120, 10, path_file("stenka (2).jpg"))
walls.add(wall_13)
wall_14 = GameSprite(180, 430, 10, 340, path_file("stenka (2).jpg"))
walls.add(wall_14)
wall_15 = GameSprite(100, 430, 90, 10, path_file("stenka (2).jpg"))
walls.add(wall_15)
wall_16 = GameSprite(100, 430, 10, 130, path_file("stenka (2).jpg"))
walls.add(wall_16)


level = 0



game = True
play = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 0:
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if button_start.rect.collidepoint(x, y):
                    button_start.color = RED
                elif button_exit.rect.collidepoint(x, y):
                    button_exit.color = RED
                else:
                    button_start.color = GREY
                    button_exit.color = GREY
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_start.rect.collidepoint(x, y):
                    level = 1
                elif button_exit.rect.collidepoint(x, y):
                    game = False
        elif level == 1:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 5
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = -5
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = -5
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 5
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    music_shoot.play()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.speed_x = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.speed_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.speed_y = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.speed_y = 0


    if level == 0:
        window.fill(RED)
        button_start.button_show(17,17)
        button_exit.button_show(17,17)
    elif level == 1:
        if play:
            window.blit(fon, (0, 0))
            player.reset()
            player.update()

            enemies.draw(window)
            enemies.update()

            teleport.reset()
            
            bullets.draw(window)
            bullets.update()
        

            walls.draw(window)

            if pygame.sprite.collide_rect(player, teleport):
                play = False
                window.blit(win_picture, (0, 0))
                pygame.mixer.music.stop()
                music_win.play()
        
            if pygame.sprite.spritecollide(player, enemies, False):
                play = False
                window.blit(win_picture, (0, 0))
                pygame.mixer.music.stop()
                music_lose.play()

            pygame.sprite.groupcollide(bullets, walls, True, False)
            pygame.sprite.groupcollide(bullets, enemies, True, True)


    clock.tick(FPS)
    pygame.display.update()