#!/usr/bin/env python3                                                      
# -*- coding: utf-8 -*-

from extracting_local_densities import *

dump_file = '/home/pc494/DL_MESO/dl_meso/post_grad/Dump_A_225/dump_24.xyz' 

counters = generate_counters_vector(half_box_size=20,d=0.5)
particle_count = counters_in_given_box(dump_file,counters)

plot_data = np.vstack([counters,particle_count])

np.savetxt('particle_count.txt',plot_data)
