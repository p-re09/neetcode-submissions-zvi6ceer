from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        count = 0
        product_exists = False
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product_exists = True
        if product_exists == True:
            total_product = 1
        else:
            total_product = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
        print(f"{total_product} ---")
        if not 0 in nums:
            for i in range(len(nums)):
                nums[i] = int(total_product/nums[i])
        else:
            if count > 1 :
                for i in range(len(nums)):
                    nums[i] = 0 
            else:  
                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i] = total_product
                    else:
                        nums[i] = 0
        return nums

nums=[0,8,0]
p1 = Solution()
print(p1.productExceptSelf(nums))
        