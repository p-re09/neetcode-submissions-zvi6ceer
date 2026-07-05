# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        def size_iterative(self, head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count
        
        for _ in range(size_iterative(self , head) // 2):
            slow = slow.next
        return slow