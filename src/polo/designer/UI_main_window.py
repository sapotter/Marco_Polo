# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ethan/Documents/github/Marco_Polo/pyqt_designer/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 644)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.runOrganizer = RunOrganizer(self.centralwidget)
        self.runOrganizer.setMinimumSize(QtCore.QSize(200, 0))
        self.runOrganizer.setMaximumSize(QtCore.QSize(450, 16777215))
        self.runOrganizer.setObjectName("runOrganizer")
        self.gridLayout.addWidget(self.runOrganizer, 0, 0, 1, 1)
        self.run_interface = QtWidgets.QTabWidget(self.centralwidget)
        self.run_interface.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.run_interface.setPalette(palette)
        self.run_interface.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.run_interface.setToolTip("")
        self.run_interface.setTabPosition(QtWidgets.QTabWidget.North)
        self.run_interface.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.run_interface.setObjectName("run_interface")
        self.tab = QtWidgets.QWidget()
        self.tab.setToolTipDuration(-1)
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.slideshowInspector = slideshowInspector(self.tab)
        self.slideshowInspector.setObjectName("slideshowInspector")
        self.gridLayout_5.addWidget(self.slideshowInspector, 0, 0, 1, 1)
        self.run_interface.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plateInspector = PlateInspectorWidget(self.tab_2)
        self.plateInspector.setObjectName("plateInspector")
        self.gridLayout_2.addWidget(self.plateInspector, 0, 0, 1, 1)
        self.run_interface.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableInspector = TableInspector(self.tab_5)
        self.tableInspector.setObjectName("tableInspector")
        self.gridLayout_3.addWidget(self.tableInspector, 0, 0, 2, 1)
        self.run_interface.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_14.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_12.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_13)
        self.listWidget_3.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_3)
        self.verticalLayout_11.addWidget(self.groupBox_13)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_13.setDefault(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_11.addWidget(self.pushButton_13)
        self.gridLayout_14.addWidget(self.groupBox_12, 0, 1, 1, 1)
        self.run_interface.addTab(self.tab_4, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.optimizeWidget = OptimizeWidget(self.tab_10)
        self.optimizeWidget.setObjectName("optimizeWidget")
        self.gridLayout_12.addWidget(self.optimizeWidget, 0, 0, 1, 1)
        self.run_interface.addTab(self.tab_10, "")
        self.gridLayout.addWidget(self.run_interface, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuImages = QtWidgets.QMenu(self.menuImport)
        self.menuImages.setStyleSheet("")
        self.menuImages.setObjectName("menuImages")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAdvanced_Tools = QtWidgets.QMenu(self.menubar)
        self.menuAdvanced_Tools.setObjectName("menuAdvanced_Tools")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuBeta_Testers = QtWidgets.QMenu(self.menubar)
        self.menuBeta_Testers.setObjectName("menuBeta_Testers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuickstart_Guide = QtWidgets.QAction(MainWindow)
        self.actionQuickstart_Guide.setObjectName("actionQuickstart_Guide")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionFAQ = QtWidgets.QAction(MainWindow)
        self.actionFAQ.setObjectName("actionFAQ")
        self.actionFrom_FTP = QtWidgets.QAction(MainWindow)
        self.actionFrom_FTP.setObjectName("actionFrom_FTP")
        self.actionCocktails = QtWidgets.QAction(MainWindow)
        self.actionCocktails.setObjectName("actionCocktails")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionFrom_Folder = QtWidgets.QAction(MainWindow)
        self.actionFrom_Folder.setObjectName("actionFrom_Folder")
        self.actionReferences = QtWidgets.QAction(MainWindow)
        self.actionReferences.setObjectName("actionReferences")
        self.actionCiting_Polo = QtWidgets.QAction(MainWindow)
        self.actionCiting_Polo.setObjectName("actionCiting_Polo")
        self.actionTime_Resolved = QtWidgets.QAction(MainWindow)
        self.actionTime_Resolved.setObjectName("actionTime_Resolved")
        self.actionAdd_Image_Type = QtWidgets.QAction(MainWindow)
        self.actionAdd_Image_Type.setObjectName("actionAdd_Image_Type")
        self.actionSelected_Runs = QtWidgets.QAction(MainWindow)
        self.actionSelected_Runs.setObjectName("actionSelected_Runs")
        self.actionAs_HTML = QtWidgets.QAction(MainWindow)
        self.actionAs_HTML.setObjectName("actionAs_HTML")
        self.actionAll_Data = QtWidgets.QAction(MainWindow)
        self.actionAll_Data.setObjectName("actionAll_Data")
        self.actionTable_View = QtWidgets.QAction(MainWindow)
        self.actionTable_View.setObjectName("actionTable_View")
        self.actionClassifications = QtWidgets.QAction(MainWindow)
        self.actionClassifications.setObjectName("actionClassifications")
        self.actionView_Log = QtWidgets.QAction(MainWindow)
        self.actionView_Log.setObjectName("actionView_Log")
        self.actionHTML = QtWidgets.QAction(MainWindow)
        self.actionHTML.setObjectName("actionHTML")
        self.actionFrom_Saved_Run = QtWidgets.QAction(MainWindow)
        self.actionFrom_Saved_Run.setObjectName("actionFrom_Saved_Run")
        self.actionSave_Run = QtWidgets.QAction(MainWindow)
        self.actionSave_Run.setObjectName("actionSave_Run")
        self.actionDelete_Run = QtWidgets.QAction(MainWindow)
        self.actionDelete_Run.setObjectName("actionDelete_Run")
        self.actionSave_Run_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Run_As.setObjectName("actionSave_Run_As")
        self.actionSaved_Run_xtal_File = QtWidgets.QAction(MainWindow)
        self.actionSaved_Run_xtal_File.setObjectName("actionSaved_Run_xtal_File")
        self.actionNew_Run = QtWidgets.QAction(MainWindow)
        self.actionNew_Run.setObjectName("actionNew_Run")
        self.actionNew_Run_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Run_2.setObjectName("actionNew_Run_2")
        self.actionFrom_Saved_Run_2 = QtWidgets.QAction(MainWindow)
        self.actionFrom_Saved_Run_2.setObjectName("actionFrom_Saved_Run_2")
        self.actionFrom_Saved_Run_3 = QtWidgets.QAction(MainWindow)
        self.actionFrom_Saved_Run_3.setObjectName("actionFrom_Saved_Run_3")
        self.actionFrom_Directory = QtWidgets.QAction(MainWindow)
        self.actionFrom_Directory.setObjectName("actionFrom_Directory")
        self.actionAS_PDF = QtWidgets.QAction(MainWindow)
        self.actionAS_PDF.setObjectName("actionAS_PDF")
        self.actionAs_CSV = QtWidgets.QAction(MainWindow)
        self.actionAs_CSV.setObjectName("actionAs_CSV")
        self.actionDelete_Run_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_Run_2.setObjectName("actionDelete_Run_2")
        self.actionView_Log_2 = QtWidgets.QAction(MainWindow)
        self.actionView_Log_2.setObjectName("actionView_Log_2")
        self.actionBatch_Import = QtWidgets.QAction(MainWindow)
        self.actionBatch_Import.setObjectName("actionBatch_Import")
        self.actionRun_Journal = QtWidgets.QAction(MainWindow)
        self.actionRun_Journal.setObjectName("actionRun_Journal")
        self.actionSecure_Save = QtWidgets.QAction(MainWindow)
        self.actionSecure_Save.setObjectName("actionSecure_Save")
        self.actionRemove_Run = QtWidgets.QAction(MainWindow)
        self.actionRemove_Run.setObjectName("actionRemove_Run")
        self.actionOptimization_Screens = QtWidgets.QAction(MainWindow)
        self.actionOptimization_Screens.setObjectName("actionOptimization_Screens")
        self.actionUser_Guide = QtWidgets.QAction(MainWindow)
        self.actionUser_Guide.setObjectName("actionUser_Guide")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionBeta_Tester_s_Guide = QtWidgets.QAction(MainWindow)
        self.actionBeta_Tester_s_Guide.setObjectName("actionBeta_Tester_s_Guide")
        self.actionEdit_Current_Run_Data = QtWidgets.QAction(MainWindow)
        self.actionEdit_Current_Run_Data.setObjectName("actionEdit_Current_Run_Data")
        self.actionAs_MSO = QtWidgets.QAction(MainWindow)
        self.actionAs_MSO.setObjectName("actionAs_MSO")
        self.actionAs_PPTX = QtWidgets.QAction(MainWindow)
        self.actionAs_PPTX.setObjectName("actionAs_PPTX")
        self.menuImages.addAction(self.actionFrom_FTP)
        self.menuImages.addSeparator()
        self.menuImages.addAction(self.actionFrom_Saved_Run_3)
        self.menuImages.addAction(self.actionFrom_Directory)
        self.menuImport.addAction(self.menuImages.menuAction())
        self.menuImport.addAction(self.actionCocktails)
        self.menuExport.addAction(self.actionAs_HTML)
        self.menuExport.addAction(self.actionAs_CSV)
        self.menuExport.addAction(self.actionAs_MSO)
        self.menuExport.addAction(self.actionAs_PPTX)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionUser_Guide)
        self.menuHelp.addAction(self.actionQuickstart_Guide)
        self.menuHelp.addAction(self.actionFAQ)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuAdvanced_Tools.addAction(self.actionTime_Resolved)
        self.menuAdvanced_Tools.addAction(self.actionAdd_Image_Type)
        self.menuAdvanced_Tools.addSeparator()
        self.menuAdvanced_Tools.addAction(self.actionView_Log_2)
        self.menuAdvanced_Tools.addSeparator()
        self.menuAdvanced_Tools.addAction(self.actionEdit_Current_Run_Data)
        self.menuFile.addAction(self.actionSave_Run)
        self.menuFile.addAction(self.actionSave_Run_As)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRemove_Run)
        self.menuBeta_Testers.addAction(self.actionBeta_Tester_s_Guide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuAdvanced_Tools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuBeta_Testers.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.run_interface.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Polo: The MARCO Companion"))
        self.tab.setToolTip(_translate("MainWindow", "View and classify images in the selected run as a slideshow."))
        self.run_interface.setTabText(self.run_interface.indexOf(self.tab), _translate("MainWindow", "Slideshow Viewer"))
        self.tab_2.setToolTip(_translate("MainWindow", "View images in a grid of multibles of 24 up to a complete plate. Works best with HWI screening runs."))
        self.run_interface.setTabText(self.run_interface.indexOf(self.tab_2), _translate("MainWindow", "Plate Viewer"))
        self.tab_5.setToolTip(_translate("MainWindow", "View current run data in table format."))
        self.run_interface.setTabText(self.run_interface.indexOf(self.tab_5), _translate("MainWindow", "Table View"))
        self.tab_4.setToolTip(_translate("MainWindow", "Make plots using data from the current run."))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plot Viewer"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Interface"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Plot Selector"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Plate Heatmaps"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "Classification Counts"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "Cocktail"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("MainWindow", "MARCO Accuracy"))
        item = self.listWidget_3.item(4)
        item.setText(_translate("MainWindow", "Classification Progress"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_13.setText(_translate("MainWindow", "Update Plot"))
        self.run_interface.setTabText(self.run_interface.indexOf(self.tab_4), _translate("MainWindow", "Plots"))
        self.run_interface.setTabText(self.run_interface.indexOf(self.tab_10), _translate("MainWindow", "Optimize"))
        self.menuImport.setTitle(_translate("MainWindow", "Import "))
        self.menuImages.setTitle(_translate("MainWindow", "Images"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAdvanced_Tools.setTitle(_translate("MainWindow", "Advanced Tools"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuBeta_Testers.setTitle(_translate("MainWindow", "Beta Testers"))
        self.actionQuickstart_Guide.setText(_translate("MainWindow", "Quickstart Guide"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ"))
        self.actionFrom_FTP.setText(_translate("MainWindow", "From FTP"))
        self.actionFrom_FTP.setToolTip(_translate("MainWindow", "Download images from a remote FTP server."))
        self.actionCocktails.setText(_translate("MainWindow", "Cocktails"))
        self.actionCocktails.setToolTip(_translate("MainWindow", "Import a new set of chemical cocktails. Only recommended if you really know what you are doing."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionFrom_Folder.setText(_translate("MainWindow", "From Folder"))
        self.actionReferences.setText(_translate("MainWindow", "References"))
        self.actionCiting_Polo.setText(_translate("MainWindow", "Citing Polo"))
        self.actionTime_Resolved.setText(_translate("MainWindow", "Add Time Resolved"))
        self.actionTime_Resolved.setToolTip(_translate("MainWindow", "Link two runs in time. Allows for visualizing progression of a well in the slideshow view."))
        self.actionAdd_Image_Type.setText(_translate("MainWindow", "Add Spectrum"))
        self.actionSelected_Runs.setText(_translate("MainWindow", "Selected Runs"))
        self.actionAs_HTML.setText(_translate("MainWindow", "As HTML"))
        self.actionAll_Data.setText(_translate("MainWindow", "All Data"))
        self.actionTable_View.setText(_translate("MainWindow", "Table View"))
        self.actionClassifications.setText(_translate("MainWindow", "Classifications"))
        self.actionView_Log.setText(_translate("MainWindow", "View Log"))
        self.actionHTML.setText(_translate("MainWindow", "HTML Report"))
        self.actionHTML.setToolTip(_translate("MainWindow", "Generate an HTML based report on the current run."))
        self.actionFrom_Saved_Run.setText(_translate("MainWindow", "From Saved Run"))
        self.actionSave_Run.setText(_translate("MainWindow", "Save Run"))
        self.actionSave_Run.setShortcut(_translate("MainWindow", "F"))
        self.actionDelete_Run.setText(_translate("MainWindow", "Delete Run"))
        self.actionSave_Run_As.setText(_translate("MainWindow", "Save Run As"))
        self.actionSaved_Run_xtal_File.setText(_translate("MainWindow", "Saved Run (.xtal File)"))
        self.actionNew_Run.setText(_translate("MainWindow", "New Run"))
        self.actionNew_Run_2.setText(_translate("MainWindow", "New Run"))
        self.actionFrom_Saved_Run_2.setText(_translate("MainWindow", "From Saved Run"))
        self.actionFrom_Saved_Run_3.setText(_translate("MainWindow", "From Saved Run"))
        self.actionFrom_Directory.setText(_translate("MainWindow", "From Rar Archive / Directory "))
        self.actionAS_PDF.setText(_translate("MainWindow", "AS PDF"))
        self.actionAs_CSV.setText(_translate("MainWindow", "As CSV"))
        self.actionDelete_Run_2.setText(_translate("MainWindow", "Remove Run"))
        self.actionView_Log_2.setText(_translate("MainWindow", "View Log"))
        self.actionBatch_Import.setText(_translate("MainWindow", "Batch Import"))
        self.actionRun_Journal.setText(_translate("MainWindow", "Run Journal"))
        self.actionSecure_Save.setText(_translate("MainWindow", "Secure Save"))
        self.actionRemove_Run.setText(_translate("MainWindow", "Remove Run"))
        self.actionOptimization_Screens.setText(_translate("MainWindow", "Optimization Screens"))
        self.actionUser_Guide.setText(_translate("MainWindow", "User\'s Guide"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionBeta_Tester_s_Guide.setText(_translate("MainWindow", "Beta Tester\'s Guide"))
        self.actionEdit_Current_Run_Data.setText(_translate("MainWindow", "Edit Current Run Data"))
        self.actionAs_MSO.setText(_translate("MainWindow", "As MSO"))
        self.actionAs_PPTX.setText(_translate("MainWindow", "As PPTX"))
from polo.widgets.optimize_widget import OptimizeWidget
from polo.widgets.plate_inspector_widget import PlateInspectorWidget
from polo.widgets.run_organizer import RunOrganizer
from polo.widgets.slideshow_inspector import slideshowInspector
from polo.widgets.table_inspector import TableInspector
