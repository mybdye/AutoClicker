# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AutoClicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 220)
        Dialog.setMinimumSize(QtCore.QSize(200, 220))
        Dialog.setMaximumSize(QtCore.QSize(200, 220))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(9, 0, 180, 120))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_counter = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_counter.setGeometry(QtCore.QRect(100, 30, 70, 20))
        self.lineEdit_counter.setAcceptDrops(False)
        self.lineEdit_counter.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_counter.setObjectName("lineEdit_counter")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_intervalTime = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_intervalTime.setGeometry(QtCore.QRect(100, 60, 70, 20))
        self.lineEdit_intervalTime.setAcceptDrops(False)
        self.lineEdit_intervalTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_intervalTime.setObjectName("lineEdit_intervalTime")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_waitFirstTime = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_waitFirstTime.setGeometry(QtCore.QRect(100, 90, 70, 20))
        self.lineEdit_waitFirstTime.setAcceptDrops(False)
        self.lineEdit_waitFirstTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_waitFirstTime.setObjectName("lineEdit_waitFirstTime")
        self.progressBar_left = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_left.setGeometry(QtCore.QRect(100, 46, 70, 10))
        self.progressBar_left.setProperty("value", 24)
        self.progressBar_left.setTextVisible(False)
        self.progressBar_left.setObjectName("progressBar_left")
        self.pushButton_pause = QtWidgets.QPushButton(Dialog)
        self.pushButton_pause.setGeometry(QtCore.QRect(140, 190, 50, 30))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(75, 190, 50, 30))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 190, 50, 30))
        self.pushButton_save.setObjectName("pushButton_save")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(9, 130, 181, 60))
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AutoClicker"))
        self.groupBox.setTitle(_translate("Dialog", "配置："))
        self.label.setText(_translate("Dialog", "点击次数"))
        self.label_2.setText(_translate("Dialog", "每次间隔(ms)"))
        self.label_3.setText(_translate("Dialog", "首次等待(s)"))
        self.pushButton_pause.setText(_translate("Dialog", "暂停"))
        self.pushButton_start.setText(_translate("Dialog", "开始"))
        self.pushButton_save.setText(_translate("Dialog", "保存"))