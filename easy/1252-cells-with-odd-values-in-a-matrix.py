class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        result_rows = [False] * m
        result_cols = [False] * n
        
        for row_index, col_index in indices:
            result_rows[row_index] = not result_rows[row_index]
            result_cols[col_index] = not result_cols[col_index]
            
        return sum(r ^ c for c in result_cols for r in result_rows)

  class Solution2:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        result_list = []
        for r in range(m):
            result_list.append([0] * n)
        
        for row_index, col_index in indices:
            for current_col in range(n):
                result_list[row_index][current_col] += 1
            for current_row in range(m):
                result_list[current_row][col_index] += 1
        
        result = 0
        for row in result_list:
            for num in row:
                if num % 2 == 0:
                    continue
                result += 1
                
        return result
