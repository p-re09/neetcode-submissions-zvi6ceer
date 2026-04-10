from typing import List

class Solution:
    def twoSum(self, numbers, target):
        start_pointer = 0
        end_pointer = len(numbers)
        while numbers[start_pointer] + numbers[end_pointer - 1] != target:
            if numbers[start_pointer] + numbers[end_pointer - 1] > target:
                end_pointer -= 1
            else:
                start_pointer += 1
        
        return [start_pointer + 1, end_pointer]
                
