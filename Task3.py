class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

class Square(Parallelogram):
    def __init__(self, side):
        super(Square, self).__init__(side, side)
        self.side = side

    def get_area(self):
        return self.side ** 2


parallelogram1 = Parallelogram(4, 4)
print(parallelogram1.get_area())

square1 = Square(7)
print(square1.get_area())
