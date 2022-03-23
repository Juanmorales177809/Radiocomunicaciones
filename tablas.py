

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabla'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        # Añadir diseño de caja(Box Layout), agregue la tabla al diseño de la caja y agregue el diseño de la caja al widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Mostrar Widget
        self.show()
 
    def createTable(self):
       # Crea Tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.setItem(4,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(4,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(5,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(5,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(6,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(6,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(7,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(7,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # cambio de selección de tabla
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

