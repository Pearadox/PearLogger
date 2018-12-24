
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import re


peopleDict = dict()  # k: ID number  v: tuple (name, picture_path, type (s=student/m=mentor)


# makes a prompt window with a Error icon, makes people cry and depressed. Also gives concussions from banging heads
def yellAtUser(title, message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)  # set the icon of the prompt
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
    msg.exec()


# makes a prompt window with a Information icon, used for giving user info
def tellUser(title,message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)  # set the icon of the prompt
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)  # set the buttons available on the prompt
    msg.exec()

class Ui_initiationDialog(object):
    def setupUi(self, initiationDialog):
        initiationDialog.setObjectName("initiationDialog")
        initiationDialog.resize(399, 374)
        font = QtGui.QFont()
        font.setPointSize(8)
        initiationDialog.setFont(font)
        self.line = QtWidgets.QFrame(initiationDialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.importBtn = QtWidgets.QPushButton(initiationDialog)
        self.importBtn.setGeometry(QtCore.QRect(110, 10, 181, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.importBtn.setFont(font)
        self.importBtn.setObjectName("importBtn")
        self.nameLineEdit = QtWidgets.QLineEdit(initiationDialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(180, 100, 191, 20))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.yearLineEdit = QtWidgets.QLineEdit(initiationDialog)
        self.yearLineEdit.setGeometry(QtCore.QRect(210, 130, 31, 20))
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.label = QtWidgets.QLabel(initiationDialog)
        self.label.setGeometry(QtCore.QRect(110, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.nameLabel = QtWidgets.QLabel(initiationDialog)
        self.nameLabel.setGeometry(QtCore.QRect(110, 100, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel_2 = QtWidgets.QLabel(initiationDialog)
        self.nameLabel_2.setGeometry(QtCore.QRect(20, 130, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.dawsonRadioButton = QtWidgets.QRadioButton(initiationDialog)
        self.dawsonRadioButton.setGeometry(QtCore.QRect(180, 160, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.dawsonRadioButton.setFont(font)
        self.dawsonRadioButton.setChecked(True)
        self.dawsonRadioButton.setObjectName("dawsonRadioButton")
        self.pearlandRadioButton = QtWidgets.QRadioButton(initiationDialog)
        self.pearlandRadioButton.setGeometry(QtCore.QRect(180, 180, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.pearlandRadioButton.setFont(font)
        self.pearlandRadioButton.setObjectName("pearlandRadioButton")
        self.nameLabel_3 = QtWidgets.QLabel(initiationDialog)
        self.nameLabel_3.setGeometry(QtCore.QRect(10, 230, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.nameLabel_3.setFont(font)
        self.nameLabel_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameLabel_3.setObjectName("nameLabel_3")
        self.pictureLineEdit = QtWidgets.QLineEdit(initiationDialog)
        self.pictureLineEdit.setGeometry(QtCore.QRect(80, 230, 251, 20))
        self.pictureLineEdit.setText("")
        self.pictureLineEdit.setObjectName("pictureLineEdit")
        self.browseButton = QtWidgets.QPushButton(initiationDialog)
        self.browseButton.setGeometry(QtCore.QRect(340, 230, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.browseButton.setFont(font)
        self.browseButton.setDefault(False)
        self.browseButton.setObjectName("browseButton")
        self.previewPic = QtWidgets.QLabel(initiationDialog)
        self.previewPic.setGeometry(QtCore.QRect(10, 260, 101, 101))
        self.previewPic.setText("")
        self.previewPic.setObjectName("previewPic")
        self.turnerRadioButton = QtWidgets.QRadioButton(initiationDialog)
        self.turnerRadioButton.setGeometry(QtCore.QRect(180, 200, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.turnerRadioButton.setFont(font)
        self.turnerRadioButton.setObjectName("turnerRadioButton")
        self.nameLabel_4 = QtWidgets.QLabel(initiationDialog)
        self.nameLabel_4.setGeometry(QtCore.QRect(100, 160, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.nameLabel_4.setFont(font)
        self.nameLabel_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameLabel_4.setObjectName("nameLabel_4")
        self.notStudentCheckBox = QtWidgets.QCheckBox(initiationDialog)
        self.notStudentCheckBox.setGeometry(QtCore.QRect(40, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.notStudentCheckBox.setFont(font)
        self.notStudentCheckBox.setObjectName("notStudentCheckBox")
        self.addPersonButton = QtWidgets.QPushButton(initiationDialog)
        self.addPersonButton.setGeometry(QtCore.QRect(130, 270, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.addPersonButton.setFont(font)
        self.addPersonButton.setObjectName("addPersonButton")
        self.statusLabel = QtWidgets.QLabel(initiationDialog)
        self.statusLabel.setGeometry(QtCore.QRect(130, 320, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(initiationDialog)
        QtCore.QMetaObject.connectSlotsByName(initiationDialog)

    def retranslateUi(self, initiationDialog):
        _translate = QtCore.QCoreApplication.translate
        initiationDialog.setWindowTitle(_translate("initiationDialog", "Add Person"))
        self.importBtn.setText(_translate("initiationDialog", "Mass Import (*.csv)"))
        self.label.setText(_translate("initiationDialog", "Manual Add"))
        self.nameLabel.setText(_translate("initiationDialog", "Name"))
        self.nameLabel_2.setText(_translate("initiationDialog", "Graduation Year   20"))
        self.dawsonRadioButton.setText(_translate("initiationDialog", "Dawson"))
        self.pearlandRadioButton.setText(_translate("initiationDialog", "Pearland"))
        self.nameLabel_3.setText(_translate("initiationDialog", "Picture"))
        self.browseButton.setText(_translate("initiationDialog", "Browse"))
        self.turnerRadioButton.setText(_translate("initiationDialog", "Turner"))
        self.nameLabel_4.setText(_translate("initiationDialog", "School"))
        self.notStudentCheckBox.setText(_translate("initiationDialog", "Not A Student"))
        self.addPersonButton.setText(_translate("initiationDialog", "Add Person"))

    def setup(self):
        readPeople()
        self.addPersonButton.clicked.connect(self.addPerson)
        self.browseButton.clicked.connect(self.browseAction)
        self.importBtn.clicked.connect(self.importCSV)
        self.notStudentCheckBox.toggled.connect(self.studentCheckboxAction)

    def addPerson(self):
        #  get form info
        name = self.nameLineEdit.text()
        year = self.yearLineEdit.text()
        school = 3  # default, 3 = not student
        type = 'm'
        pictureName = self.pictureLineEdit.text()

        if len(name) is 0 or len(year) is 0:
            yellAtUser("Blank Fields", "Error: Missing information!")
            return

        if len(pictureName) is 0:
            pictureName = "default.jpg"

        full_relative_path = Path('data/profilepics/' + pictureName)

        #  make sure picture exists in right location
        if not full_relative_path.exists():
            yellAtUser("Picture Not Found", "Please move the picture to data/profilepics/ and try again")
            return

        #  add picture preview
        pixmap_raw = QtGui.QPixmap(str(full_relative_path))
        pixmap_scaled = pixmap_raw.scaled(self.previewPic.size(), QtCore.Qt.KeepAspectRatio)
        self.previewPic.setPixmap(pixmap_scaled)  # associate picture to the label

        #  get school type
        if not self.notStudentCheckBox.isChecked():
            type = 's'
            if self.dawsonRadioButton.isChecked():
                school = 0
            if self.pearlandRadioButton.isChecked():
                school = 1
            if self.turnerRadioButton.isChecked():
                school = 2

        #  generate ID
        header = year + str(school)
        ID = str()
        #  find next unused tail
        for i in range(00, 99):
            tail = str(i)
            #  pad zero
            if i < 10:
                tail = '0' + tail
            if (header+tail) in peopleDict.keys():
                continue
            else:
                ID = header+tail
                break

        #  add person to the dictionary
        peopleDict[ID] = (name, str(full_relative_path), type)

        #  rewrite the people file so it includes the new person
        rewritePeopleFile()

        #  tell person everything worked
        self.statusLabel.setText("Successfully added " + name + " (#" + ID + ")")

        self.nameLineEdit.clear()

    #  open file browser to get picture
    def browseAction(self):
        path = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                     "Picture Files (*.jpg; *.png)")[0]

        #  return if user hits cancel
        if len(path) == 0:
            return

        try:
            index = path.index('data/profilepics/') + len('data/profilepics/')
            filename = path[index:]

            #  add picture preview
            print("data/profilepics/" + str(filename))
            pixmap_raw = QtGui.QPixmap('data/profilepics/' + filename)
            pixmap_scaled = pixmap_raw.scaled(self.previewPic.size(), QtCore.Qt.KeepAspectRatio)
            self.previewPic.setPixmap(pixmap_scaled)  # associate picture to the label

            #  set text of line edit to the file name
            self.pictureLineEdit.setText(filename)
        except:
            yellAtUser("Error with Picture", "Please move the picture to data/profilepics/ and try again")


    #  mass import people
    def importCSV(self):
        csv_path = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "CSV Files (*.csv)")
        csv = open(csv_path[0], mode='r')
        lines = csv.readlines()
        csv.close()

        for line in lines:
            delimited = re.split(',', line)
            name = str.strip(delimited[0])
            year = str.strip(delimited[1])
            school = str.strip(delimited[2])
            picName = str.strip(delimited[3])
            type = 'm'

            if len(name) is 0 or len(year) is 0 or len(type) is 0:
                yellAtUser("Import CSV Error", "Missing data: " + line)
                continue

            if len(picName) is 0:
                picName = "default.jpg"

            #  get school
            if int(school) < 3:
                type = 's'

            #  generate ID
            header = year + str(school)
            ID = str()
            #  find next unused tail
            for i in range(00, 99):
                tail = str(i)
                #  pad zero
                if i < 10:
                    tail = '0' + tail
                if (header + tail) in peopleDict.keys():
                    continue
                else:
                    ID = header + tail
                    break

            #  add person to the dictionary
            peopleDict[ID] = (name, picName, type)

            #  rewrite the people file so it includes the new person
            rewritePeopleFile()

        tellUser("Import People as CSV", "Successfully added " + str(len(lines)) + " people. Reload data to use new people")


    def studentCheckboxAction(self):
        if self.notStudentCheckBox.isChecked():
            self.dawsonRadioButton.setVisible(False)
            self.pearlandRadioButton.setVisible(False)
            self.turnerRadioButton.setVisible(False)
        else:
            self.dawsonRadioButton.setVisible(True)
            self.pearlandRadioButton.setVisible(True)
            self.turnerRadioButton.setVisible(True)

def rewritePeopleFile():
    file = open("data/people.pear", 'w')
    file.truncate(0)

    keys = list(peopleDict.keys())
    keys.sort()

    for i in range(0,len(keys)):
        ID = keys[i]
        name = peopleDict[ID][0]
        path = peopleDict[ID][1]
        type = peopleDict[ID][2]

        toWrite = str(ID) + ";" + name + ";" + path + ";" + type + "\n"
        file.write(toWrite)

    file.close()
    peopleDict.clear()
    readPeople()


def readPeople():
    #  read in data
    people_file = Path("data/people.pear")

    if not people_file.exists():
        #  create new people file
        file = open("data/people.pear", 'w')
        #  write in example data
        file.write("0;example name;example_picture.jpg")
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
                picture_name = str.strip(delimited[2])
                full_picture_path = Path("data/profilepics/"+picture_name)
                type = str.strip(delimited[3])

                #  make sure picture works or is not empty. otherwise use default
                if (len(str(full_picture_path)) is 0) or (not full_picture_path.exists()):
                    picture_name = Path('default.jpg')
            except:
                print("ERROR: Parsing error in people file (data/people.pear, line " + str(lineCount) + ")")

            #  check if number already exists in dictionary
            if number in peopleDict.keys():
                print("ERROR: Duplicate numbers in people file (#" + number + ") (data/people.pear, line " + str(
                    lineCount) + ")")
                continue

            #  record the data in a dictionary
            peopleDict[number] = (name, str(picture_name), type)