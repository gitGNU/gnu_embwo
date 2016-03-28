#!/usr/bin/env python

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
