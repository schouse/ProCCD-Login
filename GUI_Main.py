# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TouptekMainWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1215, 897)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color : rgb(0, 50, 100) ;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.actionViewDocks = QAction(MainWindow)
        self.actionViewDocks.setObjectName(u"actionViewDocks")
        self.actionHideDocks = QAction(MainWindow)
        self.actionHideDocks.setObjectName(u"actionHideDocks")
        self.actionFileNew = QAction(MainWindow)
        self.actionFileNew.setObjectName(u"actionFileNew")
        self.actionFileOpen = QAction(MainWindow)
        self.actionFileOpen.setObjectName(u"actionFileOpen")
        self.actionFileClose = QAction(MainWindow)
        self.actionFileClose.setObjectName(u"actionFileClose")
        self.actionFileExit = QAction(MainWindow)
        self.actionFileExit.setObjectName(u"actionFileExit")
        self.actionSetPenStyle = QAction(MainWindow)
        self.actionSetPenStyle.setObjectName(u"actionSetPenStyle")
        self.actionSaveImage = QAction(MainWindow)
        self.actionSaveImage.setObjectName(u"actionSaveImage")
        self.actionExport_File = QAction(MainWindow)
        self.actionExport_File.setObjectName(u"actionExport_File")
        self.actionFactory_Settings = QAction(MainWindow)
        self.actionFactory_Settings.setObjectName(u"actionFactory_Settings")
        self.actionProgram_Settings = QAction(MainWindow)
        self.actionProgram_Settings.setObjectName(u"actionProgram_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollAreaImage = QScrollArea(self.centralwidget)
        self.scrollAreaImage.setObjectName(u"scrollAreaImage")
        self.scrollAreaImage.setEnabled(True)
        self.scrollAreaImage.setMinimumSize(QSize(530, 650))
        self.scrollAreaImage.setStyleSheet(u"QWidget{background-color : rgb(0, 50, 100);\n"
"						color:rgb(255, 255, 255)}")
        self.scrollAreaImage.setLineWidth(6)
        self.scrollAreaImage.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaImage.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaImage.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 751, 836))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.graphicsView = QGraphicsView(self.scrollAreaWidgetContents_4)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QFrame.Raised)
        self.graphicsView.setLineWidth(1)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setAlignment(Qt.AlignCenter)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)

        self.verticalLayout_11.addWidget(self.graphicsView)

        self.scrollAreaImage.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_9.addWidget(self.scrollAreaImage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1215, 21))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockFeatureDisplay = QDockWidget(MainWindow)
        self.dockFeatureDisplay.setObjectName(u"dockFeatureDisplay")
        self.dockFeatureDisplay.setMinimumSize(QSize(440, 600))
        self.dockFeatureDisplay.setMaximumSize(QSize(550, 1000))
        self.dockFeatureDisplay.setAutoFillBackground(False)
        self.dockFeatureDisplay.setStyleSheet(u"QDockWidget{\n"
"background-color : rgb(0, 50, 100) ;\n"
"color:rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"font: bold;\n"
"}")
        self.dockFeatureDisplay.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockFeatureDisplay.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockFeatureDisplay.setWindowTitle(u"Control Panel")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.dockWidgetContents_4.setStyleSheet(u"QWidget{background-color : rgb(0, 50, 100);\n"
"						color:rgb(255, 255, 255)}")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonSave = QPushButton(self.dockWidgetContents_4)
        self.buttonSave.setObjectName(u"buttonSave")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSave.sizePolicy().hasHeightForWidth())
        self.buttonSave.setSizePolicy(sizePolicy)
        self.buttonSave.setMinimumSize(QSize(0, 50))
        self.buttonSave.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0, 170, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;}\n"
"\n"
"QPushButton::pressed{background-color :rgb(255, 0, 0);}")

        self.horizontalLayout_2.addWidget(self.buttonSave)

        self.buttonSaveChemi = QPushButton(self.dockWidgetContents_4)
        self.buttonSaveChemi.setObjectName(u"buttonSaveChemi")
        sizePolicy.setHeightForWidth(self.buttonSaveChemi.sizePolicy().hasHeightForWidth())
        self.buttonSaveChemi.setSizePolicy(sizePolicy)
        self.buttonSaveChemi.setMinimumSize(QSize(0, 50))
        self.buttonSaveChemi.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(10, 170, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;}\n"
"\n"
"QPushButton::pressed{background-color :rgb(200, 0,100);}")

        self.horizontalLayout_2.addWidget(self.buttonSaveChemi)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.scrollCameraSpecs = QScrollArea(self.dockWidgetContents_4)
        self.scrollCameraSpecs.setObjectName(u"scrollCameraSpecs")
        self.scrollCameraSpecs.setFocusPolicy(Qt.StrongFocus)
        self.scrollCameraSpecs.setStyleSheet(u"QScrollArea{\n"
"background-color : rgb(0, 250, 0) ;\n"
"}")
        self.scrollCameraSpecs.setFrameShape(QFrame.NoFrame)
        self.scrollCameraSpecs.setFrameShadow(QFrame.Plain)
        self.scrollCameraSpecs.setLineWidth(0)
        self.scrollCameraSpecs.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 422, 742))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"QDockWidget{background-color : rgb(0, 100, 150);\n"
"						color:rgb(255, 255, 255)}")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.buttonFitWindow = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonFitWindow.setObjectName(u"buttonFitWindow")
        self.buttonFitWindow.setMinimumSize(QSize(0, 30))
        self.buttonFitWindow.setStyleSheet(u"QPushButton{	\n"
"background-color :rgb(250, 150, 150);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color :rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color :rgb(0, 170, 255);\n"
"}")
        self.buttonFitWindow.setCheckable(True)

        self.verticalLayout_7.addWidget(self.buttonFitWindow)

        self.line_20 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_20)

        self.buttonLoadPreviousSettings = QPushButton(self.scrollAreaWidgetContents_3)
        self.buttonLoadPreviousSettings.setObjectName(u"buttonLoadPreviousSettings")
        self.buttonLoadPreviousSettings.setMinimumSize(QSize(0, 30))
        self.buttonLoadPreviousSettings.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 170, 127);}")

        self.verticalLayout_7.addWidget(self.buttonLoadPreviousSettings)

        self.line = QFrame(self.scrollAreaWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.tabTools = QWidget(self.scrollAreaWidgetContents_3)
        self.tabTools.setObjectName(u"tabTools")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabTools.sizePolicy().hasHeightForWidth())
        self.tabTools.setSizePolicy(sizePolicy1)
        self.tabTools.setAutoFillBackground(False)
        self.tabTools.setStyleSheet(u"QWidget{\n"
"background-color : rgb(0, 50, 100) ;\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.tabTools)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 6)
        self.cameraAdjustments = QToolBox(self.tabTools)
        self.cameraAdjustments.setObjectName(u"cameraAdjustments")
        self.cameraAdjustments.setEnabled(True)
        self.cameraAdjustments.setAutoFillBackground(False)
        self.cameraAdjustments.setStyleSheet(u"QToolBox{\n"
"background-color : rgb(0, 50, 100) ;\n"
"}")
        self.cameraAdjustments.setFrameShape(QFrame.NoFrame)
        self.cameraAdjustments.setFrameShadow(QFrame.Raised)
        self.cameraAdjustments.setLineWidth(2)
        self.cameraAdjustments.setMidLineWidth(0)
        self.toolExposure = QWidget()
        self.toolExposure.setObjectName(u"toolExposure")
        self.toolExposure.setGeometry(QRect(0, 0, 394, 406))
        self.toolExposure.setStyleSheet(u"QDockWidget{background-color : rgb(0, 100, 150);\n"
"						color:rgb(255, 255, 255)}")
        self.verticalLayout_15 = QVBoxLayout(self.toolExposure)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.line_7 = QFrame(self.toolExposure)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_7)

        self.radioVideoMode = QRadioButton(self.toolExposure)
        self.radioVideoMode.setObjectName(u"radioVideoMode")

        self.verticalLayout_15.addWidget(self.radioVideoMode)

        self.frameVideoMode = QFrame(self.toolExposure)
        self.frameVideoMode.setObjectName(u"frameVideoMode")
        self.frameVideoMode.setFrameShape(QFrame.StyledPanel)
        self.frameVideoMode.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameVideoMode)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonAutoExposure = QPushButton(self.frameVideoMode)
        self.buttonAutoExposure.setObjectName(u"buttonAutoExposure")
        self.buttonAutoExposure.setMinimumSize(QSize(0, 25))
        self.buttonAutoExposure.setToolTipDuration(2)
        self.buttonAutoExposure.setStyleSheet(u"QPushButton{	\n"
"background-color :rgb(100, 100, 150);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color :rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color :rgb(0, 170, 255);\n"
"}")
        self.buttonAutoExposure.setCheckable(True)

        self.verticalLayout.addWidget(self.buttonAutoExposure)

        self.label_39 = QLabel(self.frameVideoMode)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout.addWidget(self.label_39)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.sliderExposureMilliSec = QSlider(self.frameVideoMode)
        self.sliderExposureMilliSec.setObjectName(u"sliderExposureMilliSec")
        self.sliderExposureMilliSec.setMouseTracking(True)
        self.sliderExposureMilliSec.setMinimum(1)
        self.sliderExposureMilliSec.setMaximum(999)
        self.sliderExposureMilliSec.setPageStep(1)
        self.sliderExposureMilliSec.setOrientation(Qt.Horizontal)
        self.sliderExposureMilliSec.setInvertedControls(False)
        self.sliderExposureMilliSec.setTickPosition(QSlider.TicksAbove)
        self.sliderExposureMilliSec.setTickInterval(25)

        self.horizontalLayout_68.addWidget(self.sliderExposureMilliSec)

        self.spinExposureMilliSec = QSpinBox(self.frameVideoMode)
        self.spinExposureMilliSec.setObjectName(u"spinExposureMilliSec")
        self.spinExposureMilliSec.setMinimumSize(QSize(50, 25))
        self.spinExposureMilliSec.setMaximumSize(QSize(50, 16777215))
        self.spinExposureMilliSec.setLayoutDirection(Qt.LeftToRight)
        self.spinExposureMilliSec.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinExposureMilliSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinExposureMilliSec.setReadOnly(False)
        self.spinExposureMilliSec.setMinimum(1)
        self.spinExposureMilliSec.setMaximum(999)
        self.spinExposureMilliSec.setSingleStep(10)
        self.spinExposureMilliSec.setValue(1)

        self.horizontalLayout_68.addWidget(self.spinExposureMilliSec)


        self.verticalLayout.addLayout(self.horizontalLayout_68)

        self.label_40 = QLabel(self.frameVideoMode)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout.addWidget(self.label_40)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.sliderExposureSec = QSlider(self.frameVideoMode)
        self.sliderExposureSec.setObjectName(u"sliderExposureSec")
        self.sliderExposureSec.setMouseTracking(True)
        self.sliderExposureSec.setMinimum(0)
        self.sliderExposureSec.setMaximum(4)
        self.sliderExposureSec.setPageStep(1)
        self.sliderExposureSec.setOrientation(Qt.Horizontal)
        self.sliderExposureSec.setInvertedControls(False)
        self.sliderExposureSec.setTickPosition(QSlider.TicksAbove)
        self.sliderExposureSec.setTickInterval(1)

        self.horizontalLayout_69.addWidget(self.sliderExposureSec)

        self.spinExposureSec = QSpinBox(self.frameVideoMode)
        self.spinExposureSec.setObjectName(u"spinExposureSec")
        self.spinExposureSec.setMinimumSize(QSize(50, 25))
        self.spinExposureSec.setMaximumSize(QSize(50, 16777215))
        self.spinExposureSec.setLayoutDirection(Qt.LeftToRight)
        self.spinExposureSec.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinExposureSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinExposureSec.setReadOnly(False)
        self.spinExposureSec.setMinimum(0)
        self.spinExposureSec.setMaximum(4)
        self.spinExposureSec.setSingleStep(1)
        self.spinExposureSec.setValue(0)

        self.horizontalLayout_69.addWidget(self.spinExposureSec)


        self.verticalLayout.addLayout(self.horizontalLayout_69)


        self.verticalLayout_15.addWidget(self.frameVideoMode)

        self.line_5 = QFrame(self.toolExposure)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_5)

        self.radioChemiMode = QRadioButton(self.toolExposure)
        self.radioChemiMode.setObjectName(u"radioChemiMode")

        self.verticalLayout_15.addWidget(self.radioChemiMode)

        self.frameChemiMode = QFrame(self.toolExposure)
        self.frameChemiMode.setObjectName(u"frameChemiMode")
        self.frameChemiMode.setFrameShape(QFrame.StyledPanel)
        self.frameChemiMode.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frameChemiMode)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_48 = QLabel(self.frameChemiMode)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_48)

        self.spinLongExposureMin = QSpinBox(self.frameChemiMode)
        self.spinLongExposureMin.setObjectName(u"spinLongExposureMin")
        self.spinLongExposureMin.setMinimumSize(QSize(50, 25))
        self.spinLongExposureMin.setMaximumSize(QSize(50, 16777215))
        self.spinLongExposureMin.setLayoutDirection(Qt.LeftToRight)
        self.spinLongExposureMin.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(10, 200, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinLongExposureMin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinLongExposureMin.setReadOnly(False)
        self.spinLongExposureMin.setMinimum(0)
        self.spinLongExposureMin.setMaximum(59)
        self.spinLongExposureMin.setSingleStep(1)
        self.spinLongExposureMin.setValue(0)

        self.horizontalLayout_25.addWidget(self.spinLongExposureMin)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_50 = QLabel(self.frameChemiMode)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_50)

        self.spinLongExposureSec = QSpinBox(self.frameChemiMode)
        self.spinLongExposureSec.setObjectName(u"spinLongExposureSec")
        self.spinLongExposureSec.setMinimumSize(QSize(50, 25))
        self.spinLongExposureSec.setMaximumSize(QSize(50, 16777215))
        self.spinLongExposureSec.setLayoutDirection(Qt.LeftToRight)
        self.spinLongExposureSec.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(10, 200, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinLongExposureSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinLongExposureSec.setReadOnly(False)
        self.spinLongExposureSec.setMinimum(5)
        self.spinLongExposureSec.setMaximum(59)
        self.spinLongExposureSec.setSingleStep(1)
        self.spinLongExposureSec.setValue(5)

        self.horizontalLayout_22.addWidget(self.spinLongExposureSec)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_51 = QLabel(self.frameChemiMode)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_51)

        self.spinLongExposureMilliSec = QSpinBox(self.frameChemiMode)
        self.spinLongExposureMilliSec.setObjectName(u"spinLongExposureMilliSec")
        self.spinLongExposureMilliSec.setMinimumSize(QSize(50, 25))
        self.spinLongExposureMilliSec.setMaximumSize(QSize(50, 16777215))
        self.spinLongExposureMilliSec.setLayoutDirection(Qt.LeftToRight)
        self.spinLongExposureMilliSec.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(10, 200, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinLongExposureMilliSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinLongExposureMilliSec.setReadOnly(False)
        self.spinLongExposureMilliSec.setMinimum(0)
        self.spinLongExposureMilliSec.setMaximum(999)
        self.spinLongExposureMilliSec.setSingleStep(1)
        self.spinLongExposureMilliSec.setValue(0)

        self.horizontalLayout_16.addWidget(self.spinLongExposureMilliSec)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)

        self.progressExposureTime = QProgressBar(self.frameChemiMode)
        self.progressExposureTime.setObjectName(u"progressExposureTime")
        self.progressExposureTime.setValue(0)
        self.progressExposureTime.setTextVisible(True)
        self.progressExposureTime.setOrientation(Qt.Horizontal)
        self.progressExposureTime.setInvertedAppearance(False)

        self.verticalLayout_14.addWidget(self.progressExposureTime)


        self.verticalLayout_15.addWidget(self.frameChemiMode)

        self.line_30 = QFrame(self.toolExposure)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_30)

        self.verticalSpacer_3 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.line_28 = QFrame(self.toolExposure)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_28)

        self.cameraAdjustments.addItem(self.toolExposure, u"Exposure")
        self.toolCapture = QWidget()
        self.toolCapture.setObjectName(u"toolCapture")
        self.toolCapture.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_8 = QVBoxLayout(self.toolCapture)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.textSavedFolder = QTextBrowser(self.toolCapture)
        self.textSavedFolder.setObjectName(u"textSavedFolder")
        self.textSavedFolder.setMaximumSize(QSize(16777215, 50))
        self.textSavedFolder.setStyleSheet(u"background-color :rgb(0, 170, 255)")
        self.textSavedFolder.setFrameShape(QFrame.Box)
        self.textSavedFolder.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.textSavedFolder)

        self.pushSavedFolder = QPushButton(self.toolCapture)
        self.pushSavedFolder.setObjectName(u"pushSavedFolder")
        self.pushSavedFolder.setMinimumSize(QSize(0, 25))
        self.pushSavedFolder.setToolTipDuration(3)
        self.pushSavedFolder.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 170, 250);}")

        self.verticalLayout_8.addWidget(self.pushSavedFolder)

        self.line_4 = QFrame(self.toolCapture)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_4)

        self.label_2 = QLabel(self.toolCapture)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_8.addWidget(self.label_2)

        self.comboResolution = QComboBox(self.toolCapture)
        self.comboResolution.setObjectName(u"comboResolution")
        self.comboResolution.setMinimumSize(QSize(0, 25))
        self.comboResolution.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.verticalLayout_8.addWidget(self.comboResolution)

        self.line_8 = QFrame(self.toolCapture)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_8)

        self.label_3 = QLabel(self.toolCapture)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)

        self.comboFormat = QComboBox(self.toolCapture)
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.comboFormat.setObjectName(u"comboFormat")
        self.comboFormat.setMinimumSize(QSize(0, 25))
        self.comboFormat.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.verticalLayout_8.addWidget(self.comboFormat)

        self.line_9 = QFrame(self.toolCapture)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_9)

        self.label_4 = QLabel(self.toolCapture)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.comboFnamePrefix = QComboBox(self.toolCapture)
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.addItem("")
        self.comboFnamePrefix.setObjectName(u"comboFnamePrefix")
        self.comboFnamePrefix.setMinimumSize(QSize(0, 25))
        self.comboFnamePrefix.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.comboFnamePrefix.setEditable(False)
        self.comboFnamePrefix.setMaxVisibleItems(6)
        self.comboFnamePrefix.setDuplicatesEnabled(False)

        self.horizontalLayout_17.addWidget(self.comboFnamePrefix)

        self.line_18 = QFrame(self.toolCapture)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_18)

        self.label_7 = QLabel(self.toolCapture)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_17.addWidget(self.label_7)

        self.lineAddPrefix = QLineEdit(self.toolCapture)
        self.lineAddPrefix.setObjectName(u"lineAddPrefix")
        self.lineAddPrefix.setMinimumSize(QSize(0, 25))
        self.lineAddPrefix.setMaximumSize(QSize(80, 16777215))
        self.lineAddPrefix.setStyleSheet(u"QLineEdit{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.lineAddPrefix.setMaxLength(10)

        self.horizontalLayout_17.addWidget(self.lineAddPrefix)

        self.pushAddPrefix = QPushButton(self.toolCapture)
        self.pushAddPrefix.setObjectName(u"pushAddPrefix")
        self.pushAddPrefix.setMinimumSize(QSize(0, 25))
        self.pushAddPrefix.setMaximumSize(QSize(50, 16777215))
        self.pushAddPrefix.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 170, 250);}")

        self.horizontalLayout_17.addWidget(self.pushAddPrefix)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.line_19 = QFrame(self.toolCapture)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_19)

        self.label_42 = QLabel(self.toolCapture)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_8.addWidget(self.label_42)

        self.comboFnameSuffix = QComboBox(self.toolCapture)
        self.comboFnameSuffix.addItem("")
        self.comboFnameSuffix.addItem("")
        self.comboFnameSuffix.setObjectName(u"comboFnameSuffix")
        self.comboFnameSuffix.setMinimumSize(QSize(0, 25))
        self.comboFnameSuffix.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.verticalLayout_8.addWidget(self.comboFnameSuffix)

        self.verticalSpacer = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.cameraAdjustments.addItem(self.toolCapture, u"Capture Options")
        self.toolDisplay = QWidget()
        self.toolDisplay.setObjectName(u"toolDisplay")
        self.toolDisplay.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_6 = QVBoxLayout(self.toolDisplay)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.labelZoomFactor_2 = QLabel(self.toolDisplay)
        self.labelZoomFactor_2.setObjectName(u"labelZoomFactor_2")

        self.horizontalLayout_15.addWidget(self.labelZoomFactor_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)

        self.spinRotation = QSpinBox(self.toolDisplay)
        self.spinRotation.setObjectName(u"spinRotation")
        self.spinRotation.setMinimumSize(QSize(50, 25))
        self.spinRotation.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinRotation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinRotation.setMaximum(270)
        self.spinRotation.setSingleStep(90)

        self.horizontalLayout_15.addWidget(self.spinRotation)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.line_17 = QFrame(self.toolDisplay)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_17)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelOverlay_2 = QLabel(self.toolDisplay)
        self.labelOverlay_2.setObjectName(u"labelOverlay_2")

        self.horizontalLayout.addWidget(self.labelOverlay_2)

        self.comboGrid = QComboBox(self.toolDisplay)
        self.comboGrid.addItem("")
        self.comboGrid.addItem("")
        self.comboGrid.addItem("")
        self.comboGrid.addItem("")
        self.comboGrid.addItem("")
        self.comboGrid.setObjectName(u"comboGrid")
        self.comboGrid.setMinimumSize(QSize(0, 25))
        self.comboGrid.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.horizontalLayout.addWidget(self.comboGrid)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelOverlay_3 = QLabel(self.toolDisplay)
        self.labelOverlay_3.setObjectName(u"labelOverlay_3")

        self.horizontalLayout_9.addWidget(self.labelOverlay_3)

        self.comboPenColour = QComboBox(self.toolDisplay)
        self.comboPenColour.addItem("")
        self.comboPenColour.addItem("")
        self.comboPenColour.addItem("")
        self.comboPenColour.addItem("")
        self.comboPenColour.addItem("")
        self.comboPenColour.setObjectName(u"comboPenColour")
        self.comboPenColour.setMinimumSize(QSize(0, 25))
        self.comboPenColour.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.comboPenColour)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.labelOverlay_4 = QLabel(self.toolDisplay)
        self.labelOverlay_4.setObjectName(u"labelOverlay_4")

        self.horizontalLayout_14.addWidget(self.labelOverlay_4)

        self.comboPenThick = QComboBox(self.toolDisplay)
        self.comboPenThick.addItem("")
        self.comboPenThick.addItem("")
        self.comboPenThick.addItem("")
        self.comboPenThick.addItem("")
        self.comboPenThick.addItem("")
        self.comboPenThick.addItem("")
        self.comboPenThick.setObjectName(u"comboPenThick")
        self.comboPenThick.setMinimumSize(QSize(0, 25))
        self.comboPenThick.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.comboPenThick)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.line_16 = QFrame(self.toolDisplay)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.labelOverlay_5 = QLabel(self.toolDisplay)
        self.labelOverlay_5.setObjectName(u"labelOverlay_5")

        self.horizontalLayout_18.addWidget(self.labelOverlay_5)

        self.comboFrequency = QComboBox(self.toolDisplay)
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.addItem("")
        self.comboFrequency.setObjectName(u"comboFrequency")
        self.comboFrequency.setMinimumSize(QSize(0, 25))
        self.comboFrequency.setStyleSheet(u"QComboBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.comboFrequency)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.line_2 = QFrame(self.toolDisplay)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.labelZoomFactor = QLabel(self.toolDisplay)
        self.labelZoomFactor.setObjectName(u"labelZoomFactor")

        self.verticalLayout_6.addWidget(self.labelZoomFactor)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spinDisplayZoom = QSpinBox(self.toolDisplay)
        self.spinDisplayZoom.setObjectName(u"spinDisplayZoom")
        self.spinDisplayZoom.setMinimumSize(QSize(50, 25))
        self.spinDisplayZoom.setMouseTracking(False)
        self.spinDisplayZoom.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinDisplayZoom.setMinimum(20)
        self.spinDisplayZoom.setMaximum(400)
        self.spinDisplayZoom.setValue(100)

        self.horizontalLayout_8.addWidget(self.spinDisplayZoom)

        self.sliderDisplayZoom = QSlider(self.toolDisplay)
        self.sliderDisplayZoom.setObjectName(u"sliderDisplayZoom")
        self.sliderDisplayZoom.setMouseTracking(False)
        self.sliderDisplayZoom.setMinimum(20)
        self.sliderDisplayZoom.setMaximum(200)
        self.sliderDisplayZoom.setValue(100)
        self.sliderDisplayZoom.setTracking(False)
        self.sliderDisplayZoom.setOrientation(Qt.Horizontal)
        self.sliderDisplayZoom.setInvertedControls(False)
        self.sliderDisplayZoom.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout_8.addWidget(self.sliderDisplayZoom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.cameraAdjustments.addItem(self.toolDisplay, u"Display")
        self.toolTemperature = QWidget()
        self.toolTemperature.setObjectName(u"toolTemperature")
        self.toolTemperature.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_12 = QVBoxLayout(self.toolTemperature)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.buttonFanOnOff = QPushButton(self.toolTemperature)
        self.buttonFanOnOff.setObjectName(u"buttonFanOnOff")
        self.buttonFanOnOff.setMinimumSize(QSize(30, 25))
        self.buttonFanOnOff.setMaximumSize(QSize(10000, 16777215))
        self.buttonFanOnOff.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")
        self.buttonFanOnOff.setCheckable(True)

        self.verticalLayout_12.addWidget(self.buttonFanOnOff)

        self.buttonCoolingOnOff = QPushButton(self.toolTemperature)
        self.buttonCoolingOnOff.setObjectName(u"buttonCoolingOnOff")
        self.buttonCoolingOnOff.setMinimumSize(QSize(30, 25))
        self.buttonCoolingOnOff.setMaximumSize(QSize(10000, 16777215))
        self.buttonCoolingOnOff.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")
        self.buttonCoolingOnOff.setCheckable(True)

        self.verticalLayout_12.addWidget(self.buttonCoolingOnOff)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_45 = QLabel(self.toolTemperature)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_4.addWidget(self.label_45)

        self.horizontalSpacer_2 = QSpacerItem(108, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.labelTemperature = QLabel(self.toolTemperature)
        self.labelTemperature.setObjectName(u"labelTemperature")
        self.labelTemperature.setLayoutDirection(Qt.LeftToRight)
        self.labelTemperature.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.labelTemperature)

        self.label_49 = QLabel(self.toolTemperature)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setLayoutDirection(Qt.LeftToRight)
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_49)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.line_10 = QFrame(self.toolTemperature)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_10)

        self.label_47 = QLabel(self.toolTemperature)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_12.addWidget(self.label_47)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sliderCooling = QSlider(self.toolTemperature)
        self.sliderCooling.setObjectName(u"sliderCooling")
        self.sliderCooling.setMinimum(-30)
        self.sliderCooling.setMaximum(30)
        self.sliderCooling.setValue(-25)
        self.sliderCooling.setOrientation(Qt.Horizontal)
        self.sliderCooling.setInvertedAppearance(False)
        self.sliderCooling.setInvertedControls(False)
        self.sliderCooling.setTickPosition(QSlider.TicksAbove)
        self.sliderCooling.setTickInterval(5)

        self.horizontalLayout_3.addWidget(self.sliderCooling)

        self.spinCooling = QSpinBox(self.toolTemperature)
        self.spinCooling.setObjectName(u"spinCooling")
        self.spinCooling.setMinimumSize(QSize(50, 25))
        self.spinCooling.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinCooling.setMinimum(-30)
        self.spinCooling.setMaximum(30)
        self.spinCooling.setValue(-25)

        self.horizontalLayout_3.addWidget(self.spinCooling)


        self.verticalLayout_12.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 241, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.cameraAdjustments.addItem(self.toolTemperature, u"Cooling")
        self.toolLensControl = QWidget()
        self.toolLensControl.setObjectName(u"toolLensControl")
        self.toolLensControl.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_2 = QVBoxLayout(self.toolLensControl)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.toolLensControl)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.buttonFocusL3 = QPushButton(self.toolLensControl)
        self.buttonFocusL3.setObjectName(u"buttonFocusL3")
        self.buttonFocusL3.setMinimumSize(QSize(30, 25))
        self.buttonFocusL3.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusL3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusL3)

        self.buttonFocusL2 = QPushButton(self.toolLensControl)
        self.buttonFocusL2.setObjectName(u"buttonFocusL2")
        self.buttonFocusL2.setMinimumSize(QSize(30, 25))
        self.buttonFocusL2.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusL2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusL2)

        self.buttonFocusL1 = QPushButton(self.toolLensControl)
        self.buttonFocusL1.setObjectName(u"buttonFocusL1")
        self.buttonFocusL1.setMinimumSize(QSize(30, 25))
        self.buttonFocusL1.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusL1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusL1)

        self.line_11 = QFrame(self.toolLensControl)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_11)

        self.buttonFocusR1 = QPushButton(self.toolLensControl)
        self.buttonFocusR1.setObjectName(u"buttonFocusR1")
        self.buttonFocusR1.setMinimumSize(QSize(30, 25))
        self.buttonFocusR1.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusR1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusR1)

        self.buttonFocusR2 = QPushButton(self.toolLensControl)
        self.buttonFocusR2.setObjectName(u"buttonFocusR2")
        self.buttonFocusR2.setMinimumSize(QSize(30, 25))
        self.buttonFocusR2.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusR2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusR2)

        self.buttonFocusR3 = QPushButton(self.toolLensControl)
        self.buttonFocusR3.setObjectName(u"buttonFocusR3")
        self.buttonFocusR3.setMinimumSize(QSize(30, 25))
        self.buttonFocusR3.setMaximumSize(QSize(40, 16777215))
        self.buttonFocusR3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 170, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_6.addWidget(self.buttonFocusR3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line_15 = QFrame(self.toolLensControl)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_15)

        self.label_5 = QLabel(self.toolLensControl)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.buttonZoomL3 = QPushButton(self.toolLensControl)
        self.buttonZoomL3.setObjectName(u"buttonZoomL3")
        self.buttonZoomL3.setMinimumSize(QSize(30, 25))
        self.buttonZoomL3.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomL3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomL3)

        self.buttonZoomL2 = QPushButton(self.toolLensControl)
        self.buttonZoomL2.setObjectName(u"buttonZoomL2")
        self.buttonZoomL2.setMinimumSize(QSize(30, 25))
        self.buttonZoomL2.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomL2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomL2)

        self.buttonZoomL1 = QPushButton(self.toolLensControl)
        self.buttonZoomL1.setObjectName(u"buttonZoomL1")
        self.buttonZoomL1.setMinimumSize(QSize(30, 25))
        self.buttonZoomL1.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomL1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomL1)

        self.line_12 = QFrame(self.toolLensControl)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_12)

        self.buttonZoomR1 = QPushButton(self.toolLensControl)
        self.buttonZoomR1.setObjectName(u"buttonZoomR1")
        self.buttonZoomR1.setMinimumSize(QSize(30, 25))
        self.buttonZoomR1.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomR1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomR1)

        self.buttonZoomR2 = QPushButton(self.toolLensControl)
        self.buttonZoomR2.setObjectName(u"buttonZoomR2")
        self.buttonZoomR2.setMinimumSize(QSize(30, 25))
        self.buttonZoomR2.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomR2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomR2)

        self.buttonZoomR3 = QPushButton(self.toolLensControl)
        self.buttonZoomR3.setObjectName(u"buttonZoomR3")
        self.buttonZoomR3.setMinimumSize(QSize(30, 25))
        self.buttonZoomR3.setMaximumSize(QSize(40, 16777215))
        self.buttonZoomR3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 210, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_11.addWidget(self.buttonZoomR3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.line_14 = QFrame(self.toolLensControl)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_14)

        self.label_6 = QLabel(self.toolLensControl)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.buttonIrisL3 = QPushButton(self.toolLensControl)
        self.buttonIrisL3.setObjectName(u"buttonIrisL3")
        self.buttonIrisL3.setMinimumSize(QSize(30, 25))
        self.buttonIrisL3.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisL3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisL3)

        self.buttonIrisL2 = QPushButton(self.toolLensControl)
        self.buttonIrisL2.setObjectName(u"buttonIrisL2")
        self.buttonIrisL2.setMinimumSize(QSize(30, 25))
        self.buttonIrisL2.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisL2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisL2)

        self.buttonIrisL1 = QPushButton(self.toolLensControl)
        self.buttonIrisL1.setObjectName(u"buttonIrisL1")
        self.buttonIrisL1.setMinimumSize(QSize(30, 25))
        self.buttonIrisL1.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisL1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisL1)

        self.line_13 = QFrame(self.toolLensControl)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_13)

        self.buttonIrisR1 = QPushButton(self.toolLensControl)
        self.buttonIrisR1.setObjectName(u"buttonIrisR1")
        self.buttonIrisR1.setMinimumSize(QSize(30, 25))
        self.buttonIrisR1.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisR1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisR1)

        self.buttonIrisR2 = QPushButton(self.toolLensControl)
        self.buttonIrisR2.setObjectName(u"buttonIrisR2")
        self.buttonIrisR2.setMinimumSize(QSize(30, 25))
        self.buttonIrisR2.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisR2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisR2)

        self.buttonIrisR3 = QPushButton(self.toolLensControl)
        self.buttonIrisR3.setObjectName(u"buttonIrisR3")
        self.buttonIrisR3.setMinimumSize(QSize(30, 25))
        self.buttonIrisR3.setMaximumSize(QSize(40, 16777215))
        self.buttonIrisR3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(0,110, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_13.addWidget(self.buttonIrisR3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.line_21 = QFrame(self.toolLensControl)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_21)

        self.label_10 = QLabel(self.toolLensControl)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.buttonFilterL3 = QPushButton(self.toolLensControl)
        self.buttonFilterL3.setObjectName(u"buttonFilterL3")
        self.buttonFilterL3.setMinimumSize(QSize(30, 25))
        self.buttonFilterL3.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterL3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterL3)

        self.buttonFilterL2 = QPushButton(self.toolLensControl)
        self.buttonFilterL2.setObjectName(u"buttonFilterL2")
        self.buttonFilterL2.setMinimumSize(QSize(30, 25))
        self.buttonFilterL2.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterL2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterL2)

        self.buttonFilterL1 = QPushButton(self.toolLensControl)
        self.buttonFilterL1.setObjectName(u"buttonFilterL1")
        self.buttonFilterL1.setMinimumSize(QSize(30, 25))
        self.buttonFilterL1.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterL1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterL1)

        self.line_23 = QFrame(self.toolLensControl)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line_23)

        self.buttonFilterR1 = QPushButton(self.toolLensControl)
        self.buttonFilterR1.setObjectName(u"buttonFilterR1")
        self.buttonFilterR1.setMinimumSize(QSize(30, 25))
        self.buttonFilterR1.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterR1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterR1)

        self.buttonFilterR2 = QPushButton(self.toolLensControl)
        self.buttonFilterR2.setObjectName(u"buttonFilterR2")
        self.buttonFilterR2.setMinimumSize(QSize(30, 25))
        self.buttonFilterR2.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterR2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterR2)

        self.buttonFilterR3 = QPushButton(self.toolLensControl)
        self.buttonFilterR3.setObjectName(u"buttonFilterR3")
        self.buttonFilterR3.setMinimumSize(QSize(30, 25))
        self.buttonFilterR3.setMaximumSize(QSize(40, 16777215))
        self.buttonFilterR3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150,150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_21.addWidget(self.buttonFilterR3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.line_29 = QFrame(self.toolLensControl)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_29)

        self.label_12 = QLabel(self.toolLensControl)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.buttonSpareL3 = QPushButton(self.toolLensControl)
        self.buttonSpareL3.setObjectName(u"buttonSpareL3")
        self.buttonSpareL3.setMinimumSize(QSize(30, 25))
        self.buttonSpareL3.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareL3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareL3)

        self.buttonSpareL2 = QPushButton(self.toolLensControl)
        self.buttonSpareL2.setObjectName(u"buttonSpareL2")
        self.buttonSpareL2.setMinimumSize(QSize(30, 25))
        self.buttonSpareL2.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareL2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareL2)

        self.buttonSpareL1 = QPushButton(self.toolLensControl)
        self.buttonSpareL1.setObjectName(u"buttonSpareL1")
        self.buttonSpareL1.setMinimumSize(QSize(30, 25))
        self.buttonSpareL1.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareL1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareL1)

        self.line_27 = QFrame(self.toolLensControl)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.VLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_24.addWidget(self.line_27)

        self.buttonSpareR1 = QPushButton(self.toolLensControl)
        self.buttonSpareR1.setObjectName(u"buttonSpareR1")
        self.buttonSpareR1.setMinimumSize(QSize(30, 25))
        self.buttonSpareR1.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareR1.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareR1)

        self.buttonSpareR2 = QPushButton(self.toolLensControl)
        self.buttonSpareR2.setObjectName(u"buttonSpareR2")
        self.buttonSpareR2.setMinimumSize(QSize(30, 25))
        self.buttonSpareR2.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareR2.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareR2)

        self.buttonSpareR3 = QPushButton(self.toolLensControl)
        self.buttonSpareR3.setObjectName(u"buttonSpareR3")
        self.buttonSpareR3.setMinimumSize(QSize(30, 25))
        self.buttonSpareR3.setMaximumSize(QSize(40, 16777215))
        self.buttonSpareR3.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(100,150, 200);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 85, 250);}")

        self.horizontalLayout_24.addWidget(self.buttonSpareR3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_4 = QSpacerItem(20, 94, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.cameraAdjustments.addItem(self.toolLensControl, u"Lens Control")
        self.toolLightControl = QWidget()
        self.toolLightControl.setObjectName(u"toolLightControl")
        self.toolLightControl.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_13 = QVBoxLayout(self.toolLightControl)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.buttonMains = QPushButton(self.toolLightControl)
        self.buttonMains.setObjectName(u"buttonMains")
        self.buttonMains.setMinimumSize(QSize(0, 25))
        self.buttonMains.setAutoFillBackground(False)
        self.buttonMains.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonMains.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonMains)

        self.buttonEpiWhite = QPushButton(self.toolLightControl)
        self.buttonEpiWhite.setObjectName(u"buttonEpiWhite")
        self.buttonEpiWhite.setMinimumSize(QSize(0, 25))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 85, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(127, 255, 191, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(63, 255, 159, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 127, 63, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 170, 84, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush8 = QBrush(QColor(0, 255, 127, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.buttonEpiWhite.setPalette(palette)
        self.buttonEpiWhite.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonEpiWhite.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonEpiWhite)

        self.buttonTransUV = QPushButton(self.toolLightControl)
        self.buttonTransUV.setObjectName(u"buttonTransUV")
        self.buttonTransUV.setMinimumSize(QSize(0, 25))
        self.buttonTransUV.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonTransUV.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonTransUV)

        self.buttonTransWhite = QPushButton(self.toolLightControl)
        self.buttonTransWhite.setObjectName(u"buttonTransWhite")
        self.buttonTransWhite.setMinimumSize(QSize(0, 25))
        self.buttonTransWhite.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonTransWhite.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonTransWhite)

        self.buttonTransBlue = QPushButton(self.toolLightControl)
        self.buttonTransBlue.setObjectName(u"buttonTransBlue")
        self.buttonTransBlue.setMinimumSize(QSize(0, 25))
        self.buttonTransBlue.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonTransBlue.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonTransBlue)

        self.buttonEpiUVA = QPushButton(self.toolLightControl)
        self.buttonEpiUVA.setObjectName(u"buttonEpiUVA")
        self.buttonEpiUVA.setMinimumSize(QSize(0, 25))
        self.buttonEpiUVA.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonEpiUVA.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonEpiUVA)

        self.buttonEpiUVB = QPushButton(self.toolLightControl)
        self.buttonEpiUVB.setObjectName(u"buttonEpiUVB")
        self.buttonEpiUVB.setMinimumSize(QSize(0, 25))
        self.buttonEpiUVB.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonEpiUVB.setCheckable(True)

        self.verticalLayout_13.addWidget(self.buttonEpiUVB)

        self.line_22 = QFrame(self.toolLightControl)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_22)

        self.groupBox = QGroupBox(self.toolLightControl)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.sliderStainFree = QSlider(self.groupBox)
        self.sliderStainFree.setObjectName(u"sliderStainFree")
        self.sliderStainFree.setMinimum(10)
        self.sliderStainFree.setMaximum(600)
        self.sliderStainFree.setOrientation(Qt.Horizontal)
        self.sliderStainFree.setTickPosition(QSlider.TicksAbove)
        self.sliderStainFree.setTickInterval(60)

        self.horizontalLayout_23.addWidget(self.sliderStainFree)

        self.spinStainFree = QSpinBox(self.groupBox)
        self.spinStainFree.setObjectName(u"spinStainFree")
        self.spinStainFree.setMinimumSize(QSize(50, 25))
        self.spinStainFree.setStyleSheet(u"QSpinBox{	\n"
"background-color : rgb(0, 150, 250);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"border-radius: 3px;\n"
"}")
        self.spinStainFree.setMinimum(10)
        self.spinStainFree.setMaximum(600)

        self.horizontalLayout_23.addWidget(self.spinStainFree)


        self.verticalLayout_10.addLayout(self.horizontalLayout_23)

        self.line_25 = QFrame(self.groupBox)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_25)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_20.addWidget(self.label_11)

        self.labelElapsedTime = QLabel(self.groupBox)
        self.labelElapsedTime.setObjectName(u"labelElapsedTime")
        self.labelElapsedTime.setMinimumSize(QSize(20, 0))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelElapsedTime.setFont(font)
        self.labelElapsedTime.setLayoutDirection(Qt.LeftToRight)
        self.labelElapsedTime.setScaledContents(False)
        self.labelElapsedTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.labelElapsedTime.setMargin(0)

        self.horizontalLayout_20.addWidget(self.labelElapsedTime)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.line_26 = QFrame(self.groupBox)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_26)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.buttonStartStainFree = QPushButton(self.groupBox)
        self.buttonStartStainFree.setObjectName(u"buttonStartStainFree")
        self.buttonStartStainFree.setMinimumSize(QSize(0, 25))
        self.buttonStartStainFree.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")
        self.buttonStartStainFree.setCheckable(False)

        self.horizontalLayout_19.addWidget(self.buttonStartStainFree)

        self.buttonAbortStainFree = QPushButton(self.groupBox)
        self.buttonAbortStainFree.setObjectName(u"buttonAbortStainFree")
        self.buttonAbortStainFree.setMinimumSize(QSize(0, 25))
        self.buttonAbortStainFree.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(255, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{background-color :rgb(0, 170, 255);}\n"
"\n"
"QPushButton::checked{background-color :rgb(0, 255, 127);}\n"
"")

        self.horizontalLayout_19.addWidget(self.buttonAbortStainFree)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)


        self.verticalLayout_13.addWidget(self.groupBox)

        self.verticalSpacer_6 = QSpacerItem(20, 178, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.cameraAdjustments.addItem(self.toolLightControl, u"Illumination Control")
        self.toolProtocol = QWidget()
        self.toolProtocol.setObjectName(u"toolProtocol")
        self.toolProtocol.setGeometry(QRect(0, 0, 394, 406))
        self.verticalLayout_3 = QVBoxLayout(self.toolProtocol)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonSaveProtocol = QPushButton(self.toolProtocol)
        self.buttonSaveProtocol.setObjectName(u"buttonSaveProtocol")
        self.buttonSaveProtocol.setMinimumSize(QSize(0, 30))
        self.buttonSaveProtocol.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(85, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 255, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 170, 250);}")

        self.verticalLayout_3.addWidget(self.buttonSaveProtocol)

        self.buttonLoadProtocol = QPushButton(self.toolProtocol)
        self.buttonLoadProtocol.setObjectName(u"buttonLoadProtocol")
        self.buttonLoadProtocol.setMinimumSize(QSize(0, 30))
        self.buttonLoadProtocol.setStyleSheet(u"QPushButton{	\n"
"background-color : rgb(150, 150, 255);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"font: bold;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{background-color :rgb(85, 0, 127);}\n"
"\n"
"QPushButton::pressed{background-color :rgb(85, 00, 250);}")

        self.verticalLayout_3.addWidget(self.buttonLoadProtocol)

        self.line_24 = QFrame(self.toolProtocol)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_24)

        self.verticalSpacer_7 = QSpacerItem(20, 267, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.cameraAdjustments.addItem(self.toolProtocol, u"Protocols")

        self.verticalLayout_5.addWidget(self.cameraAdjustments)


        self.verticalLayout_7.addWidget(self.tabTools)

        self.scrollCameraSpecs.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollCameraSpecs)

        self.line_3 = QFrame(self.dockWidgetContents_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.dockFeatureDisplay.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockFeatureDisplay)
#if QT_CONFIG(shortcut)
        self.label_39.setBuddy(self.sliderExposureMilliSec)
        self.label_40.setBuddy(self.sliderExposureSec)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionProgram_Settings)

        self.retranslateUi(MainWindow)
        self.sliderExposureSec.valueChanged.connect(self.spinExposureSec.setValue)
        self.spinDisplayZoom.valueChanged.connect(self.sliderDisplayZoom.setValue)
        self.sliderExposureMilliSec.valueChanged.connect(self.spinExposureMilliSec.setValue)
        self.sliderDisplayZoom.valueChanged.connect(self.spinDisplayZoom.setValue)
        self.spinStainFree.valueChanged.connect(self.sliderStainFree.setValue)
        self.spinExposureMilliSec.valueChanged.connect(self.sliderExposureMilliSec.setValue)
        self.spinExposureSec.valueChanged.connect(self.sliderExposureSec.setValue)
        self.sliderStainFree.valueChanged.connect(self.spinStainFree.setValue)
        self.sliderCooling.valueChanged.connect(self.spinCooling.setValue)
        self.spinCooling.valueChanged.connect(self.sliderCooling.setValue)

        self.cameraAdjustments.setCurrentIndex(2)
        self.cameraAdjustments.layout().setSpacing(6)
        self.comboFrequency.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gel.ProCCD v2", None))
        self.actionViewDocks.setText(QCoreApplication.translate("MainWindow", u"View All Docks", None))
#if QT_CONFIG(shortcut)
        self.actionViewDocks.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionHideDocks.setText(QCoreApplication.translate("MainWindow", u"Hide All Docks", None))
#if QT_CONFIG(shortcut)
        self.actionHideDocks.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionFileNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionFileOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionFileClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionFileExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSetPenStyle.setText(QCoreApplication.translate("MainWindow", u"Pen Style", None))
#if QT_CONFIG(shortcut)
        self.actionSetPenStyle.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveImage.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.actionExport_File.setText(QCoreApplication.translate("MainWindow", u"Export File", None))
        self.actionFactory_Settings.setText(QCoreApplication.translate("MainWindow", u"Init Settings", None))
        self.actionProgram_Settings.setText(QCoreApplication.translate("MainWindow", u"Program Settings", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.buttonSaveChemi.setText(QCoreApplication.translate("MainWindow", u"Save Chemi Image", None))
        self.buttonFitWindow.setText(QCoreApplication.translate("MainWindow", u"Fit in Window", None))
        self.buttonLoadPreviousSettings.setText(QCoreApplication.translate("MainWindow", u"Load Last Run Settings", None))
        self.radioVideoMode.setText(QCoreApplication.translate("MainWindow", u"Video Mode (with Live Image display):", None))
#if QT_CONFIG(tooltip)
        self.buttonAutoExposure.setToolTip(QCoreApplication.translate("MainWindow", u"Camera will try to find an optimal exposure automaticallhy", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.buttonAutoExposure.setStatusTip(QCoreApplication.translate("MainWindow", u"Automatic Exposure", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.buttonAutoExposure.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.buttonAutoExposure.setText(QCoreApplication.translate("MainWindow", u"Auto Exposure ON | Manual Exposure Off", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Exposure in milliseconds (mS):", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Exposure in seconds (S):", None))
        self.radioChemiMode.setText(QCoreApplication.translate("MainWindow", u"Chemi Mode (recommended for exposures >5 sec):", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Sec:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"mSec:", None))
        self.progressExposureTime.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolExposure), QCoreApplication.translate("MainWindow", u"Exposure", None))
#if QT_CONFIG(tooltip)
        self.textSavedFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Displays the folder where clicked images are going to be saved", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.textSavedFolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Folder where images are going to be saved", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.pushSavedFolder.setToolTip(QCoreApplication.translate("MainWindow", u"Click to change the folder where images are saved", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushSavedFolder.setStatusTip(QCoreApplication.translate("MainWindow", u"Change the folder where images are saved", None))
#endif // QT_CONFIG(statustip)
        self.pushSavedFolder.setText(QCoreApplication.translate("MainWindow", u"Select Folder to Save Image in", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Resolution of Saved Image:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Format of Saved Image:", None))
        self.comboFormat.setItemText(0, QCoreApplication.translate("MainWindow", u"JPEG", None))
        self.comboFormat.setItemText(1, QCoreApplication.translate("MainWindow", u"TIFF", None))
        self.comboFormat.setItemText(2, QCoreApplication.translate("MainWindow", u"PNG", None))
        self.comboFormat.setItemText(3, QCoreApplication.translate("MainWindow", u"BMP", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Prefix of Filename of Saved Image:", None))
        self.comboFnamePrefix.setItemText(0, QCoreApplication.translate("MainWindow", u"Gel_", None))
        self.comboFnamePrefix.setItemText(1, QCoreApplication.translate("MainWindow", u"Protein_", None))
        self.comboFnamePrefix.setItemText(2, QCoreApplication.translate("MainWindow", u"Image_", None))
        self.comboFnamePrefix.setItemText(3, QCoreApplication.translate("MainWindow", u"DNA_", None))
        self.comboFnamePrefix.setItemText(4, QCoreApplication.translate("MainWindow", u"RNA_", None))
        self.comboFnamePrefix.setItemText(5, QCoreApplication.translate("MainWindow", u"User Defined...", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Your Prefix:", None))
        self.lineAddPrefix.setText("")
        self.lineAddPrefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Prefix", None))
        self.pushAddPrefix.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Suffix of Filename of Saved Image:", None))
        self.comboFnameSuffix.setItemText(0, QCoreApplication.translate("MainWindow", u"Auto Numbering", None))
        self.comboFnameSuffix.setItemText(1, QCoreApplication.translate("MainWindow", u"Date and Time", None))

        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolCapture), QCoreApplication.translate("MainWindow", u"Capture Options", None))
        self.labelZoomFactor_2.setText(QCoreApplication.translate("MainWindow", u"Rotation:", None))
        self.labelOverlay_2.setText(QCoreApplication.translate("MainWindow", u"Grid:", None))
        self.comboGrid.setItemText(0, QCoreApplication.translate("MainWindow", u"No Grid", None))
        self.comboGrid.setItemText(1, QCoreApplication.translate("MainWindow", u"2x2", None))
        self.comboGrid.setItemText(2, QCoreApplication.translate("MainWindow", u"3x3", None))
        self.comboGrid.setItemText(3, QCoreApplication.translate("MainWindow", u"5x5", None))
        self.comboGrid.setItemText(4, QCoreApplication.translate("MainWindow", u"10x10", None))

        self.labelOverlay_3.setText(QCoreApplication.translate("MainWindow", u"Gridlines Colour:", None))
        self.comboPenColour.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboPenColour.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboPenColour.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.comboPenColour.setItemText(3, QCoreApplication.translate("MainWindow", u"White", None))
        self.comboPenColour.setItemText(4, QCoreApplication.translate("MainWindow", u"Black", None))

        self.labelOverlay_4.setText(QCoreApplication.translate("MainWindow", u"Gridlines Thickness:", None))
        self.comboPenThick.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboPenThick.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboPenThick.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboPenThick.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboPenThick.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboPenThick.setItemText(5, QCoreApplication.translate("MainWindow", u"10", None))

        self.labelOverlay_5.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.comboFrequency.setItemText(0, QCoreApplication.translate("MainWindow", u"50Hz", None))
        self.comboFrequency.setItemText(1, QCoreApplication.translate("MainWindow", u"60 Hz", None))
        self.comboFrequency.setItemText(2, QCoreApplication.translate("MainWindow", u"Direct Current", None))

        self.labelZoomFactor.setText(QCoreApplication.translate("MainWindow", u"Zoom Factor", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolDisplay), QCoreApplication.translate("MainWindow", u"Display", None))
        self.buttonFanOnOff.setText(QCoreApplication.translate("MainWindow", u"Sensor Cooling Fan Off", None))
        self.buttonCoolingOnOff.setText(QCoreApplication.translate("MainWindow", u"Sensor Cooling Off", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Sensor Temperature:", None))
        self.labelTemperature.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Set Sensor Temperature:", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolTemperature), QCoreApplication.translate("MainWindow", u"Cooling", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Focus:", None))
        self.buttonFocusL3.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.buttonFocusL2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.buttonFocusL1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonFocusR1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonFocusR2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.buttonFocusR3.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Zoom:", None))
        self.buttonZoomL3.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.buttonZoomL2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.buttonZoomL1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonZoomR1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonZoomR2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.buttonZoomR3.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Iris:", None))
        self.buttonIrisL3.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.buttonIrisL2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.buttonIrisL1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonIrisR1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonIrisR2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.buttonIrisR3.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Filter - Stepper:", None))
        self.buttonFilterL3.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.buttonFilterL2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.buttonFilterL1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonFilterR1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonFilterR2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.buttonFilterR3.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Filter - PMDC:", None))
        self.buttonSpareL3.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.buttonSpareL2.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.buttonSpareL1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.buttonSpareR1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.buttonSpareR2.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.buttonSpareR3.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolLensControl), QCoreApplication.translate("MainWindow", u"Lens Control", None))
        self.buttonMains.setText(QCoreApplication.translate("MainWindow", u"Mains", None))
        self.buttonEpiWhite.setText(QCoreApplication.translate("MainWindow", u"Epi White Light", None))
        self.buttonTransUV.setText(QCoreApplication.translate("MainWindow", u"Transmitted UV Light", None))
        self.buttonTransWhite.setText(QCoreApplication.translate("MainWindow", u"Transmitted White Light", None))
        self.buttonTransBlue.setText(QCoreApplication.translate("MainWindow", u"Transmitted Blue Light", None))
        self.buttonEpiUVA.setText(QCoreApplication.translate("MainWindow", u"Epi UVA Light", None))
        self.buttonEpiUVB.setText(QCoreApplication.translate("MainWindow", u"Epi UVB Light", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"UV Light Timer (seconds)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"UV Light Countdown (seconds):", None))
        self.labelElapsedTime.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.buttonStartStainFree.setText(QCoreApplication.translate("MainWindow", u"UV Light On", None))
        self.buttonAbortStainFree.setText(QCoreApplication.translate("MainWindow", u"Abort UV Timer", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolLightControl), QCoreApplication.translate("MainWindow", u"Illumination Control", None))
        self.buttonSaveProtocol.setText(QCoreApplication.translate("MainWindow", u"Save Protocol", None))
        self.buttonLoadProtocol.setText(QCoreApplication.translate("MainWindow", u"Load Protocol", None))
        self.cameraAdjustments.setItemText(self.cameraAdjustments.indexOf(self.toolProtocol), QCoreApplication.translate("MainWindow", u"Protocols", None))
    # retranslateUi

