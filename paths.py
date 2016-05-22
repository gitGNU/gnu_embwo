#!/usr/bin/env python

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


"""paths.py - Path setup for BWO

Import this at the start of your program to augment the python library path.
"""


import os
import sys

progname = sys.argv[0]
progdir = os.path.dirname(progname)
sys.path.insert(0, os.path.normpath(os.path.join(progdir,'ui')))
sys.path.insert(0, os.path.normpath(os.path.join(progdir,'backend')))
sys.path.insert(0, os.path.normpath(os.path.join(progdir,'config')))
sys.path.insert(0, os.path.normpath(os.path.join(progdir,'art')))
sys.path.insert(0, progdir)
