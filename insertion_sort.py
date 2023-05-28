import time
import random
import matplotlib.pyplot as plt

def InsertionSort(array):
  n = len(array)
  for i in range(1, n):
    key = array[i]
    j = i-1
    while j >= 0 and array[j] > key:
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key

# Plotting the results
def plot_graph(x, y):
  plt.plot(x, y, label="Insertion Sort")
  plt.xlabel("Number of elements (n)")
  plt.ylabel("Time taken (s)")
  plt.title("Insertion Sort")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  n_values = [100, 500, 1000, 5000, 10000, 50000]
  insertion_sort_times = []
  for n in n_values:
    array = random.sample(range(1, 100000), n)
    start = time.time()
    InsertionSort(array)
    end = time.time()
    print(n,": ",end-start," is the time taken")
    insertion_sort_times.append(end - start)

  plot_graph(n_values, insertion_sort_times)
