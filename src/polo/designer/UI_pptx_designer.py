# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ethan/Documents/github/Marco_Polo/pyqt_designer/pptx_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PptxDialog(object):
    def setupUi(self, PptxDialog):
        PptxDialog.setObjectName("PptxDialog")
        PptxDialog.resize(743, 555)
        self.gridLayout_3 = QtWidgets.QGridLayout(PptxDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.runTreeWidget = RunTree(PptxDialog)
        self.runTreeWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.runTreeWidget.setObjectName("runTreeWidget")
        self.gridLayout_3.addWidget(self.runTreeWidget, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(PptxDialog)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 4, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 7, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 7, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 0, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 5, 0, 1, 3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 8, 0, 1, 3)
        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(PptxDialog)
        QtCore.QMetaObject.connectSlotsByName(PptxDialog)

    def retranslateUi(self, PptxDialog):
        _translate = QtCore.QCoreApplication.translate
        PptxDialog.setWindowTitle(_translate("PptxDialog", "Presentation Exporter"))
        self.groupBox.setTitle(_translate("PptxDialog", "Presentation Settings"))
        self.label_3.setText(_translate("PptxDialog", "Title"))
        self.groupBox_2.setTitle(_translate("PptxDialog", "Select Included Images"))
        self.groupBox_3.setTitle(_translate("PptxDialog", "Image Type"))
        self.checkBox.setText(_translate("PptxDialog", "Crystals"))
        self.checkBox_2.setText(_translate("PptxDialog", "Clear"))
        self.checkBox_3.setText(_translate("PptxDialog", "Precipitate"))
        self.checkBox_4.setText(_translate("PptxDialog", "Other"))
        self.checkBox_5.setText(_translate("PptxDialog", "Favorite"))
        self.groupBox_4.setTitle(_translate("PptxDialog", "Classifier"))
        self.radioButton.setText(_translate("PptxDialog", "Human"))
        self.radioButton_2.setText(_translate("PptxDialog", "Marco"))
        self.label_6.setText(_translate("PptxDialog", "Export Path"))
        self.label_5.setText(_translate("PptxDialog", "Subtitle"))
        self.pushButton.setText(_translate("PptxDialog", "Browse"))
        self.groupBox_5.setTitle(_translate("PptxDialog", "Slides"))
        self.checkBox_8.setText(_translate("PptxDialog", "Include All Spectrums"))
        self.checkBox_9.setText(_translate("PptxDialog", "Include all Dates"))
        self.pushButton_2.setText(_translate("PptxDialog", "Export Selected Run"))
from polo.widgets.run_tree import RunTree
