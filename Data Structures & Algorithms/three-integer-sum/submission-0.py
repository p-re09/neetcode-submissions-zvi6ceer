class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 1):
            j, k, = i + 1, len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[j], nums[k], nums[i]])

                    j += 1
                    k -= 1

        normalized = [tuple(sorted(triplet)) for triplet in res]
        unique_res = set(normalized)
        final_res = [list(triplet) for triplet in unique_res]
        
        return final_res  




