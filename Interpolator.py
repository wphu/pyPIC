import numpy as np

class Interpolator:
    def __init__(self, cell_length):
        self.cell_length = cell_length

    def interpolate(self, particle, EMfields, E_loc, B_loc):
        xpn = particle.x / EMfields.cell_length
        ip_ = xpn.astype(int)
        delta = xpn - ip_.astype(float)

        coeffxp_ = np.zeros(2)
        coeffyp_ = np.zeros(2)
        coeffzp_ = np.zeros(2)

        coeffxp_[0] = 1.0 - delta[0]
        coeffxp_[1] = delta[0]
        coeffyp_[0] = 1.0 - delta[1]
        coeffyp_[1] = delta[1]
        coeffzp_[0] = 1.0 - delta[2]
        coeffzp_[1] = delta[2]

        for i in np.arange(0,2):
            for j in np.arange(0,2):
                for k in np.arange(0,2):
                    E_loc = E_loc + EMfields.E[ip_[0]+i, ip_[1]+j, ip_[2]+k,:] * coeffxp_[i] * coeffyp_[j] * coeffzp_[k]
                    B_loc = B_loc + EMfields.B[ip_[0]+i, ip_[1]+j, ip_[2]+k,:] * coeffxp_[i] * coeffyp_[j] * coeffzp_[k]

        return (E_loc, B_loc)
