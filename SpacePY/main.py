import vec2
import gameObj
import player
import pygame
import bullets
import asteroids

pygame.init()

# < -- var here -- >
screenWidth = 800
screenHeight = 600
playerSize = vec2.vec2(40,40)
playerPos = vec2.vec2(screenWidth/2 - playerSize.x/2, 500)
p = player.player(playerPos, playerSize)
bulletMgr = bullets.bullets()
asteroidMgr = asteroids.asteroids()

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
gray = (128,128,128)

# ----

display = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Space Shooter')

while not p.exit:
    # < -- keys -- >
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         print(len(bulletMgr.bullets))
        p.stering(event)
    p.update(bulletMgr)
    bulletMgr.update()
    asteroidMgr.update(bulletMgr, p)
    # ----

    # < -- graphics -- >
    display.fill(black)
    p.draw(display, white)
    bulletMgr.draw(display, yellow)
    asteroidMgr.draw(display, gray)
    pygame.display.update()
    # ----