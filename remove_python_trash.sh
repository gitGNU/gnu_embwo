#!bin/bash

#
#  Small python binaries remover for pushing clean code to repository
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

find . -name "*.pyc" -exec git rm -f "{}" \;
find . -name "*.py.bak" -exec git rm -f "{}" \;
find . -name "__pycache__" -exec rm -r "{}" \;
