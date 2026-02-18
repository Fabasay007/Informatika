import time
def measure_execution_time(func, *args, **kw):
    start_time = time.time()  # Начинаем отсчет времени
    result = func(*args, **kw)  # Выполняем переданную функцию с аргументами
    end_time = time.time()  # Останавливаем отсчет времени
    execution_time = (end_time - start_time) * 1000  # Время в миллисекундах
    return result, execution_time

def pops_element(lists,values):
    for i,j in enumerate(lists):
        if j == values:
            lists.pop(i)
    return 0

lst = [0]*99999999 + [5]

print(measure_execution_time(pops_element,lst,5), len(lst)+1)