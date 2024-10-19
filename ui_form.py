# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(643, 566)
        Widget.setStyleSheet(u"background-color: rgb(255, 248, 232);")
        self.head_center = QPushButton(Widget)
        self.head_center.setObjectName(u"head_center")
        self.head_center.setGeometry(QRect(370, 40, 101, 41))
        self.head_center.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.head_nod = QPushButton(Widget)
        self.head_nod.setObjectName(u"head_nod")
        self.head_nod.setGeometry(QRect(490, 40, 101, 41))
        self.head_nod.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.head_shake = QPushButton(Widget)
        self.head_shake.setObjectName(u"head_shake")
        self.head_shake.setGeometry(QRect(370, 100, 101, 41))
        self.head_shake.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.head_roll = QPushButton(Widget)
        self.head_roll.setObjectName(u"head_roll")
        self.head_roll.setGeometry(QRect(490, 100, 101, 41))
        self.head_roll.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(340, 20, 281, 141))
        self.listView.setStyleSheet(u"background-color: rgb(103, 70, 54);")
        self.listView_2 = QListView(Widget)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(340, 180, 281, 151))
        self.listView_2.setStyleSheet(u"background-color: rgb(177, 148, 112);")
        self.listView_4 = QListView(Widget)
        self.listView_4.setObjectName(u"listView_4")
        self.listView_4.setGeometry(QRect(20, 20, 281, 441))
        self.listView_4.setStyleSheet(u"background-color: rgb(103, 70, 54);")
        self.eye_blink = QPushButton(Widget)
        self.eye_blink.setObjectName(u"eye_blink")
        self.eye_blink.setGeometry(QRect(50, 270, 101, 41))
        self.eye_blink.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.eye_sad = QPushButton(Widget)
        self.eye_sad.setObjectName(u"eye_sad")
        self.eye_sad.setGeometry(QRect(170, 270, 101, 41))
        self.eye_sad.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.eye_surprise = QPushButton(Widget)
        self.eye_surprise.setObjectName(u"eye_surprise")
        self.eye_surprise.setGeometry(QRect(170, 330, 101, 41))
        self.eye_surprise.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.eye_anger = QPushButton(Widget)
        self.eye_anger.setObjectName(u"eye_anger")
        self.eye_anger.setGeometry(QRect(50, 330, 101, 41))
        self.eye_anger.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.eye_right = QPushButton(Widget)
        self.eye_right.setObjectName(u"eye_right")
        self.eye_right.setGeometry(QRect(50, 390, 101, 41))
        self.eye_right.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.eye_left = QPushButton(Widget)
        self.eye_left.setObjectName(u"eye_left")
        self.eye_left.setGeometry(QRect(170, 390, 101, 41))
        self.eye_left.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(340, 350, 281, 111))
        self.textEdit.setStyleSheet(u"background-color: rgb(160, 147, 125);")
        self.listView_3 = QListView(Widget)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(50, 50, 211, 192))
        self.listView_3.setStyleSheet(u"border-image: url(\"images/robot.png\");\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton_11 = QPushButton(Widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(110, 480, 101, 31))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_12 = QPushButton(Widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(320, 480, 101, 31))
        self.pushButton_12.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 490, 61, 21))
        self.label.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 490, 71, 21))
        self.label_2.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.open = QPushButton(Widget)
        self.open.setObjectName(u"open")
        self.open.setGeometry(QRect(460, 480, 61, 31))
        self.open.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.close = QPushButton(Widget)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(560, 480, 61, 31))
        self.close.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.github = QPushButton(Widget)
        self.github.setObjectName(u"github")
        self.github.setGeometry(QRect(520, 520, 101, 31))
        self.github.setStyleSheet(u"background-color: rgb(247, 238, 211);\n"
"font: 12pt \"Modern No. 20\";\n"
"color: rgb(0, 0, 0);")
        self.listView.raise_()
        self.head_center.raise_()
        self.head_nod.raise_()
        self.head_shake.raise_()
        self.head_roll.raise_()
        self.listView_2.raise_()
        self.listView_4.raise_()
        self.eye_blink.raise_()
        self.eye_sad.raise_()
        self.eye_surprise.raise_()
        self.eye_anger.raise_()
        self.eye_right.raise_()
        self.eye_left.raise_()
        self.textEdit.raise_()
        self.listView_3.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.open.raise_()
        self.close.raise_()
        self.github.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.head_center.setText(QCoreApplication.translate("Widget", u"head_center", None))
        self.head_nod.setText(QCoreApplication.translate("Widget", u"head_nod", None))
        self.head_shake.setText(QCoreApplication.translate("Widget", u"head_shake", None))
        self.head_roll.setText(QCoreApplication.translate("Widget", u"head_roll", None))
        self.eye_blink.setText(QCoreApplication.translate("Widget", u"eye_blink", None))
        self.eye_sad.setText(QCoreApplication.translate("Widget", u"eye_sad", None))
        self.eye_surprise.setText(QCoreApplication.translate("Widget", u"eye_surprise", None))
        self.eye_anger.setText(QCoreApplication.translate("Widget", u"eye_anger", None))
        self.eye_right.setText(QCoreApplication.translate("Widget", u"eye_right", None))
        self.eye_left.setText(QCoreApplication.translate("Widget", u"eye_left", None))
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"eye_sad", None))
        self.pushButton_12.setText(QCoreApplication.translate("Widget", u"eye_sad", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u4e32\u53e3\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
        self.open.setText(QCoreApplication.translate("Widget", u"open", None))
        self.close.setText(QCoreApplication.translate("Widget", u"close", None))
        self.github.setText(QCoreApplication.translate("Widget", u"Github", None))
    # retranslateUi

