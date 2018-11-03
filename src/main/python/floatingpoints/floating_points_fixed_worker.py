from src.main.python.floatingpoints.floating_points_fixed_controller import living_point
from multiprocessing import Process
import random

class WorkerProcess(Process):
    """
    Describes a worker Process that processes point coordinates while taking
    window width, height and max speed into account
    """
    def __init__(self, point_info, max_speed, width, height):
        """
        Initiates the Process
        :param point_info: 0:x pos, 1:y pos, 2:alive. 3:color, 4:radius
        :param width: Window width
        :param height: Window height
        :param max_speed: Max point speed
        """
        Process.__init__(self)
        self.point_info = point_info
        self.width = width
        self.height = height
        self.max_speed = max_speed

    def run(self):
        """
        Generates velocity according to max speed and moves point
        :return: None
        """
        vx = random.randint(1, self.max_speed)
        vy = random.randint(1, self.max_speed)

        living_point(self.point_info, vx, vy, self.width, self.height)
