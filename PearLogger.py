
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from InitiationDialog import Ui_initiationDialog as Form
import re, time, datetime

peopleDict = dict()  # k: ID number  v: tuple (name, picture_path, type (s=student/m=mentor)
signedIn = list()  # numbers representing profile ID numbers
loginTime = dict()  # k: ID number  v: long (most recent login in epoch time)
record = dict()  # k: ID number  v: seconds of login time
timestamp = dict()  # k: ID number  v: logged in time

month = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# makes a prompt window with a Error icon, makes people cry and depressed. Also gives concussions from banging heads
def yellAtUser(title, message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)  # set the icon of the prompt
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.resize()
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
    msg.exec()


# makes a prompt window with a Information icon, used for giving user info
def tellUser(title,message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)  # set the icon of the prompt
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.resize(500,500)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
    msg.exec()


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
                if (len(str(picture_path)) is 0) or (not picture_path.exists()):
                    picture_path = Path('data/profilepics/default.jpg')
            except:
                print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")

            #  check if number already exists in dictionary
            if number in peopleDict.keys():
                print("ERROR: Duplicate numbers in people file (#" + number + ") (data/people.pear, line " + str(
                    lineCount) + ")")
                continue

            #  record the data in a dictionary
            peopleDict[number] = (name, str(picture_path), type)

    #  process hours into dictionary
    with open("data/record.pear") as inf:
        for line in inf:
            delimited = re.split('\|', line)
            ID = str.strip(delimited[0])
            time_raw = str.strip(delimited[1])
            time_delimited = re.split(':', time_raw)
            total_seconds = int(time_delimited[0]) * 3600 + int(time_delimited[1]) * 60 + int(time_delimited[2])
            record[ID] = total_seconds

    updateRecordFile()

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
        self.leaderboardLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
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
        self.actionGenerate_Report = QtWidgets.QAction(mainWindow)
        self.actionGenerate_Report.setObjectName("actionGenerate_Report")
        self.menuActions.addAction(self.actionSign_Out_All)
        self.menuActions.addAction(self.actionClear_All)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionAdd_Person)
        self.menuActions.addAction(self.actionGenerate_Report)
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
        self.actionGenerate_Report.setText(_translate("mainWindow", "Generate Report"))

    #  configures tables and widgets and stuff
    def configureStuff(self):

        #  random custom configurations for the ui
        self.studentTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  #  make cells unhighlightable
        self.actionSign_Out_All.triggered.connect(signOutAll)
        self.actionClear_All.triggered.connect(clearAll)
        self.actionAdd_Person.triggered.connect(openInitiationDialog)
        self.actionReload_Data.triggered.connect(setup)
        self.actionGenerate_Report.triggered.connect(generateReport)

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
            logout(number, False)
        else:
            login(number)


def login(ID):
    #  count number of mentors, used for determining which row/col to put icon in
    mentorCount = 0
    for i in signedIn:
        if peopleDict[i][2] == 'm':
            mentorCount += 1

    if peopleDict[ID][2] == 'm':
        #  calculate next available mentor cell
        rows = ui.mentorTable.rowCount()
        columns = ui.mentorTable.columnCount()

        nextRow = mentorCount / columns
        nextColumn = (mentorCount) % columns

        createIDBox(ID, nextRow, nextColumn)
    else:
        #  calculate next available student cell

        rows = ui.studentTable.rowCount()
        columns = ui.studentTable.columnCount()

        studentCount = len(signedIn) - mentorCount
        nextRow = studentCount / columns
        nextColumn = (studentCount) % columns

        createIDBox(ID, nextRow, nextColumn)

    signedIn.append(ID)
    loginTime[ID] = time.time()
    timestamp[ID] = getTimeStamp()


#  essentially signs everyone out then everyone back in except the one who just logged out (removes gaps)
#  clear = don't record hours(boolean)
def logout(ID, clear):
    print(ID)
    #  removes person from si1gned in list, stops tracking time
    signedIn.remove(ID)

    #  add timestamp to log file
    log_file = open("data/log.pear", 'a')
    log_toWrite = str(ID) + "|" + timestamp[ID] + "|" + getTimeStamp() + "\n"
    log_file.write(log_toWrite)
    log_file.close()

    #  adds new time to record and updates it
    global loginTime
    loginTime = int(time.time() - loginTime[ID])
    name = peopleDict[ID][0]
    if ID not in record.keys():
        record[ID] = 0
    if clear:
        loginTime = 0
    record[ID] += loginTime
    updateRecordFile()

    #  count number of mentors, used for determining which row/col to remove from
    mentorCount = 0
    for i in signedIn:
        if peopleDict[i][2] == 'm':
            mentorCount += 1

    #  decide to remove from mentor table or student table
    if peopleDict[ID][2] == 'm':
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


#  signs out all people
def signOutAll():
    while len(signedIn) > 0:
        logout(signedIn[0], False)


#  clears all people, doesn't record hours
def clearAll():
    while len(signedIn) > 0:
        logout(signedIn[0], True)


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
    file.truncate(0)  # clears file
    sorted_record = sorted(record.items(), key=lambda kv: kv[1])  # sort by item, gives list of tuples

    #  clear leaderboards to prepare for update
    for i in range(0, 9):
        ui.leaderboardTable.removeCellWidget(0,i)

    #  loop through all names
    for i in range(0, len(record.keys())):
        index = len(sorted_record)-i-1  # go in reverse, greatest first
        ID = sorted_record[index][0]
        hours = int(sorted_record[index][1] / 3600)
        minutes = int(sorted_record[index][1] % 3600 / 60)
        seconds = int(sorted_record[index][1] % 60)
        toWrite = ID + " | " + str("%02d" % hours) + ":" + str("%02d" % minutes) + ":" + str("%02d" % seconds) + "\n"

        if ID not in peopleDict.keys():
            i -= 1
            continue

        file.write(toWrite)

        #  add name to leaderboard if in the first 10
        if i < 10:
            leaderboardNameLabel = QtWidgets.QLabel()
            leaderboardNameLabel.setText(peopleDict[ID][0])
            ui.leaderboardTable.setCellWidget(i, 0, leaderboardNameLabel)
    file.close()


def openInitiationDialog():
    #  Hides the question mark
    InitiationDialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint |
                                         QtCore.Qt.WindowCloseButtonHint)
    InitiationDialog.ui = Form()
    InitiationDialog.ui.setupUi(InitiationDialog)
    InitiationDialog.ui.setup()
    InitiationDialog.exec_()
    InitiationDialog.show()


#  returns string
def getTimeStamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#  generates csv report
#  columns: ID, name, is_student, date in, time in, date out, time out, calculated
#  on side: ID, name, meetings attended, total time
def generateReport():
    #  read in log
    log_file = open('data/log.pear', 'r')
    logs = log_file.readlines()
    for log in logs:
        log = str.strip(log)
        delimited = re.split('\|', log)
        ID = str.strip(delimited[0])
        timestamp_in = str.strip(delimited[1])
        timestamp_out = str.strip(delimited[2])
        if ID not in peopleDict:
            continue
        timestamp_in_delimited = re.split(' ', timestamp_in)
        timestamp_out_delimited = re.split(' ', timestamp_out)
        timestamp_in_date_delimited = re.split('-', timestamp_in_delimited[0])
        timestamp_in_time_delimited = re.split(':', timestamp_in_delimited[1])
        timestamp_out_date_delimited = re.split('-', timestamp_out_delimited[0])
        timestamp_out_time_delimited = re.split(':', timestamp_out_delimited[1])

        in_year = int(timestamp_in_date_delimited[0])
        in_month = int(timestamp_in_date_delimited[1])
        in_day = int(timestamp_in_date_delimited[2])
        in_hour = int(timestamp_in_time_delimited[0])
        in_minute = int(timestamp_in_time_delimited[1])
        in_second = int(timestamp_in_time_delimited[2])
        in_hour_converted = in_hour
        in_PM = False
        if in_hour >= 12:
            in_PM = True
            if in_hour > 12:
                in_hour_converted -= 12

        out_year = int(timestamp_out_date_delimited[0])
        out_month = int(timestamp_out_date_delimited[1])
        out_day = int(timestamp_out_date_delimited[2])
        out_hour = int(timestamp_out_time_delimited[0])
        out_minute = int(timestamp_out_time_delimited[1])
        out_second = int(timestamp_out_time_delimited[2])
        out_PM = False
        out_hour_converted = out_hour
        if out_hour >= 12:
            out_PM = True
            if out_hour > 12:
                out_hour_converted -= 12

        datetime_in = datetime.datetime(in_year, in_month, in_day, in_hour, in_minute, in_second)
        datetime_out = datetime.datetime(out_year, out_month, out_day, out_hour, out_minute, out_second)
        dt_delta = datetime_out-datetime_in

        delta_h = dt_delta.seconds / 3600 + dt_delta.days * 24
        delta_m = dt_delta.seconds % 3600 / 60
        delta_s = dt_delta.seconds % 60

        in_weekday = weekday[datetime_in.weekday()]
        out_weekday = weekday[datetime_out.weekday()]

        #  gather all the data
        name = peopleDict[ID][0]
        isStudent = peopleDict[ID][2] == 's'
        dateIn = in_weekday + ", " + month[in_month-1] + " " + str("%02d" % in_day) + ", " + str(in_year)
        dateOut = out_weekday + ", " + month[out_month-1] + " " + str("%02d" % out_day) + ", " + str(out_year)
        timeIn = str("%02d" % in_hour) + ":" + str("%02d" % in_minute) + ":" + \
                 str("%02d" % in_second) + " " + 'PM' if in_PM else 'AM'
        timeOut = str("%02d" % out_hour) + ":" + str("%02d" % out_minute) + ":" + \
                  str("%02d" % out_second) + " " + 'PM' if out_PM else 'AM'
        calculated = str(delta_h) + ":" + str(delta_m) + ":" + str(delta_s)

        sorted_record = sorted(record.items(), key=lambda kv: kv[1])  # sort by item, gives list of tuples


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


