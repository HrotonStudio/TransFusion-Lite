# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar, QSizePolicy,
    QWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(568, 341)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 40, 221, 51))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 80, 111, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 220, 150, 31))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font2.setPointSize(14)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(73, 74, 73);")
        
        # 添加进度条 - 放在窗口底部，无边框，绿色，不显示文本
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 335, 568, 6))  # 放在窗口底部
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)  # 不显示进度文本
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                      u"    border: none;\n"  # 无边框
                                      u"    background-color: transparent;\n"  # 背景透明
                                      u"}\n"
                                      u"QProgressBar::chunk {\n"
                                      u"    background-color: #2ecc71;\n"  # 绿色进度条
                                      u"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 291, 291))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font3.setPointSize(11)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-image: url(./assets/icon.png);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 310, 191, 31))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 150, 211, 31))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        self.label_6.setFont(font4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TransFusion-Lite", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AppVersion 1.3.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u4e2d...", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00a9\ufe0f HrotonStudio \u4fdd\u7559\u6240\u6709\u6743\u5229", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u6b3e\u805a\u5408\u4e86\u591a\u79cd\u7ffb\u8bd1\u5f15\u64ce\u7684\u7ffb\u8bd1\u5668", None))
    # retranslateUi