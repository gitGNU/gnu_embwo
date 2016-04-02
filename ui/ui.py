#! /usr/bin/env python

#
#  DDAA's Eleanor Margaret Burbidge Work Organizer  
#
#  Copyright 2016 by it's authors. 
#
#  Some rights reserved. See COPYING, AUTHORS.
#  This file may be used under the terms of the GNU General Public
#  License version 3.0 as published by the Free Software Foundation
#  and appearing in the file COPYING included in the packaging of
#  this file.
#
#  This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
#  WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#

"""ui.py - user interface for BWO

Basic frame with file input
"""


try:
   import sys
   import backend
   import outputRedirector
   import config
   from PyQt5.QtCore import *
   from PyQt5.QtWidgets import *
   from PyQt5.QtGui import QIcon,QPixmap
   from PyQt5.QtGui import QTextCursor
   
except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)
 
class Form(QWidget):
    #custom signals
    DBstatusChange = pyqtSignal(int)
    def __init__(self, application,parent=None):
        self.application = application
        super(Form, self).__init__(parent)
 
        nameLabel = QLabel(_('.md file:'))
        DBlabel = QLabel(_('sqlite database:'))
        voidLabel = QLabel("")
        
        self.DBstatus = QLabel("")
        self.DBstatus.setPixmap(QPixmap("art/grey.png"))
        self.DBstatus.setScaledContents(False)
        
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton(_('Submit'))
        self.checkButton = QPushButton(_('Check'))
        self.setupButton = QPushButton(_('Setup'))        
        
        self.consoleOutput = QTextEdit()
        self.consoleOutput.setReadOnly(True)
 
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
         
        buttonLayout2 = QVBoxLayout()
        buttonLayout2.addWidget(voidLabel)    
        buttonLayout2.addWidget(self.submitButton)   
        
        buttonLayout3 = QVBoxLayout()
        buttonLayout3.addWidget(DBlabel)
        buttonLayout3.addWidget(self.DBstatus)
        
        buttonLayout4 = QVBoxLayout()
        buttonLayout4.addWidget(self.setupButton)    
        buttonLayout4.addWidget(self.checkButton) 
        
        bottomLayout = QVBoxLayout()
        bottomLayout.addWidget(self.consoleOutput)
        '''buttons connections'''
        self.submitButton.clicked.connect(self.submitContact)
        self.checkButton.clicked.connect(self.checkDB)
        self.setupButton.clicked.connect(self.setupDB)
 
        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)        
        mainLayout.addLayout(buttonLayout2, 0, 2)
        mainLayout.addLayout(buttonLayout3, 0, 3)
        mainLayout.addLayout(buttonLayout4, 0, 4)        
        mainLayout.addLayout(bottomLayout, 1, 1,1,4)
        mainLayout.setColumnMinimumWidth(2,40)
        
        self.setLayout(mainLayout)
        title = "BWO %s %s" % (config.version,config.status)
        self.setWindowTitle(title)
        #set geometry
        self.setGeometry(400, 300, 450, 100)
        #set window icon
        self.setWindowIcon(QIcon("art/icon.png")) 

        #output redirector initializer
        self._stdout = sys.stdout
        sys.stdout = outputRedirector.outputRedirector(textWritten=self.outputMessage)
        
        #backend initialization
        self.backend = backend.bwoBackend()
        #custom signals
        self.DBstatusChange.connect(self.changeDBstatus)
        #initialization
        self.initialization()
        
    def __del__(self):
        # Restore sys.stdout
        sys.stdout = self._stdout
 
    def submitContact(self):
        fileName = self.nameLine.text()

        if self.backend.openFile(fileName):
           ret = self.backend.fieldParse()
           self.backend.closeFile()
           #bad .md file
           if (ret != 0):
               QMessageBox.information(self, "Error!",
                                    ".md file bad formatted or invalid!")
               return
           self.backend.showParsedData()
           QMessageBox.information(self, "Success!",
                                    "File correctly parsed")
        else:
           QMessageBox.information(self, "Error!",
                                    "File not found!")
    def checkDB(self):
        self.DBstatusChange.emit(0)
        print("Checking Database status...")
        status = self.backend.checkDB()
        if status > 0:
            print("OK!!")
        else:
            print("some errors encountered")
        self.DBstatusChange.emit(status)
        
    def setupDB(self):
        if self.backend.DB.status != 1:
           print("Setting up database...")
           self.DBstatusChange.emit(0)
           status = self.backend.setupDB()
           self.DBstatusChange.emit(status)
           if status > 0:
               print("OK!!")
           else:
               print("some errors encountered")
        else:
           print("Database is already ok!")
        
    def outputMessage(self,text):
        cursor = self.consoleOutput.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.consoleOutput.setTextCursor(cursor)
        self.consoleOutput.ensureCursorVisible()
    
    def changeDBstatus(self,status):
        if status > 0:
            self.DBstatus.setPixmap(QPixmap("art/green.png"))
        elif status < 0:
            self.DBstatus.setPixmap(QPixmap("art/red.png"))
        else:
            self.DBstatus.setPixmap(QPixmap("art/grey.png"))
    '''ui initialization function'''        
    def initialization(self):
        self.checkDB()


