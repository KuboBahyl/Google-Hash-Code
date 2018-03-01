# THE MAINEST FILE

import time as t
from tqdm import tqdm # loading bars

from processing import preprocess, postprocess
from InOut import *
from best_solution import *

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
