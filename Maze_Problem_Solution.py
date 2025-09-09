from collections import deque

def bfs_maze_solver(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([start])
    visited = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]
        
        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != 1 and (r, c) not in visited:
                queue.append((r, c))
                visited[(r, c)] = current
    
    return None  # No path found

# Define the maze
maze = [
    [0, 'S', 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 'G']
]

start = (0, 1)
goal = (4, 4)

# Convert maze symbols to numerical values for processing
numeric_maze = [[0 if cell == 'S' or cell == 'G' or cell == 0 else 1 for cell in row] for row in maze]

# Find path
path = bfs_maze_solver(numeric_maze, start, goal)

print("Maze Solution using BFS:")
print(f"Start: {start}")
print(f"Goal: {goal}")
print(f"Path: {path}")