# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pygame_container = QWidget(self.centralwidget)
        self.pygame_container.setObjectName(u"pygame_container")
        self.pygame_container.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pygame_container, 0, 0, 1, 1)

        self.side = QWidget(self.centralwidget)
        self.side.setObjectName(u"side")
        self.verticalLayout = QVBoxLayout(self.side)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.side)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.scrollArea = QScrollArea(self.side)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 501, 495))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.form_w = QWidget(self.scrollAreaWidgetContents)
        self.form_w.setObjectName(u"form_w")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.form_w.sizePolicy().hasHeightForWidth())
        self.form_w.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.form_w)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.lbl_wg = QLabel(self.form_w)
        self.lbl_wg.setObjectName(u"lbl_wg")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_wg)

        self.layout_wg = QGridLayout()
        self.layout_wg.setSpacing(9)
        self.layout_wg.setObjectName(u"layout_wg")
        self.spbox_wg_gcX = QSpinBox(self.form_w)
        self.spbox_wg_gcX.setObjectName(u"spbox_wg_gcX")
        self.spbox_wg_gcX.setMinimum(1)
        self.spbox_wg_gcX.setValue(20)

        self.layout_wg.addWidget(self.spbox_wg_gcX, 1, 1, 1, 1)

        self.lbl_wg_gcX = QLabel(self.form_w)
        self.lbl_wg_gcX.setObjectName(u"lbl_wg_gcX")

        self.layout_wg.addWidget(self.lbl_wg_gcX, 1, 0, 1, 1)

        self.spbox_wg_gcY = QSpinBox(self.form_w)
        self.spbox_wg_gcY.setObjectName(u"spbox_wg_gcY")
        self.spbox_wg_gcY.setMinimum(1)
        self.spbox_wg_gcY.setValue(15)

        self.layout_wg.addWidget(self.spbox_wg_gcY, 1, 3, 1, 1)

        self.lbl_wg_csX = QLabel(self.form_w)
        self.lbl_wg_csX.setObjectName(u"lbl_wg_csX")

        self.layout_wg.addWidget(self.lbl_wg_csX, 0, 0, 1, 1)

        self.spbox_wg_csX = QSpinBox(self.form_w)
        self.spbox_wg_csX.setObjectName(u"spbox_wg_csX")
        self.spbox_wg_csX.setMinimum(1)
        self.spbox_wg_csX.setMaximum(256)
        self.spbox_wg_csX.setValue(32)

        self.layout_wg.addWidget(self.spbox_wg_csX, 0, 1, 1, 1)

        self.spbox_wg_csY = QSpinBox(self.form_w)
        self.spbox_wg_csY.setObjectName(u"spbox_wg_csY")
        self.spbox_wg_csY.setMinimum(1)
        self.spbox_wg_csY.setMaximum(256)
        self.spbox_wg_csY.setValue(32)

        self.layout_wg.addWidget(self.spbox_wg_csY, 0, 3, 1, 1)

        self.lbl_wg_csY = QLabel(self.form_w)
        self.lbl_wg_csY.setObjectName(u"lbl_wg_csY")

        self.layout_wg.addWidget(self.lbl_wg_csY, 0, 2, 1, 1)

        self.lbl_wg_gcY = QLabel(self.form_w)
        self.lbl_wg_gcY.setObjectName(u"lbl_wg_gcY")

        self.layout_wg.addWidget(self.lbl_wg_gcY, 1, 2, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.layout_wg)

        self.lbl_initspawn = QLabel(self.form_w)
        self.lbl_initspawn.setObjectName(u"lbl_initspawn")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_initspawn)

        self.spbox_initspawn = QSpinBox(self.form_w)
        self.spbox_initspawn.setObjectName(u"spbox_initspawn")
        self.spbox_initspawn.setMaximum(16384)
        self.spbox_initspawn.setValue(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spbox_initspawn)

        self.layout_w_confirm = QHBoxLayout()
        self.layout_w_confirm.setObjectName(u"layout_w_confirm")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_w_confirm.addItem(self.horizontalSpacer)

        self.btn_confirm = QPushButton(self.form_w)
        self.btn_confirm.setObjectName(u"btn_confirm")

        self.layout_w_confirm.addWidget(self.btn_confirm)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.layout_w_confirm)


        self.verticalLayout_2.addWidget(self.form_w)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.form_c = QWidget(self.scrollAreaWidgetContents)
        self.form_c.setObjectName(u"form_c")
        sizePolicy1.setHeightForWidth(self.form_c.sizePolicy().hasHeightForWidth())
        self.form_c.setSizePolicy(sizePolicy1)
        self.formLayout_2 = QFormLayout(self.form_c)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(12)
        self.lbl_world = QLabel(self.form_c)
        self.lbl_world.setObjectName(u"lbl_world")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_world)

        self.layout_world = QHBoxLayout()
        self.layout_world.setObjectName(u"layout_world")
        self.btn_world_start = QPushButton(self.form_c)
        self.btn_world_start.setObjectName(u"btn_world_start")

        self.layout_world.addWidget(self.btn_world_start)

        self.btn_world_stop = QPushButton(self.form_c)
        self.btn_world_stop.setObjectName(u"btn_world_stop")

        self.layout_world.addWidget(self.btn_world_stop)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.layout_world)

        self.lbl_progression = QLabel(self.form_c)
        self.lbl_progression.setObjectName(u"lbl_progression")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_progression)

        self.view_progression = QLabel(self.form_c)
        self.view_progression.setObjectName(u"view_progression")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.view_progression)

        self.lbl_entities = QLabel(self.form_c)
        self.lbl_entities.setObjectName(u"lbl_entities")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_entities)

        self.view_entities = QLabel(self.form_c)
        self.view_entities.setObjectName(u"view_entities")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.view_entities)

        self.btn_spawn = QPushButton(self.form_c)
        self.btn_spawn.setObjectName(u"btn_spawn")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.btn_spawn)

        self.layout_spawn = QHBoxLayout()
        self.layout_spawn.setObjectName(u"layout_spawn")
        self.spbox_spawn_count = QSpinBox(self.form_c)
        self.spbox_spawn_count.setObjectName(u"spbox_spawn_count")

        self.layout_spawn.addWidget(self.spbox_spawn_count)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.layout_spawn)


        self.verticalLayout_2.addWidget(self.form_c)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.side, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1066, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_wg.setText(QCoreApplication.translate("MainWindow", u"world grid", None))
        self.lbl_wg_gcX.setText(QCoreApplication.translate("MainWindow", u"grid count X", None))
        self.lbl_wg_csX.setText(QCoreApplication.translate("MainWindow", u"cell size X", None))
        self.lbl_wg_csY.setText(QCoreApplication.translate("MainWindow", u"cell size Y", None))
        self.lbl_wg_gcY.setText(QCoreApplication.translate("MainWindow", u"grid count Y", None))
        self.lbl_initspawn.setText(QCoreApplication.translate("MainWindow", u"initial spawns", None))
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
        self.lbl_world.setText(QCoreApplication.translate("MainWindow", u"control", None))
        self.btn_world_start.setText(QCoreApplication.translate("MainWindow", u"start age", None))
        self.btn_world_stop.setText(QCoreApplication.translate("MainWindow", u"stop age", None))
        self.lbl_progression.setText(QCoreApplication.translate("MainWindow", u"progression", None))
        self.view_progression.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.lbl_entities.setText(QCoreApplication.translate("MainWindow", u"entities", None))
        self.view_entities.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.btn_spawn.setText(QCoreApplication.translate("MainWindow", u"spawn", None))
    # retranslateUi

