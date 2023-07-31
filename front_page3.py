# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys,theme_rc
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 858)
        #MainWindow.setStyleSheet("QMainWindow:{\n"
#"background-image:url(\"./theme.jpg\")\n"
#"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 40, 831, 741))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(230, 30, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:\"pink\";\n"
"border-radius:20px;\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.show_tab_2)
        self.pushButton.setGeometry(QtCore.QRect(780, 20, 31, 41))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/download.jpg);\n"
"border-radius:10px;\n"
"color:\"red\";")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(110, 120, 631, 191))
        self.label_7.setStyleSheet("background-color:rgb(126, 184, 255);\n"
"font: 12pt \"Segoe Script\";border-radius:50px;\n"
"")
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(250, 340, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:\"pink\";\n"
"border-radius:20px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(100, 440, 631, 191))
        self.label_8.setStyleSheet("background-color:rgb(126, 184, 255);\n"
"font: 12pt \"Segoe Script\";\n"
"border-radius:50px;\n"
"")
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page)
      
        #####-----------------###############
        self.page1 = QtWidgets.QWidget()
        self.page1.setStyleSheet("background-color:rgba(255,194,8,0.5);")
        self.label_9 = QtWidgets.QLabel(self.page1)
        self.label_9.setGeometry(QtCore.QRect(110, 120, 631, 191))
        self.label_9.setStyleSheet("background-color:rgb(126, 184, 255);\n"
"font: 12pt \"Segoe Script\";border-radius:50px;\n"
"")
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page1)
        self.label_10.setGeometry(QtCore.QRect(250, 340, 300, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_9.setStyleSheet("background-color:\"pink\";\n"
        "border-radius:20px;\n"
        "") 
        self.label_10.setStyleSheet("background-color:rgb(126, 184, 255);\n"
"font: 12pt \"Segoe Script\";border-radius:50px;\n"
"")
        self.pushButton = QtWidgets.QPushButton(self.page1)
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.show_tab_3)
        self.pushButton.setGeometry(QtCore.QRect(780, 20, 31, 41))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/download.jpg);\n"
"border-radius:10px;\n"
"color:\"red\";")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page1)        
        ######################################33
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.stackedWidget.setCurrentIndex(0)
        #self.stackedWidget_2.setCurrentIndex(0)
        #self.stackedWidget_3.setCurrentIndex(2)
        #self.stackedWidget_4.setCurrentIndex(1)
        #self.stackedWidget_5.setCurrentIndex(0)
        #self.stackedWidget_6.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def recurring_timer(self):
        self.animate_labels[0].show()
        self.animate_labels.pop(0)
        
        if(len(self.animate_labels) == 0):
            self.timer.stop()   
    
    def show_tab_2(self):
        #self.stackedWidget_6.setIndex(1)    
        print("Switch to page 2")
        self.stackedWidget.setCurrentIndex(1)
        
    def show_tab_3(self):
        #self.stackedWidget_6.setIndex(1)    
        print("Switch to page 3")
        self.stackedWidget.setCurrentIndex(1)
        
    def retranslateUi(self, MainWindow):
        self.animate_labels = [self.label_7,self.label_8]
        for label in self.animate_labels:
            label.hide()
            
        _translate = QtCore.QCoreApplication.translate
        ########PAGE 1#################
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Do you stutter while speaking your name?</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Stammering affects 1 out of every 70,000 people globally. You are not alone.\n"
" Although there is no cure for stammering , most children outgrow it as they age."))
        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Can you outgrow your stammer?</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Most people outgrow stammering as they age. If you are not so lucky, some techniques in this app will help you. Remember silence is not always golden.\n"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">TEST:PAGE2</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">TEST:PAGE2</span></p></body></html>"))
#" Although there is no cure for stammering , most children outgrow it as they age."))
#import theme_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui =  Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())