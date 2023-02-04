import math

def normal_utility_function(x):
    r = 0.5
    return 1-math.exp(-x/r)