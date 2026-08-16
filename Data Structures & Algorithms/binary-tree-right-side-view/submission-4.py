# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            qLen = len(q)
            for i in q:
                if i:
                    print(i.val)
                else:
                    print("hehe")
            print("-")
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if i + 1 == qLen:
                        ans.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        return ans
        
        