import gameObj
import vec2
import pygame
import bullets
import time

screenWidth = 800
screenHeight = 600


class player():
    def __init__(self, v1, v2):
        self.var = gameObj.gameObj(v1, v2)
        self.moveLeft = False
        self.moveRight = False
        self.shoot = False
        self.desTime = time.time() + 0.4
        self.exit = False

    def draw(self, display, color):
        pygame.draw.rect(display, color, [self.var.pos.x, self.var.pos.y, self.var.size.x, self.var.size.y])

    def canShoot(self):
        if(time.time() >= self.desTime):
            self.desTime = time.time() + 0.4
            return True
        else:
            return False

    def stering(self, event):
        # DO POPRAWIENIA HELLO BO NIE DZIALA KURDE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moveRight = True
                self.moveLeft = False
            if event.key == pygame.K_LEFT:
                self.moveRight = False
                self.moveLeft = True
            if event.key == pygame.K_SPACE:
                self.shoot = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moveRight = False
            if event.key == pygame.K_LEFT:
                self.moveLeft = False
            if event.key == pygame.K_SPACE:
                self.shoot = False

    def update(self, bulletsMgr):
        if self.shoot and self.canShoot():
            bulletsMgr.new(vec2.vec2(self.var.pos.x + self.var.size.x/2, self.var.pos.y))
        if self.moveRight and self.var.pos.x < screenWidth - self.var.size.x:
            self.var.pos.x += 0.3
        if self.moveLeft and self.var.pos.x > 0:
            self.var.pos.x -= 0.3