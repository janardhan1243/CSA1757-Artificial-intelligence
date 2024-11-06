from collections import deque

def is_valid_state(m, c, boat):
    # Left side missionaries and cannibals
    m_left = m
    c_left = c
    # Right side missionaries and cannibals
    m_right = 3 - m_left  
    c_right = 3 - c_left

    # Ensure no side has more cannibals than missionaries, unless there are no missionaries on that side
    if (m_left >= c_left or m_left == 0) and (m_right >= c_right or m_right == 0):
        return True
    return False

def generate_next_states(m, c, b):
    next_states = []
    
    if b == 0:  # Boat on the left side
        moves = [
            (1, 0),  # Move 1 missionary
            (0, 1),  # Move 1 cannibal
            (2, 0),  # Move 2 missionaries
            (0, 2),  # Move 2 cannibals
            (1, 1)   # Move 1 missionary and 1 cannibal
        ]
    else:  # Boat on the right side
        moves = [
            (-1, 0),  # Move 1 missionary back
            (0, -1),  # Move 1 cannibal back
            (-2, 0),  # Move 2 missionaries back
            (0, -2),  # Move 2 cannibals back
            (-1, -1)  # Move 1 missionary and 1 cannibal back
        ]
    
    for m_move, c_move in moves:
        new_m = m + m_move
        new_c = c + c_move
        new_b = 1 - b  # Toggle the boat position
        # Ensure the new state is within bounds and valid
        if 0 <= new_m <= 3 and 0 <= new_c <= 3 and is_valid_state(new_m, new_c, new_b):
            next_states.append((new_m, new_c, new_b))
    return next_states

def bfs():
    initial_state = (3, 3, 0)  # Start: 3 missionaries, 3 cannibals, boat on left side
    goal_state = (0, 0, 1)     # Goal: 0 missionaries, 0 cannibals, boat on right side
    queue = deque([(initial_state, [])])  # (current state, path to this state)
    visited = set([initial_state])  # Track visited states
    
    while queue:
        current_state, path = queue.popleft()
        m, c, b = current_state
        
        # Check if we've reached the goal
        if current_state == goal_state:
            return path + [goal_state]
        
        # Generate and explore next states
        for next_state in generate_next_states(m, c, b):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

def print_solution(path):
    if path is None:
        print("No solution found.")
    else:
        print("Solution path:")
        for step, state in enumerate(path):
            m, c, b = state
            boat_position = "Left" if b == 0 else "Right"
            print(f"Step {step + 1}: Missionaries: {m}, Cannibals: {c}, Boat: {boat_position}")
        print("Goal Reached!")

# Run the solution
solution_path = bfs()
print_solution(solution_path)
