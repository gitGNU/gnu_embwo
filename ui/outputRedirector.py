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

"""outputRedirector.py - messages redirector for BWO

Basic redirector to show console output to the text edit of the main form
"""


try:
   from PyQt5.QtCore import *
   import sys
except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)
 
class outputRedirector(QObject):
    textWritten = pyqtSignal(str)
    
    def write(self, text):
        self.textWritten.emit(str(text))
    def flush(self):
        pass