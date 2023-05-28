import time
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Experiment to find time taken for linear search
def run_experiment(n):
    arr = list(range(n))  # Generate a list of n elements
    x = n - 1  # Search for the last element
    start_time = time.time_ns()  # Record start time
    result = linear_search(arr, x)  # Perform linear search
    end_time = time.time_ns()  # Record end time
    print(n,": ",end_time-start_time," is the time taken")
    return end_time - start_time  # Return time taken


# Plotting the results
ns = [10, 100, 1000, 10000, 100000, 1000000]
times = [run_experiment(n) for n in ns]
plt.plot(ns, times)
plt.xlabel("n")
plt.ylabel("Time (ns)")
plt.title("Time taken for Linear Search")
plt.show()
