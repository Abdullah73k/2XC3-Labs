import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xc3 import XC3

NUM_ITR = 25
HEIGHTS = {}

for i in range(NUM_ITR + 1):
    tree = XC3(i)
    HEIGHTS[i] = tree.height()

print(HEIGHTS)