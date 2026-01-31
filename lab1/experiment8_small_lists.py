"""
Experiment 8: When "Bad" Sorts Beat "Good" Sorts
Testing when Insertion Sort (O(n²)) beats Merge Sort and Quick Sort on small lists
"""

import timeit
import math
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bad_sorts import create_near_sorted_list, insertion_sort
from good_sorts import mergesort, duel_quicksort  # Using dual-pivot version to avoid recursion errors

# Configuration
LIST_LENGTHS = [500, 1000, 2000]
MAX_VALUE = 1000
NUM_RUNS = 5


def calculate_swaps_for_random(length):
    """Calculate swaps for statistically random list: length*log(length) / 2"""
    return int(length * math.log(length) / 2)


def get_swap_configurations(length):
    """
    Returns swap configurations for a given list length:
    - 0: Perfectly sorted (best case for insertion sort)
    - middle: Moderately unsorted
    - random: Statistically random (length*log(length)/2)
    """
    middle_swaps = calculate_swaps_for_random(length) // 2
    return {
        'sorted (0 swaps)': 0,
        f'moderately unsorted ({middle_swaps} swaps)': middle_swaps,
        f'random ({calculate_swaps_for_random(length)} swaps)': calculate_swaps_for_random(length)
    }


def time_sort(sort_function, test_list):
    """
    Time a sorting function on a copy of the test list.
    Returns the time in seconds, or None if error occurs.
    """
    try:
        L = test_list.copy()
        start = timeit.default_timer()
        sort_function(L)
        end = timeit.default_timer()
        return end - start
    except RecursionError:
        return None


def run_experiment():
    """
    Run the complete experiment comparing insertion sort vs good sorts on small lists.
    """
    print("=" * 100)
    print("EXPERIMENT 8: WHEN BAD SORTS BEAT GOOD SORTS")
    print("=" * 100)
    print(f"Max Value: {MAX_VALUE}")
    print(f"Number of Runs per Configuration: {NUM_RUNS}")
    print(f"List Lengths Tested: {LIST_LENGTHS}")
    print("=" * 100)
    print("\nGoal: Find when Insertion Sort (O(n²)) beats Merge Sort and Quick Sort")
    print("Hypothesis: Insertion Sort wins on sorted/nearly-sorted lists")
    print("=" * 100)
    print()
    
    # Dictionary to store all results
    # Structure: results[length][swap_config][algorithm] = {'runs': [...], 'average': ...}
    results = {}
    
    # Map algorithm names to functions
    sort_functions = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': mergesort,
        'Quick Sort': duel_quicksort  # Using dual-pivot version
    }
    
    # Run experiments for each list length and swap configuration
    for length in LIST_LENGTHS:
        results[length] = {}
        swap_configs = get_swap_configurations(length)
        
        print(f"\n{'=' * 100}")
        print(f"Testing with List Length: {length}")
        print(f"{'=' * 100}")
        
        for config_name, swaps in swap_configs.items():
            print(f"\n  Configuration: {config_name}")
            print(f"  {'-' * 90}")
            
            results[length][config_name] = {}
            
            for sort_name, sort_func in sort_functions.items():
                print(f"\n    {sort_name}:")
                
                run_times = []
                
                for run in range(1, NUM_RUNS + 1):
                    # Create a fresh near-sorted list for each run
                    test_list = create_near_sorted_list(length, MAX_VALUE, swaps)
                    
                    # Time the sorting algorithm
                    time_taken = time_sort(sort_func, test_list)
                    
                    if time_taken is None:
                        print(f"      Run {run}: FAILED (RecursionError - worst case)")
                    else:
                        run_times.append(time_taken)
                        print(f"      Run {run}: {time_taken:.8f} seconds")
                
                # Calculate average
                if run_times:
                    avg_time = sum(run_times) / len(run_times)
                    print(f"      {'─' * 86}")
                    print(f"      AVERAGE: {avg_time:.8f} seconds")
                else:
                    avg_time = float('inf')
                    print(f"      {'─' * 86}")
                    print(f"      AVERAGE: FAILED - All runs hit RecursionError (O(n²) worst case)")
                
                # Store results
                results[length][config_name][sort_name] = {
                    'runs': run_times,
                    'average': avg_time
                }
    
    # Print summary tables for each list length
    print("\n\n")
    print("=" * 100)
    print("SUMMARY TABLES BY LIST LENGTH")
    print("=" * 100)
    
    for length in LIST_LENGTHS:
        print(f"\n{'=' * 100}")
        print(f"List Length: {length}")
        print(f"{'=' * 100}")
        
        swap_configs = get_swap_configurations(length)
        
        print(f"{'Configuration':<30} {'Insertion Sort':<18} {'Merge Sort':<18} {'Quick Sort':<18} {'Winner':<15}")
        print("-" * 100)
        
        for config_name in swap_configs.keys():
            insertion_avg = results[length][config_name]['Insertion Sort']['average']
            merge_avg = results[length][config_name]['Merge Sort']['average']
            quick_avg = results[length][config_name]['Quick Sort']['average']
            
            # Determine winner (exclude failed runs)
            valid_times = [(insertion_avg, "Insertion"), (merge_avg, "Merge"), (quick_avg, "Quick")]
            valid_times = [(t, n) for t, n in valid_times if t != float('inf')]
            
            if valid_times:
                min_time, winner_name = min(valid_times, key=lambda x: x[0])
                winner = f"{winner_name} ⭐"
            else:
                winner = "All FAILED"
            
            # Format times for display
            insertion_str = "FAILED" if insertion_avg == float('inf') else f"{insertion_avg:.8f}"
            merge_str = "FAILED" if merge_avg == float('inf') else f"{merge_avg:.8f}"
            quick_str = "FAILED" if quick_avg == float('inf') else f"{quick_avg:.8f}"
            
            row = f"{config_name:<30} {insertion_str:<18} {merge_str:<18} {quick_str:<18} {winner:<15}"
            print(row)
    
    print("\n" + "=" * 100)
    
    # CSV format for graphing
    print("\n\n" + "=" * 100)
    print("CSV FORMAT (for graphing)")
    print("=" * 100)
    
    for length in LIST_LENGTHS:
        print(f"\n--- List Length: {length} ---")
        print("Configuration,Insertion Sort,Merge Sort,Quick Sort")
        
        swap_configs = get_swap_configurations(length)
        for config_name in swap_configs.keys():
            insertion_avg = results[length][config_name]['Insertion Sort']['average']
            merge_avg = results[length][config_name]['Merge Sort']['average']
            quick_avg = results[length][config_name]['Quick Sort']['average']
            
            insertion_str = "FAILED" if insertion_avg == float('inf') else f"{insertion_avg:.8f}"
            merge_str = "FAILED" if merge_avg == float('inf') else f"{merge_avg:.8f}"
            quick_str = "FAILED" if quick_avg == float('inf') else f"{quick_avg:.8f}"
            
            print(f"{config_name},{insertion_str},{merge_str},{quick_str}")
    
    print("=" * 100)
    
    # Analysis
    print("\n\n" + "=" * 100)
    print("ANALYSIS: When Does Insertion Sort Win?")
    print("=" * 100)
    
    insertion_wins = 0
    total_tests = 0
    
    for length in LIST_LENGTHS:
        swap_configs = get_swap_configurations(length)
        for config_name in swap_configs.keys():
            total_tests += 1
            insertion_avg = results[length][config_name]['Insertion Sort']['average']
            merge_avg = results[length][config_name]['Merge Sort']['average']
            quick_avg = results[length][config_name]['Quick Sort']['average']
            
            # Skip if insertion sort failed
            if insertion_avg == float('inf'):
                continue
            
            if insertion_avg < merge_avg and insertion_avg < quick_avg:
                insertion_wins += 1
                print(f"\n✓ Insertion Sort WINS: {config_name} at length {length}")
                print(f"  Insertion: {insertion_avg:.8f}s")
                
                if merge_avg != float('inf'):
                    print(f"  Merge:     {merge_avg:.8f}s")
                    speedup_vs_merge = merge_avg / insertion_avg
                    print(f"  Speedup vs Merge: {speedup_vs_merge:.2f}x")
                
                if quick_avg != float('inf'):
                    print(f"  Quick:     {quick_avg:.8f}s")
                    speedup_vs_quick = quick_avg / insertion_avg
                    print(f"  Speedup vs Quick: {speedup_vs_quick:.2f}x")
    
    print(f"\n{'─' * 100}")
    print(f"Summary: Insertion Sort won {insertion_wins}/{total_tests} configurations")
    print("=" * 100)
    
    print("\n\nKEY INSIGHTS:")
    print("- Insertion Sort is O(n) on sorted/nearly-sorted data (best case)")
    print("- Merge/Quick Sort are always O(n log n) regardless of input")
    print("- For small lists, O(n) beats O(n log n) because:")
    print("  * Lower constant factors")
    print("  * No recursion overhead")
    print("  * Better cache locality")
    print("- This is why many libraries use HYBRID sorts (e.g., TimSort, IntroSort)")
    print("  that switch to Insertion Sort for small subarrays!")
    print("=" * 100)
    
    return results


if __name__ == "__main__":
    print("\nStarting Experiment 8...")
    print("Testing when 'bad' sorts beat 'good' sorts on small lists.\n")
    
    results = run_experiment()
    
    print("\n\n" + "=" * 100)
    print("✓ Experiment 8 complete!")
    print("=" * 100)
    print("\nPRACTICAL IMPORTANCE:")
    print("This is why production sorting algorithms are HYBRID:")
    print("- Python's TimSort: Uses Insertion Sort for runs < 64 elements")
    print("- Java's DualPivotQuicksort: Switches to Insertion Sort for < 47 elements")
    print("- C++ std::sort (IntroSort): Uses Insertion Sort for < 16 elements")
    print("=" * 100)
