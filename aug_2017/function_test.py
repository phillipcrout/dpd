import os
import sys

def get_timesteps():
    """Number of frames stored in HISTORY"""
    ## This function is currently buggy
    if not os.path.isfile("CONTROL"):
        print("No CONTROL file present.")
        sys.exit()
    with open("CONTROL") as f:
        for line in f:
            line = line.rstrip()
            if "equilibration steps" in line:
                Nstart = int(line.split()[2])
            if "traj" in line:
                Nevery = int(line.split()[2])
            if "steps" in line and not "equilibration" in line:
                Nsteps = int(line.split()[1])
    return (Nsteps - Nstart) // Nevery

print(get_timesteps())
