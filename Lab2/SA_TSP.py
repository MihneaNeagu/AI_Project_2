import math
import random
import time


class City:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y


def parse_input(filename):
    cities = []
    with open(filename, 'r') as file:
        lines = file.readlines()[6:-1]
        for line in lines:
            parts = line.split()
            city = City(int(parts[0]), int(parts[1]), int(parts[2]))
            cities.append(city)
    return cities


def euclidean_distance(city1, city2):
    xd = city1.x - city2.x
    yd = city1.y - city2.y
    return round(math.sqrt(xd**2 + yd**2))


def initial_solution(cities):
    return random.sample(cities, len(cities))


def swap(cities):
    # 2-opt neighbor generation
    new_cities = cities[:]
    i, j = random.sample(range(len(cities)), 2)
    if i > j:
        i, j = j, i
    new_cities[i:j+1] = reversed(new_cities[i:j+1])
    return new_cities


def evaluate(solution):
    total_distance = 0
    for i in range(len(solution)):
        total_distance += euclidean_distance(solution[i], solution[(i + 1) % len(solution)])
    return total_distance


def simulated_annealing(cities, max_iterations, T_max, T_min, alpha):
    for _ in range(10):  # 10 rulari
        start_time = time.time()
        current_solution = initial_solution(cities)
        best_solution = current_solution
        best_distance = evaluate(best_solution)
        T = T_max
        total_distance = 0
        num_solutions = 0

        for k in range(max_iterations):
            new_solution = swap(current_solution)
            delta = evaluate(new_solution) - evaluate(current_solution)

            if delta < 0 or random.random() < math.exp(-delta / T):
                current_solution = new_solution

            distance = evaluate(current_solution)
            total_distance += distance
            num_solutions += 1

            if distance < best_distance:
                best_solution = current_solution
                best_distance = distance

            T *= alpha
            if T < T_min:
                break

        end_time = time.time()
        runtime = end_time - start_time
        return num_solutions, total_distance, best_distance, runtime

