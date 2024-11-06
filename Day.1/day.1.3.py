from collections import deque
def water_jug_bfs(jug_x, jug_y, goal):
    queue = deque([(0, 0, [])])  
    visited = set()
    while queue:
        x, y, steps = queue.popleft()
        if x == goal or y == goal:
            steps.append((x, y))
            return steps  
        if (x, y) in visited:
            continue
        visited.add((x, y))
        current_steps = steps + [(x, y)]
        moves = [
            (jug_x, y),  
            (x, jug_y),  
            (0, y),      
            (x, 0),      
            (x - min(x, jug_y - y), y + min(x, jug_y - y)),  
            (x + min(y, jug_x - x), y - min(y, jug_x - x))  
        ]
        for new_x, new_y in moves:
            if (new_x, new_y) not in visited:
                queue.append((new_x, new_y, current_steps))
    return None
def print_solution(steps):
    if steps:
        print("Steps to reach the goal:")
        for x, y in steps:
            print(f"Jug X: {x}L, Jug Y: {y}L")
    else:
        print("No solution found.")
jug_x = 4  
jug_y = 3
goal = 2
solution = water_jug_bfs(jug_x, jug_y, goal)
print_solution(solution)
