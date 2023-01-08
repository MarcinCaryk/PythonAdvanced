class Ball(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

ball1 = Ball('blue', 'small')
ball2 = Ball('blue', 'small')

print(ball1 == ball2)
print(id(ball1))
print(id(ball2))


class Ball(object):

    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self, other):
        return self.color == other.color and self.size == other.size

    def __ne__(self, other):
        return self.color != other.color or self.size != other.size


ball1 = Ball('blue', 'small')
ball2 = Ball('blue', 'small')
ball3 = Ball('green', 'small')

print(ball1 == ball2)
print(ball1 == ball3)

