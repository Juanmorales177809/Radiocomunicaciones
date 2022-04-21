from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets 
from PyQt5.QtWebEngineWidgets import QWebEngineView





app = QApplication(sys.argv)
web = QWebEngineView()

web.load(QUrl("https://www.google.com/maps/place/Guarne,+Antioquia/@6.2798404,-75.4596754,14z/data=!3m1!4b1!4m5!3m4!1s0x8e4426aedc749c1b:0x9eacd415c5a0e4c6!8m2!3d6.2825086!4d-75.4445972"))
web.setWindowTitle('Vista Radio Enlace')
web.setWindowIcon(QtGui.QIcon('./assets/antena.ico'))
web.resize(800, 600)
web.show()
app.exec()
sys.exit(app.exec_())



# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Mapas")
#         Dialog.resize(400, 400)
        
#         self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.centralwidget = QtWidgets.QWidget(Dialog)
#         self.centralwidget.setObjectName("centralwidget")
#         self.webEngineView =               QtWebEngineWidgets.QWebEngineView(self.centralwidget)
#         self.webEngineView.load(QtCore.QUrl().fromLocalFile(os.path.split(os.path.abspath(__file__))[0]+r'.\gradel\index.html'))
#         self.verticalLayout.addWidget(self.webEngineView)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.verticalLayout.addWidget(self.buttonBox)
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Mapas", "Google Maps"))
#         Dialog.setWindowIcon(QtGui.QIcon('./assets/antena.ico'))
# if __name__ == "__main__":
    
    # app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())