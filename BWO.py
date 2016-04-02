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

