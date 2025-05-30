# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 1871, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(1480, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.searchBox = QtWidgets.QLineEdit(self.frame)
        self.searchBox.setGeometry(QtCore.QRect(10, 10, 441, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.searchBox.setFont(font)
        self.searchBox.setStyleSheet("QLineEdit {\n"
"        border-radius: 5px;\n"
"        padding: 5px;\n"
"    }")
        self.searchBox.setText("")
        self.searchBox.setObjectName("searchBox")
        self.sortComboBox = QtWidgets.QComboBox(self.frame)
        self.sortComboBox.setGeometry(QtCore.QRect(1580, 10, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.sortComboBox.setFont(font)
        self.sortComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sortComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sortComboBox.setStyleSheet("QComboBox {\n"
"        padding: 6px;\n"
"        border: 1px solid #ccc;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        border: 1px solid #ccc;\n"
"        selection-background-color: #2196F3;\n"
"        selection-color: #ffffff;\n"
"        background-color: #ffffff;\n"
"        padding: 4px;\n"
"        outline: 0;\n"
"    }")
        self.sortComboBox.setObjectName("sortComboBox")
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setGeometry(QtCore.QRect(460, 10, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.searchButton.setFont(font)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setStyleSheet("QPushButton {\n"
"        background-color: #2196F3;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #1976D2;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1565C0;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: #90CAF9;\n"
"        color: #f5f5f5;\n"
"    }")
        self.searchButton.setObjectName("searchButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(40, 990, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.deleteButton.setFont(font)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet("QPushButton {\n"
"        background-color: #F44336;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #D32F2F;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #B71C1C;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: #E57373;\n"
"        color: #f5f5f5;\n"
"    }")
        self.deleteButton.setObjectName("deleteButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(1500, 990, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.editButton.setFont(font)
        self.editButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editButton.setStyleSheet("QPushButton {\n"
"        background-color: #2196F3;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #1976D2;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1565C0;\n"
"    }\n"
"    QPushButton:disabled {\n"
"        background-color: #90CAF9;\n"
"        color: #f5f5f5;\n"
"    }")
        self.editButton.setObjectName("editButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 190, 1841, 791))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"        border: 1px solid #ccc;\n"
"        border-radius: 4px;\n"
"        gridline-color: #ddd;\n"
"        background-color: #ffffff;\n"
"    }\n"
"    \n"
"    QHeaderView::section {\n"
"        background-color: #1976D2;\n"
"        color: white;\n"
"        padding: 8px;\n"
"        border: 1px solid #ccc;\n"
"        font-weight: bold;\n"
"        font-size: 20px;\n"
"    }\n"
"    \n"
"    QTableWidget::item {\n"
"        padding: 6px;\n"
"    }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.displayComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.displayComboBox.setGeometry(QtCore.QRect(1610, 140, 270, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.displayComboBox.setFont(font)
        self.displayComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.displayComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayComboBox.setStyleSheet("QComboBox {\n"
"        padding: 6px;\n"
"        border: 1px solid #ccc;\n"
"        border-radius: 4px;\n"
"        color: black\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        border: 1px solid #ccc;\n"
"        selection-background-color: #2196F3;\n"
"        selection-color: #ffffff;\n"
"        background-color: #ffffff;\n"
"        padding: 4px;\n"
"        outline: 0;\n"
"    }")
        self.displayComboBox.setObjectName("displayComboBox")
        self.displayComboBox.addItem("")
        self.displayComboBox.addItem("")
        self.displayComboBox.addItem("")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1510, 140, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(720, 10, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 140, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(199, 140, 281, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.searchComboBox.setFont(font)
        self.searchComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchComboBox.setStyleSheet("QComboBox {\n"
"        padding: 6px;\n"
"        border: 1px solid #ccc;\n"
"        border-radius: 4px;\n"
"    }\n"
"    QComboBox QAbstractItemView {\n"
"        border: 1px solid #ccc;\n"
"        selection-background-color: #2196F3;\n"
"        selection-color: #ffffff;\n"
"        background-color: #ffffff;\n"
"        padding: 4px;\n"
"        outline: 0;\n"
"    }")
        self.searchComboBox.setObjectName("searchComboBox")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(40, 20, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.refreshButton.setFont(font)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshButton.setStyleSheet("QPushButton {\n"
"        background-color: #ffffff;\n"
"        color: black;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: #f9f9f9;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightgray;\n"
"    }")
        self.refreshButton.setObjectName("refreshButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(1700, 990, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("QPushButton {\n"
"        background-color: #4CAF50;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: #43A047;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #388E3C;\n"
"    }")
        self.addButton.setObjectName("addButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1921, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Information System"))
        self.label_2.setText(_translate("MainWindow", "SORT BY"))
        self.searchBox.setPlaceholderText(_translate("MainWindow", "Search an entry..."))
        self.searchButton.setText(_translate("MainWindow", "SEARCH"))
        self.deleteButton.setText(_translate("MainWindow", "DELETE"))
        self.editButton.setText(_translate("MainWindow", "EDIT"))
        self.displayComboBox.setItemText(0, _translate("MainWindow", "STUDENT"))
        self.displayComboBox.setItemText(1, _translate("MainWindow", "PROGRAM"))
        self.displayComboBox.setItemText(2, _translate("MainWindow", "COLLEGE"))
        self.label_14.setText(_translate("MainWindow", "DISPLAY"))
        self.label_15.setText(_translate("MainWindow", "STUDENT INFORMATION SYSTEM"))
        self.label.setText(_translate("MainWindow", "SEARCH FILTER"))
        self.refreshButton.setText(_translate("MainWindow", "REFRESH"))
        self.addButton.setText(_translate("MainWindow", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
