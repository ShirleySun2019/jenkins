# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depth_sun_0615.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 761, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 61, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 90, 551, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 61, 16))
        self.label_6.setObjectName("label_6")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_4.setGeometry(QtCore.QRect(650, 90, 37, 21))
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 140, 101, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 40, 551, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_5.setGeometry(QtCore.QRect(650, 40, 37, 21))
        self.toolButton_5.setObjectName("toolButton_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 200, 761, 301))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 30, 201, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(380, 30, 101, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(490, 30, 201, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 721, 81))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 441, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(540, 30, 37, 21))
        self.toolButton.setObjectName("toolButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 260, 721, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(35, 20, 611, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 721, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 90, 441, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_2.setGeometry(QtCore.QRect(540, 90, 37, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "文件上传"))
        self.label_4.setText(_translate("MainWindow", "真值文件："))
        self.label_6.setText(_translate("MainWindow", "相机文件："))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "评估"))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.groupBox_6.setTitle(_translate("MainWindow", "评估结果"))
        self.label_7.setText(_translate("MainWindow", "误差均值（m）："))
        self.label_8.setText(_translate("MainWindow", "误差标准差（m）："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "静态测距评估"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "动态测距评估"))
        self.groupBox.setTitle(_translate("MainWindow", "真值文件"))
        self.label.setText(_translate("MainWindow", "上传文件："))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "评估结果"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "项  目"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "valid_ratio(%)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "evaluate_ratio(%)"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "mean_error(m)"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "evaluate_ratio_without_edge(%)"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "mean_error_without_edge(m)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "品  牌"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ZED"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LeadSense"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mynt"))
        self.groupBox_2.setTitle(_translate("MainWindow", "相机文件"))
        self.comboBox.setItemText(0, _translate("MainWindow", "------------请选择-------------"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ZED"))
        self.comboBox.setItemText(2, _translate("MainWindow", "LeadSense"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Mynt"))
        self.label_2.setText(_translate("MainWindow", "相机选择："))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "上传文件："))
        self.pushButton.setText(_translate("MainWindow", "评估"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "深度测距评估"))

