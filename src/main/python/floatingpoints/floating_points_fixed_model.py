import random
from multiprocessing import Array
import src.main.python.floatingpoints.floating_points_fixed_worker as worker
class FloatingPointModel():
    def __init__(self, width, height):
        self.points = []
        self.width = width
        self.height = height
        self.max_speed = 15

    def addPoint(self, color, radius):
        new_point = Array('i', 5)
        new_point[0] = random.randint(0, self.width)
        new_point[1] = random.randint(0, self.height)
        new_point[2] = 1
        new_point[3] = color
        new_point[4] = radius
        point_worker = worker.WorkerProcess(new_point, self.max_speed, self.width, self.height)
        point_worker.start()
        self.points.append([new_point, point_worker])
        pass

    def removePoint(self):
        point_worker = self.points.pop()
        point_worker[0][2] = 0
        point_worker[1].close()
        point_worker[1] = None
        point_worker[0] = None
        point_worker = None
        pass