#! /usr/bin/env python
#
#    This file is part of 'Eleanor Margaret Burbidge Work Organizer' .
#
#    'Eleanor Margaret Burbidge Work Organizer' is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    'Eleanor Margaret Burbidge Work Organizer' is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

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