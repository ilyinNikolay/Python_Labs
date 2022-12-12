import json
from abc import abstractmethod
from math import *


class Shape:
    def __int__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self.a = a
        self.name = "Square"

    def area(self):
        print(f"Area of Square with side {str(self.a)} is {self.a ** 2}")

    def perimetr(self):
        print(f"Perimetr of {self.name} is {self.a * 4}")

    def show(self):
        print(f"You have {self.name}")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = "Rectangle"

    def area(self):
        print(f"Area of {self.name} with sides {self.a} and {self.b} is {self.a * self.b}")

    def perimetr(self):
        print(f"Perimetr of {self.name} is {(self.a + self.b) * 2}")

    def show(self):
        print(f"You have a {self.name}")


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"

    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"Area of {self.name} with sides {self.a}, {self.b} and {self.c} is {_area}")

    def perimetr(self):
        print(f"Perimetr of {self.name} is {self.a + self.b + self.c}")

    def show(self):
        print(f"You have {self.name}")


class Circle(Shape):
    def __init__(self, r):
        self._r = r
        self.name = "Circle"

    def area(self):
        print(f"Area of {self.name} with radius {self._r} is {pi * self._r ** 2}")

    def perimetr(self):
        print(f"Perimetr of {self.name} is {2 * pi * self._r}")

    def show(self):
        print(f"You have {self.name}")


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


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
    if obj["name"] == "Triangle":
        shapesArray.append(Triangle(obj['a'], obj['b'], obj['c']))
    elif obj["name"] == "Circle":
        shapesArray.append(Circle(obj['_r']))
    elif obj["name"] == "Rectangle":
        shapesArray.append(Rectangle(obj['a'], obj['b']))
    else:
        shapesArray.append(Square(obj['a']))

for obj in shapesArray:
    obj.show()
