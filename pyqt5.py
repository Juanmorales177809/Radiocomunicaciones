from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys

app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("map.html"))
web.setWindowTitle('Vista Radio Enlace')
web.setWindowIcon(QtGui.QIcon('antenaroja.ico'))
web.resize(800, 600)
web.show()
app.exec()