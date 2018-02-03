class vec2:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def add(self, vec2):
        self.x += vec2.x
        self.y += vec2.y

    def sub(self, vec2):
        self.x -= vec2.x
        self.y -= vec2.y

    def toString(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

#function math.dist(x1,y1, x2,y2) return ((x2-x1)^2+(y2-y1)^2)^0.5 end
    def dist(self, vec1):
        return pow(pow((self.x - vec1.x),2) + pow((self.y - vec1.y),2),0.5)

