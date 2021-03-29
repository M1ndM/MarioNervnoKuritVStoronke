import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 600
bgImage = pygame.image.load("Assets/bg.png")
# goLeft = pygame.image.load("Assets/Charm50.png")
goRight = pygame.image.load("Assets/ReversCharm50.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.startX = 3
        self.startY = 550
        self.speed = 10
        self.isJump = False
        self.jumpCount = 15
        self.animCount = 0
        self.right = False
        self.left = False
        self.image = pygame.image.load('Assets/Charm50.png')
        self.rect = self.image.get_rect()

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):

        super().__init__()

        self.image = pygame.image.load('Assets/platform.png')


        self.rect = self.image.get_rect()

class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()

        self.player = player


    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        screen.blit(bgImage, (0, 0))
        self.platform_list.draw(screen)


class Level_01(Level):
    def __init__(self, player):
        Level.__init__(self, player)


        level = [
            [150, 71, 500, 500],
            [150, 71, 200, 400],
            [150, 71, 600, 300],
        ]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    hero = Player()

    level_list = []
    level_list.append((Level_01(hero)))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    hero.level = current_level

    active_sprite_list.add(hero)



    run = True
    while run:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                run = False

        clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.startX > 5:
            hero.startX -= hero.speed
            hero.left = True
            hero.right = False

        if keys[pygame.K_RIGHT] and hero.startX < 790:
            hero.startX += hero.speed
            hero.right = True
            hero.left = False

        if not(hero.isJump):
            if keys[pygame.K_SPACE]:
                hero.isJump = True

        else:
            if hero.jumpCount >= -15:
                hero.startY -= hero.jumpCount*2
                hero.jumpCount -= 1
            else:
                hero.isJump = False
                hero.jumpCount = 15

        win.blit(bgImage, (0, 0))

        active_sprite_list.update()
        current_level.update()

        current_level.draw(win)
        


        if hero.left:
            win.blit(hero.image, (hero.startX, hero.startY))
        elif hero.right:
            win.blit(goRight, (hero.startX, hero.startY))
        else:
            win.blit(goRight, (hero.startX, hero.startY))

        pygame.display.update()





if __name__ == '__main__':
    main()