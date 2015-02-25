import sys
import os
import re
import time
from pylab import *

# timestamp format
timestamp_fmt = r'%Y-%b-%d %H:%M:%S'
# timestamp for file
file_timestamp_fmt = r'%Y-%m-%d-%H-%M-%S'
# general prefix for OpenNERO log lines (date and time with msec resolution)
log_prefix = r'(?P<date>[^\[]*)\.(?P<msec>[0-9]+) \(.\) '

# log pattern
# example
# 2014-Nov-29 16:14:52.793461 (M) [python] [experiments.stats] min: 72.4442117559, mean: 141.365512494, max: 202.472638814
dist_pattern = re.compile(log_prefix + r'\[python\] \[experiments\.stats\] min: (?P<dmin>\S+), mean: (?P<davg>\S+), max: (?P<dmax>\S+)')
ai = ["rtneat", "rtneatq", "qlearning"]

dmin, davg, dmax = [], [], []

def process_line(line):
    """
    Process a line of the log file and record the information in it in the LearningCurve
    """
    global dmin, davg, dmax
    line = line.strip().lower()
    m = dist_pattern.search(line)
    if m:
        #t = time.strptime(m.group('date'), timestamp_fmt) # time of the record
        #ms = int(m.group('msec')) / 1000000.0 # the micro-second part in seconds
        #base = time.mktime(t) + ms # seconds since the epoch
	dmax.append(float(m.group('dmax')))
        dmin.append(float(m.group('dmin')))
        davg.append(float(m.group('davg')))

def process_file(f):
    line = f.readline()
    while line:
        process_line(line.strip())
        line = f.readline()

def main():
    global dmin, davg, dmax

    # plot each dimension in a separate subplot
    for d in range(3):
        dmin, davg, dmax = [], [], []
        fname = os.getenv("HOME")+r'/.opennero/flag_'+ai[d]+".log"
        with open(fname) as f:
            process_file(f)
        dmin, davg, dmax = np.array(dmin), np.array(davg), np.array(dmax)
        print np.shape(dmin), np.shape(davg), np.shape(dmax)
        fig, ax = plt.subplots()
    	ax.set_title(ai[d])
        ax.hold(True)
	#ax.plot(dmax, label='max')
        ax.plot(dmin, label='min')
        ax.plot(davg, label='avg')
        ax.legend()
        fig.savefig(ai[d])

if __name__ == "__main__":
    main()

