__Throughout this project we will use a timestep = 0.01__

## Discussion

These images contain analysis over two dimensions, the first is the value of **A**

Images mXX_60.png are run over 10k steps, we see a movement from liquid like to gas like behaviour even at these short time scales. The axis on the bottom is x, the height is number of particles over a thin (0.5) slice. This converts to local density with division by (25*0.5).

At **A** = -30: 

<img src="images/m30_60.png" alt="Drawing" width="500"/>

At **A** = -20:

<img src="images/m20_60.png" alt="Drawing" width="500"/>

This is well and good to start, but things get more complicated as we approach the boundary. As a concrete example consider the image produced for **A** = -22.5; which can't naturally be described as either a liquid or a gas.

<img src="images/m22.5_60.png" alt="Drawing" width="500"/>

The first thing to note is that one value is 0. This prevents calculations of the the form **max x 0.9 > min** working, however this can be worked around. The underlying physics is more interesting and can be seen by expanding the number of timesteps.

## Extending the timestep
### Working with **A** = -22.5

Below we have three images, which reading from left to right are taken from steps=0 , steps = 250k and steps = 500k

<div>
            <img src="images/dump_1.png" alt="Drawing" width="250"/>
            <img src="images/dump_12.png" alt="Drawing" width="250"/>
            <img src="images/dump_24.png" alt="Drawing" width="250"/>
</div>
