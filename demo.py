import collections

def solve_maze_iddfs(grid, start, target, max_depth=None):
    
    rows, cols = len(grid), len(grid[0])
    
    if max_depth is None:
        max_depth = rows * cols 

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs_limited(current_node, current_path, current_depth, limit):
        
        if current_node == target:
            return True, current_path
        
        if current_depth == limit:
            return False, []

        r, c = current_node
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            next_node = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and \
               grid[nr][nc] == 0 and next_node not in current_path:
                
                found, final_path = dfs_limited(
                    next_node, 
                    current_path + [next_node], 
                    current_depth + 1, 
                    limit
                )
                
                if found:
                    return True, final_path
        
        return False, []

    for limit in range(1, max_depth + 1):
        found, path = dfs_limited(start, [start], 0, limit)
        
        if start == target:
             return True, [start], 0

        if found:
            return True, path, limit
    
    return False, [], max_depth

print("--- Case #1 ---")
grid1 = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1]
]
start1 = (0, 0)
target1 = (2, 3)

found1, path1, depth1 = solve_maze_iddfs(grid1, start1, target1)

if found1:
    print(f"Path found at depth {depth1} using IDDFS")
    print(f"Traversal Order: {path1}")
else:
    print(f"Path not found at max depth {depth1} using IDDFS")

print("\n")

print("--- Case #2 ---")
grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
start2 = (0, 0)
target2 = (2, 2)
max_depth2 = 6 

found2, path2, depth2 = solve_maze_iddfs(grid2, start2, target2, max_depth=max_depth2)

if found2:
    print(f"Path found at depth {depth2} using IDDFS")
    print(f"Traversal Order: {path2}")
else:
    print(f"Path not found at max depth {depth2} using IDDFS")