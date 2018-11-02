from src.main.python.floatingpoints.floating_points_fixed_controller import living_point
import random
from multiprocessing import Process, Value, Array
class FloatingPointModel():
    def __init__(self, width, height):
        self.points = []
        self.width = width
        self.height = height

    def addPoint(self, color, radius):
        new_point = Array('i', 5)
        new_point[0] = random.randint(0, self.width)
        new_point[1] = random.randint(0, self.height)
        new_point[2] = 1
        new_point[3] = color
        new_point[4] = radius
        self.points.append(new_point)

        pass

    def removePoint(self):
        pass