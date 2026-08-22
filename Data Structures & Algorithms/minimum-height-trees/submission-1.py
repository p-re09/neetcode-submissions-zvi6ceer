class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        visit, cycle = set(), set()
        ans = []
        final_ans = []
        final_final_ans = []
        height = 0
        curr_max = 0
        max_height = 0
        edge_map = {k:[] for k in range(n)}

        for a, b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)

        def dfs(node, height, max_height):
            if node in cycle:
                return False

            new_height = height + 1
            new_max_height = max_height
            cycle.add(node)
            for i in edge_map[node]:
                if dfs(i, new_height, new_max_height) == False:
                    continue
            
            new_max_height = max(new_height, new_max_height)
            ans.append(new_max_height)
            height -= 1
            cycle.remove(node)
            return True

        for i in range(n):
            dfs(i, height, max_height)
            height = 0
            max_height = 0
            for i in ans:
                curr_max = max(i,curr_max)
            final_ans.append(curr_max)
            ans = []
            curr_max = 0
        print(final_ans)
        min_value = math.inf
        for i in final_ans:
            min_value = min(i, min_value)
        print(min_value)
        for i in range(len(final_ans)):
            if final_ans[i] == min_value:
                final_final_ans.append(i)
        return final_final_ans
                



        