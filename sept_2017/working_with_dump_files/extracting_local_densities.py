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

def generate_counters_vector(half_box_size,d):
    return np.linspace(-half_box_size,half_box_size-d,num=half_box_size*2/d)

def counters_in_given_box(dump_file,counters):
        Atoms = xyz_lib.Atoms
        Alpha = xyz_lib.Atoms.read(Atoms,dump_file)
        location = Alpha.xyz

        particle_count = np.zeros_like(counters)
        d = counters[1]-counters[0]
        for count in counters:
            index = int(np.where(count==counters)[0])
            particle_count[index] = box_count(location,count,d)

        return particle_count

"""
is_it_a_liquid = []
for folder in folders:
    files = os.listdir(folder_root+folder)
    for file in files:
            #is_it_a_liquid.append(frame_result)

            plt.figure()
            plt.plot(counters,particle_count)
            plt.xlabel('x')
            plt.ylabel('Dproxy')
            save_string = file[:-4]+'.png' 
            plt.title(save_string)
            plt.savefig(save_string)
#print((is_it_a_liquid))
"""
