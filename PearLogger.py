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
signedIn = list()


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
        lineCount = 0
        for line in inf:
            lineCount += 1

            #  parse through data in each line
            try:
                raw = str.strip(line)
                delimited = re.split(';', raw)
                number = str.strip(delimited[0])
                name = str.strip(delimited[1])
                picture_path = "data/profilepics/"+str.strip(delimited[2])
                # print(number+"|"+name+"|"+picture_path)
            except:
                print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")

            #  check if number already exists in dictionary
            if (number in peopleDict.keys()):
                print("ERROR: Duplicate numbers in people file (#" + number + ") (data/people.pear, line " + str(
                    lineCount) + ")")
                continue

            #  record the data in a dictionary
            peopleDict[number] = (name, picture_path)


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
        self.studentTable.setRowCount(4)
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
        self.mentorTable.setRowCount(4)
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

    #  configures tables and widgets and stuff
    def configureStuff(self):
        #  enter key will call logEntry method
        self.numberEntry.returnPressed.connect(self.logEntry)

    #  signs in the number inside the line edit
    def logEntry(self):
        try:
            #  get the number, clear the line
            number = int(self.numberEntry.text())
            self.numberEntry.setText('')
        except:
            return
        #  decide whether to sign the number in/out
        if(number in signedIn):
            logOut(number)
        else:
            logIn(number)

def logIn(self, number):
    signedIn.append(number)

def logOut(self, number):
    signedIn.remove(number)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    setup();
    Ui_MainWindow.configureStuff(ui)

    sys.exit(app.exec_())