from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(591, 424)
        self.graphicsView = QtWidgets.QGraphicsView(MainForm)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 591, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(MainForm)
        self.pushButton.setGeometry(QtCore.QRect(-10, 390, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainForm)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 390, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainForm)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 390, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.pushButton.setText(_translate("MainForm", "PushButton"))
        self.pushButton_2.setText(_translate("MainForm", "PushButton"))
        self.pushButton_3.setText(_translate("MainForm", "PushButton"))
