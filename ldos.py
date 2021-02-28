#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:18:57 2021

@author: yavar001
"""




import  numpy as np
import matplotlib.pyplot as plt
from shutil import copyfile

import os
from glob import glob



files=glob("tmp.pp*")
files.sort()
i=1
###  !!!  I now row number in avg.dat
ldosdata=np.empty((0,360))
for ff in files:
    f = open("average.in", "w")
    f.write("1\n")
    f.write(str(ff)+"\n")
    f.write("1.D0\n200\n3\n1\n")
    os.system("/home/yavar001/SOURCES/q-e-qe-6.4/bin/average.x < average.in > average.out")
    copyfile("avg.dat", "avg"+str(i)+".dat")
    data=np.loadtxt("avg.dat")
    a=np.reshape(data[:,1], (1,360))
    ldosdata=np.append(ldosdata, a, axis=0)
    i=i+1
f.close()






#plt.imshow(ldosdata, vmax=0.1,interpolation="gaussian"), plt.colorbar()
