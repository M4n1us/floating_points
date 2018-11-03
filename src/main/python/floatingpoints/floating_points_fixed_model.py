import random
from multiprocessing import Array
import src.main.python.floatingpoints.floating_points_fixed_worker as worker
class FloatingPointModel():
    """
    Model package which implements the floating_point logic
    """
    def __init__(self, width, height):
        """
        Initiates the model logic
        :param width: window height
        :param height: window width
        """
        self.points = []
        self.width = width
        self.height = height
        self.max_speed = 15

    def addPoint(self, color, radius):
        """
        Adds a point to the point list and starts the worker process
        :param color: color, value 0 <= x <= 3
        :param radius: radius of point, value 3 <= x <= 50
        :return: None
        """
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
        """
        Removes a point with LIFO
        :return: None
        """
        point_worker = self.points.pop()
        point_worker[0][2] = 0
        point_worker[1].close()
        point_worker[1] = None
        point_worker[0] = None
        point_worker = None
        pass

    def close(self):
        """
        Called when all worker processes should be shut down
        :return: None
        """
        for el in self.points:
            self.removePoint()