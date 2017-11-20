#
#  csv_plot.py
#  
#  Copyright (C) 2017, Federal University of Santa Catarina
#  
#  This file is part of FloripaSat-GRS.
#
#  FloripaSat-GRS is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-GRS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-GRS; if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino"
__copyright__   = "Copyright (C) 2017, Federal University of Santa Catarina"
__credits__     = ["Gabriel Mariano Marcelino"]
__license__     = "GPL3"
__version__     = "1.0-dev"
__maintainer__  = "Gabriel Mariano Marcelino"
__email__       = "gabriel.mm8@gmail.com"
__status__      = "Prototype"


import csv
import pylab
import datetime

def plot_data(x, y, y_label="Data", c_title="Time x Data", con_points="1", best_curve="0", file_name=""):
    x_label = "Time [sec]"
    
    # Cubic Linear Regression
    if best_curve == "1":
        fit = pylab.polyfit(x, y, 3)
        fit_fn = pylab.poly1d(fit)
        pylab.plot(x, fit_fn(x), '-g', label='Best curve')
    
    if con_points == "1":
        if best_curve == "1":
            pylab.plot(x, y, '-bo', label='Measures')
        else:
            pylab.plot(x, y, '-bo')
    else:
        if best_curve == "1":
            pylab.plot(x, y, 'bo', label='Measures')
        else:
            pylab.plot(x, y, 'bo')
    
    pylab.title(c_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    if best_curve == "1":
        pylab.legend(loc='best')
    #pylab.axis([0, x[-1], min(y)*0.999, max(y)*1.001])
    if len(file_name) > 0:
        pylab.savefig(file_name, bbox_inches='tight', dpi=600, transparent=True)
    pylab.show()


def main(args):
    if len(args) <= 2 or args[2] == '--help':
        print "Usage:"
        print "\t- 1st argument must be the CSV file"
        print "\t- 2nd argument must be the column to display the data"
        print "\t- 3rd argument (OPTIONAL) is the axis y label"
        print "\t- 4th argument (OPTIONAL) is the plot title"
        print "\t- 5th argument (OPTIONAL) is the connect points flag (True/False)"
        print "\t- 6th argument (OPTIONAL) is the plot best curve flag (True/False)"
        print "\t- 7th argument (OPTIONAL) is the name of the pdf file to save the plot"
        
        return 0
    
    column = list()
    time_sec = list()
    with open(args[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            for row in reader:
                if len(row) > int(args[2]):
                    column.append(float(row[int(args[2])]))
                    time_sec.append(datetime.datetime(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])))
        except:
            pass
    
    initial_time_sec = time_sec[0]
    i = 0
    for i in range(len(time_sec)):
        time_sec[i] = (time_sec[i] - initial_time_sec).seconds
    
    if len(args) == 4:
        plot_data(time_sec, column, args[3])
    elif len(args) == 5:
        plot_data(time_sec, column, args[3], args[4])
    elif len(args) == 6:
        plot_data(time_sec, column, args[3], args[4], args[5])
    elif len(args) == 7:
        plot_data(time_sec, column, args[3], args[4], args[5], args[6])
    elif len(args) == 8:
        plot_data(time_sec, column, args[3], args[4], args[5], args[6], args[7])
    else:
        plot_data(time_sec, column)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))