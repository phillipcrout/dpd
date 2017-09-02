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
    
def density_finding(particle_count,A,d):
    main_value = np.max(particle_count)/2
    high_counters = particle_count[particle_count>main_value]
    counted = np.sum(high_counters)
    volume_considered = len(high_counters)*d*A
    density = counted/volume_considered
    return density



folder = '/home/pc494/DL_MESO/dl_meso/post_grad/Dump/'
files = os.listdir(folder)

half_box_size = 20
d = 0.25
A = 25
counters = np.linspace(-half_box_size,half_box_size-d,num=half_box_size*2/d)
total_density_frame = []
for file in files:
      Atoms = xyz_lib.Atoms
      Alpha = xyz_lib.Atoms.read(Atoms,folder+file)

      location = Alpha.xyz

      
      particle_count = np.zeros_like(counters)

      for count in counters:
          index = int(np.where(count==counters)[0])
          particle_count[index] = box_count(location,count,d)
    
      #plt.plot(particle_count)
      density = density_finding(particle_count,A,d)
      total_density_frame.append(density)

#print(total_density_frame)
print(np.mean(total_density_frame))

plt.figure()
plt.plot(counters,particle_count)
plt.savefig('test.png')
