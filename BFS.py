from collections import deque

class BFS:
    @staticmethod
    def grid(rows, columns, start, end):
        grid = [[0] * columns for _ in range(rows)]
        
        start_row, start_col = divmod(start, columns)
        grid[start_row][start_col] = start
    
        end_row, end_col = divmod(end, columns)
        grid[end_row][end_col] = end
    
        return grid
    
    @staticmethod
    def print_grid(grid, start, end, optimal_path):
        grid_copy = [row[:] for row in grid]

        for point in optimal_path:
            grid_copy[point[0]][point[1]] = -1

        for row in grid_copy:
            for cell in row:
                if cell == start:
                    print("S", end=" ")
                elif cell == end:
                    print("E", end=" ")
                elif cell == -1:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
    
    @staticmethod
    def bfs(rows, cols, start, end):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        parent_map = {}
        queue = deque()
        start_point = (start // cols, start % cols)
        end_point = (end // cols, end % cols)
        
        queue.append(start_point)
        parent_map[start_point] = None
        optimal_path = []
        
        while queue:
            curr = queue.popleft()
            if curr == end_point:
                backtrack = curr
                while backtrack is not None:
                    optimal_path.append(backtrack)
                    backtrack = parent_map.get(backtrack)
                optimal_path.reverse()
                return optimal_path
            for i in range(4):
                new_x = curr[0] + dx[i]
                new_y = curr[1] + dy[i]
                new_point = (new_x, new_y)
                if 0 <= new_x < rows and 0 <= new_y < cols and new_point not in parent_map:
                    queue.append(new_point)
                    parent_map[new_point] = curr
        
        return None

if __name__ == "__main__":
    print("Enter number of rows:")
    rows = int(input())
    print("Enter number of columns:")
    cols = int(input())
    print("Enter the starting position:")
    start = int(input())
    print("Enter the ending position:")
    end = int(input())

    grid = BFS.grid(rows, cols, start, end)
    BFS.print_grid(grid, start, end, [])

    optimal_path = BFS.bfs(rows, cols, start, end)
    if optimal_path:
        print("Optimal Path:")
        for point in optimal_path:
            print(point)
        BFS.print_grid(grid, start, end, optimal_path)
    else:
        print("No path exists from S to E.")
