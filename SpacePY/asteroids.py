import vec2
import gameObj
import pygame
import time
import random
import collide
import time

class asteroids:
    def __init__(self):
        self.asteroids = []
        self.desTime = time.time() + 0.2
        self.bigImg = pygame.image.load("png/meteorBig.png").convert_alpha()
        self.smallImg = pygame.image.load("png/meteorSmall.png").convert_alpha()
        self.startTime = time.time()

    def timer(self):
        self.curentTime = time.time() - self.startTime

    def new(self, v1):
        image = None
        rand = random.randint(0,100)
        if rand > 25:
            image = self.smallImg
        else:
            image = self.bigImg

        newAsteroid = gameObj.gameObj(v1, vec2.vec2(image.get_width(),image.get_height()), image)
        self.asteroids.append(newAsteroid)

    def clear(self):
        for asteroid in self.asteroids:
            self.asteroids.remove(asteroid)

    def canSpawn(self):
        if time.time() > self.desTime:
            self.desTime = time.time() + 0.4 - self.curentTime/50
            return True
        else:
            return False

    def draw(self, display):
        for asteroid in self.asteroids:
            #pygame.draw.rect(display, color, [asteroid.pos.x, asteroid.pos.y, asteroid.size.x, asteroid.size.y])
            display.blit(asteroid.image, (asteroid.pos.x, asteroid.pos.y))

    def update(self, bulletsMgr, player):
        colider = collide.collide()
        self.timer()

        if self.canSpawn():
            self.new(vec2.vec2(random.randint(20,780), -50))

        for bullet in bulletsMgr.bullets:
            for asteroid in self.asteroids:
                if colider.collideRectRect(asteroid, bullet):
                    bulletsMgr.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    player.score += 1
                    print(player.score)

        for asteroid in self.asteroids:

            if colider.collideRectRect(player.var, asteroid):
                player.exit = True
                self.clear()
                bulletsMgr.clear()

            asteroid.pos.y += 0.2
            if asteroid.pos.y >= 600:
                self.asteroids.remove(asteroid)

