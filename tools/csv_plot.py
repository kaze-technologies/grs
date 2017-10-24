#
#  csv_plot.py
#  
#  Copyright (C) 2017, Gabriel Mariano Marcelino <gabriel.mm8@gmail.com>
#  
#  This file is part of FloripaSat-Packet-Analyzer.
#
#  FloripaSat-Packet-Analyzer is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-Packet-Analyzer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-Packet-Analyzer;
#  if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino"
__copyright__   = "Copyright (C) 2017, Gabriel Mariano Marcelino"
__credits__     = ["Gabriel Mariano Marcelino"]
__license__     = "GPL3"
__version__     = "1.0"
__maintainer__  = "Gabriel Mariano Marcelino"
__email__       = "gabriel.mm8@gmail.com"
__status__      = "Prototype"


import csv
import pylab

def plot_data(x, y, y_label="Data", c_title="Time x Data", save=False):
    x_label = "Time [sec]"
    
    # Linear Regression
    #fit = pylab.polyfit(x, y, 3)
    #fit_fn = pylab.poly1d(fit)
    #pylab.plot(x, fit_fn(x), '-g', label='Best curve')
    
    pylab.plot(x, y, '-bo')#, label='Measures')
    pylab.title(c_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    #pylab.legend(loc='best')
    #pylab.axis([0, x[-1], min(y)*0.999, max(y)*1.001])
    if save:
        pylab.savefig('plot.pdf', bbox_inches='tight', dpi=600, transparent=True)
    pylab.show()


def main(args):
    if len(args) <= 2 or args[2] == '--help':
        print "Usage:"
        print "\t- First argument must be the CSV file"
        print "\t- Second argument must be the column to display the data"
        print "\t- Third argument (OPTIONAL) can be the axis y label"
        print "\t- Fourth argument (OPTIONAL) can be the plot title"
        print "\t- Fifth argument (OPTIONAL) can be True or False (Save or not the plot)"
        
        return 0
    
    column = list()
    time_sec = list()
    with open(args[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            for row in reader:
                if len(row) > (int(args[2]) + 1):
                    column.append(float(row[int(args[2])]))
                    time_sec.append((int(row[3])*3600) + (int(row[4])*60) + (int(row[5])))
        except:
            pass
    
    initial_time_sec = time_sec[0]
    i = 0
    for i in range(len(time_sec)):
        time_sec[i] = time_sec[i] - initial_time_sec
    
    if len(args) == 4:
        plot_data(time_sec, column, args[3])
    elif len(args) == 5:
        plot_data(time_sec, column, args[3], args[4])
    elif len(args) == 6:
        plot_data(time_sec, column, args[3], args[4], bool(args[5]))
    else:
        plot_data(time_sec, column)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
