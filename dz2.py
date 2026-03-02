import random

def monte_carlo_area(num_points):
    inside_points = 0
    for _ in range(num_points):
        x = random.uniform(1,2)
        y = random.uniform(-25, 50)
        if  (-x**2 + 6*x + 3) > y and y> (3*x**2 - 2*x - 6):
            inside_points += 1

    # Площадь прямоугольника
    square_area = 75
    necessary_area = (inside_points / num_points) * square_area
    return necessary_area 

# Пример использования
cnt = 100000000
estimated_area = monte_carlo_area(cnt)
print(estimated_area) 

