class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        heights = deque()
        res = []
        hashmap = {}
        for i in range(len(nums2) - 1, -1, -1):
            if not stack:
                stack.append(nums2[i])
                heights.appendleft(-1)
                hashmap[nums2[i]] = heights[0]
                continue
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if not stack:
                heights.appendleft(-1)
            else:
                heights.appendleft(stack[-1])
            stack.append(nums2[i])
                
            if nums2[i] < stack[-1]:
                heights.appendleft(stack[-1])
                stack.append(nums2[i])
            hashmap[nums2[i]] = heights[0]
        print(hashmap)
        for i in range(len(nums1)):
            res.append(hashmap[nums1[i]])
        return res
