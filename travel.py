import itertools
import sys


"""def calculate_distance(city1, city2):
    # Calculate the Euclidean distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
"""

def calculate_total_distance(path, distances):
    # Calculate the total distance of a given path
    total_distance = 0
    for i in range(len(path) - 1):
        city1 = path[i]
        city2 = path[i + 1]
        total_distance += distances[city1][city2]
    return total_distance


def tsp_optimal_solution(distances):
    n = len(distances)
    cities = range(n)
    optimal_path = None
    optimal_cost = sys.maxsize

    # Generate all possible permutations of the cities
    all_permutations = itertools.permutations(cities)
    '''print(type(all_permutations))'''
    for permutation in all_permutations:
        # Add the starting city at the end of the permutation
        path = list(permutation) + [permutation[0]]

        # Calculate the total distance for the current path
        total_distance = calculate_total_distance(path, distances)

        # Update the optimal path and cost if a better solution is found
        if total_distance < optimal_cost:
            optimal_path = path
            optimal_cost = total_distance

    return optimal_cost, optimal_path


def tsp_approximation_solution(distances):
    n = len(distances)
    current_city = 0
    visited_cities = {current_city}
    approximation_path = [current_city]
    approximation_cost = 0

    while len(visited_cities) < n:
        min_distance = sys.maxsize
        next_city = None

        # Find the nearest unvisited city
        for city in range(n):
            if city not in visited_cities and distances[current_city][city] < min_distance:
                min_distance = distances[current_city][city]
                next_city = city

        # Move to the next city
        current_city = next_city
        visited_cities.add(current_city)
        approximation_path.append(current_city)
        approximation_cost += min_distance

    # Add the starting city to complete the cycle
    approximation_path.append(0)
    approximation_cost += distances[current_city][0]

    return approximation_cost, approximation_path


# Example usage

# Distance matrix representing the distances between cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Optimal solution
optimal_cost, optimal_path = tsp_optimal_solution(distances)
print("Optimal Solution:")
print("The optimal path is:", optimal_path)
print("The optimal cost is:", optimal_cost)

# Approximation solution
approx_cost, approx_path = tsp_approximation_solution(distances)
print("\nApproximation Solution:")
print("The approximated path is:", approx_path)
print("The approximated cost is:", approx_cost)

# Calculate the error in the approximation
error = ((approx_cost - optimal_cost) / optimal_cost) * 100
print("\nError in approximation is:", error, "%")