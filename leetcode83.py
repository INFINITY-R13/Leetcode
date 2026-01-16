# LeetCode Problem 83: Remove Duplicates from Sorted List


# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    """
    Remove duplicates from a sorted linked list.
    
    Args:
        head: The head node of the sorted linked list
        
    Returns:
        The head of the modified linked list with duplicates removed
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(1) - only using pointers, no extra space
    """
    # Handle empty list
    if not head:
        return head
    
    # Start from the head
    current = head
    
    # Traverse the list
    while current and current.next:
        # If current value equals next value, skip the next node
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            # Move to next node only if no duplicate was found
            current = current.next
    
    return head


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Convert linked list to Python list for easy visualization."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,1,2] -> [1,2]
    head1 = create_linked_list([1, 1, 2])
    result1 = deleteDuplicates(head1)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 2]
    
    # Test case 2: [1,1,2,3,3] -> [1,2,3]
    head2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = deleteDuplicates(head2)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [1, 2, 3]
    
    # Test case 3: [1,1,1,1] -> [1]
    head3 = create_linked_list([1, 1, 1, 1])
    result3 = deleteDuplicates(head3)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: [1]
    
    # Test case 4: [1,2,3] -> [1,2,3] (no duplicates)
    head4 = create_linked_list([1, 2, 3])
    result4 = deleteDuplicates(head4)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [1, 2, 3]
    
    # Test case 5: [] -> [] (empty list)
    head5 = create_linked_list([])
    result5 = deleteDuplicates(head5)
    print(f"Test 5: {linked_list_to_list(result5)}")  # Expected: []