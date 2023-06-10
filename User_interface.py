import sys
import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtWidgets import QApplication, QMainWindow,QColorDialog
from OpenGL import GL as gl
from ctypes import CDLL, c_char_p, c_float
from PyQt6.QtCore import Qt
class Gl_Widget(QOpenGLWidget):
    def __init__(self, parent):
        QOpenGLWidget.__init__(self, parent)

        self.a = CDLL("./bin/libprotolib.so")
        self.a.init_svg()
        self.a.parse_svg(c_char_p('./test_files/test.svg'.encode('UTF-8')))

    def paintGL(self):
        self.a.draw()

    def initializeGL(self):
        self.a.init_gl()
        self.a.resize(c_float(500), c_float(420))
        #self.a.add_line(c_float(10), c_float(10), c_float(300), c_float(300))  # Example of adding a line

    def resizeGL(self, w: int, h: int):
        self.a.resize(c_float(w), c_float(h))


class Ui_MainWindow:
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 420)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = Gl_Widget(parent=self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 500, 420))

        self.openGLWidget.setObjectName("openGLWidget")

        #self.openGLWidget.setStyleSheet("background-color: white")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 0))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuColor = QtWidgets.QMenu(parent=self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuFigure = QtWidgets.QMenu(parent=self.menubar)
        self.menuFigure.setObjectName("menuFigure")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionDelete_all = QtGui.QAction(parent=MainWindow)
        self.actionDelete_all.setObjectName("actionDelete_all")

        self.actionChange_color = QtGui.QAction(parent=MainWindow)
        self.actionChange_color.setObjectName("actionChange_color")

        self.actionCircle = QtGui.QAction(parent=MainWindow)
        self.actionCircle.setObjectName("actionCircle")
        self.actionEllipse = QtGui.QAction(parent=MainWindow)
        self.actionEllipse.setObjectName("actionEllipse")
        self.actionRectangle = QtGui.QAction(parent=MainWindow)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionLine = QtGui.QAction(parent=MainWindow)
        self.actionLine.setObjectName("actionLine")


        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionDelete_all)
        self.menuColor.addAction(self.actionChange_color)

        self.menuFigure.addAction(self.actionCircle)
        self.menuFigure.addAction(self.actionEllipse)
        self.menuFigure.addAction(self.actionRectangle)
        self.menuFigure.addAction(self.actionLine)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuFigure.menuAction())


        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuFigure.setTitle(_translate("MainWindow", "Figure"))

        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionDelete_all.setText(_translate("MainWindow", "Delete all"))

        self.actionChange_color.setText(_translate("MainWindow", "Change color"))

        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.actionEllipse.setText(_translate("MainWindow", "Ellipse"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
