from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import res

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(1200, 800)
        Settings.setStyleSheet("QMainWindow#Settings{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget{background-color: rgb(24, 24, 24);}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.TeacherPage = QtWidgets.QWidget()
        self.TeacherPage.setObjectName("TeacherPage")
        font = QtGui.QFont()
        self.TitleComboBox = QtWidgets.QComboBox(self.TeacherPage)
        self.TitleComboBox.setGeometry(QtCore.QRect(300, 250, 100, 35))
        font.setPointSize(15)
        font.setBold(False)
        self.TitleComboBox.setFont(font)
        titles = ["Mr","Mrs","Miss","Ms","Dr"]
        self.TitleComboBox.addItems(titles)
        self.TitleComboBox.setObjectName("TitleComboBox")
        self.CurrentPassLabel = QtWidgets.QLabel(self.TeacherPage)
        self.CurrentPassLabel.setGeometry(QtCore.QRect(630, 240, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.CurrentPassLabel.setFont(font)
        self.CurrentPassLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.CurrentPassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentPassLabel.setObjectName("CurrentPassLabel")
        self.FNameLabel = QtWidgets.QLabel(self.TeacherPage)
        self.FNameLabel.setGeometry(QtCore.QRect(90, 320, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.FNameLabel.setFont(font)
        self.FNameLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.FNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FNameLabel.setObjectName("FNameLabel")
        self.PasswordErrorLabel = QtWidgets.QLabel(self.TeacherPage)
        self.PasswordErrorLabel.setGeometry(QtCore.QRect(630, 170, 510, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.PasswordErrorLabel.setFont(font)
        self.PasswordErrorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PasswordErrorLabel.setStyleSheet("QLabel#PasswordErrorLabel{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.PasswordErrorLabel.setObjectName("PasswordErrorLabel")
        
        self.NewPassLabel = QtWidgets.QLabel(self.TeacherPage)
        self.NewPassLabel.setGeometry(QtCore.QRect(630, 320, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.NewPassLabel.setFont(font)
        self.NewPassLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.NewPassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NewPassLabel.setObjectName("NewPassLabel")
        self.UsernameLabel = QtWidgets.QLabel(self.TeacherPage)
        self.UsernameLabel.setGeometry(QtCore.QRect(90, 500, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.UsernameLabel.setFont(font)
        self.UsernameLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.UsernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.TitleLabel = QtWidgets.QLabel(self.TeacherPage)
        self.TitleLabel.setGeometry(QtCore.QRect(90, 240, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.FNameLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.FNameLineEdit.setGeometry(QtCore.QRect(300, 320, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FNameLineEdit.setFont(font)
        self.FNameLineEdit.setObjectName("FNameLineEdit")
        self.SurnameLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.SurnameLineEdit.setGeometry(QtCore.QRect(300, 410, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SurnameLineEdit.setFont(font)
        self.SurnameLineEdit.setObjectName("SurnameLineEdit")
        self.UsernameLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.UsernameLineEdit.setGeometry(QtCore.QRect(300, 500, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.UsernameLineEdit.setFont(font)
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.CurrentPassLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.CurrentPassLineEdit.setGeometry(QtCore.QRect(890, 240, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CurrentPassLineEdit.setFont(font)
        self.CurrentPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CurrentPassLineEdit.setObjectName("CurrentPassLineEdit")
        self.NewPassLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.NewPassLineEdit.setGeometry(QtCore.QRect(890, 320, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.NewPassLineEdit.setFont(font)
        self.NewPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassLineEdit.setObjectName("NewPassLineEdit")
        self.ConfirmPassLineEdit = QtWidgets.QLineEdit(self.TeacherPage)
        self.ConfirmPassLineEdit.setGeometry(QtCore.QRect(890, 400, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ConfirmPassLineEdit.setFont(font)
        self.ConfirmPassLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassLineEdit.setObjectName("ConfirmPassLineEdit")
        self.ConfirmPassLabel = QtWidgets.QLabel(self.TeacherPage)
        self.ConfirmPassLabel.setGeometry(QtCore.QRect(630, 400, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.ConfirmPassLabel.setFont(font)
        self.ConfirmPassLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.ConfirmPassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfirmPassLabel.setObjectName("ConfirmPassLabel")
        self.ErrorLabel = QtWidgets.QLabel(self.TeacherPage)
        self.ErrorLabel.setGeometry(QtCore.QRect(70, 170, 500, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorLabel.setStyleSheet("QLabel#ErrorLabel{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.ErrorLabel.setObjectName("ErrorLabel")
        
        self.SurnameLabel = QtWidgets.QLabel(self.TeacherPage)
        self.SurnameLabel.setGeometry(QtCore.QRect(90, 410, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.SurnameLabel.setFont(font)
        self.SurnameLabel.setStyleSheet("color: rgb(170, 170, 170)")
        self.SurnameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SurnameLabel.setObjectName("SurnameLabel")
        self.EditProfileLabel = QtWidgets.QLabel(self.TeacherPage)
        self.EditProfileLabel.setGeometry(QtCore.QRect(355, 60, 450, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.EditProfileLabel.setFont(font)
        self.EditProfileLabel.setStyleSheet("color: rgb(255, 255, 255)")
        self.EditProfileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EditProfileLabel.setObjectName("EditProfileLabel")
        self.SaveButton = QtWidgets.QPushButton(self.TeacherPage, clicked=lambda: self.save_teacher())
        self.SaveButton.setGeometry(QtCore.QRect(430, 640, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SaveButton.setFont(font)
        self.SaveButton.setStyleSheet("QPushButton#SaveButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SaveButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SaveButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SaveButton.setObjectName("SaveButton")
        self.stackedWidget.addWidget(self.TeacherPage)
#------------------------------------------------------------------------------------Student Page
        self.StudentPage = QtWidgets.QWidget()
        self.StudentPage.setObjectName("page")
        
        self.EditProfileLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.EditProfileLabel_2.setGeometry(QtCore.QRect(355, 60, 450, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.EditProfileLabel_2.setFont(font)
        self.EditProfileLabel_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.EditProfileLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.EditProfileLabel_2.setObjectName("EditProfileLabel_2")
        self.NewPassLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.NewPassLabel_2.setGeometry(QtCore.QRect(630, 360, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.NewPassLabel_2.setFont(font)
        self.NewPassLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.NewPassLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.NewPassLabel_2.setObjectName("NewPassLabel_2")
        self.SurnameLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.SurnameLabel_2.setGeometry(QtCore.QRect(90, 360, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.SurnameLabel_2.setFont(font)
        self.SurnameLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.SurnameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SurnameLabel_2.setObjectName("SurnameLabel_2")
        self.PasswordErrorLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.PasswordErrorLabel_2.setGeometry(QtCore.QRect(630, 200, 510, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.PasswordErrorLabel_2.setFont(font)
        self.PasswordErrorLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PasswordErrorLabel_2.setStyleSheet("QLabel#PasswordErrorLabel_2{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.PasswordErrorLabel_2.setObjectName("PasswordErrorLabel_2")
        self.FNameLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.FNameLabel_2.setGeometry(QtCore.QRect(90, 270, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.FNameLabel_2.setFont(font)
        self.FNameLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.FNameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.FNameLabel_2.setObjectName("FNameLabel_2")
        self.UsernameLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.UsernameLabel_2.setGeometry(QtCore.QRect(90, 450, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.UsernameLabel_2.setFont(font)
        self.UsernameLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.UsernameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.UsernameLabel_2.setObjectName("UsernameLabel_2")
        self.CurrentPassLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.CurrentPassLabel_2.setGeometry(QtCore.QRect(630, 270, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.CurrentPassLabel_2.setFont(font)
        self.CurrentPassLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.CurrentPassLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentPassLabel_2.setObjectName("CurrentPassLabel_2")
        
        self.ErrorLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.ErrorLabel_2.setGeometry(QtCore.QRect(70, 200, 500, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.ErrorLabel_2.setFont(font)
        self.ErrorLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorLabel_2.setStyleSheet("QLabel#ErrorLabel_2{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.ErrorLabel_2.setObjectName("ErrorLabel_2")
        self.ConfirmPassLabel_2 = QtWidgets.QLabel(self.StudentPage)
        self.ConfirmPassLabel_2.setGeometry(QtCore.QRect(630, 450, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.ConfirmPassLabel_2.setFont(font)
        self.ConfirmPassLabel_2.setStyleSheet("color: rgb(170, 170, 170)")
        self.ConfirmPassLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfirmPassLabel_2.setObjectName("ConfirmPassLabel_2")
        self.FNameLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.FNameLineEdit_2.setGeometry(QtCore.QRect(300, 270, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FNameLineEdit_2.setFont(font)
        self.FNameLineEdit_2.setObjectName("FNameLineEdit_2")
        self.SurnameLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.SurnameLineEdit_2.setGeometry(QtCore.QRect(300, 360, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SurnameLineEdit_2.setFont(font)
        self.SurnameLineEdit_2.setObjectName("SurnameLineEdit_2")
        self.UsernameLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.UsernameLineEdit_2.setGeometry(QtCore.QRect(300, 450, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.UsernameLineEdit_2.setFont(font)
        self.UsernameLineEdit_2.setObjectName("UsernameLineEdit_2")
        self.CurrentPassLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.CurrentPassLineEdit_2.setGeometry(QtCore.QRect(890, 270, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CurrentPassLineEdit_2.setFont(font)
        self.CurrentPassLineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CurrentPassLineEdit_2.setObjectName("CurrentPassLineEdit_2")
        self.NewPassLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.NewPassLineEdit_2.setGeometry(QtCore.QRect(890, 360, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.NewPassLineEdit_2.setFont(font)
        self.NewPassLineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassLineEdit_2.setObjectName("NewPassLineEdit_2")
        self.ConfirmPassLineEdit_2 = QtWidgets.QLineEdit(self.StudentPage)
        self.ConfirmPassLineEdit_2.setGeometry(QtCore.QRect(890, 450, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ConfirmPassLineEdit_2.setFont(font)
        self.ConfirmPassLineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassLineEdit_2.setObjectName("ConfirmPassLineEdit_2")
        self.SaveButton_2 = QtWidgets.QPushButton(self.StudentPage, clicked=lambda: self.save_student())
        self.SaveButton_2.setGeometry(QtCore.QRect(430, 620, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SaveButton_2.setFont(font)
        self.SaveButton_2.setStyleSheet("QPushButton#SaveButton_2{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SaveButton_2:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SaveButton_2:pressed{background-color: rgb(170, 170, 170);}")
        self.SaveButton_2.setObjectName("SaveButton_2")
        self.stackedWidget.addWidget(self.StudentPage)
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        self.teacher_names()
        self.student_names()

    def teacher_names(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT title,firstName,surname,username FROM tblTeacherUsers WHERE Logged_in = '1'")
        items = cursor.fetchall()
        for teacher in items:
            self.TitleComboBox.setCurrentText(teacher[0])
            self.FNameLineEdit.setText(teacher[1])
            self.SurnameLineEdit.setText(teacher[2])
            self.UsernameLineEdit.setText(teacher[3])

    def save_teacher(self):
        self.save_teacher_names()
        current_password = self.CurrentPassLineEdit.text()
        new_password = self.NewPassLineEdit.text()
        confirm_password = self.ConfirmPassLineEdit.text()
        if current_password != "" or new_password != "" or confirm_password != "":
            self.save_teacher_password()

    def save_teacher_names(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        title = self.TitleComboBox.currentText()
        first_name = self.FNameLineEdit.text()
        surname = self.SurnameLineEdit.text()
        new_username = self.UsernameLineEdit.text()
        if first_name != "" and surname != "" and new_username != "":
            cursor.execute(f"SELECT username FROM tblTeacherUsers WHERE Logged_in = '0'")
            items = cursor.fetchall()
            username_list = []
            for username in items:
                username_list.append(username[0])
            if new_username not in username_list:
                cursor.execute(f"UPDATE tblTeacherUsers SET title='{title}',firstName='{first_name}',surname='{surname}',username='{new_username}' WHERE Logged_in='1'")
            else:
                self.ErrorLabel.setText("Username already exists, Please try again.")
                self.ErrorLabel.setFixedHeight(50)
        else:
            self.ErrorLabel.setText("Fields are incomplete. Please fill in all the boxes.")
            self.ErrorLabel.setFixedHeight(50)
        connection.commit()
        connection.close()

    def save_teacher_password(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        current_password = self.CurrentPassLineEdit.text()
        new_password = self.NewPassLineEdit.text()
        confirm_password = self.ConfirmPassLineEdit.text()
        if current_password != "" and new_password != "" and confirm_password != "":
            cursor.execute(f"SELECT password FROM tblTeacherUsers WHERE Logged_in ='1'")
            items = cursor.fetchone()
            password = items[0]
            if current_password == password:
                if confirm_password == new_password:
                    if len(new_password) >= 8:
                        cursor.execute(f"UPDATE tblTeacherUsers set password ='{new_password}' WHERE Logged_in ='1'")
                    else:
                        self.PasswordErrorLabel.setText("Password must be at least 8 characters long.")
                        self.PasswordErrorLabel.setFixedHeight(50)
                else:
                    self.PasswordErrorLabel.setText("Passwords do not match, Please try again.")
                    self.PasswordErrorLabel.setFixedHeight(50)
            else:
                self.PasswordErrorLabel.setText("Current password is incorrect, Please try again.")
                self.PasswordErrorLabel.setFixedHeight(50)
        else:
            self.PasswordErrorLabel.setText("Fields are incomplete. Please fill in all the boxes.")
            self.PasswordErrorLabel.setFixedHeight(50)

    def student_names(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT firstName,surname,username FROM tblStudentUsers WHERE Logged_in = '1'")
        items = cursor.fetchall()
        for student in items:
            self.FNameLineEdit_2.setText(student[0])
            self.SurnameLineEdit_2.setText(student[1])
            self.UsernameLineEdit_2.setText(student[2])

    def save_student(self):
        self.save_student_names()
        current_password = self.CurrentPassLineEdit_2.text()
        new_password = self.NewPassLineEdit_2.text()
        confirm_password = self.ConfirmPassLineEdit_2.text()
        if current_password != "" or new_password != "" or confirm_password != "":
            self.save_student_password()

    def save_student_names(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        first_name = self.FNameLineEdit_2.text()
        surname = self.SurnameLineEdit_2.text()
        new_username = self.UsernameLineEdit_2.text()
        if first_name != "" and surname != "" and new_username != "":
            cursor.execute(f"SELECT username FROM tblStudentUsers WHERE Logged_in = '0'")
            items = cursor.fetchall()
            username_list = []
            for username in items:
                username_list.append(username[0])
            if new_username not in username_list:
                cursor.execute(f"UPDATE tblTeacherUsers SET firstName='{first_name}',surname='{surname}',username='{new_username}' WHERE Logged_in='1'")
            else:
                self.ErrorLabel_2.setText("Username already exists, Please try again.")
                self.ErrorLabel_2.setFixedHeight(50)
        else:
            self.ErrorLabel_2.setText("Fields are incomplete. Please fill in all the boxes.")
            self.ErrorLabel_2.setFixedHeight(50)
        connection.commit()
        connection.close()

    def save_student_password(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        current_password = self.CurrentPassLineEdit_2.text()
        new_password = self.NewPassLineEdit_2.text()
        confirm_password = self.ConfirmPassLineEdit_2.text()
        if current_password != "" and new_password != "" and confirm_password != "":
            cursor.execute(f"SELECT password FROM tblStudentUsers WHERE Logged_in ='1'")
            items = cursor.fetchone()
            password = items[0]
            if current_password == password:
                if confirm_password == new_password:
                    if len(new_password) >= 8:
                        cursor.execute(f"UPDATE tblStudentUsers set password ='{new_password}' WHERE Logged_in ='1'")
                    else:
                        self.PasswordErrorLabel_2.setText("Password must be at least 8 characters long.")
                        self.PasswordErrorLabel_2.setFixedHeight(50)
                else:
                    self.PasswordErrorLabel_2.setText("Passwords do not match, Please try again.")
                    self.PasswordErrorLabel_2.setFixedHeight(50)
            else:
                self.PasswordErrorLabel_2.setText("Current password is incorrect, Please try again.")
                self.PasswordErrorLabel_2.setFixedHeight(50)
        else:
            self.PasswordErrorLabel_2.setText("Fields are incomplete. Please fill in all the boxes.")
            self.PasswordErrorLabel_2.setFixedHeight(50)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.CurrentPassLabel.setText(_translate("Settings", "Current Password"))
        self.FNameLabel.setText(_translate("Settings", "First Name"))
        self.NewPassLabel.setText(_translate("Settings", "New Password"))
        self.UsernameLabel.setText(_translate("Settings", "Username"))
        self.TitleLabel.setText(_translate("Settings", "Title"))
        self.ConfirmPassLabel.setText(_translate("Settings", "Confirm Password"))
        self.SurnameLabel.setText(_translate("Settings", "Surname"))
        self.EditProfileLabel.setText(_translate("Settings", "Edit Profile"))
        self.SaveButton.setText(_translate("Settings", "Save Changes"))
        self.EditProfileLabel_2.setText(_translate("Settings", "Edit Profile"))
        self.NewPassLabel_2.setText(_translate("Settings", "New Password"))
        self.SurnameLabel_2.setText(_translate("Settings", "Surname"))
        self.FNameLabel_2.setText(_translate("Settings", "First Name"))
        self.UsernameLabel_2.setText(_translate("Settings", "Username"))
        self.CurrentPassLabel_2.setText(_translate("Settings", "Current Password"))
        self.ConfirmPassLabel_2.setText(_translate("Settings", "Confirm Password"))
        self.SaveButton_2.setText(_translate("Settings", "Save Changes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
