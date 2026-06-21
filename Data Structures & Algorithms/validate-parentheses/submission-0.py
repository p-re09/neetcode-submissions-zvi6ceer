class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackMap = {'(' : ')', '{' : '}','[' : ']'}
        for i in range(len(s)):
            if s[i] in stackMap:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == stackMap[stack[len(stack) - 1]]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False