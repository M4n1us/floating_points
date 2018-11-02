from src.main.python.floatingpoints.floating_points_fixed_controller import living_point
from multiprocessing import Process
import random

class WorkerProcess(Process):
    def __init__(self, point_info, width, height, max_speed):
        """

        :param point_info:
        :param width:
        :param height:
        """
        Process.__init__(self)
        self.point_info = point_info
        self.width = width
        self.height = height
        self.max_speed = max_speed

    def run(self):
        """

        :return:
        """
        vx = random.randint(1, self.max_speed)
        vy = random.randint(1, self.max_speed)

        living_point(self.point_info, vx, vy, self.width, self.height)
