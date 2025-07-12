# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 493)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei"])
        font1.setPointSize(11)
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.combobox_tramslate_method = QComboBox(self.centralwidget)
        self.combobox_tramslate_method.addItem("")
        self.combobox_tramslate_method.addItem("")
        self.combobox_tramslate_method.addItem("")
        self.combobox_tramslate_method.addItem("")
        self.combobox_tramslate_method.addItem("")
        self.combobox_tramslate_method.setObjectName(u"combobox_tramslate_method")

        self.horizontalLayout_3.addWidget(self.combobox_tramslate_method)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.textBrowser_input = QTextBrowser(self.centralwidget)
        self.textBrowser_input.setObjectName(u"textBrowser_input")
        self.textBrowser_input.setReadOnly(False)

        self.verticalLayout.addWidget(self.textBrowser_input)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.textBrowser_output = QTextBrowser(self.centralwidget)
        self.textBrowser_output.setObjectName(u"textBrowser_output")
        self.textBrowser_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.textBrowser_output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_baidu = QRadioButton(self.centralwidget)
        self.radioButton_baidu.setObjectName(u"radioButton_baidu")
        self.radioButton_baidu.setFont(font1)
        self.radioButton_baidu.setCheckable(True)
        self.radioButton_baidu.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_baidu)

        self.radioButton_xiaoniu = QRadioButton(self.centralwidget)
        self.radioButton_xiaoniu.setObjectName(u"radioButton_xiaoniu")
        self.radioButton_xiaoniu.setFont(font1)

        self.horizontalLayout.addWidget(self.radioButton_xiaoniu)

        self.radioButton_caiyun = QRadioButton(self.centralwidget)
        self.radioButton_caiyun.setObjectName(u"radioButton_caiyun")
        self.radioButton_caiyun.setFont(font1)

        self.horizontalLayout.addWidget(self.radioButton_caiyun)

        self.radioButton_deepseek = QRadioButton(self.centralwidget)
        self.radioButton_deepseek.setObjectName(u"radioButton_deepseek")
        self.radioButton_deepseek.setFont(font1)

        self.horizontalLayout.addWidget(self.radioButton_deepseek)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_translate = QPushButton(self.centralwidget)
        self.pushButton_translate.setObjectName(u"pushButton_translate")
        font3 = QFont()
        font3.setFamilies([u"Microsoft JhengHei"])
        font3.setPointSize(12)
        self.pushButton_translate.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButton_translate)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 540, 23))
        self.menuabout = QMenu(self.menuBar)
        self.menuabout.setObjectName(u"menuabout")
        self.menuabout.setStyleSheet(u"font: 25 10pt \"Microsoft JhengHei UI Light\";")
        self.menuoptions = QMenu(self.menuBar)
        self.menuoptions.setObjectName(u"menuoptions")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuoptions.menuAction())
        self.menuBar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1\u5668", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1\u65b9\u5f0f\uff1a", None))
        self.combobox_tramslate_method.setItemText(0, QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u68c0\u6d4b\u8bd1\u4e2d", None))
        self.combobox_tramslate_method.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u8bd1\u82f1", None))
        self.combobox_tramslate_method.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e2d\u8bd1\u65e5", None))
        self.combobox_tramslate_method.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d\u8bd1\u6cd5", None))
        self.combobox_tramslate_method.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e2d\u8bd1\u4fc4", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u5b57:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u72b6\u6001\u7801:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1\u7ed3\u679c\uff1a", None))
        self.radioButton_baidu.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5ea6\u7ffb\u8bd1", None))
        self.radioButton_xiaoniu.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u725b\u7ffb\u8bd1", None))
        self.radioButton_caiyun.setText(QCoreApplication.translate("MainWindow", u"\u5f69\u4e91\u7ffb\u8bd1", None))
        self.radioButton_deepseek.setText(QCoreApplication.translate("MainWindow", u"DeepSeek\u7ffb\u8bd1", None))
        self.pushButton_translate.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menuoptions.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

