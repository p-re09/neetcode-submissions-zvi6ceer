class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        num_array = []
        for i in digits:
            num_array.append(str(i))
        
        num = ''.join(num_array)
        new_num = int(num) + 1
        
        for i in str(new_num):
            ans.append(i)
        
        return ans

        