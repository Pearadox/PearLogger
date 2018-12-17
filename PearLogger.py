# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PearLog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import re, time

peopleDict = dict()  # k: ID number  v: tuple (name, picture_path, type (s=student/m=mentor)
signedIn = list()  # numbers representing profile ID numbers
log = dict()  # k: ID number  v: long (log in time in seconds)
record = dict()


def setup():
    #  read in data
    people_file = Path("data/people.pear")
    record_file = Path("data/record.pear")

    if not people_file.exists():
        #  create new people file
        file = open("data/people.pear", 'w')
        #  write in example data
        file.write("0;example name;example_picture.jpg")
        file.close()

    if not record_file.exists():
        #  create new record file
        file = open("data/record.pear", 'w')
        file.close()

    #  process people into dictionary
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
                picture_path = Path("data/profilepics/"+str.strip(delimited[2]))
                type = str.strip(delimited[3])

                #  make sure picture works or is not empty. otherwise use default
                if(len(str(picture_path)) is 0 or not picture_path.exists()):
                    picture_path = Path("data/profilepics/default.jpg")

            except:
                print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")

            #  check if number already exists in dictionary
            if (number in peopleDict.keys()):
                print("ERROR: Duplicate numbers in people file (#" + number + ") (data/people.pear, line " + str(
                    lineCount) + ")")
                continue

            #  record the data in a dictionary
            peopleDict[number] = (name, str(picture_path), type)

    #  process hours into dictionary
    with open("data/record.pear") as inf:
        for line in inf:
            delimited = re.split('\|', line)
            name = str.strip(delimited[0])
            time_raw = str.strip(delimited[1])
            time_delimited = re.split(':', time_raw)
            total_seconds = int(time_delimited[0]) * 3600 + int(time_delimited[1]) * 60 + int(time_delimited[2])
            record[name] = total_seconds


class Ui_mainWindow(object):

    def setupUi(self, MainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("G:/Private/Pictures/Pearadox Logo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.studentTable = QtWidgets.QTableWidget(self.centralwidget)
        self.studentTable.setGeometry(QtCore.QRect(10, 10, 811, 751))
        self.studentTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.studentTable.setRowCount(15)
        self.studentTable.setColumnCount(5)
        self.studentTable.setObjectName("studentTable")
        self.studentTable.horizontalHeader().setVisible(False)
        self.studentTable.horizontalHeader().setDefaultSectionSize(158)
        self.studentTable.horizontalHeader().setHighlightSections(False)
        self.studentTable.horizontalHeader().setMinimumSectionSize(39)
        self.studentTable.verticalHeader().setVisible(False)
        self.studentTable.verticalHeader().setDefaultSectionSize(187)
        self.studentTable.verticalHeader().setHighlightSections(False)
        self.numberEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEntry.setGeometry(QtCore.QRect(830, 10, 241, 41))
        self.numberEntry.setObjectName("numberEntry")
        self.mentorTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mentorTable.setGeometry(QtCore.QRect(1080, 10, 331, 751))
        self.mentorTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mentorTable.setRowCount(15)
        self.mentorTable.setColumnCount(2)
        self.mentorTable.setObjectName("mentorTable")
        self.mentorTable.horizontalHeader().setVisible(False)
        self.mentorTable.horizontalHeader().setDefaultSectionSize(156)
        self.mentorTable.horizontalHeader().setHighlightSections(False)
        self.mentorTable.verticalHeader().setVisible(False)
        self.mentorTable.verticalHeader().setDefaultSectionSize(187)
        self.mentorTable.verticalHeader().setHighlightSections(False)
        self.leaderboardLabel = QtWidgets.QLabel(self.centralwidget)
        self.leaderboardLabel.setGeometry(QtCore.QRect(830, 70, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        self.leaderboardLabel.setFont(font)
        self.leaderboardLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.leaderboardLabel.setObjectName("leaderboardLabel")
        self.leaderboardTable = QtWidgets.QTableWidget(self.centralwidget)
        self.leaderboardTable.setGeometry(QtCore.QRect(830, 120, 241, 641))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.menuActions.addAction(self.actionClear_All)
        self.menuActions.addAction(self.actionSign_Out_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.leaderboardLabel.setText(_translate("mainWindow", "Leaderboard"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuActions.setTitle(_translate("mainWindow", "Actions"))
        self.actionClear_All.setText(_translate("mainWindow", "Clear All"))
        self.actionSign_Out_All.setText(_translate("mainWindow", "Sign Out All"))

    #  configures tables and widgets and stuff
    def configureStuff(self):

        #  random custom configurations for the ui
        self.studentTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  #  make cells unhighlightable

        #  enter key will call logEntry method
        self.numberEntry.returnPressed.connect(self.logEntry)

    #  when enter key is pressed, signs in the number inside the line edit
    def logEntry(self):
        try:
            #  get the number, clear the line
            #  the int() cast will throw an error if the lineEdit value is not a integer (good thing)
            number = str(int(self.numberEntry.text()))

            self.numberEntry.setText('')
        except:
            return

        #  make sure we have the number
        if number not in peopleDict.keys():
            return

        #  decide whether to sign the number in/out
        if number in signedIn:
            logout(number)
        else:
            login(number)


def login(number):
    #  count number of mentors, used for determining which row/col to put icon in
    mentorCount = 0
    for i in signedIn:
        if peopleDict[i][2] == 'm':
            mentorCount += 1

    if peopleDict[number][2] == 'm':
        #  calculate next available mentor cell
        rows = ui.mentorTable.rowCount()
        columns = ui.mentorTable.columnCount()

        nextRow = mentorCount / columns
        nextColumn = (mentorCount) % columns

        createIDBox(number, nextRow, nextColumn)
    else:
        #  calculate next available student cell

        rows = ui.studentTable.rowCount()
        columns = ui.studentTable.columnCount()

        studentCount = len(signedIn) - mentorCount
        nextRow = studentCount / columns
        nextColumn = (studentCount) % columns

        createIDBox(number, nextRow, nextColumn)

    signedIn.append(number)
    log[number] = time.time()


#  essentially signs everyone out then everyone back in except the one who just logged out (removes gaps)
def logout(number):
    #  removes person from signed in list, stops tracking time
    signedIn.remove(number)

    #  adds new time to record and updates it
    loginTime = int(time.time() - log[number])
    name = peopleDict[number][0]
    if name not in record.keys():
        record[name] = 0
    record[name] += loginTime
    updateRecordFile()

    #  count number of mentors, used for determining which row/col to put icon in
    mentorCount = 0
    for i in signedIn:
        if peopleDict[i][2] == 'm':
            mentorCount += 1

    #  decide to remove from mentor table or student table
    if peopleDict[number][2] == 'm':
        #  clears all mentor table cells
        for r in range(0, ui.mentorTable.rowCount()):
            for c in range(0, ui.mentorTable.columnCount()):
                ui.mentorTable.removeCellWidget(r, c)

        #  get some table data
        rows = ui.mentorTable.rowCount()
        columns = ui.mentorTable.columnCount()

        #  add mentors back in
        studentsEncountered = 0
        for i in range(0, len(signedIn)):
            #  don't want to sign the students into the mentor table
            if (peopleDict[signedIn[i]][2] is not 'm'):
                studentsEncountered += 1
                continue
            createIDBox(signedIn[i], (i - studentsEncountered) / columns, (i - studentsEncountered) % columns)
    else:
        #  clears all student table cells
        for r in range(0, ui.studentTable.rowCount()):
            for c in range(0, ui.studentTable.columnCount()):
                ui.studentTable.removeCellWidget(r, c)

        #  get some table data
        rows = ui.studentTable.rowCount()
        columns = ui.studentTable.columnCount()

        #  add students back in
        mentorsEncountered = 0
        for i in range(0, len(signedIn)):
            #  don't want to sign the mentors into the students table
            if(peopleDict[signedIn[i]][2] == 'm'):
                mentorsEncountered += 1
                continue
            createIDBox(signedIn[i], (i-mentorsEncountered) / columns, (i-mentorsEncountered) % columns)


def createIDBox(number, row, column):
    #  bring in some info about the person
    name = peopleDict[number][0]
    picture_path = peopleDict[number][1]

    #  create their icon
    groupBox = QtWidgets.QGroupBox()  # container for holding everything
    personLabel = QtWidgets.QLabel(name + " (" + number + ")")  # label for name & ID number
    personLabel.setAlignment(QtCore.Qt.AlignCenter)
    personLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    pictureLabel = QtWidgets.QLabel()  # holds the picture/pixmap
    pictureLabel.setMaximumSize(150, 150)
    pixmap_raw = QtGui.QPixmap(picture_path)
    pixmap_scaled = pixmap_raw.scaled(pictureLabel.size(), QtCore.Qt.KeepAspectRatio)
    pictureLabel.setPixmap(pixmap_scaled)  # associate picture to the label
    #  put the name/ID label and the picture together in one vertical box container
    vbox = QtWidgets.QVBoxLayout()
    vbox.addWidget(pictureLabel)
    vbox.addWidget(personLabel)
    vbox.addStretch(1)
    groupBox.setLayout(vbox)  # add the vbox to groupbox

    #  add icon to mentor or student table
    if peopleDict[number][2] == 'm':
        ui.mentorTable.setCellWidget(row, column, groupBox)
    else:
        ui.studentTable.setCellWidget(row, column, groupBox)


#  updates the record file with the current records
def updateRecordFile():
    file = open("data/record.pear", 'w')
    file.truncate(0)
    sorted_record = sorted(record.items(), key=lambda kv: kv[1])  # sort by item, gives list of tuples

    #  clear leaderboards to prepare for update
    for i in range(0, 9):
        ui.leaderboardTable.removeCellWidget(0,i)

    #  loop through all names
    for i in range(0, len(record.keys())):
        index = len(sorted_record)-i-1  # go in reverse, greatest first
        name = sorted_record[index][0]
        hours = int(sorted_record[index][1] / 3600)
        minutes = int(sorted_record[index][1] % 3600 / 60)
        seconds = int(sorted_record[index][1] % 60)
        toWrite = name + " | " + str("%02d" % hours) + ":" + str("%02d" % minutes) + ":" + str("%02d" % seconds) + "\n"
        file.write(toWrite)

        #  add name to leaderboard if in the first 10
        if i < 10:
            print(i)
            leaderboardNameLabel = QtWidgets.QLabel()
            leaderboardNameLabel.setText(name)
            print(leaderboardNameLabel.text())
            ui.leaderboardTable.setCellWidget(i, 0, leaderboardNameLabel)
    file.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()

    setup()
    Ui_mainWindow.configureStuff(ui)

    sys.exit(app.exec_())


