class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
      
        top_row = 0
        bottom_row = len(matrix)
       
        target_row = -1

        while top_row < bottom_row:
            
            mid_row = (bottom_row + top_row) //2
            if matrix[mid_row][0]>target:
                bottom_row = mid_row
            elif matrix[mid_row][-1]<target:
                top_row = mid_row + 1
            else:
                target_row = mid_row
                break

        if target_row == -1:
            return False
        
        left_col = 0
        right_col = len(matrix[0])

        while left_col < right_col:

            mid = (left_col + right_col) // 2
            if matrix[target_row][mid]<target:
                left_col = mid + 1
            elif matrix[target_row][mid]>target:
                right_col = mid
            else:
                return True
        return False
        