import vec2
import gameObj
import pygame

class bullets:
    def __init__(self):
        self.bullets = []

    def new(self, v1):
        newBullet = gameObj.gameObj(v1, vec2.vec2(2,8))
        self.bullets.append(newBullet)

    def draw(self, display, color):
        for bullet in self.bullets:
            pygame.draw.rect(display, color, [bullet.pos.x, bullet.pos.y, bullet.size.x, bullet.size.y])

    def update(self):
        for bullet in self.bullets:
            bullet.pos.y -= 0.2
            if bullet.pos.y <= 0:
                self.bullets.remove(bullet)

    def delete(self, bullet):
        self.bullets.remove(bullet)