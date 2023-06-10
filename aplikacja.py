import sys
import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow,QColorDialog,QInputDialog
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage
from User_interface import Ui_MainWindow
from ctypes import CDLL, c_char_p, c_float


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.a = CDLL("./bin/libprotolib.so")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionChange_color.triggered.connect(self.show_color_dialog)
        self.ui.actionCircle.triggered.connect(self.Circle)
        self.ui.actionEllipse.triggered.connect(self.Ellipse)
        self.ui.actionRectangle.triggered.connect(self.Rectangle)
        #self.ui.actionLine.triggered.connect(self.Line)
        self.ui.actionLine.triggered.connect(self.set_current_tool_line)  # Установка текущего инструмента на линии
        self.start_coords = None
        self.end_coords = None
        self.current_tool = None

    def set_current_tool_line(self):  
        self.current_tool = 'Line'
        #pass


    def Circle(self):
        x, k1 = QInputDialog.getInt(self, "Circle coordinates", "Enter x-coordinate:")
        y, k2 = QInputDialog.getInt(self, "Circle coordinates", "Enter y-coordinate:")
        if k1 and k2:
            print("Circle coordinates:", x, y)
    def Line(self):
            #self.a.add_line(c_float(0), c_float(0), c_float(300), c_float(300))
            self.a.add_line(c_float(self.start_coords.x()), c_float(self.start_coords.y()- 21), c_float(self.end_coords.x()), c_float(self.end_coords.y()- 21))
            self.ui.openGLWidget.update()


    def Ellipse(self):
        print("Ellipse")

    def Rectangle(self):
        x, k1 = QInputDialog.getInt(self, "Height of Rectangle", "Enter x-coordinate:")
        y, k2 = QInputDialog.getInt(self, "Length  of Rectangle", "Enter y-coordinate:")
        if k1 and k2:
            print("Circle coordinates:", x, y)

    def show_color_dialog(self):
        color = QColorDialog.getColor()
        # if color.isValid():
        #     self.ui.openGLWidget.setStyleSheet("background-color: {}".format(color.name()))
        
    def resizeEvent(self, event):
        self.ui.openGLWidget.resize(event.size())  # Изменение размера виджета при изменении размеров окна
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.current_tool == 'Line': 
                self.start_coords = event.pos()
            #self.lastPoint = event.position()
            #print(self.lastPoint)
            #print(event.pos())

            #x, y = event.pos().x(), event.pos().y()


            #print(self.start_coords.x() if self.start_coords else None)
            #print(self.start_coords.y() if self.start_coords else None)

            #print(x, y)
    def mouseReleaseEvent(self, event):
        
        if event.button() == Qt.MouseButton.LeftButton:
            if self.current_tool == 'Line':
                self.end_coords = event.pos()
                self.Line()



            #x, y = event.pos().x(), event.pos().y()
            #print(self.end_coords.x() if self.end_coords else None)
            #print(self.end_coords.y() if self.end_coords else None)     
            #print(x, y)




    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.MouseButton.LeftButton):
            self.lastPoint = event.position()
            self.update()
            #print(self.lastPoint)

# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())
def main():
    QtWidgets.QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseOpenGLES, True)
    app = QtWidgets.QApplication([''])
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    os.putenv("QT_OPENGL", "angle")
    main()
