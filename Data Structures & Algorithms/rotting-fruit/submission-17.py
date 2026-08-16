class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        visit = set()
        new_grid = []
        grid_index = []
        q = collections.deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        ans = -1
        no_ones = True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([2,i,j])
                    visit.add((i,j))
                if grid[i][j] == 1:
                    no_ones = False

        if not q and no_ones:
            return 0

        for i in range(rows):
            for j in range(cols):
                grid_index.append([grid[i][j],i,j])
            new_grid.append(grid_index)
            grid_index = []

        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    for dr, dc in directions:
                        r,c = dr + node[1], dc + node[2]
                        if r in range(rows) and c in range(cols) and new_grid[r][c][0] == 1 and (r,c) not in visit:
                            q.append([new_grid[r][c][0],r,c])
                            visit.add((r,c))
            ans += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    return -1
        return ans