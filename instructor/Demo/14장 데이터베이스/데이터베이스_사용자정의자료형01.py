class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Point(%f, %f)" % (self.x, self.y)

    
