import vec2
import gameObj
import pygame
import time
import random
import collide

class asteroids:
    def __init__(self):
        self.asteroids = []
        self.desTime = time.time() + 0.2

    def new(self, v1):
        newAsteroid = gameObj.gameObj(v1, vec2.vec2(40,40))
        self.asteroids.append(newAsteroid)

    def canSpawn(self):
        if time.time() > self.desTime:
            self.desTime = time.time() + 0.2
            return True
        else:
            return False

    def draw(self, display, color):
        for asteroid in self.asteroids:
            pygame.draw.rect(display, color, [asteroid.pos.x, asteroid.pos.y, asteroid.size.x, asteroid.size.y])

    def update(self, bulletsMgr, player):
        colider = collide.collide()

        if self.canSpawn():
            self.new(vec2.vec2(random.randint(20,780), -50))

        for bullet in bulletsMgr.bullets:
            for asteroid in self.asteroids:
                if colider.collideRectRect(asteroid, bullet):
                    bulletsMgr.delete(bullet)
                    self.asteroids.remove(asteroid)

        for asteroid in self.asteroids:
            if colider.collideRectRect(player.var, asteroid):
                player.exit = True
            asteroid.pos.y += 0.2
            if asteroid.pos.y >= 600:
                self.asteroids.remove(asteroid)

