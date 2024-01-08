class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        matrix_len = len(grid)
        end_index = matrix_len - 2        
        for start_row in range(0, end_index):
            result.append([])
            for start_col in range(0, end_index):
                local_max = 0
                for current_row in range(start_row, start_row + 3):
                    for current_col in range(start_col, start_col + 3):
                        local_max = max(grid[current_row][current_col], local_max)
                result[start_row].append(local_max)
        return result
