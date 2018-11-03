# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/my_floating_points.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 480)
        Form.setMinimumSize(QtCore.QSize(480, 480))
        Form.setMaximumSize(QtCore.QSize(480, 480))
        Form.setAutoFillBackground(False)
        self.button_new_point = QtWidgets.QPushButton(Form)
        self.button_new_point.setGeometry(QtCore.QRect(10, 420, 221, 23))
        self.button_new_point.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_new_point.setObjectName("button_new_point")
        self.button_del_last_point = QtWidgets.QPushButton(Form)
        self.button_del_last_point.setGeometry(QtCore.QRect(250, 420, 221, 23))
        self.button_del_last_point.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_del_last_point.setObjectName("button_del_last_point")
        self.point_area = QtWidgets.QWidget(Form)
        self.point_area.setGeometry(QtCore.QRect(10, 10, 461, 401))
        self.point_area.setAutoFillBackground(False)
        self.point_area.setObjectName("point_area")
        self.sl_radius = QtWidgets.QSlider(Form)
        self.sl_radius.setGeometry(QtCore.QRect(40, 450, 160, 22))
        self.sl_radius.setMinimum(3)
        self.sl_radius.setMaximum(50)
        self.sl_radius.setOrientation(QtCore.Qt.Horizontal)
        self.sl_radius.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sl_radius.setTickInterval(5)
        self.sl_radius.setObjectName("sl_radius")
        self.rb_black = QtWidgets.QRadioButton(Form)
        self.rb_black.setGeometry(QtCore.QRect(260, 450, 51, 17))
        self.rb_black.setChecked(True)
        self.rb_black.setObjectName("rb_black")
        self.rb_red = QtWidgets.QRadioButton(Form)
        self.rb_red.setGeometry(QtCore.QRect(310, 450, 41, 17))
        self.rb_red.setObjectName("rb_red")
        self.rb_green = QtWidgets.QRadioButton(Form)
        self.rb_green.setGeometry(QtCore.QRect(360, 450, 51, 17))
        self.rb_green.setObjectName("rb_green")
        self.rb_blue = QtWidgets.QRadioButton(Form)
        self.rb_blue.setGeometry(QtCore.QRect(420, 450, 41, 17))
        self.rb_blue.setObjectName("rb_blue")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 450, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 450, 16, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "My Floating Points"))
        self.button_new_point.setText(_translate("Form", "New Point"))
        self.button_del_last_point.setText(_translate("Form", "Remove Last Point"))
        self.rb_black.setText(_translate("Form", "Black"))
        self.rb_red.setText(_translate("Form", "Red"))
        self.rb_green.setText(_translate("Form", "Green"))
        self.rb_blue.setText(_translate("Form", "Blue"))
        self.label.setText(_translate("Form", "3"))
        self.label_2.setText(_translate("Form", "50"))

