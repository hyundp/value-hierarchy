import math

def normal_utility_function(x):

    # r이 작을수록 risk averse.
    r = 0.5
    return 1-math.exp(-x/r)