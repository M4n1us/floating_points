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
        self.draw_area = self.ui.point_area.contentsRect()
        self.ui.point_area.show()
        self.setUpdatesEnabled(True)
        width = self.draw_area.width()
        height = self.draw_area.height()
        self.model = model.FloatingPointModel(self, width, height)
        self.running = True
        self.app = application
        pass

    def new_point(self):
        """
        Add a new point
        """
        print("new_point")
        if self.ui.rb_black.isChecked():
            color = 0
        elif self.ui.rb_red.isChecked():
            color = 1
        elif self.ui.rb_green.isChecked():
            color = 2
        elif self.ui.rb_blue.isChecked():
            color = 3
        radius = self.ui.sl_radius.value()
        self.model.addPoint(color, radius)
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

        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        qp.end()

        pass

    def draw_points(self, qt_painter):
        """
        Drawing all the Points from the point_positions List in their colours and sizes

        :param qt_painter: Painter Object for Widget painting
        :return:
        """
        for point in self.model.points:
            x = point[0][0] + self.draw_area.topLeft().x()
            y = point[0][1] + self.draw_area.topLeft().y()
            color_id = point[0][3]
            radius = point[0][4]
            color = self.model.color[str(color_id)]
            qt_painter.setBrush(color)
            qt_painter.drawEllipse(QPoint(x, y), radius, radius)
        pass

    def closeEvent(self, event):
        """
        Overriding QWidget method for implementing the close event

        Closing all running process from point_positions
        Setting also safe_close to True, which closes the application.

        :param event: Event object which contains the event parameters
        :return:
        """
        with self.model.condition as cond:
            self.model.close()
            cond.wait()
            self.running = False
            self.app.exit()
            sys.exit()

    def refresh_loop(self):
        """
        Refreshing the GUI every .025 seconds and processing any QApplication Events
        """
        while self.running:
            #self.update()
            #QWidget.update()
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
        #print(str(point_position[0]) + " " + str(point_position[1]))
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
    sys.exit(app.exec())
