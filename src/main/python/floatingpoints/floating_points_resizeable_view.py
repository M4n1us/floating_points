# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/my_floating_points_resizable.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 480)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(65536, 65536))
        Form.setAutoFillBackground(False)
        self.button_new_point = QtWidgets.QPushButton(Form)
        self.button_new_point.setGeometry(QtCore.QRect(10, 450, 221, 23))
        self.button_new_point.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_new_point.setObjectName("button_new_point")
        self.button_del_last_point = QtWidgets.QPushButton(Form)
        self.button_del_last_point.setGeometry(QtCore.QRect(250, 450, 221, 23))
        self.button_del_last_point.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_del_last_point.setObjectName("button_del_last_point")
        self.point_area = QtWidgets.QWidget(Form)
        self.point_area.setGeometry(QtCore.QRect(10, 10, 461, 431))
        self.point_area.setObjectName("point_area")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "My Floating Points"))
        self.button_new_point.setText(_translate("Form", "New Point"))
        self.button_del_last_point.setText(_translate("Form", "Remove Last Point"))

