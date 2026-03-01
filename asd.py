import random

def monte_carlo_circle_area(radius, num_points=1000):
    inside_points = 0
    for _ in range(num_points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if 1<x and x<2 and (-x**2 + 6*x + 3) > (3*x**2 - 2*x - 6):
            inside_points += 1

    # Площадь квадрата, в который вписан круг = (2*radius)^2
    square_area = (2 * radius) ** 2
    circle_area = (inside_points / num_points) * square_area
    return circle_area

# Пример использования
radius = 5
estimated_area = monte_carlo_circle_area(radius)
print(f"Оцененная площадь круга с радиусом {radius}: {estimated_area}")

