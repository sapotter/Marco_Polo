# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ethan/Documents/github/Marco_Polo/pyqt_designer/plate_inspector_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlateInspector(object):
    def setupUi(self, PlateInspector):
        PlateInspector.setObjectName("PlateInspector")
        PlateInspector.resize(949, 632)
        self.gridLayout = QtWidgets.QGridLayout(PlateInspector)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(PlateInspector)
        self.label_18.setMaximumSize(QtCore.QSize(200, 30))
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)
        self.plateViewer = plateViewer(PlateInspector)
        self.plateViewer.setObjectName("plateViewer")
        self.gridLayout.addWidget(self.plateViewer, 1, 0, 1, 2)
        self.groupBox_26 = QtWidgets.QGroupBox(PlateInspector)
        self.groupBox_26.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_26.setObjectName("groupBox_26")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_26)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_29 = QtWidgets.QGroupBox(self.groupBox_26)
        self.groupBox_29.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_29.setObjectName("groupBox_29")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_29)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_12.addWidget(self.pushButton_18, 0, 1, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_12.addWidget(self.pushButton_21, 1, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_12.addWidget(self.pushButton_22, 2, 0, 1, 2)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_12.addWidget(self.pushButton_20, 1, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_29)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_12.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_29, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_26)
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_21 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout.addWidget(self.checkBox_21)
        self.checkBox_22 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout.addWidget(self.checkBox_22)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_23 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_3.addWidget(self.checkBox_23, 0, 0, 1, 1)
        self.checkBox_24 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_3.addWidget(self.checkBox_24, 0, 1, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_25.setObjectName("checkBox_25")
        self.gridLayout_3.addWidget(self.checkBox_25, 1, 0, 1, 1)
        self.checkBox_26 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_26.setObjectName("checkBox_26")
        self.gridLayout_3.addWidget(self.checkBox_26, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_3.setToolTip("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_8)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_8)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_8)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_8)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_8)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_8)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.tab_8)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 3, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_8)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 4, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 4, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_8)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 4, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_8)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_9)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_13.addWidget(self.comboBox_7, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem1, 1, 2, 1, 1)
        self.checkBox_28 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_28.setObjectName("checkBox_28")
        self.gridLayout_13.addWidget(self.checkBox_28, 1, 0, 1, 1)
        self.checkBox_27 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_27.setObjectName("checkBox_27")
        self.gridLayout_13.addWidget(self.checkBox_27, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_9)
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 0, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_13.addWidget(self.pushButton_23, 2, 3, 2, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_13.addWidget(self.pushButton_19, 1, 3, 1, 1)
        self.checkBox_29 = QtWidgets.QCheckBox(self.tab_9)
        self.checkBox_29.setObjectName("checkBox_29")
        self.gridLayout_13.addWidget(self.checkBox_29, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_9, "")
        self.gridLayout_19.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_26, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)

        self.retranslateUi(PlateInspector)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(PlateInspector)

    def retranslateUi(self, PlateInspector):
        _translate = QtCore.QCoreApplication.translate
        PlateInspector.setWindowTitle(_translate("PlateInspector", "Form"))
        self.label_18.setText(_translate("PlateInspector", "Viewing Page 0 of 0"))
        self.plateViewer.setToolTip(_translate("PlateInspector", "Plate views are shown here. If you are viewing an HWI Run each view is a subsection of the larger plate."))
        self.groupBox_26.setTitle(_translate("PlateInspector", "Controls"))
        self.groupBox_29.setTitle(_translate("PlateInspector", "Page Navigation"))
        self.pushButton_18.setToolTip(_translate("PlateInspector", "Navigate to the next page of images"))
        self.pushButton_18.setText(_translate("PlateInspector", "Next"))
        self.pushButton_18.setShortcut(_translate("PlateInspector", "Right"))
        self.pushButton_21.setToolTip(_translate("PlateInspector", "Switch to the next imaging run for this sample"))
        self.pushButton_21.setText(_translate("PlateInspector", "Next Date"))
        self.pushButton_21.setShortcut(_translate("PlateInspector", "Up"))
        self.pushButton_22.setToolTip(_translate("PlateInspector", "Switch to alternative spectrum for this sample"))
        self.pushButton_22.setText(_translate("PlateInspector", "Swap Spectrum"))
        self.pushButton_22.setShortcut(_translate("PlateInspector", "Ctrl+Up"))
        self.pushButton_20.setToolTip(_translate("PlateInspector", "Switch to previous imaging run for this sample"))
        self.pushButton_20.setText(_translate("PlateInspector", "Previous Date"))
        self.pushButton_17.setToolTip(_translate("PlateInspector", "Navigate to previous page of images"))
        self.pushButton_17.setText(_translate("PlateInspector", "Previous"))
        self.pushButton_17.setShortcut(_translate("PlateInspector", "Left"))
        self.groupBox.setToolTip(_translate("PlateInspector", "Highlight images that meet your selected filters"))
        self.groupBox.setTitle(_translate("PlateInspector", "Classifier"))
        self.checkBox_21.setText(_translate("PlateInspector", "Human"))
        self.checkBox_22.setText(_translate("PlateInspector", "MARCO"))
        self.groupBox_2.setTitle(_translate("PlateInspector", "Image Type"))
        self.checkBox_23.setText(_translate("PlateInspector", "Crystal"))
        self.checkBox_24.setText(_translate("PlateInspector", "Clear"))
        self.checkBox_25.setText(_translate("PlateInspector", "Precipitate"))
        self.checkBox_26.setText(_translate("PlateInspector", "Other"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("PlateInspector", "Image Filtering"))
        self.label_22.setText(_translate("PlateInspector", "Color Intensity"))
        self.label_4.setText(_translate("PlateInspector", "TextLabel"))
        self.label_24.setText(_translate("PlateInspector", "Classifier"))
        self.label_19.setText(_translate("PlateInspector", "Crystal"))
        self.radioButton.setText(_translate("PlateInspector", "MARCO"))
        self.radioButton_2.setText(_translate("PlateInspector", "Human"))
        self.label_20.setText(_translate("PlateInspector", "TextLabel"))
        self.label_21.setText(_translate("PlateInspector", "Precipitate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("PlateInspector", "Image Coloring"))
        self.checkBox_28.setToolTip(_translate("PlateInspector", "Apply image colorings selected in the \"Image Coloring\" tab"))
        self.checkBox_28.setText(_translate("PlateInspector", "Apply Image Colors"))
        self.checkBox_27.setToolTip(_translate("PlateInspector", "Apply image filters selected in the \"Image Filtering\" tab."))
        self.checkBox_27.setText(_translate("PlateInspector", "Apply Image Filters"))
        self.label_23.setText(_translate("PlateInspector", "Images Per Plate"))
        self.pushButton_23.setToolTip(_translate("PlateInspector", "Reload the current view. Like a refresh button."))
        self.pushButton_23.setText(_translate("PlateInspector", "Reload Current View"))
        self.pushButton_19.setToolTip(_translate("PlateInspector", "Apply the currently selected coloring and filtering options if selected"))
        self.pushButton_19.setText(_translate("PlateInspector", "Apply Plate Settings"))
        self.pushButton_19.setShortcut(_translate("PlateInspector", "A"))
        self.checkBox_29.setToolTip(_translate("PlateInspector", "Keep the aspect ratio of the images in the grid. Favors accuracy to the image over image size."))
        self.checkBox_29.setText(_translate("PlateInspector", "Preserve Aspect Ratio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("PlateInspector", "Plate View"))
from polo.widgets.plate_viewer import plateViewer
