import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, heuristic(start, goal)))
    closed_set = set()
    nodes = {start: Node(start)}

    while open_set:
        current_node = heapq.heappop(open_set)
        current_pos = current_node.position

        if current_pos == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_pos)

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

            if 0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and grid[neighbor_pos[0]][neighbor_pos[1]] == 0:
                if neighbor_pos in closed_set:
                    continue

                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor_pos, goal)
                neighbor_node = nodes.get(neighbor_pos, Node(neighbor_pos))

                if neighbor_pos not in nodes or g_cost < neighbor_node.g:
                    neighbor_node.g = g_cost
                    neighbor_node.h = h_cost
                    neighbor_node.f = g_cost + h_cost
                    neighbor_node.parent = current_node
                    nodes[neighbor_pos] = neighbor_node
                    heapq.heappush(open_set, neighbor_node)

    return None

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(start, goal, grid)
print("Path found:", path)
