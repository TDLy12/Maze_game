import pygame

Width = 1000
Height = 500
Blue = (0, 135, 255)

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


player = GameSprite(50, 50, 50, 400, "player.png")
wall1 = GameSprite(50, 300, 150, 250, "wall.png")
wall2 = GameSprite(50, 300, 300, 0, "wall.png")
wall3 = GameSprite(400, 50, 300, 375, "wall.png")
wall4 = GameSprite(50, 50, 300, 375, "wall.png")
wall5 = GameSprite(50, 275, 450, 100, "wall.png")
wall6 = GameSprite(150, 50, 500, 225, "wall.png")
wall7 = GameSprite(50, 300, 750, 0, "wall.png")
wall8 = GameSprite(175, 50, 750, 250, "wall.png")
enemy1 = GameSprite(50,50,450,30,"ghost.png")
reward1 = GameSprite(75,75,875,40,"treasure.png")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    wall4.reset()
    wall3.reset()
    wall2.reset()
    wall1.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    enemy1.reset()
    reward1.reset()
    player.reset()
    pygame.display.update()

