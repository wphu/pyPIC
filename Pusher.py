import numpy as np
import Interpolator


class Pusher:
    def __init__(self, dt):
        self.dt = dt

    def push(self, particle, EMfields):
        E_loc = np.zeros((3), dtype = float)
        B_loc = np.zeros((3), dtype = float)

        interpolator = Interpolator.Interpolator(EMfields.cell_length)
        E_loc, B_loc = interpolator.interpolate(particle, EMfields, E_loc, B_loc)


        t = 0.5 * self.dt * particle.q * B_loc / particle.m
        s = 2.0 * t / ( 1.0 + np.dot(t,t) )
        v_minus = particle.v + 0.5 * self.dt * particle.q * E_loc / particle.m
        v_dot = v_minus + np.cross(v_minus, t)
        v_plus = v_minus + np.cross(v_dot, s)
        particle.v = v_plus + 0.5 * self.dt * particle.q * E_loc / particle.m
        particle.x = particle.x + particle.v * self.dt
