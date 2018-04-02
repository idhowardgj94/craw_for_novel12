#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program centers a window
on the screen.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from costomWidget.buttonForSearchPath import searchButton
from craw.craw import craw
import threading
class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class applicationGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(800, 600)
        self.center()
        self.layout = QGridLayout(self)
        self.setTopic()
        self.setForm()
        self.setTextEdit()
        self.setWindowTitle('craw practice by Howard Chang')
        # self.setLayout(self.layout);
        #

        self.show()
    def onUpdateText(self, text):
        cursor = self.editor.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.editor.setTextCursor(cursor)
        self.editor.ensureCursorVisible()
    def setTextEdit(self):
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("log....")
        self.editor.readOnly = True
        self.layout.addWidget(self.editor, 2, 0, 2,2)
        # 改寫stdout的副程式成Stream
        sys.stdout = Stream(newText=self.onUpdateText)

    def setForm(self):
        formGroupBox = QGroupBox("action")
        layout = QFormLayout()
        self.url=QLineEdit()
        layout.addRow(QLabel("url(full, only novel112): "), self.url);
        self.fileName=QLineEdit()
        layout.addRow(QLabel("file Name: "), self.fileName);
        self.path = searchButton(self, 'browse')
        layout.addRow(QLabel("store path: "), self.path)
        confirm = QPushButton("start Craw!")
        confirm.clicked.connect(self.handleConfirm)
        layout.addRow(confirm)
        formGroupBox.setLayout(layout)
        self.layout.addWidget(formGroupBox, 1,0)
    def handleConfirm(self):
        checkNull = [self.url.text(), self.fileName.text(), self.path.line.text()]
        isConfirm = all(val for val in checkNull)
        if(not isConfirm):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("please check your config form\n every form need to be written");
            msg.setWindowTitle("warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(self.handleMessage)
            retval = msg.exec_()
        else:
            self.timer_evt = threading.Event()
            threading.Thread(target=self.crawThread, name="_proc").start()

    def crawThread(self):
        crawObject = craw(self.url.text())
        crawObject.grabIndex()
        crawObject.grabFromChapter()
        if ".pub" in self.fileName.text():
            save = self.fileName.text()
        else:
            save = self.fileName.text() + ".epub"
        crawObject.outputToEpub(self.path.line.text(), save)
    def handleMessage(self, i):
        print(i.text())

    def setTopic(self):
        topic = QLabel();
        topic.setPixmap(QPixmap("./assets/img/topic.png"))
        hlayout= QHBoxLayout()
        hlayout.addWidget(topic, stretch=1, alignment=Qt.AlignHCenter);
        self.layout.addLayout(hlayout, 0,0)
        self.layout.setAlignment(Qt.AlignTop)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = applicationGUI()
    sys.exit(app.exec_())
