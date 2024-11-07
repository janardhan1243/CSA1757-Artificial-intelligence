import itertools

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Return to starting point
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = range(n)
    shortest_route = None
    min_distance = float('inf')
    
    for route in itertools.permutations(cities):
        distance = calculate_total_distance(route, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            shortest_route = route
    
    return shortest_route, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_route, min_distance = tsp_brute_force(distance_matrix)
print(f"Shortest route: {shortest_route}")
print(f"Minimum distance: {min_distance}")
