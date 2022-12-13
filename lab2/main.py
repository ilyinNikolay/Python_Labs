import json
from abc import abstractmethod
from math import *


class Shape:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimetr(self):
        return self.a * 4

    def __repr__(self):
        return f"You have {type(self).__name__}"


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a + self.b) * 2

    def __repr__(self):
        return f"You have {type(self).__name__}"


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimetr(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f"You have {type(self).__name__}"


class Circle(Shape):
    def __init__(self, r):
        self._r = r

    def area(self):
        return pi * self._r ** 2

    def perimetr(self):
        return 2 * pi * self._r

    def __repr__(self):
        return f"You have {type(self).__name__}"


def write(data, filename):
    json.dump(data, open(filename, 'w'), indent=4)


def read_json(filename):
    return json.load(open(filename, 'r'))


shapesArray = [Triangle(3, 4, 5), Circle(5), Rectangle(4, 5), Square(5), Circle(3), Triangle(3, 3, 3)]

shapes = {
    'shape': []
}

for obj in shapesArray:
    shapes['shape'].append(obj.__dict__)

write(shapes, 'test.json')

shapesArray.clear()
shapes['shape'].clear()

shapes = read_json('test.json')

for obj in shapes['shape']:
    if type(obj).__name__ == "Triangle":
        shapesArray.append(Triangle(obj['a'], obj['b'], obj['c']))
    elif type(obj).__name__ == "Circle":
        shapesArray.append(Circle(obj['_r']))
    elif type(obj).__name__ == "Rectangle":
        shapesArray.append(Rectangle(obj['a'], obj['b']))
    elif type(obj).__name__ == "Square":
        shapesArray.append(Square(obj['a']))

for obj in shapesArray:
    print(obj.__repr__())
