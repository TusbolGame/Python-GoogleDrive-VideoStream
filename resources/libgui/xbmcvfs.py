'''
    Copyright (C) 2014-2017 ddurdle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''
import os

#
# The purpose of this class is to override  xbmcgui and supply equivalent subroutines when ran without KODI
#



def File(filename, type):
    return open(filename, type)

def mkdir(path):
    try:
        os.mkdir(path)
    except:
        return


def exists(path):
    if path is not None and path != '':
        return os.path.exists(path)
    else:
        return False


def delete(path):
    return




class xbmcvfs:
    # CloudService v0.3.0


    ##
    ##
    def __init__(self):
        return



