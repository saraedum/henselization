# -*- coding: utf-8 -*-

#*****************************************************************************
#       Copyright (C) 2016 Julian Rüth <julian.rueth@fsfe.org>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

# TODO: This should be an actual monkey patch and not be part of the henselization package proper
class Fields:
    class ElementMethods:
        def is_squarefree(self):
            return True
