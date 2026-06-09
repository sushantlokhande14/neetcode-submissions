class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #finding the row 
        top = 0 
        bot = ROWS - 1 

        while top <= bot: 
            tar_row = (top+bot)//2 

            if target > matrix[tar_row][-1]: 
                top = tar_row + 1 
            elif target < matrix[tar_row][0]: 
                bot = tar_row - 1 
            else: 
                break 
        


        l = 0 
        r = COLS -1 
        while l <= r : 
            m = (l+r)//2 

            if target > matrix[tar_row][m]: 
                l = m + 1 
            elif target < matrix[tar_row][m]:
                r = m -1 
            else : 
                return True 

        return False  



