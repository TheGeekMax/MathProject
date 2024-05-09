

class Runge:
    def __init__(self, f,t0, y0, h):
        self.f = f
        self.y0 = y0
        self.t0 = t0
        self.h = h

    def runge(self):
        # localise variables
        f = self.f
        t0 = self.t0
        y0 = self.y0
        h = self.h

        # calculate coefficients
        k1 = h*f(t0, y0)
        k2 = h*f(t0 + h/2, y0 + k1/2)
        k3 = h*f(t0 + h/2, y0 + k2/2)
        k4 = h*f(t0 + h, y0 + k3)

        # calculate result
        y1 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6

        # prepare for next iteration
        self.t0 += h
        self.y0 = y1
        return y1