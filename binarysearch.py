import time
import matplotlib.pyplot as plt

def binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1

# Experiment to find average time taken for binary search
def run_experiment(n, num_iterations):
    arr = list(range(n))  # Generate a list of n elements
    x = n - 1  # Search for the last element
    total_time = 0
    for _ in range(num_iterations):
        start_time = time.time()  # Record start time
        result = binary_search(arr, 0, n - 1, x)  # Perform binary search
        end_time = time.time()  # Record end time
        total_time += end_time - start_time
    avg_time = total_time / num_iterations
    print(n, ": ", avg_time, " is the average time taken")
    return avg_time

# Plotting the results
ns = [10, 100, 1000, 10000, 100000, 1000000]
num_iterations = 1000  # Number of iterations for averaging
times = [run_experiment(n, num_iterations) for n in ns]
plt.plot(ns, times)
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Average Time taken for Binary Search")
plt.show()