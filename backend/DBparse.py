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
   import sqlite3

except ImportError as err:
   print("couldn't load module. %s" % (err))
   sys.exit(2)

class DBparser(object):
   def __init__(self):
      self.pythonSqlite = sqlite3.version
      self.sqlite = sqlite3.sqlite_version
      self.status = -1
      print("=>PySqlite Version:",self.pythonSqlite,
                                    ", sqlite version: ",self.sqlite)
   def check(self,file):
       '''try to open/Create blank file'''
       print("=>Checking Database connection...")
       try:
           self.DBconnection = sqlite3.connect('BWO.db')
                 
       except sqlite3.Error as E:
           print("Database error: ",E)
           self.status = -1
           return -1
       print("=>passed!")
       print("=>Checking Tables...")
       '''Clients table'''
       try:
           self.checkClients()
       except ValueError as Error:
           print(Error)
           self.DBconnection.close()
           self.status = -1
           return -1
       '''Jobs table'''      
       try:
           self.checkJobs()
       except ValueError as Error:
           print(Error)
           self.DBconnection.close()
           self.status = -1
           return -1 
       '''Devices table'''      
       try:
           self.checkDevices()
       except ValueError as Error:
           print(Error)
           self.DBconnection.close()
           self.status = -1
           return -1      
       self.DBconnection.close()
       self.status = 1
       print("=>passed!")
       return 1
       
   '''checking for clients table'''        
   def checkClients(self):
       '''check if table is created'''
       con = self.DBconnection.cursor()
       con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients'")
       if con.fetchone() == None:
          raise ValueError("Table clients doesn't exists!")
       '''check if table is correctly created'''
       ok = self.checkSanity('clients',con)
       if ok < 0:
          raise ValueError("EE:Table clients doesn't match the standard one!")

   '''checking for jobs table'''        
   def checkJobs(self):
       '''check if table is created'''
       con = self.DBconnection.cursor()
       con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jobs'")
       if con.fetchone() == None:
          raise ValueError("EE:Table jobs doesn't exists!")
       '''check if table is correctly created'''
       ok = self.checkSanity('jobs',con)
       if ok < 0:
          raise ValueError("EE:Table jobs doesn't match the standard one!")
          
   '''checking for devices table'''        
   def checkDevices(self):
       '''check if table is created'''
       con = self.DBconnection.cursor()
       con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='devices'")
       if con.fetchone() == None:
          raise ValueError("EE:Table devices doesn't exists!")
       '''check if table is correctly created'''
       ok = self.checkSanity('devices',con)
       if ok < 0:
          raise ValueError("EE:Table devices doesn't match the standard one!")
          
   '''create a blank database for work!'''       
   def createBlank(self,file):
       '''try to open/Create blank file'''
       print("=>Creating Database skeleton...")
       try:
           self.DBconnection = sqlite3.connect('BWO.db')
                
       except sqlite3.Error as E:
           print("EE:Database error: ",E)
           self.status = -1
           return -1
       '''try creating clients table'''
       print("=>Creating Tables...")
       try:
           self.setupClients()

       except ValueError as Error:
           print(Error)
           '''self.DBconnection.close()'''
           '''self.status = -1'''
           '''return -1'''
       '''try creating jobs table'''    
       try:
           self.setupJobs()

       except ValueError as Error:
           print(Error)
           '''self.DBconnection.close()'''
           '''self.status = -1'''
           '''return -1   '''
       '''try creating devices table'''    
       try:
           self.setupDevices()

       except ValueError as Error:
           print(Error)
           '''self.DBconnection.close()'''
           '''self.status = -1'''
           '''return -1   '''
       self.DBconnection.close()
       self.status = 1
       return 1           
   '''setting up clients table'''        
   def setupClients(self):
       
       con = self.DBconnection.cursor()
       con.execute("CREATE TABLE IF NOT EXISTS clients (id INT,client_name STRING, date DATE)")
       try:
           self.checkClients()           
       except:
           raise ValueError("EE:Table clients could not be created!")
          
   '''setting up jobs table'''        
   def setupJobs(self):
       
       con = self.DBconnection.cursor()
       con.execute("CREATE TABLE IF NOT EXISTS jobs (id INT,client_name STRING, job_date DATE, device_name STRING, description STRING)")
       try:
           self.checkJobs()           
       except:
          raise ValueError("EE:Table jobs could not be created!")   
          
   '''setting up devices table'''        
   def setupDevices(self):
       
       con = self.DBconnection.cursor()
       con.execute("CREATE TABLE IF NOT EXISTS devices (id INT,client STRING, name STRING, last_job_date DATE, OS_version STRING, hints STRING)")
       try:
           self.checkDevices()           
       except:
          raise ValueError("EE:Table devices could not be created!")           
          
   '''check sanity of every table in DB'''
   '''CHECK FOR OVERFLOW!! RAISE EXCEPTION, TO IMPROVE'''     
   def checkSanity(self,table,connection):
       clients = (('id','INT'),('client_name','STRING'),('date','DATE'))
       jobs = (('id','INT'),('client_name','STRING'),('job_date','DATE'),('device_name','STRING'),('description','STRING'))       
       devices = (('id','INT'),('client','STRING'),('name','STRING'),('last_job_date','DATE'),('OS_version','STRING'),('hints','STRING'))       
       ok = -1
       '''table clients'''
       if table == 'clients':
           i = 0
           ok = 1
           for row in connection.execute("pragma table_info('clients')").fetchall():
               '''print(row[1],row[2])'''
               '''print(clients[i][0],clients[i][1])'''
               if (row[1] != clients[i][0]) | (row[2] != clients[i][1]):
                   ok = -1
               i = i+1
       elif table == 'jobs':
           i = 0
           ok = 1
           for row in connection.execute("pragma table_info('jobs')").fetchall():
               '''print(row[1],row[2])'''
               '''print(clients[i][0],clients[i][1])'''
               if (row[1] != jobs[i][0]) | (row[2] != jobs[i][1]):
                   ok = -1
               i = i+1
       elif table == 'devices':
           i = 0
           ok = 1
           for row in connection.execute("pragma table_info('devices')").fetchall():
               '''print(row[1],row[2])'''
               '''print(clients[i][0],clients[i][1])'''
               if (row[1] != devices[i][0]) | (row[2] != devices[i][1]):
                   ok = -1
               i = i+1               
       return ok          
        