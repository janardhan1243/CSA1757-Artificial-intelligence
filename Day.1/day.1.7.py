from collections import deque

def bfs(graph, start):
    # Initialize the visited set and queue
    visited = set()  
    queue = deque([start])
    
    # Keep track of the traversal order
    traversal_order = []
    
    # Loop while the queue is not empty
    while queue:
        # Dequeue the next node from the queue
        node = queue.popleft()
        
        # If the node has not been visited, mark it as visited
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            
            # Enqueue all unvisited neighbors of the node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for BFS
start_node = 'A'

# Perform BFS
bfs_traversal = bfs(graph, start_node)

# Output the traversal order
print("BFS Traversal Order:", bfs_traversal)
