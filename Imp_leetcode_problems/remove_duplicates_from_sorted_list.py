# Example 1
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_duplicates_from_sorted_list(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# Helper function to create linked list
def createLinkedList(values):
    head = ListNode(values[0])
    current = head 
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Input values
values = [1, 1, 2]
head = createLinkedList(values)

# Call the method
solution = Solution()
new_head = solution.remove_duplicates_from_sorted_list(head)

# Print result
printLinkedList(new_head)