
from PySide6.QtWidgets import (QWidget, QVBoxLayout,
                               QHBoxLayout,
                               QProgressBar, QLabel)
from PySide6.QtGui import QPainter, QBrush, QPixmap, QBitmap, QColor 
from PySide6.QtCore import QRect


class GProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)

    def paintEvent(self, event):
        super().paintEvent(event)

        # Draw mask on top
        bm = QBitmap(self.size())
        bm.fill(QColor(255,255,255))
        p = QPainter(bm) 
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(QColor(0,0,0))
        p.pen().setWidth(300)
        p.setBrush(QColor(0,0,0))
        radius = 7 
        p.drawRoundedRect(QRect(0,0, bm.width() - 50, bm.height()),radius,radius)
        p.end()
        self.setMask(bm)


class GDisplayWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        # Horizontal layout
        Hlayout = QHBoxLayout(self)

        # Set icon to the right of everything
        self.icon = QLabel()
        Hlayout.addWidget(self.icon)

        # Vertical layout
        Vlayout = QVBoxLayout()
        Hlayout.addLayout(Vlayout)

        # setup other sub-components
        self.description = QLabel()
        self.pbar = GProgressBar()
        self.pbar.setTextVisible(True)
        
        # Set progress bar on top of description
        Vlayout.addWidget(self.pbar)
        Vlayout.addWidget(self.description)

        

    def setIcon(self, icon):
        if icon:
            self.icon.setPixmap(icon.pixmap(32, 32))
        else:
            self.icon.setPixmap(QPixmap())

