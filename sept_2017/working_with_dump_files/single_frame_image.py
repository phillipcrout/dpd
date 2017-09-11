from extracting_local_densities import *

dump_file = 2 #placeholder 

counters = generate_counters_vector(half_box_size=20,d=0.5)
particle_count = counters_in_a_given_box(dump_file,counters)
