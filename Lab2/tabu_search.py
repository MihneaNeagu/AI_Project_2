import time
import numpy as np

def generate_random_solution(num_objects):
    return np.random.randint(2, size=num_objects)


def is_valid(solution, weights, max_weight):
    total_weight = np.sum(solution * weights)
    return total_weight <= max_weight


def evaluate_solution(solution, values):
    return np.sum(solution * values)


def get_neighborhood(current_solution):
    neighborhood = []
    num_objects = len(current_solution)

    for i in range(num_objects):
        neighbor = np.copy(current_solution)
        neighbor[i] = 1 - neighbor[i]  # Bit swap
        neighborhood.append(neighbor)

    return neighborhood


class TabuSearch:

    def __init__(self, num_objects, values, weights, max_weight, tabu_list_size):
        self.num_objects = num_objects
        self.values = values
        self.weights = weights
        self.max_weight = max_weight
        self.tabu_list = []
        self.tabu_list_size = tabu_list_size

    def search(self, iterations):
        for _ in range(10): # 10 rulari
            best_solution = None
            best_score = float('-inf')
            valid_scores = []
            valid_weights = []
            start_time = time.time()

            for _ in range(iterations):
                current_solution = generate_random_solution(self.num_objects)
                current_score = evaluate_solution(current_solution, self.values)

                if is_valid(current_solution, self.weights, self.max_weight):
                    valid_scores.append(current_score)
                    valid_weights.append(np.sum(current_solution * self.weights))

                if current_score > best_score:
                    best_solution = current_solution
                    best_score = current_score

                if len(self.tabu_list) >= self.tabu_list_size:
                    self.tabu_list.pop(0)

                self.tabu_list.append(current_solution)

            end_time = time.time()
            runtime = end_time - start_time

            # Calculate average score and weight of valid solutions
            average_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0
            average_weight = sum(valid_weights) / len(valid_weights) if valid_weights else 0

            return iterations, average_score, average_weight, best_score, runtime, best_solution


def parse_rucksack_data(file_path):
    values = []
    weights = []
    max_weight = None
    num_objects = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

        num_objects = int(lines[0])

        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 3:
                values.append(int(parts[1]))
                weights.append(int(parts[2]))
            elif len(parts) == 1:
                max_weight = int(parts[0])

    return num_objects, values, weights, max_weight

