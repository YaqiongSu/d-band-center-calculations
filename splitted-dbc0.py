# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:42:45 2019
Copyright: 24th August, Yaqiong Su, Eindhoven
@author: Yaqiong Su
"""
import numpy as np
from scipy.integrate import simps
import datetime
import time
import sys

######   timing   ######
start = time.time()
print '********** d-band center from Yaqiong Su Eindhoven **********'
print 'is getting d-band center'
### current time ###
start_time = datetime.datetime.now()
print "Start time:       " + start_time.strftime('%Y.%m.%d-%H:%M:%S')   #strftime可以自定义时间的输出格式

######   read DOS file from the output of split_dos script   ######
file = 'DOS16'  # the selected atom
energy = np.array([float(l.split()[0]) for l in open(file,'rb')])   # extract energy
emin, emax = energy[0], 0.05   # integral energy range
erange = (energy[0],energy[-1])
emask = (energy >= emin) & (energy <= emax) # bool to make a mapping between energy and dos

d_up = np.array([float(l.split()[5]) for l in open(file,'rb')])   # extract d_up
d_down = np.array([float(l.split()[6]) for l in open(file,'rb')])   # extract d_down

x = energy[emask]
y1 = d_up[emask]
y2 = d_down[emask]

dbc_up   = simps(y1*x, x) / simps(y1, x)
dbc_down = simps(y2*x, x) / simps(y2, x)
dbc = []
dbc.append(dbc_up)
dbc.append(dbc_down)
print 'dbc_up(eV), dbc_down(eV)'
print dbc

##########   timing   #############
stop=time.time()
print("running time:     " + str(stop-start) + " seconds")
terminal_time = datetime.datetime.now()
print "Terminal time:    " + terminal_time.strftime('%Y.%m.%d-%H:%M:%S')   #strftime可以自定义时间的输出格式
print 'd-band center has been obtained'
print '********** d-band center from Yaqiong Su Eindhoven **********'
