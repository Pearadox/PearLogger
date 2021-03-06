
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from InitiationDialog import Ui_initiationDialog as Form
import re, time, datetime

peopleDict = dict()  # k: ID number  v: tuple (name, picture_path, type (s=student/m=mentor)
signedIn = list()  # numbers representing profile ID numbers
loginTime = dict()  # k: ID number  v: long (most recent login in epoch time)
record = dict()  # k: ID number  v: seconds of login time
timestamp = dict()  # k: ID number  v: logged in time

#  configuration variables
shortest_time_sec = int()
longest_time_sec = int()
earliest_time_sec = int()
latest_time_sec = int()

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
    config_file = Path("data/config.pear")

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

    if not config_file.exists():
        #  create new config file, add default settings
        file = open("data/config.pear", 'w')
        file.write("Shortest_Time_Allowed=00:10:00\n")
        file.write("Longest_Time_Allowed=12:00:00\n")
        file.write("Earliest_Time_Allowed=08:00:00\n")
        file.write("Latest_Time_Allowed=00:00:00\n")
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

                #  check if number already exists in dictionary
                if number in peopleDict.keys():
                    print(
                        "ERROR: Duplicate numbers in people file (#" + number + ") (data/people.pear, line " + str(
                            lineCount) + ")")
                    continue

                #  record the data in a dictionary
                peopleDict[number] = (name, str(picture_path), type)
            except:
                print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")


    #  process hours into dictionary
    with open("data/record.pear") as inf:
        for line in inf:
            delimited = re.split('\|', line)
            ID = str.strip(delimited[0])
            time_raw = str.strip(delimited[1])
            time_delimited = re.split(':', time_raw)
            total_seconds = int(time_delimited[0]) * 3600 + int(time_delimited[1]) * 60 + int(time_delimited[2])
            record[ID] = total_seconds

    #  read in configuration
    with open("data/config.pear") as inf:
        for line in inf:
            delimited = re.split('=', line)
            if str.strip(delimited[0]) == "Longest_Time_Allowed":
                global longest_time_sec
                time_delimited = re.split(':', str.strip(delimited[1]))
                longest_time_sec = int(str.strip(time_delimited[0]))*3600 + \
                                   int(str.strip(time_delimited[1]))*60 + \
                                   int(str.strip(time_delimited[2]))
            elif str.strip(delimited[0]) == "Shortest_Time_Allowed":
                global shortest_time_sec
                time_delimited = re.split(':', str.strip(delimited[1]))
                shortest_time_sec = int(str.strip(time_delimited[0])) * 3600 + \
                                   int(str.strip(time_delimited[1])) * 60 + \
                                   int(str.strip(time_delimited[2]))
            elif str.strip(delimited[0]) == "Latest_Time_Allowed":
                global latest_time_sec
                time_delimited = re.split(':', str.strip(delimited[1]))
                latest_time_sec = int(str.strip(time_delimited[0])) * 3600 + \
                                   int(str.strip(time_delimited[1])) * 60 + \
                                   int(str.strip(time_delimited[2]))
            elif str.strip(delimited[0]) == "Earliest_Time_Allowed":
                global earliest_time_sec
                time_delimited = re.split(':', str.strip(delimited[1]))
                earliest_time_sec = int(str.strip(time_delimited[0])) * 3600 + \
                                   int(str.strip(time_delimited[1])) * 60 + \
                                   int(str.strip(time_delimited[2]))
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
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(1100, 70, 311, 231))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setObjectName("messageLabel")
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
    #  removes person from signed in list, stops tracking time
    signedIn.remove(ID)

    #  adds new time to record and updates it
    timeLogged = int(time.time() - loginTime[ID])
    name = peopleDict[ID][0]
    #  if first time signing in, add key to dictionary
    if ID not in record.keys():
        record[ID] = 0

    #  decide if time should be cleared based on configurations
    if timeLogged > longest_time_sec\
            or timeLogged < shortest_time_sec\
            or not inBetween(getCurrentTimeSeconds(), earliest_time_sec, latest_time_sec):
        clear = True

    if not clear:
        #  add timestamp to log file
        log_file = open("data/log.pear", 'a')
        log_toWrite = str(ID) + "|" + timestamp[ID] + "|" + getTimeStamp() + "\n"
        log_file.write(log_toWrite)
        log_file.close()

        #  add logged time and update the record file to show it
        record[ID] += timeLogged

        #  update file to show new hours
        updateRecordFile()

        #  add status message
        hoursJustLogged = round(timeLogged/3600.,2);
        hoursLoggedTotal = round(record[ID]/3600,2);
        print(hoursJustLogged)
        ui.messageLabel.setText("Logged out ID #" + ID + ". You logged " + str(hoursJustLogged) +
                                " hours, adding on to your total of " + str(hoursLoggedTotal) + " hours!")


    #  Everything below is for graphics/UI

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

    sortLogFile()

    #  read in log
    log_file = open('data/log.pear', 'r')
    logs = log_file.readlines()
    log_file.close()

    toPrint = list()
    for i in range(len(logs)+100):
        columns = list()
        for j in range(60):
            columns.append('')
        toPrint.append(columns)
    toPrint[0][0] = 'ID'
    toPrint[0][1] = 'Name'
    toPrint[0][2] = 'Student?'
    toPrint[0][3] = 'Date In'
    toPrint[0][4] = 'Time In'
    toPrint[0][5] = 'Date Out'
    toPrint[0][6] = 'Time Out'
    toPrint[0][7] = 'Calculated'
    toPrint[0][8] = ''
    toPrint[0][9] = ''
    toPrint[0][10] = ''
    toPrint[0][11] = 'ID'
    toPrint[0][12] = 'Student?'
    toPrint[0][13] = 'Name'
    toPrint[0][14] = 'Meetings Attended'
    toPrint[0][15] = 'Total Time'

    row = 1
    meetingsAttended = dict()

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
        calculated = str("%02d" % delta_h) + ":" + str("%02d" % delta_m) + ":" + str("%02d" % delta_s)

        #  add to meetings attended
        if ID in meetingsAttended.keys():
            meetingsAttended[ID] += 1
        else:
            meetingsAttended[ID] = 1

        #  add to print array
        toPrint[row][0] = '"' + ID + '"'
        toPrint[row][1] = '"' + name + '"'
        toPrint[row][2] = '"' + str(isStudent) + '"'
        toPrint[row][3] = '"' + dateIn + '"'
        toPrint[row][4] = '"' + timeIn + '"'
        toPrint[row][5] = '"' + dateOut + '"'
        toPrint[row][6] = '"' + timeOut + '"'
        toPrint[row][7] = '"' + calculated + '"'

        row += 1

    sorted_record = sorted(record.items(), key=lambda kv: kv[1])  # sort by item, gives list of tuples
    sorted_record.reverse()  # we want highest on top
    row = 1

    for recordTuple in sorted_record:

        ID = recordTuple[0]

        if ID not in peopleDict.keys() or ID not in meetingsAttended.keys():
            continue

        isStudent = peopleDict[ID][2] == 's'
        name = peopleDict[ID][0]
        meetings = meetingsAttended[ID]
        seconds_total = recordTuple[1]
        hours = seconds_total / 3600
        minutes = seconds_total % 3600 / 60
        seconds = seconds_total % 60
        combined = str("%02d" % hours) + ":" + str("%02d" % minutes) + ":" + str("%02d" % seconds)

        toPrint[row][11] = '"' + ID + '"'
        toPrint[row][12] = '"' + str(isStudent) + '"'
        toPrint[row][13] = '"' + name + '"'
        toPrint[row][14] = '"' + str(meetings) + '"'
        toPrint[row][15] = '"' + combined + '"'

        row += 1

    #  Array -> .csv file
    report_file = open('data/generated_report.csv', 'w')
    report_file.truncate(0)

    for r in range(len(toPrint)):
        for c in range(len(toPrint[r])):
            report_file.write(toPrint[r][c] + ',')
        report_file.write('\n')

    report_file.close()

    tellUser("Generate Report", "Successfully generated report (" + str(report_file.name) + ")")


def sortLogFile():
    #  read in log
    log_file = open('data/log.pear', 'r')
    logs = log_file.readlines()
    log_file.close()

    #  add everything to dictionary
    logDict = dict()
    for line in logs:
        line = str.strip(line)
        delimited = re.split('\|', line)
        ID = str.strip(delimited[0])
        timestamp_in = str.strip(delimited[1])
        timestamp_out = str.strip(delimited[2])

        if ID not in logDict.keys():
            logDict[ID] = list()

        logDict[ID].append((timestamp_in, timestamp_out))

    keys = list(logDict.keys())
    keys.sort()

    log_file = open('data/log.pear', 'w')
    log_file.truncate(0)
    for ID in keys:
        tupleList = logDict[ID]
        for tuple in tupleList:
            log_file.write(ID + "|" + tuple[0] + "|" + tuple[1] + "\n")


def getCurrentTimeSeconds():
    time = datetime.datetime.now().time()
    return time.hour * 3600 + time.minute * 60 + time.second


def inBetween(now, start, end):
    if start <= end:
        return start <= now < end
    else:  # over midnight
        return start <= now or now < end


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


