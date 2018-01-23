'''
    Copyright (C) 2014-2016 ddurdle

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
import anydbm

class scheduler:
    # Settings

    ##
    ##
    def __init__(self, dbmfile):

        self.dbmfile = dbmfile
        #setup encryption password

        self.dbm = anydbm.open(dbmfile,'c')


    # instanceName
    # frequency
    # lastRun
    # folder
    # type

    # type - 0 exhaustive, 1 changes only
    def setScheduleTask(self, instanceName, frequency, folder, type):
        #key = instanceName_type_frequency_folder
        return

    # type - 0 exhaustive, 1 changes only
    def recordScheduleTask(self, job,instanceName, frequency, folder, type, runtime, status):
        #key = instanceName_type_frequency_folder
        return

    def getScheduledTask(self, job):

        try:
            return (self.dbm[job + '_instance'], self.dbm[job + '_frequency'], self.dbm[job + '_folder'], self.dbm[job + '_type'], self.dbm[job + '_runtime'], self.dbm[job + '_stauts'])
        except:
            return None

    def countScheduledTask(self):
        count = 0
        while (1):
            try:
                self.dbm[count]
                count += 1
            except:
                return count

    def saveChangeNumber(self, instanceName, changeNumber):
        self.dbm[instanceName + '_changenumber'] = changeNumber

    def getChangeNumber(self, instanceName):

        return self.dbm[instanceName + '_changenumber']
