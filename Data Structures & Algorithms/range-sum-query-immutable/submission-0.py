class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        totalSum = 0
        prefixSum = [0] * (len(self.nums) + 1)
        print(len(prefixSum))
        print(len(self.nums))
        for i in range(len(self.nums)):
            sum += self.nums[i]
            prefixSum[i + 1] = sum
        return (prefixSum[right + 1] - prefixSum[left])
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)