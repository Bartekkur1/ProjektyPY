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

display = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Space Shooter')


playerSize = vec2.vec2(40,40)
playerPos = vec2.vec2(screenWidth/2 - playerSize.x/2, 500)
p = player.player(playerPos)
bulletMgr = bullets.bullets()
asteroidMgr = asteroids.asteroids()
exit = False
clock = pygame.time.Clock()
clock.tick(50)

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
gray = (128,128,128)
czcionka = pygame.font.SysFont("monospace", 20)
resetMsg = czcionka.render("Game over - press r to reset", 1, white)
# ----

while not exit:
    # < -- keys -- >
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        p.stering(event, asteroidMgr)
    if not p.exit:
        p.update(bulletMgr)
        bulletMgr.update()
        asteroidMgr.update(bulletMgr, p)
    else:
        if len(bulletMgr.bullets) > 0:
            bulletMgr.clear()
            print("clearing bullets")
        if len(asteroidMgr.asteroids) > 0:
            asteroidMgr.clear()
            print("clearing asteroids")
    # ----

    # < -- graphics -- >
    if not p.exit:
        display.fill(black)
        p.draw(display, white)
        bulletMgr.draw(display, yellow)
        asteroidMgr.draw(display)
        pygame.display.update()
    else:
        scoreMsg = czcionka.render("Your score : " + str(p.score), 1, white)
        display.fill(black)
        display.blit(resetMsg, (400 - resetMsg.get_width()/2,300))
        display.blit(scoreMsg, (400 - resetMsg.get_width()/2,200))
        pygame.display.update()
    # ----