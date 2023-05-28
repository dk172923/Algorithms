import sys

def findMinAndMax(nums, left, right, min=sys.maxsize, max=-sys.maxsize):
    # Base case: if the list contains only one element
    if left == right:
        # Comparison 1: Update minimum if needed
        if min > nums[right]:
            min = nums[right]
        # Comparison 2: Update maximum if needed
        if max < nums[left]:
            max = nums[left]
        return min, max
    
    # If the list contains only two elements
    if right - left == 1:
        if nums[left] < nums[right]:
            # Comparison 3: Update minimum if needed
            if min > nums[left]:
                min = nums[left]
            # Comparison 4: Update maximum if needed
            if max < nums[right]:
                max = nums[right]
        else:
            # Comparison 5: Update minimum if needed
            if min > nums[right]:
                min = nums[right]
            # Comparison 6: Update maximum if needed
            if max < nums[left]:
                max = nums[left]
        return min, max
    
    # Find the middle element
    mid = (left + right) // 2
    
    # Recur for the left sublist
    min, max = findMinAndMax(nums, left, mid, min, max)
    
    # Recur for the right sublist
    min, max = findMinAndMax(nums, mid + 1, right, min, max)
    
    return min, max

if __name__ == '__main__':
    nums = [7, 2, 9, 3, 1, 6, 7, 8, 4]
    
    # Initialize the minimum element by INFINITY and the maximum element by -INFINITY
    (min, max) = findMinAndMax(nums, 0, len(nums) - 1)
    
    print("The minimum element in the list is", min)
    print("The maximum element in the list is", max)