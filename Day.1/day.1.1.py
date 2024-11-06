import heapq

# Define the 8-puzzle goal state
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Helper functions to find the position of a value in the puzzle
def find_position(value, state):
    for i, row in enumerate(state):
        if value in row:
            return i, row.index(value)
    return None

# Heuristic function: Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = find_position(value, GOAL_STATE)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Check if the current state is the goal state
def is_goal(state):
    return state == GOAL_STATE

# Get neighbors of the current state (possible moves)
def get_neighbors(state):
    neighbors = []
    x, y = find_position(0, state)  # Find the blank tile position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Swap the blank with the neighboring tile
            new_state = [row[:] for row in state]  # Deep copy
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# A* Search algorithm
def a_star(start):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start), start, 0, []))  # (heuristic + cost, state, cost, path)
    visited = set()

    while open_set:
        estimated_cost, state, cost, path = heapq.heappop(open_set)

        if is_goal(state):
            return path + [state]  # Return the path to reach the goal

        # Mark the current state as visited by hashing the tuple version
        visited.add(tuple(tuple(row) for row in state))

        for neighbor in get_neighbors(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                new_cost = cost + 1
                estimated_cost = new_cost + manhattan_distance(neighbor)
                heapq.heappush(open_set, (estimated_cost, neighbor, new_cost, path + [state]))

    return None  # No solution found

# Helper function to print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(tile) if tile != 0 else " " for tile in row))
    print()

# Example Usage
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution_path = a_star(initial_state)
if solution_path:
    print("Solution found in", len(solution_path) - 1, "moves:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        print_state(state)
else:
    print("No solution found.")
