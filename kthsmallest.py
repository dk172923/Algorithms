import random

def kth_smallest(arr, k):
    pivot = random.choice(arr)  # Choose a random pivot element
    
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    right = [x for x in arr if x > pivot]  # Elements larger than the pivot
    
    if k <= len(left):
        return kth_smallest(left, k)  # Recur on the left sublist
    elif k > len(arr) - len(right):
        return kth_smallest(right, k - (len(arr) - len(right)))  # Recur on the right sublist
    else:
        return pivot  # The kth smallest element is the pivot itself

# Example usage
arr = [3, 7, 2, 1, 8, 4, 5]
k = 3
result = kth_smallest(arr, k)
print(f"The {k}th smallest element in {arr} is {result}.")
