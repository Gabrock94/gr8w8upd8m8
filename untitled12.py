#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:31:40 2023

@author: giulio
"""

import pandas as pd
import matplotlib.pyplot as plt


from matplotlib.animation import FuncAnimation# update the frames based on the parameter i
import numpy as np


df = pd.read_csv('/home/giulio/Desktop/output16806059100779474.csv')
print(pd.Series(np.diff(df.time)).describe())
pd.Series(np.diff(df.time)).hist()

# we will need the fig object later
fig = plt.figure()# plot our original data
tr = plt.scatter(0.1, 0.1, s = df['top_right'][0]*100, color='red')# create a line to update
br = plt.scatter(0.1, -0.1, s = df['bottom_right'][0]*100, color='red')# create a line to update
tl = plt.scatter(-0.1, 0.1, s = df['top_left'][0]*100, color='red')# create a line to update
bl = plt.scatter(-0.1, -0.1, s = df['bottom_left'][0]*100, color='red')# create a line to update

plt.xlim(-0.2, 0.2)
plt.ylim(-0.2, 0.2)

def animate(i):
    print(i)
    # set the title to indicate the iteration
    plt.title(f'Gradient Descent step {i}')
    
    # change the data for the y axis points of the line
    tr.set_sizes([ df['top_right'][i]*100])
    br.set_sizes([df['bottom_right'][i]*100])
    tl.set_sizes([df['top_left'][i]*100])
    bl.set_sizes([df['bottom_left'][i]*100])
    return(tr)

animation = FuncAnimation(fig, animate, frames=len(df), interval=1)

# 'top_right':    self.calc_mass(b2i(data[0:2]), TOP_RIGHT),
# 'bottom_right': self.calc_mass(b2i(data[2:4]), BOTTOM_RIGHT),
# 'top_left':     self.calc_mass(b2i(data[4:6]), TOP_LEFT),
# 'bottom_left':  self.calc_mass(b2i(data[6:8]), BOTTOM_LEFT),df[]