# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mini_project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.columnView = QtGui.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 40, 131, 241))
        self.columnView.setAutoScroll(False)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.columnView_2 = QtGui.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(150, 40, 171, 241))
        self.columnView_2.setAutoScroll(False)
        self.columnView_2.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.columnView_2.setObjectName(_fromUtf8("columnView_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 40, 141, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 101, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 101, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(74, 210, 61, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 61, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 290, 461, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 32, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 10, 86, 121))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_2.addWidget(self.label_19)
        self.layoutWidget1 = QtGui.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 10, 131, 121))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.layoutWidget1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.layoutWidget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label_13 = QtGui.QLabel(self.layoutWidget1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.label_34 = QtGui.QLabel(self.widget)
        self.label_34.setGeometry(QtCore.QRect(19, 53, 81, 16))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.widget)
        self.label_35.setGeometry(QtCore.QRect(30, 67, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setMouseTracking(True)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.widget)
        self.label_36.setGeometry(QtCore.QRect(21, 100, 111, 16))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_40 = QtGui.QLabel(self.widget)
        self.label_40.setGeometry(QtCore.QRect(31, 110, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setMouseTracking(True)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(10, 455, 241, 171))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_20 = QtGui.QLabel(self.widget_2)
        self.label_20.setGeometry(QtCore.QRect(0, 16, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(10, 45, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(_fromUtf8(""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.layoutWidget_3 = QtGui.QWidget(self.widget_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(98, 81, 131, 91))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_25 = QtGui.QLabel(self.layoutWidget_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.verticalLayout_4.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.layoutWidget_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout_4.addWidget(self.label_26)
        self.label_28 = QtGui.QLabel(self.layoutWidget_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout_4.addWidget(self.label_28)
        self.label_29 = QtGui.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.verticalLayout_4.addWidget(self.label_29)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 468, 451, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(15, 521, 91, 91))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_22 = QtGui.QLabel(self.layoutWidget_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout_3.addWidget(self.label_22)
        self.label_23 = QtGui.QLabel(self.layoutWidget_2)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout_3.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(self.layoutWidget_2)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_3.addWidget(self.label_24)
        self.label_27 = QtGui.QLabel(self.layoutWidget_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout_3.addWidget(self.label_27)
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(255, 482, 211, 151))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_30 = QtGui.QLabel(self.widget_3)
        self.label_30.setGeometry(QtCore.QRect(0, 15, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Aharoni"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setMouseTracking(True)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.layoutWidget_4 = QtGui.QWidget(self.widget_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 55, 141, 91))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_31 = QtGui.QLabel(self.layoutWidget_4)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.verticalLayout_5.addWidget(self.label_31)
        self.label_32 = QtGui.QLabel(self.layoutWidget_4)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.verticalLayout_5.addWidget(self.label_32)
        self.label_33 = QtGui.QLabel(self.layoutWidget_4)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.verticalLayout_5.addWidget(self.label_33)
        self.layoutWidget_5 = QtGui.QWidget(self.widget_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(150, 55, 51, 91))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_37 = QtGui.QLabel(self.layoutWidget_5)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.verticalLayout_7.addWidget(self.label_37)
        self.label_38 = QtGui.QLabel(self.layoutWidget_5)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.verticalLayout_7.addWidget(self.label_38)
        self.label_39 = QtGui.QLabel(self.layoutWidget_5)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.verticalLayout_7.addWidget(self.label_39)
        self.label_41 = QtGui.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(120, 430, 341, 20))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.columnView_2, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "마스크하시개", None))
        self.label_2.setText(_translate("MainWindow", "서울 통합대기환경", None))
        self.label_3.setText(_translate("MainWindow", "좋음", None))
        self.label_4.setText(_translate("MainWindow", "주요 오염물질", None))
        self.label_5.setText(_translate("MainWindow", "오존", None))
        self.pushButton.setText(_translate("MainWindow", "비교하기", None))
        self.pushButton_2.setText(_translate("MainWindow", "상세보기", None))
        self.label_6.setText(_translate("MainWindow", "성동구", None))
        self.label_7.setText(_translate("MainWindow", "2018. 5. 21.", None))
        self.label_14.setText(_translate("MainWindow", "초미세먼지", None))
        self.label_15.setText(_translate("MainWindow", "미세먼지", None))
        self.label_16.setText(_translate("MainWindow", "오존농도", None))
        self.label_17.setText(_translate("MainWindow", "아황산가스", None))
        self.label_18.setText(_translate("MainWindow", "일산화탄소", None))
        self.label_19.setText(_translate("MainWindow", "이산화질소", None))
        self.label_10.setText(_translate("MainWindow", "초미세먼지(㎍/㎥)", None))
        self.label_11.setText(_translate("MainWindow", "미세먼지(㎍/㎥)", None))
        self.label_12.setText(_translate("MainWindow", "오존농도(ppm)", None))
        self.label_8.setText(_translate("MainWindow", "아황산가스(ppm)", None))
        self.label_9.setText(_translate("MainWindow", "일산화탄소(ppm)", None))
        self.label_13.setText(_translate("MainWindow", "이산화질소(ppm)", None))
        self.label_34.setText(_translate("MainWindow", "통합대기환경", None))
        self.label_35.setText(_translate("MainWindow", "좋음", None))
        self.label_36.setText(_translate("MainWindow", "주요 오염물질", None))
        self.label_40.setText(_translate("MainWindow", "오존", None))
        self.label_20.setText(_translate("MainWindow", "차대시개", None))
        self.label_21.setText(_translate("MainWindow", "비상저감조치가 발령되었습니다. \n"
"가까운 공영주차장을 이용하세요.", None))
        self.label_25.setText(_translate("MainWindow", "주차장위치:", None))
        self.label_26.setText(_translate("MainWindow", "주차가능대수:", None))
        self.label_28.setText(_translate("MainWindow", "현재 주차대수:", None))
        self.label_29.setText(_translate("MainWindow", "전화번호:", None))
        self.label_22.setText(_translate("MainWindow", "주차장위치:", None))
        self.label_23.setText(_translate("MainWindow", "주차가능대수:", None))
        self.label_24.setText(_translate("MainWindow", "현재 주차대수:", None))
        self.label_27.setText(_translate("MainWindow", "전화번호:", None))
        self.label_30.setText(_translate("MainWindow", "가까운 공영주차장", None))
        self.label_31.setText(_translate("MainWindow", "1. 예원주차장", None))
        self.label_32.setText(_translate("MainWindow", "2. 명동주차장", None))
        self.label_33.setText(_translate("MainWindow", "3. 혜화주차장", None))
        self.label_37.setText(_translate("MainWindow", "2.6km", None))
        self.label_38.setText(_translate("MainWindow", "3.1km", None))
        self.label_39.setText(_translate("MainWindow", "4.5km", None))
        self.label_41.setText(_translate("MainWindow", "주요 오염물질", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

