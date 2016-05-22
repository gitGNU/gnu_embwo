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

try:
   import os
   import sys
   import paths
   import ui
   import config
   from PyQt5.QtCore import *
   from PyQt5.QtWidgets import *
   import gettext

except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)

"""

BWO.py - main app class

it constructs and destructs the main dialog and starts the app

"""


class BWO(object):

 def __init__(self):
   es = gettext.translation('messages', localedir='po', languages=['es'])
   es.install()
   
   print(_('initialized BWO'));
   print(_('version: '),config.version);
   self.app = QApplication(sys.argv)
   self.app.aboutToQuit.connect(self.app.deleteLater)

   self.screen = ui.Form(self.app)

 def run(self):
     self.screen.show()
   
 def __del__(self):
     del(self.screen)

 def exit(self):
     sys.exit(self.app.exec_())

#APPLICATION running!
app = BWO()

app.run()

app.exit()

