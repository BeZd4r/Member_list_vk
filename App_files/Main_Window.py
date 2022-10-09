# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/Uchi_icon.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(3, 133, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 481, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Path.setFont(font)
        self.Path.setToolTip("")
        self.Path.setStatusTip("")
        self.Path.setWhatsThis("")
        self.Path.setStyleSheet("")
        self.Path.setInputMask("")
        self.Path.setObjectName("Path")
        self.verticalLayout.addWidget(self.Path)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.New = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.New.setObjectName("New")
        self.horizontalLayout.addWidget(self.New)
        self.Exist = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Exist.setObjectName("Exist")
        self.horizontalLayout.addWidget(self.Exist)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Uchiton = QtWidgets.QLabel(self.centralwidget)
        self.Uchiton.setGeometry(QtCore.QRect(320, 300, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Uchiton.setFont(font)
        self.Uchiton.setObjectName("Uchiton")
        self.Picture = QtWidgets.QLabel(self.centralwidget)
        self.Picture.setGeometry(QtCore.QRect(140, 10, 200, 200))
        self.Picture.setStyleSheet("")
        self.Picture.setText("")
        self.Picture.setPixmap(QtGui.QPixmap("media/Vk_icon.png"))
        self.Picture.setScaledContents(True)
        self.Picture.setObjectName("Picture")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Member list"))
        self.Path.setPlaceholderText(_translate("MainWindow", "Введите id группы"))
        self.New.setText(_translate("MainWindow", "Создать новую таблицу"))
        self.Exist.setText(_translate("MainWindow", "Обновить существующую таблицу"))
        self.Uchiton.setText(_translate("MainWindow", "@UchiTon"))