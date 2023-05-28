import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
    result = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    result += left_arr[i:]
    result += right_arr[j:]
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left_arr = []
    right_arr = []
    equal_arr = []
    for element in arr:
        if element < pivot:
            left_arr.append(element)
        elif element > pivot:
            right_arr.append(element)
        else:
            equal_arr.append(element)
    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)

n_values = [100, 1000, 5000, 10000, 50000]
merge_sort_times = []
quick_sort_times = []

for n in n_values:
    arr = [i for i in range(n, 0, -1)]
    
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    merge_sort_times.append(end_time - start_time)
    
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    quick_sort_times.append(end_time - start_time)

plt.plot(n_values, merge_sort_times, label='Merge Sort')
plt.plot(n_values, quick_sort_times, label='Quick Sort')
plt.xlabel('Number of Elements (n)')
plt.ylabel('Time Taken (Seconds)')
plt.legend()
plt.show()
