import numpy as np
from tabu_search import parse_rucksack_data, TabuSearch
from SA_TSP import parse_input, simulated_annealing


def main_tabu_search():
    file_path = "data.txt"
    num_objects, values, weights, max_weight = parse_rucksack_data(file_path)
    iterations = 10000

    tabu_list_size = 10

    tabu_search = TabuSearch(num_objects, values, weights, max_weight, tabu_list_size)
    k, avg_score, avg_weight, best_score, runtime, best_solution = tabu_search.search(iterations)

    print("Tabu Search Algorithm Results:")
    print("k (iterations):", k)
    print("Average Score:", avg_score)
    print("Average Weight:", avg_weight)
    print("Best Score:", best_score)
    print("Runtime:", runtime, "seconds")
    print("Best Solution:", best_solution)


def main_SA_TSP(filename, max_iterations, T_max, T_min, alpha):
    cities = parse_input(filename)
    num_solutions, total_distance, best_distance, runtime = simulated_annealing(cities, max_iterations, T_max, T_min, alpha)
    average_distance = total_distance / num_solutions
    print("Number of iterations:", num_solutions)
    print("Average length of route:", average_distance)
    print("Best route:", best_distance)
    print("Runtime:", runtime)


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Tabu Search Algorithm")
        print("2. SA TSP Problem")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            main_tabu_search()
        elif choice == "2":
            filename = "tsp.txt"
            max_iterations = 100000
            T_max = 10000
            T_min = 0.00001
            alpha = 0.9999
            main_SA_TSP(filename, max_iterations, T_max, T_min, alpha)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
