class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        boolc = False
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            
            while stack and temperatures[i] > stack[-1][0]:
                steps = i - stack[-1][1]
                res[stack[-1][1]] += steps
                stack.pop()
                boolc = True 
            if boolc:
                stack.append([temperatures[i], i])
            if not boolc and stack and temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
            boolc = False
        return res