import sys
import os
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDir, Qt, QPointF, QPoint

class searchButton(QGridLayout):
    def __init__(self, parent, text="browse"):
        super().__init__()
        self.parent = parent
        selectFile = self
        self.button=QPushButton(text)
        self.line = QLineEdit()
        selectFile.addWidget(self.button, 0,0)
        selectFile.addWidget(self.line, 0,1)
        self.button.clicked.connect(self.handleClickedEvent)
    def handleClickedEvent(self):
        #設定dialog
        options=QFileDialog.Options()
        # 下面那句等同於 options = options|QFILE....，是or運算
        # options type 是一個使用or做運算的flag
        # options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self.parent,"select directory", os.getcwd(), options=options)
        if directory:
            self.line.setText(directory)
