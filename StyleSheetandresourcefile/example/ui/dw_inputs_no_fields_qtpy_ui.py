# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_inputs_no_fields.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(402, 405)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.dial = QtWidgets.QDial(self.dockWidgetContents)
        self.dial.setMinimumSize(QtCore.QSize(0, 0))
        self.dial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dial.setProperty("value", 50)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 7, 0, 1, 1)
        self.horizontalScrollBarDis = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBarDis.setEnabled(False)
        self.horizontalScrollBarDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBarDis.setProperty("value", 50)
        self.horizontalScrollBarDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarDis.setObjectName("horizontalScrollBarDis")
        self.gridLayout.addWidget(self.horizontalScrollBarDis, 3, 2, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.dockWidgetContents)
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalSlider.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 7, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 4, 1, 2, 1)
        self.horizontalSliderDis = QtWidgets.QSlider(self.dockWidgetContents)
        self.horizontalSliderDis.setEnabled(False)
        self.horizontalSliderDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSliderDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSliderDis.setProperty("value", 50)
        self.horizontalSliderDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderDis.setObjectName("horizontalSliderDis")
        self.gridLayout.addWidget(self.horizontalSliderDis, 4, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalScrollBarDis = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBarDis.setEnabled(False)
        self.verticalScrollBarDis.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBarDis.setProperty("value", 50)
        self.verticalScrollBarDis.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarDis.setObjectName("verticalScrollBarDis")
        self.gridLayout.addWidget(self.verticalScrollBarDis, 5, 2, 2, 1)
        self.label_21 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBar.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBar.setProperty("value", 50)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 6, 1, 1, 1)
        self.comboBoxDis = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxDis.setEnabled(False)
        self.comboBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxDis.setObjectName("comboBoxDis")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.gridLayout.addWidget(self.comboBoxDis, 1, 2, 1, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBar.setProperty("value", 50)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 9, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.dialDis = QtWidgets.QDial(self.dockWidgetContents)
        self.dialDis.setEnabled(False)
        self.dialDis.setMinimumSize(QtCore.QSize(0, 0))
        self.dialDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dialDis.setProperty("value", 50)
        self.dialDis.setObjectName("dialDis")
        self.gridLayout.addWidget(self.dialDis, 2, 2, 1, 1)
        self.verticalSliderDis = QtWidgets.QSlider(self.dockWidgetContents)
        self.verticalSliderDis.setEnabled(False)
        self.verticalSliderDis.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalSliderDis.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalSliderDis.setProperty("value", 50)
        self.verticalSliderDis.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderDis.setObjectName("verticalSliderDis")
        self.gridLayout.addWidget(self.verticalSliderDis, 7, 2, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.dial.sliderMoved['int'].connect(self.dialDis.setValue)
        self.horizontalScrollBar.sliderMoved['int'].connect(self.horizontalScrollBarDis.setValue)
        self.horizontalSlider.sliderMoved['int'].connect(self.horizontalSliderDis.setValue)
        self.verticalScrollBar.sliderMoved['int'].connect(self.verticalScrollBarDis.setValue)
        self.verticalSlider.sliderMoved['int'].connect(self.verticalSliderDis.setValue)
        self.comboBox.currentIndexChanged['int'].connect(self.comboBoxDis.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Inputs - No Fields"))
        self.dial.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dial.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dial.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_25.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_25.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_25.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_25.setText(_translate("DockWidget", "VerticalSlider"))
        self.horizontalScrollBarDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.horizontalScrollBarDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.horizontalScrollBarDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.verticalSlider.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.verticalSlider.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.verticalSlider.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_24.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_24.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_24.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_24.setText(_translate("DockWidget", "HorizontalSlider"))
        self.horizontalSlider.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.horizontalSlider.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.horizontalSlider.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.horizontalSliderDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.horizontalSliderDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.horizontalSliderDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_23.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_23.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_23.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_23.setText(_translate("DockWidget", "VerticalScroolBar"))
        self.label_2.setText(_translate("DockWidget", "Disabled"))
        self.verticalScrollBarDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.verticalScrollBarDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.verticalScrollBarDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_21.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_21.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_21.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_21.setText(_translate("DockWidget", "Dial"))
        self.verticalScrollBar.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.verticalScrollBar.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.verticalScrollBar.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.comboBoxDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.comboBoxDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.comboBoxDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.comboBoxDis.setItemText(0, _translate("DockWidget", "ComboBox A"))
        self.comboBoxDis.setItemText(1, _translate("DockWidget", "ComboBox B"))
        self.comboBoxDis.setItemText(2, _translate("DockWidget", "ComboBox C"))
        self.horizontalScrollBar.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.horizontalScrollBar.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.horizontalScrollBar.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.comboBox.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.comboBox.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.comboBox.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.comboBox.setItemText(0, _translate("DockWidget", "ComboBox A"))
        self.comboBox.setItemText(1, _translate("DockWidget", "ComboBox B"))
        self.comboBox.setItemText(2, _translate("DockWidget", "ComboBox C"))
        self.label_22.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_22.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_22.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_22.setText(_translate("DockWidget", "HorizontalScroolBar"))
        self.label.setText(_translate("DockWidget", "Enabled"))
        self.label_50.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_50.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_50.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_50.setText(_translate("DockWidget", "Inside DockWidget"))
        self.label_11.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_11.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_11.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_11.setText(_translate("DockWidget", "ComboBox"))
        self.dialDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dialDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dialDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.verticalSliderDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.verticalSliderDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.verticalSliderDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))

