import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

import ElectroMagn
import Pusher
import Particle

dt = 1.0e-13
dx = 1.0e-5
Nx = 100

e = 1.6021766208e-19
q = -1.6021766208e-19
m = 9.109382616e-31
Te = 20


particle = Particle.Particle(q, m)
EMfields = ElectroMagn.ElectroMagn((Nx, Nx, Nx), (dx, dx, dx))
pusher = Pusher.Pusher(dt)

print type(EMfields.E),EMfields.E.shape
EMfields.E[:,:,:,:] = 0.0
EMfields.B[:,:,:,:] = 0.0

EMfields.E[:,:,:,0] = 0.0 #-1.0e6
EMfields.B[:,:,:,1] = 2.0

particle.x[0] = 0.9 * Nx * dx
particle.x[1] = 0.5 * Nx * dx
particle.x[2] = 0.5 * Nx * dx

particle.v[0] = -math.sqrt(2.0 * e * Te / m)
particle.v[1] = math.sqrt(2.0 * e * Te / m)
particle.v[2] = math.sqrt(2.0 * e * Te / m)

ntime = 1000
trajectory_x = np.zeros(ntime)
trajectory_y = np.zeros(ntime)
trajectory_z = np.zeros(ntime)

for itime in np.arange(0, ntime):
    print itime, particle.x[1]
    pusher.push(particle, EMfields)
    trajectory_x[itime] = particle.x[0]
    trajectory_y[itime] = particle.x[1]
    trajectory_z[itime] = particle.x[2]





fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(trajectory_x, trajectory_y, trajectory_z)

xmin = trajectory_x.min()
xmax = trajectory_x.max()
ymin = trajectory_y.min()
ymax = trajectory_y.max()
#ax.axis([xmin, xmax, ymin, ymax])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
