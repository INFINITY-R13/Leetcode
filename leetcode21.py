# 21. Merge Two Sorted Lists
"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        p1, p2 = list1, list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # Attach remaining nodes
        if p1:
            current.next = p1
        elif p2:
            current.next = p2
        
        return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to list for easy printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
def test_merge_two_lists():
    solution = Solution()
    
    # Test case 1: Regular merge
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 1: {linked_list_to_list(result)}")  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test case 2: One empty list
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 2: {linked_list_to_list(result)}")  # Expected: [0]
    
    # Test case 3: Both empty lists
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 3: {linked_list_to_list(result)}")  # Expected: []
    
    # Test case 4: Different lengths
    list1 = create_linked_list([1, 3, 5, 7])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 4: {linked_list_to_list(result)}")  # Expected: [1, 2, 3, 4, 5, 7]
    
    # Test case 5: All elements in list1 smaller than list2
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 5: {linked_list_to_list(result)}")  # Expected: [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    test_merge_two_lists()