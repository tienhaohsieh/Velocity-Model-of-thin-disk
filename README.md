# Disk line of sight velocity model

A simple tool to visual the disk velocity at the line of sight. The model takes a simple thin disk with a Keplerian velocity field. To see the model, simply run >> python ToShow.py.

One can move the cursor to adjust the position angle, and scroll wheel to change the inclination angle.
The position angle and inclination angle will simultanelously shown in the top-left corner.

A different velocity field might be input in Function.py for visualization.

#### Requirments:
* Numpy
* Matplotlib

### Example
A simple model with a Keplerian rotation with a velocity=10 km/s at a radius R=10 au.
The distance and velocity (scaled to r=10au) can be modified in the Function.py and ToShow.py.

![image](https://github.com/tienhaohsieh/Disk_Vmodel/blob/main/demo.gif)
