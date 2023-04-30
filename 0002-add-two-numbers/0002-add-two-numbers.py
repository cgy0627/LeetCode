# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1 = self.nodeToInt(l1)
        num2 = self.nodeToInt(l2)
        
        res = num1 + num2
        
        resNode = ListNode()
        curr = resNode
        for d in str(res)[::-1]:
            curr.next = ListNode()
            curr = curr.next
            curr.val = int(d)
        
        return resNode.next
        
    def nodeToInt(self, nodeList):
        num = 0
        i = 0
        while nodeList:
            num = nodeList.val * pow(10, i) + num
            nodeList = nodeList.next
            i += 1
        
        return num
