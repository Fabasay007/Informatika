import time
import random

lst = [random.randint(1,10000) for _ in range(100000)]

def measure_execution_time(func, *args, **kw):
    start_time = time.time()  # Начинаем отсчет времени
    result = func(*args, **kw)  # Выполняем переданную функцию с аргументами
    end_time = time.time()  # Останавливаем отсчет времени
    execution_time = (end_time - start_time) * 1000  # Время в миллисекундах
    return  execution_time


def sort_rascheska(arr):
    n = len(arr)
    step = n-1
    while step >1:
        step = int(step//1.3)
        i =0
        while (i+step)<n:
            if arr[i]> arr[(i+step)]:
                arr[i],arr[(i+step)]=arr[(i+step)],arr[i]
            i+=1
    return arr




def razryad_sor(arr):
    max_num = max(arr)
    raz =1 
    while (max_num // raz)>0:
        arr = sort_raz(arr, raz)
        raz = raz*10
    return arr



def sort_raz(arr,raz):
    box =  [[] for _ in range(10)]
    for i in arr:
        indbox = (i//raz)%10
        box[indbox].append(i)
    arr = together_arr(box)
    return arr   


def together_arr(box):
    tog_arr = []
    for i in box:
        tog_arr.extend(i)
    return tog_arr




def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x< pivot ]
    middle = [x for x in arr if x== pivot ]
    right = [x for x in arr if x> pivot ]
    return quicksort(left)+ middle+ quicksort(right)


a = measure_execution_time(sort_rascheska,lst)
b = measure_execution_time(razryad_sor,lst)
c = measure_execution_time(quicksort,lst)

print(a)
print(b)
print(c)
