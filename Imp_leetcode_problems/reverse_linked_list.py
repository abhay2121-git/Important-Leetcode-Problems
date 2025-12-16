# Input: head = [1,2,3,4,5]  : 1->2->3->4->5
# Output: [5,4,3,2,1]   : 5->4->3->2->1

# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            next_temp = cur.next
            cur.next = prev

            prev = cur
            cur = next_temp
        
        return prev