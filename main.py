# THE MAINEST FILE

import time as t
import numpy as np
from tqdm import tqdm # loading bars

from processing import preprocess, postprocess
from InOut import *
from best_solution import *

import numpy as np

def ride_length(ride):
    xlen = np.absolute(ride[0] - ride[1])
    ylen = np.absolute(ride[2] - ride[3])
    return xlen + ylen

def if_bonus(, ride):
    pass

def calc_score(cars, rides):
    pass(ride):
    """
    calculates time needed for a ride
    """
    return np.absolute(ride[0] - ride[2]) + np.absolute(ride[1] - ride[3])

def read_input(path):
    with open(path, 'r') as f:
        Nrows, Ncols, Ncars, Nrides, bonus, Nsteps = [int(i) for i in f.readline().split(" ")]

        rides = []

        for ride in range(Nrides):
            rides.append([int(i) for i in f.readline().split(" ")])

        sorted(rides, key = lambda x: x[4])

    return {
        'Nrows': Nrows,
        'Ncols': Ncols,
        'Ncars': Ncars,
        'bonus': bonus,
        'Nsteps': Nsteps,
        'rides': rides
    }

def write_output(path, *args):
    with open(path, 'w') as f:
        f.write("best output")
        f.write('\n')

def postprocess():
    pass

def greedy_search():
    pass

if __name__ == '__main__':
    """
    READING INPUT
    """

    time_start = t.time()

    """
    PREPROCESSING
    """

    print("Preprocessing time: {0:.2f}s".format(t.time() - time_start))

    """
    MAINEST THING
    """

    end_start = t.time()
    print("Preprocessing time: {0:.2f}s".format(end_start - time_start))
