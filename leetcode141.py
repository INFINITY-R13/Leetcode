# LeetCode Problem 141: Linked List Cycle


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ---------- Helper ----------
def build_list(values, cycle_pos):
    """
    Builds a linked list from `values`.
    If cycle_pos >= 0, connects the tail back to the node at that index.
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)

    # Create cycle if cycle_pos is valid
    if 0 <= cycle_pos < len(nodes):
        current.next = nodes[cycle_pos]  # tail -> node at cycle_pos

    return head


# ---------- Tests ----------
def run_tests():
    sol = Solution()

    # Test 1: Cycle exists (tail connects back to index 1)
    # 3 -> 2 -> 0 -> -1 -> (back to 2)
    head = build_list([3, 2, 0, -1], cycle_pos=1)
    result = sol.hasCycle(head)
    print(f"Test 1 | Expected: True  | Got: {result} | {'PASS' if result == True else 'FAIL'}")

    # Test 2: Cycle exists (tail connects back to index 0)
    # 1 -> 2 -> (back to 1)
    head = build_list([1, 2], cycle_pos=0)
    result = sol.hasCycle(head)
    print(f"Test 2 | Expected: True  | Got: {result} | {'PASS' if result == True else 'FAIL'}")

    # Test 3: No cycle, single node
    # 1 -> None
    head = build_list([1], cycle_pos=-1)
    result = sol.hasCycle(head)
    print(f"Test 3 | Expected: False | Got: {result} | {'PASS' if result == False else 'FAIL'}")

    # Test 4: No cycle, multiple nodes
    # 1 -> 2 -> 3 -> 4 -> None
    head = build_list([1, 2, 3, 4], cycle_pos=-1)
    result = sol.hasCycle(head)
    print(f"Test 4 | Expected: False | Got: {result} | {'PASS' if result == False else 'FAIL'}")

    # Test 5: Empty list
    head = build_list([], cycle_pos=-1)
    result = sol.hasCycle(head)
    print(f"Test 5 | Expected: False | Got: {result} | {'PASS' if result == False else 'FAIL'}")

    # Test 6: Cycle back to itself (single node loop)
    # 1 -> (back to 1)
    head = build_list([1], cycle_pos=0)
    result = sol.hasCycle(head)
    print(f"Test 6 | Expected: True  | Got: {result} | {'PASS' if result == True else 'FAIL'}")

    # Test 7: Longer list, cycle at the end
    # 1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)
    head = build_list([1, 2, 3, 4, 5], cycle_pos=2)
    result = sol.hasCycle(head)
    print(f"Test 7 | Expected: True  | Got: {result} | {'PASS' if result == True else 'FAIL'}")


if __name__ == "__main__":
    run_tests()