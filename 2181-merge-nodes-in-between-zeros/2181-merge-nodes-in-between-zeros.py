# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = pointer = head
        
        while pointer.next:
            pointer = pointer.next
            
            if pointer.val != 0:
                curr.val += pointer.val
            else:
                if pointer.next:
                    curr = curr.next
                    curr.val = 0
                else:
                    curr.next = None
            
        return head