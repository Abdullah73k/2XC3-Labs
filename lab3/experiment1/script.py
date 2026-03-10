import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bst import BST
from rbt import RBTree
from utils import create_random_list

NUM_TRIALS = 100
LIST_LENGTH = 10000
MAX_VALUE = 100000

total_bst_height = 0
total_rbt_height = 0

for _ in range(NUM_TRIALS):
    data = create_random_list(LIST_LENGTH, MAX_VALUE)

    bst = BST()
    rbt = RBTree()

    for val in data:
        bst.insert(val)
        rbt.insert(val)

    total_bst_height += bst.height()
    total_rbt_height += rbt.get_height()

avg_bst = total_bst_height / NUM_TRIALS
avg_rbt = total_rbt_height / NUM_TRIALS

print(f"Trials:          {NUM_TRIALS}")
print(f"List length:     {LIST_LENGTH}")
print(f"Avg BST height:  {avg_bst:.2f}")
print(f"Avg RBT height:  {avg_rbt:.2f}")
print(f"Avg difference:  {avg_bst - avg_rbt:.2f}")
