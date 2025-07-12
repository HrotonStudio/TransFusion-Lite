# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(619, 409)
        icon = QIcon()
        icon.addFile(u"assets/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 20, 621, 391))
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 619, 389))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 121, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 65, 151, 43))
        self.label_2.setFont(font)
        self.textBrowser_baiduappid = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_baiduappid.setObjectName(u"textBrowser_baiduappid")
        self.textBrowser_baiduappid.setGeometry(QRect(170, 25, 421, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        self.textBrowser_baiduappid.setFont(font1)
        self.textBrowser_baiduappid.setReadOnly(False)
        self.textBrowser_baidusecretkey = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_baidusecretkey.setObjectName(u"textBrowser_baidusecretkey")
        self.textBrowser_baidusecretkey.setGeometry(QRect(170, 70, 421, 31))
        self.textBrowser_baidusecretkey.setFont(font1)
        self.textBrowser_baidusecretkey.setReadOnly(False)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 115, 131, 43))
        self.label_4.setFont(font)
        self.textBrowser_xiaoniuapikey = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_xiaoniuapikey.setObjectName(u"textBrowser_xiaoniuapikey")
        self.textBrowser_xiaoniuapikey.setGeometry(QRect(170, 120, 421, 31))
        self.textBrowser_xiaoniuapikey.setFont(font1)
        self.textBrowser_xiaoniuapikey.setReadOnly(False)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 170, 141, 31))
        self.label_5.setFont(font)
        self.textBrowser_caiyunapikey = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_caiyunapikey.setObjectName(u"textBrowser_caiyunapikey")
        self.textBrowser_caiyunapikey.setGeometry(QRect(170, 170, 421, 31))
        self.textBrowser_caiyunapikey.setFont(font1)
        self.textBrowser_caiyunapikey.setReadOnly(False)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 220, 141, 31))
        self.label_6.setFont(font)
        self.textBrowser_deepseekapikey = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_deepseekapikey.setObjectName(u"textBrowser_deepseekapikey")
        self.textBrowser_deepseekapikey.setGeometry(QRect(170, 220, 421, 31))
        self.textBrowser_deepseekapikey.setFont(font1)
        self.textBrowser_deepseekapikey.setReadOnly(False)
        self.radioButton_enable_dsr1 = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_enable_dsr1.setObjectName(u"radioButton_enable_dsr1")
        self.radioButton_enable_dsr1.setGeometry(QRect(170, 270, 331, 21))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        self.radioButton_enable_dsr1.setFont(font2)
        self.pushButton_save = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(490, 330, 101, 41))
        self.pushButton_save.setStyleSheet(u"background-color: rgb(79, 188, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;  border: 2px groove white;\n"
"border-style: outset;")
        self.comboBox_theme = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        self.comboBox_theme.setGeometry(QRect(170, 310, 181, 22))
        self.comboBox_theme.setFont(font2)
        self.comboBox_theme.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_theme.setAutoFillBackground(False)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 305, 81, 31))
        self.label_7.setFont(font)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 0, 51, 31))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e - TransFusion-Lite", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5ea6\u7ffb\u8bd1AppID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5ea6\u7ffb\u8bd1SecretKey:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u725b\u7ffb\u8bd1APIKey:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5f69\u4e91\u7ffb\u8bd1APIKey:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DeepSeekAPIKEY:", None))
        self.radioButton_enable_dsr1.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u6df1\u5ea6\u601d\u8003 (\u7ffb\u8bd1\u8017\u65f6\u66f4\u957f)", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.comboBox_theme.setItemText(0, QCoreApplication.translate("MainWindow", u"Aqua", None))
        self.comboBox_theme.setItemText(1, QCoreApplication.translate("MainWindow", u"ConsoleStyle", None))
        self.comboBox_theme.setItemText(2, QCoreApplication.translate("MainWindow", u"MacOS", None))
        self.comboBox_theme.setItemText(3, QCoreApplication.translate("MainWindow", u"NeonButtons", None))
        self.comboBox_theme.setItemText(4, QCoreApplication.translate("MainWindow", u"Ubuntu", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"App\u4e3b\u9898\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

