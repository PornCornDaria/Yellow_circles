import sys

from random import randint

from PyQt5.QtGui import QPainter, QColor

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('UI.ui', self)
		self.pushButton.clicked.connect(self.paint)
		self.do_paint = False
		
	def paintEvent(self, event):
		if self.do_paint:
			qp = QPainter()
			qp.begin(self)
			self.draw_ellipse(qp)
			qp.end()
	
	def paint(self):
		self.do_paint = True
		self.repaint()
	
	def draw_ellipse(self, qp):
		qp.setBrush(QColor(255, 255, 0))
		a = randint(20, 150)
		x = randint(0, 450)
		y = randint(0, 350)
		qp.drawEllipse(x, y, a, a)
	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.show()
	sys.exit(app.exec_())
