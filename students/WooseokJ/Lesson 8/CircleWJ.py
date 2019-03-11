import io
import pytest
import math
from math import pi

# Basic properties of circle
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * (self.radius**2)

#  alternator constructor that will let the use create a circle directly with the diameter
    @classmethod
    def from_diameter(cls, value):
        return cls(value/2)

    def __str__(self):
        return "circle with radius: {:.4f}".format(self.radius)

    def __repr__(self):
        return "circle({})".format(self.radius)

    def __add__(self, other):
        return self.radius + other.radius

    def __rmul__(self, other):
        return self.radius * other

    def __mul__(self, other):
        return self.radius * other

    def __div__(self, value):
        return self.radius / value

# allow to compre between two circles
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False

    def sort_var(self):
        return self.radius

# sphere class for properties spheres

class Sphere(Circle):
    @property
    def __str__(self):
        return "sphere with radius: {:.2f}".format(self.radius)

    def __repr__(self):
        return "sphere({})".format(self.radius)

    @property
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    @property
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)


#Test the Circle class


def test_radius():
    c = Circle(3)
    assert c.radius == 3


def test_diameter():
    c = Circle(2)
    assert c.diameter == 4


def test_set_diameter():
    c = Circle(4)
    c.diameter = 5
    assert c.diameter == 5
    assert c.radius == 2.5


def test_constructor():
    c = Circle.from_diameter(4)
    assert c.diameter == 4
    assert c.radius == 2


def test_str():
    c = Circle(4)
    string = str(c)
    assert string == "circle with radius: 4.0000"


def test_repr():
    c = Circle(4)
    d = repr(c)
    assert d == 'circle(4)'


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    assert (c1 + c2) == Circle(6)


def test_mul():
    c1 = Circle(4)
    assert (c1 * 3) == Circle(12)


def test_less():
    c1 = Circle(3)
    c2 = Circle(5)
    assert c1.radius < c2.radius


def test_greater():
    c1 = Circle(5)
    c2 = Circle(3)
    assert c1.radius > c2.radius


def test_equal():
    c1 = Circle(6)
    c2 = Circle(6)
    assert c1.radius == c2.radius
