class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""
        
        if len(words) == 1:
            return words[0]
        
        visit = set()
        cycle = set()
        ans = []
        char_set = set()
        correct_order = False
        index = 0

        for i in words:
            for j in i:
                char_set.add(j)
        
        order_map = {c:[] for c in char_set}
        
        for i in range(len(words) - 1):
            if len(words[i]) > len(words[i + 1]):
                while words[i][index] == words[i + 1][index]:
                    index += 1
                    if index not in range(len(words[i + 1])):
                        return ""
            elif len(words[i + 1]) >= len(words[i]):
                while words[i][index] == words[i + 1][index]:
                    index += 1
                    if index not in range(len(words[i])):
                        correct_order = True
                        break
            if correct_order == False:
                order_map[words[i + 1][index]].append(words[i][index])
            index = 0
            correct_order = False

        def dfs(char):
            if char in cycle:
                return False
            if char in visit:
                return True

            cycle.add(char)
            for i in order_map[char]:
                if dfs(i) == False:
                    return False

            cycle.remove(char)
            visit.add(char)
            ans.append(char)
            return True

        for i in order_map:
            if dfs(i) == False:
                return ""

        final_ans = ''.join(ans)
        return final_ans
        
        