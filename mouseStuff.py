from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class GrafixScene(QGraphicsScene):
    mousePressSignal = Signal(int, int)
    mouseReleasedSignal = Signal(int, int)
    mouseMoveSignal = Signal(int, int)
    procDone = Signal(str)

    def __init__(self, parent=None):
        super(GrafixScene, self).__init__(parent)
        self.position = None
        self.pressedRXY = QPoint()
        self.releasedRXY = QPoint()
        self.presentXY = QPoint()
        self.lastPoint = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.position = QPointF(event.scenePos())
            self.mousePressSignal.emit(int(self.position.x()), int(self.position.y()))
            self.pressedRXY = event.scenePos()
            self.lastPoint = event.scenePos()
            # print(self.position.x(), ", ", self.position.y())
            self.update()
        super(GrafixScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.position = QPointF(event.scenePos())
        self.mouseMoveSignal.emit(int(self.position.x()), int(self.position.y()))
        self.presentXY = event.scenePos()
        # print(self.position.x(), ", ", self.position.y())
        self.update()
        super(GrafixScene, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            self.position = QPointF(event.scenePos())
            self.mouseReleasedSignal.emit(int(self.position.x()), int(self.position.y()))
            self.releasedRXY = event.scenePos()
            self.update()
        super(GrafixScene, self).mouseReleaseEvent(event)

    def keyPressEvent(self, event):  # QKeyEvent
        if event.key() == Qt.Key_Delete:
            print('del key pressed')
        if event.key() == Qt.Key_Escape:
            print('escape key pressed')
        super(GrafixScene, self).keyPressEvent(event)

