class Solution:
    def trap(self, height: List[int]) -> int:
        
        stored_water, max_prefix, max_suffix = 0, 0, 0
        prefix, suffix = [0], deque()
        for i in range(1, len(height)):
            max_prefix = max(height[i - 1], max_prefix)
            prefix.append(max_prefix)
        
        for i in range(len(height) - 1, -1, -1):
            suffix.appendleft(max_suffix)
            max_suffix = max(height[i], max_suffix)

        for i in range(len(height)) :
            stored_water += max(0, min(prefix[i], suffix[i]) - height[i])

        return stored_water