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

"""parse.py - parse .md file info for BWO

Here will take care of the data coming from the .md file. 
Once it's in memory we can insert it to the database.

We'll be able to get data from data base to .md too

"""

try:
   import os
   import sys

except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)

class device(object):
   def __init__(self):
      self.jobsQuery = []
      self.hintsQuery = []
   
   def setDevice(self,deviceName):
      self.name = deviceName

   def addJob(self,job):
      self.jobsQuery.append(job)

   def getJob(self,index):
      return self.jobsQuery.pop(index)
   
   def addHint(self,hint):
      self.hintsQuery.append(hint)

   def getHint(self,index):
      return self.hintsQuery.pop(index)

class parsedData(object):
   def __init__(self):
      self.client = ''
      self.date = ''
      self.device = device
      self.devices = []
 

   def parseFile(self,fileOpened):
      line_before = ''
      tipo = 0

      for line in fileOpened:
         if '---' in line:
            self.client = line_before.replace("\n","")
         if '***' in line:
            self.date = line_before.replace("\n", "")
         if '#' in line:
            if '##' in line:
               if (("trabajos" in line) or ("jobs" in line)) :
                  tipo = 1
               else:
                  tipo = 2
            else:
               newDevice = device()
               name = line.lstrip('#')
               newDevice.setDevice(name.replace("\n", ""))
               self.devices.append(newDevice)
         if '+' in line:
            if tipo == 1:
               newDevice = self.devices.pop()
               name = line.lstrip('+ ')
               newDevice.addJob(name.replace("\n", ""))
               self.devices.append(newDevice)
            elif tipo == 2:
               newDevice = self.devices.pop()
               name = line.lstrip('+ ')
               newDevice.addHint(name.replace("\n", ""))
               self.devices.append(newDevice)
            else:
               continue
            
               
         line_before=line

   def showParsedData(self):

      print('cliente: ',self.client)
      print('fecha: ',self.date)

      for equipment in self.devices:
         print('equipo: ', equipment.name)
        
         print('trabajos realizados:')
         for job in equipment.jobsQuery:
           print('---> ',job)

         print('a tener en cuenta:')
         for hint in equipment.hintsQuery:
           print('---> ',hint)


