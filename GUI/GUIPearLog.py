# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PearLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:/Private/Pictures/Pearadox Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.studentTable = QtWidgets.QTableWidget(self.centralwidget)
        self.studentTable.setGeometry(QtCore.QRect(10, 10, 1071, 1011))
        self.studentTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.studentTable.setRowCount(15)
        self.studentTable.setColumnCount(6)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.horizontalHeader().setVisible(False)
        self.studentTable.horizontalHeader().setDefaultSectionSize(175)
        self.studentTable.horizontalHeader().setHighlightSections(False)
        self.studentTable.horizontalHeader().setMinimumSectionSize(39)
        self.studentTable.verticalHeader().setVisible(False)
        self.studentTable.verticalHeader().setDefaultSectionSize(187)
        self.studentTable.verticalHeader().setHighlightSections(False)
        self.numberEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEntry.setGeometry(QtCore.QRect(1130, 10, 241, 41))
        self.numberEntry.setObjectName("numberEntry")
        self.mentorTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mentorTable.setGeometry(QtCore.QRect(1430, 0, 491, 1021))
        self.mentorTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mentorTable.setRowCount(15)
        self.mentorTable.setColumnCount(3)
        self.mentorTable.setObjectName("mentorTable")
        self.mentorTable.horizontalHeader().setVisible(False)
        self.mentorTable.horizontalHeader().setDefaultSectionSize(156)
        self.mentorTable.horizontalHeader().setHighlightSections(False)
        self.mentorTable.verticalHeader().setVisible(False)
        self.mentorTable.verticalHeader().setDefaultSectionSize(187)
        self.mentorTable.verticalHeader().setHighlightSections(False)
        self.leaderboardLabel = QtWidgets.QLabel(self.centralwidget)
        self.leaderboardLabel.setGeometry(QtCore.QRect(1080, 310, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        self.leaderboardLabel.setFont(font)
        self.leaderboardLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.leaderboardLabel.setObjectName("leaderboardLabel")
        self.leaderboardTable = QtWidgets.QTableWidget(self.centralwidget)
        self.leaderboardTable.setGeometry(QtCore.QRect(1090, 380, 331, 641))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.leaderboardTable.setFont(font)
        self.leaderboardTable.setRowCount(10)
        self.leaderboardTable.setColumnCount(1)
        self.leaderboardTable.setObjectName("leaderboardTable")
        self.leaderboardTable.horizontalHeader().setVisible(False)
        self.leaderboardTable.horizontalHeader().setDefaultSectionSize(300)
        self.leaderboardTable.verticalHeader().setVisible(True)
        self.leaderboardTable.verticalHeader().setDefaultSectionSize(63)
        self.leaderboardTable.verticalHeader().setSortIndicatorShown(False)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionClear_All = QtWidgets.QAction(mainWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionSign_Out_All = QtWidgets.QAction(mainWindow)
        self.actionSign_Out_All.setObjectName("actionSign_Out_All")
        self.actionAdd_Person = QtWidgets.QAction(mainWindow)
        self.actionAdd_Person.setObjectName("actionAdd_Person")
        self.actionReload_Data = QtWidgets.QAction(mainWindow)
        self.actionReload_Data.setObjectName("actionReload_Data")
        self.menuActions.addAction(self.actionSign_Out_All)
        self.menuActions.addAction(self.actionClear_All)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionAdd_Person)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionReload_Data)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.leaderboardLabel.setText(_translate("mainWindow", "Leaderboard"))
        self.menuActions.setTitle(_translate("mainWindow", "Actions"))
        self.actionClear_All.setText(_translate("mainWindow", "Clear All"))
        self.actionSign_Out_All.setText(_translate("mainWindow", "Sign Out All"))
        self.actionAdd_Person.setText(_translate("mainWindow", "Add Person"))
        self.actionReload_Data.setText(_translate("mainWindow", "Reload Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

