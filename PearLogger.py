# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PearLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import re


peopleDict = dict()


def setup():
    #  read in data
    people_file = Path("data/people.pear")

    if not people_file.exists():
        #  create new people file
        file = open("data/people.pear", 'w')
        #  writen in example data
        file.write("0;example name;example_picture.png")
        file.close()

    #  loop through file and process people
    with open("data/people.pear") as inf:
        for line in inf:
            raw = str.strip(line)
            delimited = re.split(';', raw)
            print(delimited)
            



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/Pearadox Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 811, 751))
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(161)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(187)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(830, 90, 241, 671))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setGridSize(QtCore.QSize(0, 0))
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(830, 10, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(1080, 10, 331, 751))
        self.tableWidget_2.setRowCount(4)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(164)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(187)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClear_All = QtWidgets.QAction(MainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionSign_Out_All = QtWidgets.QAction(MainWindow)
        self.actionSign_Out_All.setObjectName("actionSign_Out_All")
        self.menuActions.addAction(self.actionClear_All)
        self.menuActions.addAction(self.actionSign_Out_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionClear_All.setText(_translate("MainWindow", "Clear All"))
        self.actionSign_Out_All.setText(_translate("MainWindow", "Sign Out All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    setup();

    sys.exit(app.exec_())