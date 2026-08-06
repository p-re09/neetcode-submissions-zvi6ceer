class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:     
        if not board:
            return False

        rows, cols = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        count = 0
        visit = set()

        def dfs(row,col,q):
            visit.add((row,col))
            q_copy = deque(q)
            q_copy.popleft() 
            #print(q)
            if not q_copy:
                return True
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and board[r][c] == q_copy[0] and (r,c) not in visit:
                    print(q_copy)
                    if dfs(r,c,q_copy):
                        return True
                    visit.remove((r,c))
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    q = collections.deque([i for i in word])
                    word_found = dfs(row,col, q)
                    visit = set()
                    if word_found:
                        return True
        return False
                    
        