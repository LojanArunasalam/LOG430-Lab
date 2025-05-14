from circle import circumference
from circle import diameter
import math

def test_circumference():
    assert circumference(3) == 2*3*math.pi

def test_diameter():
    assert diameter(3) == 6