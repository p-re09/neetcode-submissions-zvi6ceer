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
                print(f"{stack} + {stack[-1]} + {temperatures[i]}")
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
        '''boolc = False
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                stack.append(temperatures[i])
                res.appendleft(0)
                cnt_map[temperatures[i]] = count
                continue
            while stack and temperatures[i] > stack[-1]:
                print(f"{stack} + {stack[-1]} + {cnt_map[stack[-1]]} + {temperatures[i]} + {count}")
                count += cnt_map[stack[-1]]
                print(count)
                stack.pop()
                boolc = True
            #print(count)
            if not stack and boolc:
                res.appendleft(0)
            elif boolc:
                #print(res)
                res.appendleft(count)
               
            if not boolc and stack and temperatures[i] < stack[-1]:
                count = 1
                res.appendleft(count)
            stack.append(temperatures[i])
            cnt_map[temperatures[i]] = count
            boolc = False

            #print(cnt_map)
        return list(res)'''