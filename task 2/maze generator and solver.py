import random

def create_maze(rows, cols):
    """Create a grid representing the maze."""
    maze = [["#" for _ in range(cols)] for _ in range(rows)]
    return maze
def generate_maze(maze, start_row, start_col):
    """Generate a random maze using DFS."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    
    for direction in directions:
        new_row = start_row + direction[0] * 2
        new_col = start_col + direction[1] * 2
        
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == "#":
            maze[new_row][new_col] = " "
            maze[start_row + direction[0]][start_col + direction[1]] = " "
            generate_maze(maze, new_row, new_col)

def print_maze(maze):
    """Print the maze in the terminal."""
    for row in maze:
        print("".join(row))
def is_solvable(maze, start, end):
    """Check if the maze is solvable using BFS."""
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set()
    visited.add(start)
    
    while queue:
        row, col = queue.pop(0)
        if (row, col) == end:
            return True
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + direction[0], col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == " " and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))
    
    return False
rows, cols = 11, 11
maze = create_maze(rows, cols)
start, end = (0, 0), (rows - 1, cols - 1)
maze[start[0]][start[1]] = " "
generate_maze(maze, start[0], start[1])

# Ensure the maze is solvable
if is_solvable(maze, start, end):
    print("Maze is solvable:")
else:
    print("Maze is not solvable.")

print_maze(maze)
