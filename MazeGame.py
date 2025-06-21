import pygame
import time

Width = 1000
Height = 500
Blue = (0, 135, 255)
pygame.font.init()

window = pygame.display.set_mode((Width, Height))
window.fill(Blue)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, self.rect)


class Player(GameSprite):
    def __init__(self, width, height, x, y, image, speed_x, speed_y):
        GameSprite.__init__(self, width, height, x, y, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.start_x = x
        self.start_y = y

    def control(self):
        #if player.rect.x <= Width and player.speed_x > 0 or player.rect.x >= 0 and player.speed_x < 0:
            #player.rect.x += self.speed_x
            pass

    def update_wall(self, walls):
        self.rect.x += self.speed_x

        for wall in pygame.sprite.spritecollide(self, walls, False):
            if self.speed_x > 0:
                self.rect.right = wall.rect.left
            if self.speed_x < 0:
                self.rect.left = wall.rect.right


        self.rect.y += self.speed_y
        for wall in pygame.sprite.spritecollide(self, walls, False):
            if self.speed_y > 0:
                self.rect.bottom = wall.rect.top
            if self.speed_y < 0:
                self.rect.top = wall.rect.bottom

    def update_enemy(self, enemies):
        if pygame.sprite.spritecollide(self, enemies, False):
            self.rect.x = self.start_x
            self.rect.y = self.start_y

    def update_reward(self, reward, run):
        if pygame.sprite.collide_rect(self, reward):
            reward.rect.x = 10000
            reward.rect.y = -10000
            reward.reset()
            font = pygame.font.SysFont("Arial", 60)
            win = font.render("You Win!", True, (255, 255, 255))
            window.blit(win, (Width/2, Height/2))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False
            exit()





class Enemy(GameSprite):
    side = "right"
    def __init__(self, width, height, x, y, image, speed_x):
        GameSprite.__init__(self, width, height, x, y, image)
        self.speed_x = speed_x

    def update(self, left_point, right_point):
        time.sleep(0.01)
        if self.rect.x < left_point:
            self.side = "right"
        elif self.rect.x > right_point:
            self.side = "left"

        if self.side == "left":
            self.rect.x -= self.speed_x
        elif self.side == "right":
            self.rect.x += self.speed_x







player = Player(50, 50, 50, 400, "player.png", 20, 10)
wall1 = GameSprite(50, 300, 150, 250, "wall.png")
wall2 = GameSprite(50, 300, 300, 0, "wall.png")
wall3 = GameSprite(400, 50, 300, 375, "wall.png")
wall4 = GameSprite(50, 50, 300, 375, "wall.png")
wall5 = GameSprite(50, 275, 450, 100, "wall.png")
wall6 = GameSprite(150, 50, 500, 225, "wall.png")
wall7 = GameSprite(50, 300, 750, 0, "wall.png")
wall8 = GameSprite(175, 50, 750, 250, "wall.png")
enemy1 = Enemy(50,50,375,30,"ghost.png", 2)
enemy2 = Enemy(50, 50,225, 435,"ghost.png",2)
reward1 = GameSprite(75,75,875,30,"treasure.png")

walls = pygame.sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)
walls.add(wall8)

enemies = pygame.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)

reward_collected = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    player.speed_x = 0
    player.speed_y = 0

    if keys[pygame.K_LEFT]:
        player.speed_x = -4
    if keys[pygame.K_RIGHT]:
        player.speed_x = 4
    if keys[pygame.K_UP]:
        player.speed_y = -4
    if keys[pygame.K_DOWN]:
        player.speed_y = 4



    window.fill(Blue)
    enemy1.update(375, 625)
    enemy2.update(225, 800)
    player.control()
    for wall in walls:
        wall.reset()
    for enemy in enemies:
        enemy.reset()
    if not reward_collected:
        reward1.reset()
    player.reset()

    player.update_wall(walls)
    player.update_enemy(enemies)
    player.update_reward(reward1, run)

    pygame.display.update()


