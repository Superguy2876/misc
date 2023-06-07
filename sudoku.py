class Solution:

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {i: set() for i in range(9)}

        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rows[i]:
                    return False
                
                if board[i][j] in cols[j]:
                    return False
                
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in boxes[box_index]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[box_index].add(board[i][j])

        return True