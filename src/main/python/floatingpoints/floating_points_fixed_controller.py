import sys, time

from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from src.main.python.floatingpoints import floating_points_fixed_view as view, floating_points_fixed_model as model


class FloatingPointController(QWidget):
    """
    MVC pattern: Creates a controller according to the mvc pattern.

    :ivar safe_close: Safe closing of initiated points
    :ivar point_positions: List of points as a reference to a Integer-Array of Shared memory
    :ivar main_form: Qt Form
    """

    def __init__(self, application):
        super().__init__()
        #uic.loadUi('../ui/my_floating_points.ui', self)
        self.ui = view.Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_new_point.clicked.connect(self.new_point)
        self.ui.button_del_last_point.clicked.connect(self.remove_point)
        draw_area = self.ui.point_area.contentsRect()
        width = draw_area.width()
        height = draw_area.height()
        self.model = model.FloatingPointModel(self, width, height)
        self.running = True
        self.app = application
        pass

    def new_point(self):
        """
        Add a new point
        """
        print("new_point")
        self.model.addPoint(2, 1)
        pass

    def remove_point(self):
        """
        Remove the last initiated point
        """
        print("del_last_point")
        self.model.removePoint()
        pass

    def paintEvent(self, event):
        """ React to a paint event

        :param event: QPaintEvent, but we ignore the value and repaint the whole qwidget
        """

        pass

    def draw_points(self, qt_painter):
        """
        Drawing all the Points from the point_positions List in their colours and sizes

        :param qt_painter: Painter Object for Widget painting
        :return:
        """
        pass

    def closeEvent(self, event):
        """
        Overriding QWidget method for implementing the close event

        Closing all running process from point_positions
        Setting also safe_close to True, which closes the application.

        :param event: Event object which contains the event parameters
        :return:
        """
        self.model.close()
        self.running = False
        self.app.exit()

    def refresh_loop(self):
        """
        Refreshing the GUI every .025 seconds and processing any QApplication Events
        """
        self.app.exec()
        while self.running:
            self.update()
            QApplication.processEvents()
            time.sleep(0.025)

    def get_view(self):
        return self.ui

    def get_model(self):
        return self.model


def living_point(point_position, vx, vy, window_width, window_height):
    """
    Method for concurrent processing of 2D-points

    :param point_position: Reference to Integer-Array as Shared memory
    :param vx:
    :param vy:
    :param window_width:
    :param window_height:

    """
    while point_position[2]:
        print(str(point_position[0]) + " " + str(point_position[1]))
        dx = int((point_position[0] + vx) / window_width)
        dy = int((point_position[1] + vy) / window_height)
        dx2 = point_position[0] + vx < 0
        dy2 = point_position[1] + vy < 0
        point_position[0] = point_position[0] + vx - dx * ((point_position[0] + vx) % window_width) - dx2 * (
                    point_position[0] + vx)
        point_position[1] = point_position[1] + vy - dy * ((point_position[1] + vy) % window_height) - dy2 * (
                    point_position[1] + vy)
        vx = int((-2 * (dx - 0.5)) * int(-2 * (dx2 - 0.5)) * vx)
        vy = int((-2 * (dy - 0.5)) * int(-2 * (dy2 - 0.5)) * vy)
        time.sleep(0.05)


if __name__ == "__main__":
    """
    Changed from specifications because the way it was implemented doesn't work when exiting the program as it enters
    an infinite loop while the even loop has already been exited.
    Positioned start of app into refresh_loop where events are processed.
    """
    app = QApplication(sys.argv)
    c = FloatingPointController(app)
    c.show()
    c.refresh_loop()
    sys.exit()
