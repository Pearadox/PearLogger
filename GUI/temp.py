# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PearLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:/Private/Pictures/Pearadox Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.studentTable = QtWidgets.QTableWidget(self.centralwidget)
        self.studentTable.setGeometry(QtCore.QRect(10, 10, 811, 751))
        self.studentTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.studentTable.setRowCount(10)
        self.studentTable.setColumnCount(5)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.horizontalHeader().setVisible(False)
        self.studentTable.horizontalHeader().setDefaultSectionSize(161)
        self.studentTable.horizontalHeader().setHighlightSections(False)
        self.studentTable.horizontalHeader().setMinimumSectionSize(39)
        self.studentTable.verticalHeader().setVisible(False)
        self.studentTable.verticalHeader().setDefaultSectionSize(187)
        self.studentTable.verticalHeader().setHighlightSections(False)
        self.extraList = QtWidgets.QListWidget(self.centralwidget)
        self.extraList.setGeometry(QtCore.QRect(830, 90, 241, 671))
        self.extraList.setAutoFillBackground(False)
        self.extraList.setProperty("isWrapping", True)
        self.extraList.setGridSize(QtCore.QSize(0, 0))
        self.extraList.setWordWrap(True)
        self.extraList.setObjectName("extraList")
        self.numberEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEntry.setGeometry(QtCore.QRect(830, 10, 241, 41))
        self.numberEntry.setObjectName("numberEntry")
        self.mentorTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mentorTable.setGeometry(QtCore.QRect(1080, 10, 331, 751))
        self.mentorTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mentorTable.setRowCount(10)
        self.mentorTable.setColumnCount(2)
        self.mentorTable.setObjectName("mentorTable")
        self.mentorTable.horizontalHeader().setVisible(False)
        self.mentorTable.horizontalHeader().setDefaultSectionSize(164)
        self.mentorTable.horizontalHeader().setHighlightSections(False)
        self.mentorTable.verticalHeader().setVisible(False)
        self.mentorTable.verticalHeader().setDefaultSectionSize(187)
        self.mentorTable.verticalHeader().setHighlightSections(False)
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
        self.extraList.setCurrentRow(-1)
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
    sys.exit(app.exec_())

