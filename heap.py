array=[23,67,14,63,98]
def heapsort(array):
    n = len(array)
    for i in range(n//2-1,-1,-1):
        heapify(array,n,i)
    for i in range(n-1,0,-1):
        array[0],array[i]=array[i],array[0]
        heapify(array,i,0)
    return array
def heapify(array,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and array[l]>array[largest]):
        largest=l
    if(r<n and array[r]>array[largest]):
        largest=r
    if(largest!=i):
        array[i],array[largest]=array[largest],array[i]
        heapify(array,n,largest)

result=heapsort(array)
print(result)