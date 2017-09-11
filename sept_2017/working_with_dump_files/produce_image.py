#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

particle_count = np.loadtxt('particle_count.txt')

plt.figure()
plt.plot(particle_count[0],particle_count[1])
plt.xlabel('x')
plt.ylabel('Proxy Density')
plt.show()
