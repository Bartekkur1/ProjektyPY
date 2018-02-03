import vec2
import gameObj

class collide:
    def collideRectRect(self, gameobj1, gameobj2):
        if(gameobj1.pos.x + gameobj1.size.x >= gameobj2.pos.x and
           gameobj1.pos.x <= gameobj2.pos.x + gameobj2.size.x and
           gameobj1.pos.y + gameobj1.size.y >= gameobj2.pos.y and
           gameobj1.pos.y <= gameobj2.pos.y + gameobj2.size.y):
            return True
        else:
            return False