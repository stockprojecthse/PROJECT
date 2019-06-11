import numpy
import math
import scipy.optimize as optimization

class SimpleMath:
        
    def __init__(self):
        self.__x0 = numpy.array([0.0, 0.0, 0.0])

    def __func(self, x, a, b, c):
        return a + b * x
    
    def __radiansToDegree(self, value):
        return value * 180 / math.pi
    
    def getInclinationAngle(self, data, interval):
        xdata = list(range(0, len(data) * interval, interval))
        w, _ = optimization.curve_fit(self.__func, xdata, data, self.__x0)
        return self.__radiansToDegree(math.atan(w[1]))
