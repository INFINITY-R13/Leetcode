# 2. Add Two Numbers
""""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    carry = 0
    fake_head = ListNode(0)
    current = fake_head
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return fake_head.next

# Helper functions for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" → ".join(values))

# Test Case 1: 342 + 465 = 807
print("Test 1:")
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
print("  Input: ", end="")
print_linked_list(l1)
print("       + ", end="")
print_linked_list(l2)
result = addTwoNumbers(l1, l2)
print("  Output:", end=" ")
print_linked_list(result)
print()

# Test Case 2: 0 + 0 = 0
print("Test 2:")
l1 = create_linked_list([0])
l2 = create_linked_list([0])
print("  Input: ", end="")
print_linked_list(l1)
print("       + ", end="")
print_linked_list(l2)
result = addTwoNumbers(l1, l2)
print("  Output:", end=" ")
print_linked_list(result)
print()

# Test Case 3: 9999999 + 9999 = 10009998
print("Test 3:")
l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
print("  Input: ", end="")
print_linked_list(l1)
print("       + ", end="")
print_linked_list(l2)
result = addTwoNumbers(l1, l2)
print("  Output:", end=" ")
print_linked_list(result)
