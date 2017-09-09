#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import config2xyz 
import xyz_lib
import os
import matplotlib.pyplot as plt

def box_count(location,counter,d):
    mask = (location[:,0] > counter) & (location[:,0] < counter+d)
    counted = np.sum(mask)
    return counted
    
def ten_percent_liquid(particle_count):
   ma = np.max(particle_count)
   mi = np.min(particle_count)
   print(str(ma) + ' ' + str(mi))
   return ((mi) > (0.1*ma))

folder_root = '/home/pc494/DL_MESO/dl_meso/post_grad/folders/'
folders = os.listdir(folder_root)
## override this to investigate a single folder
folders = ['60_-24']

half_box_size = 20
d = 0.5
A = 25
counters = np.linspace(-half_box_size,half_box_size-d,num=half_box_size*2/d)
is_it_a_liquid = []
for folder in folders:
    files = os.listdir(folder_root+folder)
    for file in files:
            Atoms = xyz_lib.Atoms
            Alpha = xyz_lib.Atoms.read(Atoms,folder_root+folder+'/'+file)
            location = Alpha.xyz

            particle_count = np.zeros_like(counters)

            for count in counters:
                index = int(np.where(count==counters)[0])
                particle_count[index] = box_count(location,count,d)
            #frame_result = ten_percent_liquid(particle_count)
            #is_it_a_liquid.append(frame_result)

            plt.figure()
            plt.plot(counters,particle_count)
            plt.xlabel('x')
            plt.ylabel('Dproxy')
            save_string = file[:-4]+'.png' 
            plt.title(save_string)
            plt.savefig(save_string)
#print((is_it_a_liquid))

