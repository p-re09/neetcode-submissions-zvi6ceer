class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        visit = set()
        rows, cols = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        words_set = set(words)
        trie_dummy = collections.deque([])
        trie_step_dummy = set()
        longest_index = 0

        word_section = []
        small_ws = []
        smaller_ws = ""
        complete_sect = set()

        for i in words:
            for j in range(len(i)):
                smaller_ws += i[j]
                if j + 1 in range(len(i)):
                    small_ws.append((smaller_ws,i[j + 1]))
                else:
                    small_ws.append((smaller_ws,""))
            word_section.append(small_ws)
            small_ws = []
            smaller_ws = ""

        for i in word_section:
            for j in i:
                complete_sect.add(j)

        for i in word_section:
            longest_index = max(longest_index, len(i))

        for i in range(longest_index):
            for j in words:
                if i in range(len(j)):
                    trie_step_dummy.add(j[i])
            trie_dummy.append(trie_step_dummy)
            trie_step_dummy = set()

        ans = []
        q_copy = []

        def dfs(row, col):
            visit.add((row,col))
            q_copy.append(board[row][col])
            current_word = ''.join(q_copy)
            if current_word in words_set:
                ans.append(current_word)
            
            for dr, dc in directions:
                r,c = dr + row, dc + col
                if r in range(rows) and c in range(cols) and (current_word, board[r][c]) in complete_sect and (r,c) not in visit:
                    dfs(r, c)
            q_copy.pop()
            visit.remove((row,col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie_dummy[0]:
                    visit = set()
                    word_valid = dfs(row, col)
                    q_copy = []                   

        ans = set(ans)
        return list(ans)
