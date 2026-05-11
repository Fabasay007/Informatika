import threading

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_parallel(arr, result, index):
    result[index] = quicksort(arr)

def par_quicksort(arr, num_threads):
    if len(arr) < 1000 or num_threads <= 1: 
        return quicksort(arr)
    
    n = len(arr)
    chunk_size = n // num_threads
    threads = []
    result = [None] * num_threads
    
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else n
        s = arr[start:end]  
        thread = threading.Thread(target=quicksort_parallel, args=(s, result, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    sorted_parts = result
    return merge_sorted_arrs(sorted_parts)


def merge_sorted_arrs(arrs):
    if len(arrs) == 1:
        return a[0]
    result = []
    indices = [0] * len(arrs)
    while True:
        min_val = None
        min_index = -1
        for i, arr in enumerate(arrs):
            if indices[i] < len(arr):
                if min_val is None or arr[indices[i]] < min_val:
                    min_val = arr[indices[i]]
                    min_index = i
        if min_index == -1:
            break   
        result.append(min_val)
        indices[min_index] += 1
    return result
    
arr = [3, 6, 8, 10, 1, 2, 1,4,5,7,8,5,3,2,2,34,56,7,89,0,9,87,6,5]

a = par_quicksort(arr,2)
print(a)

    
