from collections import deque

# Define the state space of the vacuum cleaner problem
def vacuum_cleaner_problem(start_state):
    # Possible actions
    def clean(state):
        current_room, left_room, right_room = state
        if current_room == 'L' and left_room == 'D':  # Clean Left room if it's dirty
            return ('L', 'C', right_room)
        elif current_room == 'R' and right_room == 'D':  # Clean Right room if it's dirty
            return ('R', left_room, 'C')
        return state

    def move_left(state):
        current_room, left_room, right_room = state
        if current_room == 'R':
            return ('L', left_room, right_room)
        return state

    def move_right(state):
        current_room, left_room, right_room = state
        if current_room == 'L':
            return ('R', left_room, right_room)
        return state

    # Goal state: both rooms are clean
    goal_state = ('L', 'C', 'C')

    # Perform BFS (Breadth-First Search) to find the solution path
    queue = deque([(start_state, [])])  # (current state, path taken to get here)
    visited = set([start_state])  # Set to store visited states

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        # Apply actions
        next_states = [
            clean(current_state),
            move_left(current_state),
            move_right(current_state)
        ]
        
        # Add next states to the queue if they have not been visited
        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # If no solution is found

# Print the solution path
def print_solution(path):
    if path is None:
        print("No solution found.")
    else:
        print("Solution path:")
        for step, state in enumerate(path):
            current_room, left_room, right_room = state
            print(f"Step {step + 1}: Vacuum cleaner at {current_room}, Left: {left_room}, Right: {right_room}")
        print("Goal Reached: Both rooms are clean.")

# Initial state: 'L' is Left, 'R' is Right, 'D' is Dirty, 'C' is Clean
start_state = ('L', 'D', 'D')  # Vacuum cleaner starts in the Left room with both rooms dirty

# Solve the problem
solution_path = vacuum_cleaner_problem(start_state)
print_solution(solution_path)
