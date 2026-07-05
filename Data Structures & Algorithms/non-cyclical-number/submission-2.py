class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            total = 0

            while n:
                digit = n % 10
                total += digit * digit
                n //= 10

            return total
        
        slow = n
        fast = getNext(n)

        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1