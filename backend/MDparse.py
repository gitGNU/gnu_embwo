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
      #no client or date, bad .md file!
      if self.client == '' or self.date == '':
          return -1
      #correct    
      else:
          return 0
               

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


