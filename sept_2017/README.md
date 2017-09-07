## Preliminaries

_The experiments under discussion here use a timestep = 0.01_ and **B** = 60. Plots are of local density (this is a particle count over a distance of 0.5 and a cross sectional area of 25). The distance axis (x) is given in units of the DPD length.

## Results

These images contain analysis over two dimensions, the first is the value of **A**

Images mXX_60.png are run over 10k steps, we see a movement from liquid like to gas like behaviour even at these short time scales.

At **A** = -30: 

<img src="images/A_var/m30_60.png" alt="Drawing" width="500"/>

At **A** = -20:

<img src="images/A_var/m20_60.png" alt="Drawing" width="500"/>

This is well and good to start, but things get more complicated as we approach the boundary. As a concrete example consider the image produced for **A** = -22.5; which can't naturally be described as either a liquid or a gas.

<img src="images/A_var/m22.5_60.png" alt="Drawing" width="500"/>

The first thing to note is that one value is 0. This prevents calculations of the the form **max x 0.9 > min** working, however this can be worked around. The underlying physics is more interesting and can be seen by expanding the number of timesteps.

## Extending the timestep
### Working with **A** = -22.5

Below we have three images, which reading from left to right are taken from steps=0 , steps = 250k and steps = 500k

<div>
            <img src="images/A_225/dump_1.png" alt="Drawing" width="250"/>
            <img src="images/A_225/dump_12.png" alt="Drawing" width="250"/>
            <img src="images/A_225/dump_24.png" alt="Drawing" width="250"/>
</div>

### Working with **A** = -25

<div>
            <img src="images/A_250/dump_1.png" alt="Drawing" width="250"/>
            <img src="images/A_250/dump_12.png" alt="Drawing" width="250"/>
            <img src="images/A_250/dump_24.png" alt="Drawing" width="250"/>
</div>


