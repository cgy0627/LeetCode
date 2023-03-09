# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = False
        middle = head
        now = head
        
        while now.next:
            even = not even
            now = now.next
            if even:
                middle = middle.next
        
        return middle