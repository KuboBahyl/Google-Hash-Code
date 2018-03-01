# THE MAINEST FILE

import time as t
from tqdm import tqdm # loading bars

from processing import preprocess, postprocess
from InOut import *
from best_solution import *

def read_input(path):
    with open(path, 'r') as f:
        Nrows, Ncols, Ncars, Nrides, bonus, Nsteps = [int(i) for i in f.readline().split(" ")]

        rides = []

        for ride in range(Nrides):
            rides.append([int(i) for i in f.readline().split(" ")])

def write_output(path, *args):
    with open(path, 'w') as f:
        f.write("best output")
        f.write('\n')

def preprocess():
    pass

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


main()
