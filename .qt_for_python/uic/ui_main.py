# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(737, 437)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.Main_frame = QFrame(self.centralwidget)
        self.Main_frame.setObjectName(u"Main_frame")
        self.Main_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(33, 108, 194, 255), stop:0.86828 rgba(59, 180, 160, 205));border-radius:7px;\n"
"\n"
"")
        self.Main_frame.setFrameShape(QFrame.NoFrame)
        self.Main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.Main_frame)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMinimumSize(QSize(0, 60))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setBold(True)
        self.title_bar.setFont(font)
        self.title_bar.setLayoutDirection(Qt.LeftToRight)
        self.title_bar.setAutoFillBackground(False)
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, -1, -1)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setStyleSheet(u"border:none;")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_intro = QFrame(self.frame_title)
        self.frame_intro.setObjectName(u"frame_intro")
        self.frame_intro.setLayoutDirection(Qt.LeftToRight)
        self.frame_intro.setFrameShape(QFrame.StyledPanel)
        self.frame_intro.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_intro)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 5, 0, 0)
        self.label_title = QLabel(self.frame_intro)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_title)

        self.label_time = QLabel(self.frame_intro)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(0, 0))
        self.label_time.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamily(u"Microsoft JhengHei")
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_time.setFont(font2)
        self.label_time.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_time)


        self.horizontalLayout_7.addWidget(self.frame_intro)

        self.rightButtons = QFrame(self.frame_title)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setMaximumSize(QSize(130, 16777215))
        self.rightButtons.setLayoutDirection(Qt.LeftToRight)
        self.rightButtons.setStyleSheet(u"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(235, 245, 225); border-style: solid; border-radius: 4px; }")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"images/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"images/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.closeAppBtn)


        self.horizontalLayout_7.addWidget(self.rightButtons)


        self.horizontalLayout.addWidget(self.frame_title)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame = QFrame(self.Main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.card_1 = QFrame(self.frame)
        self.card_1.setObjectName(u"card_1")
        self.card_1.setGeometry(QRect(20, 30, 541, 283))
        self.card_1.setAutoFillBackground(False)
        self.card_1.setStyleSheet(u"background-color: rgba(255, 225, 255, 10);")
        self.card_1.setFrameShape(QFrame.StyledPanel)
        self.card_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card_1)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_card_2 = QLabel(self.card_1)
        self.label_card_2.setObjectName(u"label_card_2")
        self.label_card_2.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_card_2.setFont(font3)
        self.label_card_2.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"background-color: none;\n"
"}")
        self.label_card_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_card_2)

        self.card_bg = QFrame(self.card_1)
        self.card_bg.setObjectName(u"card_bg")
        self.card_bg.setMinimumSize(QSize(0, 220))
        self.card_bg.setAutoFillBackground(False)
        self.card_bg.setStyleSheet(u"border-image : url(5.png);border : 2px")
        self.card_bg.setFrameShape(QFrame.StyledPanel)
        self.card_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card_bg)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_card_1 = QLabel(self.card_bg)
        self.label_card_1.setObjectName(u"label_card_1")
        self.label_card_1.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"News701 BT")
        font4.setPointSize(35)
        font4.setBold(False)
        font4.setKerning(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_card_1.setFont(font4)
        self.label_card_1.setStyleSheet(u"background:none;\n"
"color: rgb(173, 50, 28);")
        self.label_card_1.setText(u"First Topic")
        self.label_card_1.setTextFormat(Qt.AutoText)
        self.label_card_1.setScaledContents(False)
        self.label_card_1.setAlignment(Qt.AlignCenter)
        self.label_card_1.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_card_1)


        self.verticalLayout_3.addWidget(self.card_bg)

        self.frame_credit = QFrame(self.frame)
        self.frame_credit.setObjectName(u"frame_credit")
        self.frame_credit.setGeometry(QRect(10, 320, 521, 20))
        self.frame_credit.setMaximumSize(QSize(16777215, 20))
        self.frame_credit.setFrameShape(QFrame.StyledPanel)
        self.frame_credit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_credit)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.label_credit = QLabel(self.frame_credit)
        self.label_credit.setObjectName(u"label_credit")
        self.label_credit.setMinimumSize(QSize(0, 0))
        self.label_credit.setMaximumSize(QSize(150, 16777215))
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setItalic(True)
        self.label_credit.setFont(font5)
        self.label_credit.setStyleSheet(u"color: rgba(7, 0, 86, 120);")
        self.label_credit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_credit.setMargin(5)

        self.horizontalLayout_3.addWidget(self.label_credit)

        self.label = QLabel(self.frame_credit)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255,54,18);")

        self.horizontalLayout_3.addWidget(self.label)

        self.label_number = QLabel(self.frame)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setGeometry(QRect(560, 140, 161, 91))
        self.label_number.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamily(u"Verdana")
        font6.setPointSize(25)
        font6.setBold(False)
        self.label_number.setFont(font6)
        self.label_number.setStyleSheet(u"QLabel{\n"
"color: rgb(173, 50, 28);\n"
"background-color: none;\n"
"}")
        self.label_number.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.Main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"RANDOM CARD", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_card_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_credit.setText(QCoreApplication.translate("MainWindow", u"#v21.01  #tht5hc ", None))
        self.label.setText("")
        self.label_number.setText(QCoreApplication.translate("MainWindow", u"NUMBER", None))
    # retranslateUi

