import time
import random
import matplotlib.pyplot as plt

def heapify(array, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and array[i] < array[l]:
    largest = l

  if r < n and array[largest] < array[r]:
    largest = r

  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    heapify(array, n, largest)

def HeapSort(array):
  n = len(array)
  for i in range(n, -1, -1):
    heapify(array, n, i)

  for i in range(n - 1, 0, -1):
    array[i], array[0] = array[0], array[i]
    heapify(array, i, 0)

# Plotting the results
def plot_graph(x, y):
  plt.plot(x, y, label="Heap Sort")
  plt.xlabel("Number of elements (n)")
  plt.ylabel("Time taken (s)")
  plt.title("Heap Sort")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  n_values = [100, 500, 1000, 5000, 10000, 50000]
  heap_sort_times = []
  for n in n_values:
    array = random.sample(range(1, 100000), n)
    start = time.time()
    HeapSort(array)
    end = time.time()
    print(n,": ",end-start," is the time taken")
    heap_sort_times.append(end - start)

  plot_graph(n_values, heap_sort_times)
