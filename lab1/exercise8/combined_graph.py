import matplotlib.pyplot as plt
import numpy as np

# Data from experiment results
# List lengths and swap configurations
list_lengths = [10, 50, 100]

# Average times for each algorithm at each list length (across all swap configs)
# Sorted (0 swaps)
insertion_sorted = [0.00000093, 0.00000207, 0.00000389]
merge_sorted = [0.00000588, 0.00002918, 0.00006190]
quick_sorted = [0.00000372, 0.00003257, 0.00011221]

# Random (worst case for insertion)
insertion_random = [0.00000218, 0.00003699, 0.00021288]
merge_random = [0.00000504, 0.00003173, 0.00007171]
quick_random = [0.00000279, 0.00001625, 0.00003613]

# Create a single comprehensive plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot sorted case (best for insertion)
ax.plot(list_lengths, insertion_sorted, marker='o', linestyle='-', linewidth=2.5, 
         markersize=10, color='#2E86AB', label='Insertion Sort (Sorted)', alpha=0.9)
ax.plot(list_lengths, merge_sorted, marker='s', linestyle='--', linewidth=2, 
         markersize=8, color='#A23B72', label='Merge Sort (Sorted)', alpha=0.7)
ax.plot(list_lengths, quick_sorted, marker='^', linestyle='-.', linewidth=2, 
         markersize=8, color='#F18F01', label='Quick Sort (Sorted)', alpha=0.7)

# Plot random case (worst for insertion)
ax.plot(list_lengths, insertion_random, marker='o', linestyle=':', linewidth=2.5, 
         markersize=10, color='#2E86AB', label='Insertion Sort (Random)', alpha=0.5)
ax.plot(list_lengths, merge_random, marker='s', linestyle=':', linewidth=2, 
         markersize=8, color='#A23B72', label='Merge Sort (Random)', alpha=0.4)
ax.plot(list_lengths, quick_random, marker='^', linestyle=':', linewidth=2, 
         markersize=8, color='#F18F01', label='Quick Sort (Random)', alpha=0.4)

# Add annotations for key insights
ax.annotate('Insertion Sort O(n)\nDominates on sorted data!', 
            xy=(50, 0.00000207), xytext=(25, 0.000015),
            arrowprops=dict(arrowstyle='->', color='#2E86AB', lw=2),
            fontsize=10, fontweight='bold', color='#2E86AB',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

ax.annotate('Quick Sort wins\non random data', 
            xy=(100, 0.00003613), xytext=(70, 0.000055),
            arrowprops=dict(arrowstyle='->', color='#F18F01', lw=2),
            fontsize=10, fontweight='bold', color='#F18F01',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

ax.annotate('Insertion Sort O(n²)\nSlows down dramatically!', 
            xy=(100, 0.00021288), xytext=(50, 0.00018),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, fontweight='bold', color='red',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.3))

ax.set_xlabel('List Length', fontweight='bold', fontsize=13)
ax.set_ylabel('Time (seconds)', fontweight='bold', fontsize=13)
ax.set_title('Experiment 8: When "Bad" Sorts Beat "Good" Sorts\nCrossover Point: ~50-100 elements on random data', 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(loc='upper left', fontsize=9, ncol=2)
ax.grid(True, alpha=0.3)
ax.set_xticks(list_lengths)

# Add key insight text box
textstr = 'KEY INSIGHTS:\n' \
          '✓ Insertion Sort wins on sorted/nearly-sorted small lists\n' \
          '✓ Crossover occurs around 50-100 elements for random data\n' \
          '✓ This is why hybrid sorts (TimSort, IntroSort) exist!\n' \
          '✓ Production algorithms switch to Insertion Sort for small subarrays'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.5, 0.97, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()

# Save the graph
plt.savefig('/Users/abdullah/Desktop/2XC3-Labs/lab1/exercise8/experiment8_combined.png', 
            dpi=300, bbox_inches='tight')
print("Combined graph saved to: /Users/abdullah/Desktop/2XC3-Labs/lab1/exercise8/experiment8_combined.png")

plt.show()
