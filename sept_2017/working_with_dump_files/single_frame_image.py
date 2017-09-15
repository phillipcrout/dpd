#!/usr/bin/env python3                                                      
# -*- coding: utf-8 -*-

from extracting_local_densities import generate_counters_vector,counters_in_given_box
import numpy as np

root = '/home/pc494/DL_MESO/dl_meso/post_grad/Dump_A_225/'  
counters = generate_counters_vector(half_box_size=20,d=0.5)
particle_count = np.zeros_like(counters)

for file_name in ['dump_12.xyz','dump_11.xyz']:
    dump_file = root + file_name 
    particle_count += counters_in_given_box(dump_file,counters)

plot_data = np.vstack([counters,particle_count])

np.savetxt('particle_count_2.txt',plot_data)
