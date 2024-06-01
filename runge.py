

class Runge:
    def __init__(self, f,h,t0, y0,t0p = None,y0p = None ):
        self.f = f
        self.y0 = y0
        self.t0 = t0
        self.y0p = y0p
        self.t0p = t0p
        self.h = h
        self.order = 1 if t0p is None else 2

    def runge(self):
        if self.order == 1:
            return self.runge1()
        else:
            return self.runge2()
    
    def runge1(self):
        # localise variables
        f = self.f
        t0 = self.t0
        y0 = self.y0
        h = self.h

        # calculate coefficients
        k1 = h*f(t0, y0)
        k2 = h*f(t0 + h/2, y0 + k1*h/2)
        k3 = h*f(t0 + h/2, y0 + k2*h/2)
        k4 = h*f(t0 + h, y0 + h*k3)

        # calculate result
        y1 = y0 + (k1 + 2*k2 + 2*k3 + k4)/6

        # prepare for next iteration
        self.t0 += h
        self.y0 = y1
        return y1
    
    def runge2(self):
        # localise variables
        f = self.f
        t0 = self.t0
        y0 = self.y0
        h = self.h
        t0p = self.t0p
        y0p = self.y0p

        # calculate coefficients
        k1 = h*f(t0, y0,y0p)
        k2 = h*f(t0 + h/2, y0 + (h/2)*y0p, y0p + (h*k1)/2)
        k3 = h*f(t0 + h/2, y0 + (h/2)*y0p + (h**2)*k1/4, y0p + (h*k2)/2)
        k4 = h*f(t0 + h, y0 + h*y0p + (h**2)*k2/2, y0p + h*k3)

        # calculate result
        y1 = y0 + h*y0p + (h/6)*(k1+k2+k3)
        yp1 = y0p + (k1 + 2*k2 + 2*k3 + k4)/6
        # prepare for next iteration
        self.t0 += h
        self.y0 = y1
        self.t0p += h
        self.y0p = yp1
        return y1,yp1