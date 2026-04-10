from typing import List

class Solution:
    def has_duplicates(self, lst):
        element_to_remove = '.'
        result = [x for x in lst if x != element_to_remove]
        print(result)
        return len(result) != len(set(result))
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if self.has_duplicates(i) == True:
                return False
        
        for num in range(9):
            columns = []
            for num2 in range(9):
                columns.append(board[num2][num])
            if self.has_duplicates(columns) == True:
                return False
        
        columns = []
        # For each of the 3 x 3 sections
        for num in range(3):
             for num2 in range(3):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(3):
             for num2 in range(3, 6):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(3):
             for num2 in range(6, 9):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(3, 6):
             for num2 in range(3):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(3, 6):
             for num2 in range(3, 6):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(3, 6):
             for num2 in range(6, 9):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(6, 9):
             for num2 in range(3):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        columns = []
        for num in range(6, 9):
             for num2 in range(3, 6):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False

        columns = []
        for num in range(6, 9):
             for num2 in range(6, 9):
                  columns.append(board[num][num2])
        if self.has_duplicates(columns) == True:
                    return False
        
        return True
                  
            
        


# Example
nums = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(nums))  

        