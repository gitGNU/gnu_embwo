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

"""backend.py - Backend for BWO

this class will take care of file and data base process
"""


try:
   import os
   import MDparse
   import DBparse

except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)

class bwoBackend(object):
 def __init__(self):
   '''print('backend initialized')'''
   self.DB = DBparse.DBparser()
   self.data = MDparse.parsedData()

 def openFile(self,fileName):
   try:
      self.file = open(fileName)
   except IOError:
      return False
   return True

 def bruteParse(self):
   for line in self.file:
      print(line)

 def fieldParse(self):
   ret = self.data.parseFile(self.file)
   return ret
 
 def showParsedData(self):
   self.data.showParsedData()

 def closeFile(self):
   self.file.close()

 def cleanLine(self,text):
   text.rstrip('\r\n ')

 def cleanTitle(self,text):
   text.lstrip('#')
 #data base methods
 '''check if database exists'''
 def checkDB(self):
     status = self.DB.check('BWO.db')
     return status   
     
 '''create the basis of database''' 
 def setupDB(self):
     status = self.DB.createBlank('BWO.db')
     return status



