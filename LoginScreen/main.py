from cgi import test
from xml.dom.minidom import Document
import pyrebase
from rsa import sign 
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox,QMainWindow

#------------login-signin--------------#
firebaseConfig = {'apiKey': "AIzaSyCToO30ig7k8cdQffl0vc99v-7uma5nnQU",
  'authDomain': "chat-34e7c.firebaseapp.com",
  'databaseURL': "https://chat-34e7c.firebaseip.com",
  'projectId': "chat-34e7c",
  'storageBucket': "chat-34e7c.appspot.com",
  'messagingSenderId': "561847321161",
  'appId': "1:561847321161:web:cf510b20b99aee4f487598",
  'measurementId': "G-GCKW2YCTJK"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class login(QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_login.clicked.connect(self.verification)
        self.btn_signin.clicked.connect(self.gotosignin)
        self.label.setPixmap(QPixmap("background2.png"))

    def verification(self):
        email = self.line_mail.text()
        password = self.line_password.text()
        try:
            login = auth.sign_in_with_email_and_password(email,password)
            ask=QMessageBox.question(self,"?","Do you want to enter the main menu?",\
                        QMessageBox.Yes | QMessageBox.No)
            if ask==QMessageBox.Yes:
                self.gotomainwindow()
            else:
                self.show()
        except:
            QMessageBox.about(self, "Error", "Invalid email or password!")

    def gotosignin(self):
        self.close()
        self.cams = signin()
        self.cams.show()
    
    def gotomainwindow(self):
        self.close()
        self.cams = main_window()
        self.cams.show()


class signin(QMainWindow):
    def __init__(self):
        super(signin,self).__init__()
        loadUi("signin.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.btn_signin.clicked.connect(self.new_account)
        self.btn_backtologin.clicked.connect(self.backtologin)
        self.label.setPixmap(QPixmap("background2.png"))

    def new_account(self):
        email = self.line_mail.text()
        password = self.line_password.text()
        try:
            user = auth.create_user_with_email_and_password(email,password)
            ask=QMessageBox.question(self,"?",""""Succesfully created account!
Do you want to enter the login screen?""",\
                        QMessageBox.Yes | QMessageBox.No)
            if ask==QMessageBox.Yes:
                self.backtologin()
            else:
                self.show()    
        except:
            QMessageBox.about(self, "Error", "Mail or password already exists!")

    def backtologin(self):
        self.close()
        self.cams = login()
        self.cams.show()


class main_window(QMainWindow):
    def __init__(self):
        super(main_window,self).__init__()
        loadUi("main_window.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btn_quit.clicked.connect(self.quit)
        #self.btn_fscreen.clicked.connect(self.fscreen)
        self.btn_hide.clicked.connect(self.bhide)
        self.label.setPixmap(QPixmap("background.png"))

    def bhide(self):
        self.showMinimized()

    #def fscreen(self):
        #self.showFullScreen()   

    def quit(self):
        cevap=QMessageBox.question(self,"QUİT","Are you sure you want to exit ?",\
                        QMessageBox.Yes | QMessageBox.No,
                        )
        if cevap==QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            self.show()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login()
    window.show()
    sys.exit(app.exec_())