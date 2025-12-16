# Linked List Cycle
# Input: head = [3,2,0,-4], pos = 1
# Output: true

# Input: head = [1,2], pos = 0
# Output: true

# Input: head = [1], pos = -1
# Output: false


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# Helper function to create linked list with optional cycle
def createLinkedList(values, pos):
    head = ListNode(values[0])
    current = head 
    nodes = [head]

    for val in values[1:]:
        newNode = ListNode(val)
        current.next = newNode
        current = newNode
        nodes.append(newNode)

    if pos != -1:  # create cycle
        current.next = nodes[pos]

    return head


# Test 1: has cycle
head1 = createLinkedList([3, 2, 0, -4], 1)  # cycle at index 1
print(Solution().hasCycle(head1))  # Output: True

# Test 2: no cycle
head2 = createLinkedList([1], -1)
print(Solution().hasCycle(head2))  # Output: False
