import vec2

class gameObj:
    def __init__(self, v1, v2, img=None):
        self.pos = vec2.vec2(v1.x, v1.y)
        self.size = vec2.vec2(v2.x, v2.y)
        self.image = img